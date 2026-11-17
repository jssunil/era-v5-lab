"""Review tests (area A: MoE and model). Added by the week-3 G6 code review; no source file is changed.

Tests marked xfail(strict=True, reason="REVIEW-A<n>: ...") expose a confirmed problem: they fail today and the
suite stays green; when the problem is fixed the test passes, strict xfail turns that into a failure, and the
marker should then be removed. Unmarked tests pin a boundary that holds today.
"""
from __future__ import annotations

import copy
import importlib.util
import sys
import warnings
from pathlib import Path

import pytest
import torch
import torch.nn as nn

import models.moe as moe_mod
from models.config import ModelConfig, load_config, model_config
from models.gpt import Block
from models.moe import DISPATCH, SparseMoE, replay_routing
from models.reversible import ReversibleOnePassStack, ReversibleStack, reconstruction_error

PERF = Path(__file__).resolve().parents[1]
TEAMS = PERF.parent
G5_MODEL = TEAMS / "05-architecture" / "harness" / "week2" / "model.py"
G5_CONFIG_V1 = TEAMS / "05-architecture" / "configs" / "config_v1.yaml"
DISPATCHES = list(DISPATCH)


def _moe(dispatch, dim=16, E=4, k=2, shared=1, seed=0, **kw):
    torch.manual_seed(seed)
    m = SparseMoE(dim, E, k, num_shared=shared, dispatch=dispatch, router_init_std=0.5, **kw)
    with torch.no_grad():
        m.router.bias.normal_(0, 0.5)
    return m


def _run(m, x):
    """out, x.grad, router grads, counts after one forward + backward in train mode."""
    m.train()
    m._counts = None
    x = x.detach().clone().requires_grad_(True)
    y = m(x)
    (y * torch.linspace(-1, 1, y.numel()).view_as(y)).sum().backward()
    return y.detach(), x.grad, m.router.weight.grad.clone(), m.router.bias.grad.clone(), m._counts.clone()


def _close(a, b, tol=1e-5):
    return (a - b).abs().max().item() <= tol * max(1.0, b.abs().max().item())


# ------------------------------------------------------------------------------ dispatch boundaries (pass)

@pytest.mark.parametrize("n", [0, 1])
@pytest.mark.parametrize("dispatch", DISPATCHES)
def test_tiny_token_counts(dispatch, n):
    m = _moe(dispatch)
    x = torch.randn(n, 16, requires_grad=True)
    y = m.train()(x)
    y.sum().backward()
    assert y.shape == (n, 16)
    assert m._counts.sum().item() == n * m.top_k


@pytest.mark.parametrize("case", ["top_k_equals_E", "no_shared", "odd_dims", "all_to_two_experts"])
def test_dispatch_paths_agree_on_boundaries(case):
    """loop / sorted / grouped: same output, input grad, router grads and counts on edge configurations."""
    kw = dict(dim=16, E=4, k=2, shared=1)
    if case == "top_k_equals_E":
        kw.update(E=4, k=4)
    elif case == "no_shared":
        kw.update(shared=0)
    elif case == "odd_dims":
        kw.update(dim=13, E=3, k=2, expert_hidden=7)
    x = torch.randn(11, kw["dim"], generator=torch.Generator().manual_seed(1))
    results = []
    for d in DISPATCHES:
        m = _moe(d, **kw)
        if case == "all_to_two_experts":
            with torch.no_grad():
                m.router_bias[:2] = 10.0         # every token picks experts 0 and 1; 2, 3 idle
        results.append(_run(m, x))
    ref = results[0]
    for d, r in zip(DISPATCHES[1:], results[1:]):
        for name, a, b in zip(["out", "x.grad", "router.w.grad", "router.b.grad", "counts"], r, ref):
            assert _close(a, b), f"{case}: {d} vs loop differ in {name}"


@pytest.mark.parametrize("dispatch", DISPATCHES)
def test_nan_token_does_not_leak_into_other_rows(dispatch):
    m = _moe(dispatch, shared=0)
    x = torch.randn(6, 16)
    x[0, 0] = float("nan")
    with torch.no_grad():
        y = m(x)
    assert torch.isnan(y[0]).all() and torch.isfinite(y[1:]).all()


