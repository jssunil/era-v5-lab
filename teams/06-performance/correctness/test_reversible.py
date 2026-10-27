"""Reversible stack: custom backward against plain autograd, plus inversion.

Pairs: ReversibleStack.apply(x, blocks) (fast) vs models.reversible.plain_forward on an fp64 copy
of the same blocks (ref), for ffn="mlp" and ffn="moe"; gradients of x and of every parameter.
Extra test: run forward, then invert every block in reverse: the input comes back (rel err < 1e-4).
Pairs run in fp32 / fp64 (correctness/framework.py: precision). bf16 is a property test, not a pair:
with ffn="moe" under bf16 autocast, models.reversible.reconstruction_error < 1e-3 at 9 and 24 layers
(measured ~2.5e-4 on CPU and A100), and the custom-backward gradient of x is within 1e-3 of plain_forward's.
"""
from __future__ import annotations

import copy

import pytest
import torch

from correctness.framework import PAIRS, Case, check, pair, pairs_in, rel_err, to64
from models.config import ModelConfig
from models.gpt import Block
from models.reversible import ReversibleStack, plain_forward, reconstruction_error, _forward_recording, _replaying

N_EMBD, N_HEAD, N_LAYER_PAIR = 32, 4, 3
B, T = 2, 17
WEIGHT_STD = 0.02


def _blocks(ffn: str, n_layer: int, seed: int = 0) -> torch.nn.ModuleList:
    moe = dict(num_experts=4, top_k=2, num_shared=1, bias_gamma=0.01, dispatch="loop")
    cfg = ModelConfig(
        n_embd=N_EMBD,
        n_head=N_HEAD,
        n_kv_head=N_HEAD // 2,
        n_layer=n_layer,
        mlp_ratio=2,
        ffn=ffn,
        moe=moe,
        reversible=True,
        rev_h=1.0,
        vocab_size=256,
        block_size=T,
    )
    blocks = torch.nn.ModuleList(Block(cfg, i) for i in range(n_layer))
    g = torch.Generator().manual_seed(seed)
    with torch.no_grad():
        for p in blocks.parameters():
            if p.ndim >= 2:
                p.copy_(torch.randn(p.shape, generator=g) * WEIGHT_STD)
            else:
                p.zero_()
        # Clear MoE top-k margins if present.
        for blk in blocks:
            ffn_mod = blk.ffn
            if hasattr(ffn_mod, "router"):
                ffn_mod.router.weight.mul_(8.0)   # large margins
                ffn_mod.router_bias.copy_(
                    torch.linspace(-0.05, 0.05, ffn_mod.num_experts)
                )
    return blocks


def _all_params(blocks):
    return [p for p in blocks.parameters()]


def _register(ffn: str):
    name = f"reversible.{ffn}"

    @pair(name, tol=1e-5, grad_tol=5e-5)
    def build(device):
        fast_blocks = _blocks(ffn, N_LAYER_PAIR, seed=0).to(device)
        ref_blocks = to64(fast_blocks)
        # Input must require grad: ReversibleStack.apply only sees tensor inputs (blocks
        # are a non-tensor arg), so without this the Function output is detached while
        # plain_forward still requires grad via module parameters.
        x = torch.randn(
            B, T, N_EMBD, device=device,
            generator=torch.Generator(device=device).manual_seed(1),
        ).requires_grad_(True)

        def fast_fn(inp):
            return ReversibleStack.apply(inp, fast_blocks)

        def ref_fn(inp):
            return plain_forward(inp, ref_blocks)

        return Case(
            ref=ref_fn,
            fast=fast_fn,
            inputs=[x],
            params_ref=_all_params(ref_blocks),
            params_fast=_all_params(fast_blocks),
        )

    return build


_register("mlp")
_register("moe")


parametrize = pytest.mark.parametrize


@parametrize("name", pairs_in(__name__))
def test_pair(name, device):
    errors = check(PAIRS[name], device)
    assert errors, f"{name}: check returned no errors, nothing was compared"


@parametrize("ffn", ["mlp", "moe"])
def test_inversion(ffn, device):
    blocks = _blocks(ffn, N_LAYER_PAIR, seed=2).to(device)
    x = torch.randn(B, T, N_EMBD, device=device, generator=torch.Generator(device=device).manual_seed(3))
    po, co, routes = _forward_recording(blocks, x)
    for i in reversed(range(len(blocks))):
        with _replaying(blocks[i], routes[i]):
            po, co = blocks[i].invert(po, co), po
    err = rel_err(po, x)
    assert err < 1e-4, f"inversion rel_err={err:.3e}"


@parametrize("n_layer", [9, 24])
def test_bf16_reconstruction_moe(n_layer, device):
    blocks = _blocks("moe", n_layer, seed=4).to(device)
    x = torch.randn(B, T, N_EMBD, device=device, generator=torch.Generator(device=device).manual_seed(5))
    with torch.autocast(device_type=device.type, dtype=torch.bfloat16):
        err = reconstruction_error(x, blocks)
    assert err < 1e-3, f"bf16 reconstruction_error={err:.3e} at {n_layer} layers"


def test_bf16_grad_agrees_with_plain(device):
    blocks = _blocks("moe", N_LAYER_PAIR, seed=6).to(device)
    x0 = torch.randn(B, T, N_EMBD, device=device, generator=torch.Generator(device=device).manual_seed(7))
    try:
        with torch.autocast(device_type=device.type, dtype=torch.bfloat16):
            x_fast = x0.detach().clone().requires_grad_(True)
            y_fast = ReversibleStack.apply(x_fast, blocks)
            y_fast.float().sum().backward()
            g_fast = x_fast.grad.detach().float()

            blocks_plain = copy.deepcopy(blocks)
            x_ref = x0.detach().clone().requires_grad_(True)
            y_ref = plain_forward(x_ref, blocks_plain)
            y_ref.float().sum().backward()
            g_ref = x_ref.grad.detach().float()
    except RuntimeError as exc:
        msg = str(exc)
        if "bf16" in msg.lower() or "DNNL" in msg or "f16" in msg.lower():
            pytest.skip(f"bf16 backward unsupported on this device: {exc}")
        raise
    err = rel_err(g_fast, g_ref)
    assert err < 1e-3, f"bf16 grad rel_err={err:.3e}"
