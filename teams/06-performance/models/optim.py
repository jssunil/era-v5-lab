"""Optimizers: AdamW, or Muon on every 2D weight + AdamW on the rest.  [implemented: MVP]

  * build_optimizer(model, ocfg) -> object with zero_grad(), step(scaler=None), unscale(scaler), flops().
    ocfg = cfg["optim"]: name adamw | muon, lr, muon_lr, weight_decay.
  * adamw: torch.optim.AdamW (fused=True on CUDA).
  * muon: Muon (Keller Jordan): momentum 0.95 nesterov, update = NS5(momentum grad) * max(1, rows/cols)**0.5,
    Newton-Schulz coefficients (3.4445, -4.7750, 2.0315), 5 steps, bf16 (fp32 on GPUs without bf16: T4/P100/V100).
    Muon handles 2D block weights (including routers). AdamW handles embedding parameters
    (token table / KE projection / position table), output head, norm gains and biases. Decoupled
    weight decay applies to AdamW matrices, not 1D biases or norm gains.
    A parameter with grad=None is skipped, matching AdamW's unused-expert behavior.
  * Regions (level 2): "opt.muon", "opt.adamw"; (level 3): "opt.zero_grad".
  * flops(): Newton-Schulz FLOPs per step = sum over matrices of 5 * (4 m^2 n + 2 m^3), m <= n (for HFU).
Cost to watch: one small matmul chain per matrix (8 experts x 2 x layers + attention + ...): likely
launch-bound. A batched version (same-shaped matrices through bmm) is a week-2 target.
"""
from __future__ import annotations

import math

import torch

from perfkit.regions import region

NS_COEFFS = (3.4445, -4.7750, 2.0315)


def _native_bf16():
    try:
        return torch.cuda.is_bf16_supported(including_emulation=False)
    except TypeError:  # torch < 2.4
        return torch.cuda.get_device_capability()[0] >= 8


def zeropower_via_newtonschulz5(G: torch.Tensor, steps: int = 5, eps: float = 1e-7) -> torch.Tensor:
    """Approximately orthogonalise G (the U V^T of its SVD), in bf16 where the GPU has it."""
    a, b, c = NS_COEFFS
    X = G.to(torch.bfloat16 if (not G.is_cuda or _native_bf16()) else torch.float32)
    transpose = X.size(0) > X.size(1)
    if transpose:
        X = X.T
    X = X / (X.norm() + eps)
    for _ in range(steps):
        A = X @ X.T
        B = b * A + c * A @ A
        X = a * X + B @ X
    return X.T if transpose else X


class Muon(torch.optim.Optimizer):
    def __init__(self, params, lr=0.02, momentum=0.95, nesterov=True, ns_steps=5, weight_decay=0.0):
        super().__init__(params, dict(lr=lr, momentum=momentum, nesterov=nesterov,
                                      ns_steps=ns_steps, weight_decay=weight_decay))

    @torch.no_grad()
    def step(self, closure=None):
        for group in self.param_groups:
            for p in group["params"]:
                st = self.state[p]
                # Match AdamW: an unused expert receives no update and its moments stay unchanged.
                if p.grad is None:
                    continue
                if "buf" not in st:
                    st["buf"] = torch.zeros_like(p.grad)
                buf = st["buf"]
                buf.lerp_(p.grad, 1 - group["momentum"])
                g = p.grad.lerp(buf, group["momentum"]) if group["nesterov"] else buf
                with region("opt.muon.ns", 3):
                    u = zeropower_via_newtonschulz5(g, group["ns_steps"])
                if group["weight_decay"]:
                    p.mul_(1 - group["lr"] * group["weight_decay"])
                p.add_(u.to(p.dtype), alpha=-group["lr"] * max(1.0, p.size(0) / p.size(1)) ** 0.5)