@pytest.mark.parametrize("dispatch", DISPATCHES)
def test_topk_indices_are_distinct_so_one_expert_gets_at_most_n_routes(dispatch):
    """The fact REVIEW-A1 rests on: top-k picks k different experts per token, so counts[e] <= N, not N * k."""
    m = _moe(dispatch, E=4, k=3)
    with torch.no_grad():
        m.router_bias[0] = 10.0
    n = 9
    m._counts = None
    m.train()(torch.randn(n, 16))
    assert m._counts.max().item() == n


# ------------------------------------------------------------------------------ REVIEW-A1: grouped buffer size

@pytest.mark.xfail(strict=True, reason="REVIEW-A1: dispatch_grouped sizes each expert's buffer at N*top_k rows; "
                   "the most one expert can receive is N (top-k indices are distinct), so the batched GEMM does "
                   "top_k times the work of running every expert on every token (G5's dense fast path)")
def test_grouped_buffer_not_larger_than_dense_all_experts(monkeypatch):
    seen = []
    real = moe_mod._batched_experts

    def spy(moe, buf, region_name):
        seen.append(tuple(buf.shape))
        return real(moe, buf, region_name)

    monkeypatch.setattr(moe_mod, "_batched_experts", spy)
    m = _moe("grouped", E=8, k=2)
    n = 32
    m(torch.randn(n, 16))
    E, cap, _ = seen[0]
    assert E * cap <= E * n, f"grouped buffer {E} x {cap} rows; dense all-experts needs {E} x {n}"


# ------------------------------------------------------------------------------ REVIEW-A2: idle-expert optimizer drift

class _Wrap(nn.Module):
    def __init__(self, m):
        super().__init__()
        self.blocks = nn.ModuleList([m])       # "blocks." prefix: Muon takes the 2D weights, as in the GPT


def _two_steps(dispatch):
    from models.optim import build_optimizer
    m = _moe(dispatch, E=4, k=2, shared=0, bias_gamma=0.0)
    opt = build_optimizer(_Wrap(m), dict(name="polar_muon_adamw", muon_impl="batched", adamw_impl="foreach",
                                         lr=1e-3, muon_lr=0.02, weight_decay=0.0))
    x = torch.randn(8, 16, generator=torch.Generator().manual_seed(1))
    used = None
    for step in range(2):
        if step == 1:
            with torch.no_grad():
                m.router_bias[3] = -10.0      # expert 3 gets no token in step 2
        m._counts = None
        m.train()(x).sum().backward()
        if step == 0:
            used = m._counts[3].item()
        opt.step()
        opt.zero_grad()
    return used, {k: v.clone() for k, v in m.experts[3].state_dict().items()}


@pytest.mark.xfail(strict=True, reason="REVIEW-A2: an expert idle in a step gets grad=None under loop (optimizer "
                   "skips it) but a zero grad under sorted/grouped (Muon/AdamW momentum keeps moving it), so "
                   "swapping the dispatch changes the trained weights")
def test_dispatch_choice_does_not_change_training_with_an_idle_expert():
    used_loop, w_loop = _two_steps("loop")
    used_sorted, w_sorted = _two_steps("sorted")
    assert used_loop > 0 and used_sorted > 0, "expert 3 must be used in step 1 for the test to mean anything"
    for k in w_loop:
        assert torch.allclose(w_loop[k], w_sorted[k], atol=1e-6), f"expert3.{k} differs loop vs sorted"


# ------------------------------------------------------------------------------ REVIEW-A6: top_k=1 router gradient

@pytest.mark.xfail(strict=True, reason="REVIEW-A6: with top_k=1 the renormalised gate is s/s = 1 for every token, "
                   "so the router gets no gradient from the loss; config allows top_k=1 without a warning")
def test_top1_router_still_learns():
    m = _moe("loop", E=4, k=1, shared=0)
    x = torch.randn(10, 16)
    m(x).pow(2).sum().backward()
    assert m.router.weight.grad.abs().max().item() > 1e-6


# ------------------------------------------------------------------------------ REVIEW-A7: config validation

@pytest.mark.parametrize("bad", [dict(num_shared=-1), dict(bias_gamma=-0.01), dict(top_k=0), dict(top_k=9),
                                 dict(num_experts=0), dict(dispatch="bogus")])
@pytest.mark.xfail(strict=True, reason="REVIEW-A7: ModelConfig validates moe key names but not values; bad values "
                   "load and fail late (SparseMoE assert) or silently (num_shared<0 -> 0, bias_gamma<0 -> "
                   "anti-balancing)")
