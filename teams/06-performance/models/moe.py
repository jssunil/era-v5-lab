"""Top-k sparse Mixture of Experts.  [implemented: MVP]

Lab setting: 1 shared expert (always on) + top-2 routed of 8 (configs/lab_small.yaml).

  * SparseMoE(dim, num_experts=8, top_k=2, expert_hidden=None, num_shared=0, bias_gamma=0.01,
              dispatch="loop", name="moe")
  * Attributes the fp64 test reference reads (keep these names):
      router       nn.Linear(dim, num_experts), run in fp32 (cast x to router.weight.dtype, autocast off)
      router_bias  buffer [num_experts]: steers *selection* only, never the gate weights
      experts      ModuleList of ExpertMLP (c_fc: Linear(dim, hidden), GELU, c_proj: Linear(hidden, dim))
      shared       ModuleList of ExpertMLP, always on, same hidden size as a routed expert
      top_k, num_experts
  * Init as the dense NanoGPT MLP: weights normal(0, 0.02), biases zero, c_proj normal(0, proj_std)
    (gpt.py passes the residual std 0.02 / sqrt(2 n_layer)). Router normal(0, router_init_std = 0.02).
    PyTorch's default Linear init makes f ~8x larger than the dense model at init, which breaks the
    reversible reconstruction in bf16 (2.5e-2 vs 1.8e-4 at 9 layers).
  * forward(x [..., dim]) -> same shape:
      scores = softmax(router(x)); top-k on (scores + router_bias); gates = scores of the chosen,
      renormalised to sum 1; out = sum gate * expert(x) + sum shared(x).
  * update_bias(): router_bias += gamma * sign(mean_count - count), counts summed since the last call.
    Counts are kept only in training mode (not in eval). In the reversible stack the forward runs 3 times
    per step (forward, invert, recompute) with the same routing (replayed), so counts triple exactly;
    sign() makes the update the same.
  * Routing replay (used by models/reversible.py): with `record_routing(moe, out_list)` the chosen top-k
    indices are appended to out_list; with `replay_routing(moe, idx)` forward uses idx instead of top-k.
    Without it a reconstructed input that differs by 1e-5 can flip a near-tie token to other experts,
    and the reversible backward rebuilds the wrong state (bf16: gradient errors up to 23%).
    Gates are always recomputed from the router scores, so the router still gets its gradient.
  * DISPATCH = {"loop": dispatch_loop, "sorted": dispatch_sorted}. The loop path gathers per expert and is
    the reference. The sorted path sorts token/expert assignments and applies expert weights with bounded
    batched matrix multiplies; it does not read route counts or masks back to the host.
    Both paths compute token counts with a device-side compare-and-sum over topk_idx. Since sorted packs all
    expert parameters together, idle experts receive zero gradients rather than None; the loop remains default
    until the optimizer-state effect of that difference is resolved and server timings are collected.
  * Regions (level 3): f"{name}.router", f"{name}.dispatch", f"{name}.dispatch.expert{e}", f"{name}.shared".

Extra: "dense" dispatch (every expert on every token, exact, slow), capacity factor, aux / z loss.
Done when: correctness/test_moe.py passes for every entry in DISPATCH.
"""
from __future__ import annotations

from contextlib import contextmanager

import torch
import torch.nn as nn
import torch.nn.functional as F

from perfkit.regions import region


class ExpertMLP(nn.Module):
    def __init__(self, dim, hidden, std=0.02, proj_std=0.02):
        super().__init__()
        self.c_fc = nn.Linear(dim, hidden)
        self.c_proj = nn.Linear(hidden, dim)
        for lin, s in ((self.c_fc, std), (self.c_proj, proj_std)):
            nn.init.normal_(lin.weight, mean=0.0, std=s)
            nn.init.zeros_(lin.bias)

    def forward(self, x):
        return self.c_proj(F.gelu(self.c_fc(x)))


def dispatch_loop(moe, x, topk_idx, gates):
    """x [N, dim], topk_idx [N, k], gates [N, k] -> (out [N, dim], counts [num_experts])."""
    out = torch.zeros_like(x)
    # No host sync: a per-expert `counts[e] = idx.numel()` copied a host int to the GPU (1 sync each), and
    # torch.bincount on CUDA reads max() back to size its output. Compare-and-sum needs neither, and no atomics.
    counts = (topk_idx.reshape(-1, 1) == torch.arange(moe.num_experts, device=x.device)).sum(0).float()
    for e in range(moe.num_experts):
        with region(f"{moe.name}.dispatch.expert{e}", 3):
            pos = topk_idx == e
            tok = pos.any(dim=1)
            if not tok.any():                                   # host sync
                continue
            idx = tok.nonzero(as_tuple=True)[0]                 # host sync
            w = (gates * pos.to(gates.dtype)).sum(dim=1)
            out.index_add_(0, idx, moe.experts[e](x[idx]) * w[idx].unsqueeze(1).to(x.dtype))
    return out, counts


_SORTED_CHUNK_SIZE = 64


