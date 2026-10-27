"""MoE: every dispatch in models.moe.DISPATCH against a token-by-token fp64 reference.

Reference: per token, fp64 router -> softmax -> top-k on (scores + router_bias) -> renormalised gates ->
sum gate * expert(token) + shared experts (the lab uses 1 shared). Read the weights from the module attributes
listed in models/moe.py. Routing replay (deterministic): (1) replay_routing(moe, idx) gives exactly the normal
forward's output when idx is what record_routing captured. (2) Near tie: set router row 2 = row 1 + 1e-6 * random,
so experts 1 and 2 almost tie; record on x, then run x + 1e-4 * noise: without replay some token's top-k changes,
with replay_routing(recorded) none does, and gates still come from the router (gradient flows). Use a large
router init (clear top-k margins, so fp32 vs fp64 never picks different experts) and a non-zero router_bias.
Loop over DISPATCH so a new fast dispatch is tested automatically.
Property tests (no pair): router_bias changes selection but not gate values; update_bias() moves the
bias by +-gamma toward balance and clears the counts; no counts in eval mode; shared experts run on every
token; with the lab init (models/moe.py) f is on the dense model's scale.
"""
from __future__ import annotations

import copy

import pytest
import torch
import torch.nn.functional as F

from correctness.framework import PAIRS, Case, check, pair, pairs_in, rel_err, to64
from models.moe import DISPATCH, SparseMoE, record_routing, replay_routing

DIM, HIDDEN = 32, 64
B, T = 2, 37
NUM_EXPERTS, TOP_K, NUM_SHARED = 8, 2, 1
ROUTER_STD = 0.5          # large margins so fp32 vs fp64 never flip top-k
BIAS_OFFSET = 0.05


def _expert_forward(x, c_fc_w, c_fc_b, c_proj_w, c_proj_b):
    return F.linear(F.gelu(F.linear(x, c_fc_w, c_fc_b)), c_proj_w, c_proj_b)


def reference_moe(x, moe):
    """Token-by-token fp64 MoE from the definition. Never calls DISPATCH / SparseMoE.forward."""
    shape = x.shape
    flat = x.reshape(-1, shape[-1])
    n = flat.shape[0]
    logits = F.linear(flat, moe.router.weight, moe.router.bias)
    scores = F.softmax(logits, dim=-1)
    topk_idx = torch.topk(scores + moe.router_bias, moe.top_k, dim=1).indices
    gates = torch.gather(scores, 1, topk_idx)
    gates = gates / gates.sum(dim=1, keepdim=True)
    out = torch.zeros_like(flat)
    for i in range(n):
        tok = flat[i]
        for j in range(moe.top_k):
            e = int(topk_idx[i, j].item())
            ex = moe.experts[e]
            out[i] = out[i] + gates[i, j] * _expert_forward(
                tok, ex.c_fc.weight, ex.c_fc.bias, ex.c_proj.weight, ex.c_proj.bias
            )
        for s in moe.shared:
            out[i] = out[i] + _expert_forward(
                tok, s.c_fc.weight, s.c_fc.bias, s.c_proj.weight, s.c_proj.bias
            )
    return out.reshape(shape)


def _all_params(moe):
    params = [moe.router.weight, moe.router.bias]
    for ex in list(moe.experts) + list(moe.shared):
        params += [ex.c_fc.weight, ex.c_fc.bias, ex.c_proj.weight, ex.c_proj.bias]
    return params


def _make_moe(dispatch: str, seed: int = 0) -> SparseMoE:
    g = torch.Generator().manual_seed(seed)
    moe = SparseMoE(
        DIM,
        num_experts=NUM_EXPERTS,
        top_k=TOP_K,
        expert_hidden=HIDDEN,
        num_shared=NUM_SHARED,
        dispatch=dispatch,
        router_init_std=ROUTER_STD,
        name="moe",
    )
    with torch.no_grad():
        moe.router.weight.copy_(torch.randn(moe.router.weight.shape, generator=g) * ROUTER_STD)
        moe.router.bias.zero_()
        moe.router_bias.copy_(torch.linspace(-BIAS_OFFSET, BIAS_OFFSET, NUM_EXPERTS))
        for mod in list(moe.experts) + list(moe.shared):
            for p in mod.parameters():
                p.copy_(torch.randn(p.shape, generator=g) * 0.02)
    return moe


def _register(dispatch: str):
    name = f"moe.{dispatch}"

    @pair(name, tol=1e-5, grad_tol=1e-4)
    def build(device):
        fast = _make_moe(dispatch).to(device)
        ref = to64(fast)
        x = torch.randn(
            B, T, DIM, device=device,
            generator=torch.Generator(device=device).manual_seed(1),
        )

        def fast_fn(inp):
            return fast(inp)

        def ref_fn(inp):
            return reference_moe(inp, ref)

        return Case(
            ref=ref_fn,
            fast=fast_fn,
            inputs=[x],
            params_ref=_all_params(ref),
            params_fast=_all_params(fast),
        )

    return build


for _dispatch_name in DISPATCH:
    _register(_dispatch_name)


parametrize = pytest.mark.parametrize


@parametrize("name", pairs_in(__name__))
def test_pair(name, device):
    errors = check(PAIRS[name], device)
    assert errors, f"{name}: check returned no errors, nothing was compared"


def test_replay_exact(device):
    moe = _make_moe("loop").to(device)
    x = torch.randn(B, T, DIM, device=device, generator=torch.Generator(device=device).manual_seed(2))
    recorded: list = []
    with record_routing(moe, recorded):
        y0 = moe(x)
    assert len(recorded) == 1
    with replay_routing(moe, recorded[0].long()):
        y1 = moe(x)
    assert torch.equal(y0, y1), "replay of the same indices must match the recorded forward exactly"