def test_config_rejects_bad_moe_values(bad):
    moe = dict(num_experts=8, top_k=2, num_shared=1, bias_gamma=0.01, dispatch="loop", ffn_hidden=None)
    moe.update(bad)
    with pytest.raises((AssertionError, ValueError)):
        ModelConfig(ffn="moe", moe=moe)


@pytest.mark.parametrize("h", [0.0, -1.0])
@pytest.mark.xfail(strict=True, reason="REVIEW-A7: rev_h <= 0 is accepted (0 makes every block the identity)")
def test_config_rejects_non_positive_rev_h(h):
    with pytest.raises((AssertionError, ValueError)):
        ModelConfig(reversible=True, rev_h=h)


def test_silently_ignored_negative_num_shared_builds_zero_shared_experts():
    """Pins the silent part of REVIEW-A7."""
    m = SparseMoE(16, 4, 2, num_shared=-1)
    assert len(m.shared) == 0


@pytest.mark.parametrize("dispatch", ["loop"])
@pytest.mark.xfail(strict=True, reason="REVIEW-A8: replay_routing does not check the forced index shape; on the "
                   "loop path a stale [M < N, k] index silently zeroes the routed output of tokens M..N-1")
def test_replay_with_wrong_token_count_raises(dispatch):
    m = _moe(dispatch)
    with pytest.raises(Exception):
        with replay_routing(m, torch.tensor([[0, 1], [2, 3]])):
            m(torch.randn(6, 16))


# ------------------------------------------------------------------------------ reversible + MoE

def _rev_blocks(n_layer, std, dispatch="sorted", seed=0, dim=32):
    cfg = ModelConfig(n_embd=dim, n_head=4, n_layer=n_layer, mlp_ratio=2, ffn="moe",
                      moe=dict(num_experts=4, top_k=2, num_shared=1, bias_gamma=0.01, dispatch=dispatch,
                               ffn_hidden=None),
                      reversible=True, rev_h=1.0, vocab_size=256, block_size=16)
    torch.manual_seed(seed)
    blocks = nn.ModuleList(Block(cfg, i) for i in range(n_layer))
    g = torch.Generator().manual_seed(seed)
    with torch.no_grad():
        for p in blocks.parameters():
            if p.ndim >= 2:
                p.copy_(torch.randn(p.shape, generator=g) * std)
    return blocks


@pytest.mark.parametrize("stack,mult", [(ReversibleStack, 3), (ReversibleOnePassStack, 2)])
def test_reversible_backward_recounts_routes(stack, mult):
    """Pins: invert / recompute run the MoE again in train mode, so _counts is mult x the forward's counts.
    update_bias uses sign(mean - count), which is scale-invariant, so balancing is unaffected; any reader of
    _counts as a load metric (G8 monitoring) must divide by mult."""
    blocks = _rev_blocks(2, 0.02)
    x = torch.randn(2, 16, 32, generator=torch.Generator().manual_seed(1))
    with torch.no_grad():
        for b in blocks:
            b.ffn._counts = None
        ReversibleStack.apply(x, blocks)            # forward only (no grad): counts once
    once = [b.ffn._counts.clone() for b in blocks]
    for b in blocks:
        b.ffn._counts = None
    xr = x.clone().requires_grad_(True)
    stack.apply(xr, blocks).sum().backward()
    for b, c in zip(blocks, once):
        assert torch.equal(b.ffn._counts, mult * c)


@pytest.mark.xfail(strict=True, reason="REVIEW-A4: bf16 reversible reconstruction error grows with weight scale "
                   "and depth (midpoint has no error damping); test_reversible only checks init-scale weights "
                   "(std 0.02). At std 0.2, 12 layers the reconstructed input is off by >1% (RTX 5070 Ti: 119%)")
def test_bf16_reconstruction_at_trained_weight_scale(device):
    blocks = _rev_blocks(12, 0.2).to(device).eval()
    x = torch.randn(2, 16, 32, generator=torch.Generator().manual_seed(1)).to(device)
    with torch.autocast(device_type=device.type, dtype=torch.bfloat16):
        err = reconstruction_error(x, blocks)
    assert err < 1e-2, f"bf16 reconstruction_error={err:.3e}"


# ------------------------------------------------------------------------------ host syncs (CUDA only)