class Optimizers:
    """One or two torch optimizers behind one zero_grad() / step(), with timed regions."""

    def __init__(self, named: list):
        self.named = named          # [(region name, torch optimizer)]
        for _, optimizer in named:
            for group in optimizer.param_groups:
                group.setdefault("initial_lr", group["lr"])

    def set_lr(self, step: int, total_steps: int, schedule="constant", warmup_steps=0,
               min_lr_ratio=0.1):
        """Set each optimizer group's LR from its own base LR.

        cosine warms linearly from zero, then decays to min_lr_ratio. constant
        keeps timing runs at fixed rates unless a warmup is explicitly requested.
        """
        if schedule not in ("constant", "cosine"):
            raise ValueError(f"optim.schedule={schedule!r}: constant | cosine")
        if total_steps <= 0 or warmup_steps < 0 or warmup_steps >= total_steps:
            raise ValueError("Require total_steps > warmup_steps >= 0")
        if not 0.0 <= min_lr_ratio <= 1.0:
            raise ValueError("min_lr_ratio must be in [0, 1]")
        if step < 0 or step >= total_steps:
            raise ValueError("step must be in [0, total_steps)")
        warmup = (step + 1) / warmup_steps if warmup_steps and step < warmup_steps else 1.0
        if schedule == "cosine" and step >= warmup_steps:
            progress = (step - warmup_steps) / max(1, total_steps - warmup_steps - 1)
            decay = min_lr_ratio + (1 - min_lr_ratio) * 0.5 * (1 + math.cos(progress * math.pi))
        else:
            decay = 1.0
        multiplier = warmup * decay
        for _, optimizer in self.named:
            for group in optimizer.param_groups:
                group["lr"] = group["initial_lr"] * multiplier

    def zero_grad(self):
        with region("opt.zero_grad", 3):
            for _, o in self.named:
                o.zero_grad(set_to_none=True)

    def step(self, scaler=None):
        for name, o in self.named:
            with region(name, 2):
                scaler.step(o) if scaler is not None else o.step()

    def unscale(self, scaler):
        for _, o in self.named:
            scaler.unscale_(o)

    def flops(self):
        """Newton-Schulz FLOPs per step (Muon is not free; counted in HFU, not in MFU)."""
        total = 0
        for _, o in self.named:
            if isinstance(o, Muon):
                for g in o.param_groups:
                    for p in g["params"]:
                        m, n = sorted(p.shape[:2])
                        total += g["ns_steps"] * (4 * m * m * n + 2 * m ** 3)
        return total


def build_optimizer(model, ocfg: dict):
    named_params = [(n, p) for n, p in model.named_parameters() if p.requires_grad]
    params = [p for _, p in named_params]
    fused = params[0].is_cuda

    def adamw(named):
        decay, no_decay = [], []
        for name, p in named:
            (decay if p.ndim >= 2 and not name.endswith(".bias") else no_decay).append(p)
        groups = []
        if decay:
            groups.append({"params": decay, "weight_decay": ocfg["weight_decay"]})
        if no_decay:
            groups.append({"params": no_decay, "weight_decay": 0.0})
        return torch.optim.AdamW(groups, lr=ocfg["lr"], betas=(0.9, 0.95), fused=fused)

    if ocfg["name"] == "adamw":
        return Optimizers([("opt.adamw", adamw(named_params))])
    if ocfg["name"] == "muon":
        if "muon_params" in ocfg and ocfg["muon_params"] != "hidden":
            raise ValueError("Remove optim.muon_params: embeddings and head must use AdamW")

        def use_muon(name, p):
            return p.dim() == 2 and name.startswith("blocks.") and name.endswith(".weight")
        two_d = [p for n, p in named_params if use_muon(n, p)]
        rest = [(n, p) for n, p in named_params if not use_muon(n, p)]
        named = []
        if two_d:
            named.append(("opt.muon", Muon(two_d, lr=ocfg["muon_lr"], weight_decay=ocfg["weight_decay"])))
        if rest:
            named.append(("opt.adamw", adamw(rest)))
        return Optimizers(named)
    raise ValueError(f"optim.name={ocfg['name']!r}: adamw | muon")