def dispatch_sorted(moe, x, topk_idx, gates):
    """Sort flattened token/expert assignments and process them in bounded batched GEMM chunks.

    Unlike a per-expert mask loop, this path never asks Python whether a route group is empty or how many
    tokens it contains. The fixed chunk size bounds the temporary expert-weight gathers for long sequences.
    """
    n_tokens = x.size(0)
    flat_experts = topk_idx.reshape(-1)
    counts = (flat_experts.reshape(-1, 1) == torch.arange(moe.num_experts, device=x.device)).sum(0).float()
    order = torch.argsort(flat_experts)
    sorted_experts = flat_experts.index_select(0, order)
    token_ids = torch.arange(n_tokens, device=x.device).repeat_interleave(moe.top_k).index_select(0, order)
    sorted_gates = gates.reshape(-1).index_select(0, order)

    # Pack each parameter family once. index_select below gathers only the current chunk's experts.
    fc_weights = torch.stack([expert.c_fc.weight for expert in moe.experts])
    fc_biases = torch.stack([expert.c_fc.bias for expert in moe.experts])
    proj_weights = torch.stack([expert.c_proj.weight for expert in moe.experts])
    proj_biases = torch.stack([expert.c_proj.bias for expert in moe.experts])

    sorted_updates = []
    with region(f"{moe.name}.dispatch.grouped", 3):
        for start in range(0, token_ids.numel(), _SORTED_CHUNK_SIZE):
            end = min(start + _SORTED_CHUNK_SIZE, token_ids.numel())
            experts = sorted_experts[start:end]
            tokens = token_ids[start:end]
            inputs = x.index_select(0, tokens)

            w1 = fc_weights.index_select(0, experts)
            b1 = fc_biases.index_select(0, experts)
            hidden = torch.bmm(w1, inputs.unsqueeze(-1)).squeeze(-1)
            hidden = F.gelu(hidden + b1.to(hidden.dtype))

            w2 = proj_weights.index_select(0, experts)
            b2 = proj_biases.index_select(0, experts)
            updates = torch.bmm(w2, hidden.unsqueeze(-1)).squeeze(-1)
            updates = updates + b2.to(updates.dtype)
            updates = updates * sorted_gates[start:end].to(updates.dtype).unsqueeze(1)
            sorted_updates.append(updates.to(x.dtype))

    if not sorted_updates:
        return torch.zeros_like(x), counts
    # Restore the original [token, top-k slot] order, then sum each token's k contributions.
    # Each output row is reduced locally, avoiding the nondeterministic atomics in index_add_ on CUDA.
    inverse_order = torch.argsort(order)
    updates = torch.cat(sorted_updates, dim=0).index_select(0, inverse_order)
    out = updates.reshape(n_tokens, moe.top_k, x.size(-1)).sum(dim=1)
    return out, counts


DISPATCH = {"loop": dispatch_loop, "sorted": dispatch_sorted}


@contextmanager
def record_routing(moe, out: list):
    moe._record = out
    try:
        yield
    finally:
        moe._record = None


@contextmanager
def replay_routing(moe, topk_idx):
    moe._forced = topk_idx
    try:
        yield
    finally:
        moe._forced = None


class SparseMoE(nn.Module):
    def __init__(self, dim, num_experts=8, top_k=2, expert_hidden=None, num_shared=0,
                 bias_gamma=0.01, dispatch="loop", name="moe", router_init_std=0.02, proj_std=0.02):
        super().__init__()
        assert dispatch in DISPATCH, f"dispatch {dispatch!r} not in {list(DISPATCH)}"
        assert 0 < top_k <= num_experts
        self.dim, self.num_experts, self.top_k = dim, num_experts, top_k
        self.expert_hidden = expert_hidden or 4 * dim
        self.gamma, self.dispatch, self.name = bias_gamma, dispatch, name
        self.router = nn.Linear(dim, num_experts)
        nn.init.normal_(self.router.weight, std=router_init_std)
        nn.init.zeros_(self.router.bias)
        self.register_buffer("router_bias", torch.zeros(num_experts))
        self.experts = nn.ModuleList(ExpertMLP(dim, self.expert_hidden, proj_std=proj_std) for _ in range(num_experts))
        self.shared = nn.ModuleList(ExpertMLP(dim, self.expert_hidden, proj_std=proj_std) for _ in range(num_shared))
        self._counts = self._record = self._forced = None

    def forward(self, x):
        shape = x.shape
        x = x.reshape(-1, shape[-1])
        with region(f"{self.name}.router", 3):
            with torch.autocast(device_type=x.device.type, enabled=False):
                logits = self.router(x.to(self.router.weight.dtype))
            scores = F.softmax(logits, dim=-1)
            if self._forced is not None:
                topk_idx = self._forced.long()
            else:
                topk_idx = torch.topk(scores + self.router_bias, self.top_k, dim=1).indices
            if self._record is not None:
                self._record.append(topk_idx.to(torch.uint8 if self.num_experts <= 256 else torch.int32))
            gates = torch.gather(scores, 1, topk_idx)
            gates = gates / gates.sum(dim=1, keepdim=True)
        with region(f"{self.name}.dispatch", 3):
            out, counts = DISPATCH[self.dispatch](self, x, topk_idx, gates)
        with region(f"{self.name}.shared", 3):
            for s in self.shared:
                out = out + s(x)
        if self.training:
            c = counts.detach()
            self._counts = c if self._counts is None else self._counts + c
        return out.reshape(shape)

    @torch.no_grad()
    def update_bias(self):
        if self._counts is not None:
            self.router_bias += self.gamma * torch.sign(self._counts.mean() - self._counts)
            self._counts = None