def _syncs(m, x):
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        torch.cuda.set_sync_debug_mode("warn")
        try:
            m(x).float().sum().backward()
        finally:
            torch.cuda.set_sync_debug_mode(0)
    # count only the per-op warnings, not torch's one-off "debug mode is a prototype feature" notice
    return sum("called a synchronizing CUDA operation" in str(i.message) for i in w)


@pytest.mark.skipif(not torch.cuda.is_available(), reason="needs CUDA")
def test_sorted_and_grouped_sync_budget():
    x = torch.randn(256, 64, device="cuda")
    for d, budget in [("sorted", 1), ("grouped", 0)]:
        m = SparseMoE(64, 8, 2, num_shared=1, dispatch=d).cuda()
        m(x).sum().backward()                       # warm-up
        assert _syncs(m, x) <= budget, d


@pytest.mark.skipif(not torch.cuda.is_available(), reason="needs CUDA")
@pytest.mark.xfail(strict=True, reason="REVIEW-A3: the default dispatch (ModelConfig, SparseMoE and base.yaml: "
                   "loop) is a Python loop over experts with 2 host syncs per expert; TSAI rule of 13 Nov: no "
                   "Python loops over experts, no avoidable host-device syncs")
def test_default_dispatch_has_no_host_sync():
    d = model_config(load_config(PERF / "configs" / "base.yaml")).moe["dispatch"]
    x = torch.randn(256, 64, device="cuda")
    m = SparseMoE(64, 8, 2, num_shared=1, dispatch=d).cuda()
    m(x).sum().backward()
    assert _syncs(m, x) == 0, f"dispatch={d}"


# ------------------------------------------------------------------------------ cross-team: G5 model

def _load_g5():
    if not G5_MODEL.is_file():
        pytest.skip("G5 harness model not in this checkout")
    spec = importlib.util.spec_from_file_location("g5_week2_model", G5_MODEL)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.mark.parametrize("dispatch", DISPATCHES)
def test_matches_g5_moe_when_configured_like_g5(dispatch):
    """G6 SparseMoE equals G5's MoE only with: swiglu, router bias 0 (G5 router has none), router_bias 0 and
    bias_gamma 0 (G5 has no aux-free balancing), all tokens valid. A G6 MoE timing is valid for G5's model only
    under these settings."""
    g5 = _load_g5()
    dim, E, k, h = 32, 8, 2, 24
    spec = {"n_embd": dim, "moe": {"ffn_hidden": h, "top_k": k, "num_experts": E, "num_shared": 1, "bias": False}}
    torch.manual_seed(0)
    ref = g5.MoE(spec)
    with torch.no_grad():
        ref.router.weight.normal_(0, 0.5)
    m = SparseMoE(dim, E, k, expert_hidden=h, num_shared=1, bias_gamma=0.0, dispatch=dispatch,
                  activation="swiglu")
    with torch.no_grad():
        m.router.weight.copy_(ref.router.weight)
        m.router.bias.zero_()
        for mine, theirs in zip([*m.experts, *m.shared], [*ref.experts, *ref.shared]):
            mine.c_gate.weight.copy_(theirs.gate.weight)
            mine.c_fc.weight.copy_(theirs.up.weight)
            mine.c_proj.weight.copy_(theirs.down.weight)
    x = torch.randn(3, 7, dim, generator=torch.Generator().manual_seed(2))
    valid = torch.ones(3, 7, dtype=torch.bool)
    with torch.no_grad():
        assert _close(m(x), ref(x, valid), 1e-5)


@pytest.mark.xfail(strict=True, reason="REVIEW-A10: run_dryrun1_prof maps config_v1 onto base.yaml but keeps "
                   "base.yaml's gelu experts, learned positions and reversible=true; G5's week-2 harness requires "
                   "swiglu, rope and reversible=false, so the dry-run profile times a different model")
def test_dryrun1_mapping_builds_g5_model_shape():
    if not G5_CONFIG_V1.is_file():
        pytest.skip("G5 config_v1 not in this checkout")
    sys.path.insert(0, str(PERF / "jobs"))
    try:
        from run_dryrun1_prof import _load_g5_overrides
    finally:
        sys.path.remove(str(PERF / "jobs"))
    overrides, _ = _load_g5_overrides(G5_CONFIG_V1)
    mc = model_config(load_config(PERF / "configs" / "base.yaml", overrides))
    got = dict(activation=mc.activation, position=mc.position, reversible=mc.reversible)
    assert got == dict(activation="swiglu", position="rope", reversible=False), got