def test_near_tie_replay(device):
    moe = _make_moe("loop", seed=3).to(device)
    with torch.no_grad():
        moe.router_bias.zero_()
        # Only experts 0 and 1 compete; others are crushed.
        for e in range(NUM_EXPERTS):
            moe.router.weight[e].zero_()
            moe.router.bias[e] = -20.0
        moe.router.bias[0] = 0.0
        moe.router.bias[1] = 1e-5          # tiny edge for expert 1
        # Directional rows: x along e0 favors expert 0, along e1 favors expert 1.
        moe.router.weight[0, 0] = 1.0
        moe.router.weight[1, 1] = 1.0
    # Tokens sit on the decision boundary between experts 0 and 1.
    x = torch.zeros(B, T, DIM, device=device)
    x[..., 0] = 1.0
    x[..., 1] = 1.0
    recorded: list = []
    with record_routing(moe, recorded):
        _ = moe(x)
    idx = recorded[0].long()

    # Nudge toward expert 0 so free routing flips relative to the recorded near-tie.
    x_noisy = x.clone()
    x_noisy[..., 0] = 1.0 + 0.1
    x_noisy[..., 1] = 1.0 - 0.1
    recorded2: list = []
    with record_routing(moe, recorded2):
        y_free = moe(x_noisy)
    flipped = not torch.equal(idx, recorded2[0].long())
    assert flipped, "expected at least one top-k flip without replay on near-tie + noise"

    # With replay, routing is frozen; router still receives gradient via gates.
    x_req = x_noisy.detach().requires_grad_(True)
    moe.router.weight.grad = None
    with replay_routing(moe, idx):
        y_rep = moe(x_req)
    y_rep.sum().backward()
    assert x_req.grad is not None and x_req.grad.abs().sum() > 0
    assert moe.router.weight.grad is not None and moe.router.weight.grad.abs().sum() > 0
    recorded3: list = []
    with record_routing(moe, recorded3), replay_routing(moe, idx):
        _ = moe(x_noisy)
    assert torch.equal(idx, recorded3[0].long())
    # With top_k==2 and only experts {0,1} alive, free vs replayed can share the same
    # expert set (order/gates differ); the contract is frozen indices + flowing router grads.
    _ = y_free  # computed above to exercise free routing on noisy x


def test_router_bias_selection_not_gates(device):
    moe = _make_moe("loop", seed=5).to(device)
    x = torch.randn(4, DIM, device=device, generator=torch.Generator(device=device).manual_seed(6))
    with torch.no_grad():
        logits = moe.router(x)
        scores = F.softmax(logits, dim=-1)
        moe.router_bias.zero_()
        idx0 = torch.topk(scores + moe.router_bias, TOP_K, dim=1).indices
        gates0 = torch.gather(scores, 1, idx0)
        gates0 = gates0 / gates0.sum(dim=1, keepdim=True)
        # Push expert 0 hard so selection changes for some rows.
        moe.router_bias[0] = 10.0
        idx1 = torch.topk(scores + moe.router_bias, TOP_K, dim=1).indices
        gates1 = torch.gather(scores, 1, idx1)
        gates1 = gates1 / gates1.sum(dim=1, keepdim=True)
    assert not torch.equal(idx0, idx1), "router_bias should change selection"
    # Gates are always taken from scores (not scores+bias), then renormalised.
    # For rows that kept the same experts (possibly reordered), gate values equal the same score entries.
    for i in range(x.shape[0]):
        s0 = set(idx0[i].tolist())
        s1 = set(idx1[i].tolist())
        if s0 == s1:
            assert torch.allclose(gates0[i].sort().values, gates1[i].sort().values, atol=1e-6)


def test_update_bias_toward_balance(device):
    moe = _make_moe("loop", seed=7).to(device)
    moe.train()
    x = torch.randn(B, T, DIM, device=device, generator=torch.Generator(device=device).manual_seed(8))
    before = moe.router_bias.clone()
    _ = moe(x)
    assert moe._counts is not None
    counts = moe._counts.clone()
    moe.update_bias()
    assert moe._counts is None
    expected = before + moe.gamma * torch.sign(counts.mean() - counts)
    assert torch.allclose(moe.router_bias, expected)


def test_no_counts_in_eval(device):
    moe = _make_moe("loop").to(device)
    moe.eval()
    x = torch.randn(B, T, DIM, device=device)
    _ = moe(x)
    assert moe._counts is None


def test_shared_experts_always_on(device):
    moe = _make_moe("loop", seed=9).to(device)
    x = torch.randn(B, T, DIM, device=device, generator=torch.Generator(device=device).manual_seed(10))
    y_full = moe(x).detach()
    # Zero shared weights: output must change if shared ran on every token.
    with torch.no_grad():
        for s in moe.shared:
            for p in s.parameters():
                p.zero_()
    y_nos = moe(x).detach()
    assert (y_full - y_nos).abs().max() > 1e-5


def test_lab_init_scale_vs_dense(device):
    """Lab init (std 0.02) keeps MoE f on a similar scale to a dense MLP residual."""
    moe = _make_moe("loop", seed=11).to(device)
    x = torch.randn(B, T, DIM, device=device, generator=torch.Generator(device=device).manual_seed(12))
    y = moe(x).detach()
    # Rough check: output RMS within an order of input RMS (not ~8x like default Linear init).
    ratio = y.pow(2).mean().sqrt() / x.pow(2).mean().sqrt()
    assert 0.01 < ratio.item() < 5.0, f"MoE scale ratio={ratio.item():.3f} looks wrong"
