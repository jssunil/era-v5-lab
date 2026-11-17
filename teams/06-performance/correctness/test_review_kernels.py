"""Week-3 code review, area B (Triton kernels and loss): adversarial tests.

Strict xfails mark confirmed defects (REVIEW-B<n>, see the review notes); they turn into
failures the moment a fix lands, so the marker must be removed with the fix.
Passing tests pin edge cases the existing suites do not reach (real vocabulary with forced
forward chunking, |logit| ~ 1e4, N*V >= 2**31, padded+tied head through triton_ce, LayerNorm
at D=8192 / non-power-of-two / zero variance), each against an fp64 reference.
CUDA-only tests skip cleanly without CUDA + Triton.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import pytest
import torch
import torch.nn.functional as F
from torch.utils._python_dispatch import TorchDispatchMode

from kernels import linear_ce_fused as ce
from kernels.linear_ce_fused import linear_cross_entropy_fused_triton
from models.config import ModelConfig
from models.gpt import GPT
from models.linear_ce import linear_cross_entropy_cached, linear_cross_entropy_cce

ROOT = Path(__file__).resolve().parents[1]
CUDA = torch.cuda.is_available() and ce.triton is not None
needs_cuda = pytest.mark.skipif(not CUDA, reason="CUDA + Triton required")


def _ref_fp64(x, w, y, b=None, ignore=-100):
    """Mean CE in fp64 from the definition; 0 when every target is ignored."""
    logits = x.double() @ w.double().T
    if b is not None:
        logits = logits + b.double()
    valid = y != ignore
    lz = torch.logsumexp(logits, -1)
    picked = logits.gather(1, torch.where(valid, y, 0)[:, None]).squeeze(1)
    return torch.where(valid, lz - picked, 0.).sum() / valid.sum().clamp_min(1)


def _grads(loss, params):
    return torch.autograd.grad(loss, params)


def _rel(a, b):
    return ((a.double() - b.double()).norm() / b.double().norm().clamp_min(1e-30)).item()


# ============================================================================ CPU: confirmed defects

@pytest.mark.xfail(strict=True, reason="REVIEW-B2: fused_cce returns a finite, wrong loss for a target id >= vocab "
                                       "(triton_ce gives NaN, fused_cached raises)")
def test_cce_out_of_range_target_is_not_silently_accepted():
    torch.manual_seed(0)
    x, w = torch.randn(4, 8), torch.randn(16, 8)
    y = torch.tensor([1, 2, 16, 3])                      # 16 == vocab: e.g. a padded id after the head is sliced
    loss = linear_cross_entropy_cce(x, w, y, vocab_chunk=8)
    assert not torch.isfinite(loss)                      # fail loudly like triton_ce (NaN) / F.cross_entropy (raise)


class _CountMatmuls(TorchDispatchMode):
    def __init__(self):
        super().__init__()
        self.n = 0

    def __torch_dispatch__(self, func, types, args=(), kwargs=None):
        if func.overloadpacket in (torch.ops.aten.mm, torch.ops.aten.addmm, torch.ops.aten.bmm):
            self.n += 1
        return func(*args, **(kwargs or {}))


@pytest.mark.xfail(strict=True, reason="REVIEW-B3: fused/fused_cached/fused_liger compute dX and dW inside forward "
                                       "even under torch.no_grad (eval) or with frozen inputs: ~3x the head matmuls")
def test_cached_ce_does_no_gradient_work_without_grad():
    torch.manual_seed(0)
    x, w = torch.randn(32, 16), torch.randn(64, 16)
    y = torch.randint(0, 64, (32,))
    with torch.no_grad(), _CountMatmuls() as count:
        linear_cross_entropy_cached(x, w, y, token_chunk=8)
    assert count.n == 4                                  # 4 chunks x 1 logits matmul; today 4 x 3


@pytest.mark.xfail(strict=True, reason="REVIEW-B4: ce_impl=torch (the default) returns a NaN loss for an all-ignored "
                                       "batch (gradients are 0); every memory-bounded ce_impl returns 0")
def test_all_ignored_batch_is_consistent_across_ce_impls():
    cfg = dict(vocab_size=53, block_size=8, n_layer=1, n_head=2, n_embd=16)
    torch.manual_seed(5)
    ref = GPT(ModelConfig(**cfg, ce_impl="fused_cached", ce_token_chunk=4))
    plain = GPT(ModelConfig(**cfg, ce_impl="torch"))
    plain.load_state_dict(ref.state_dict())
    ids = torch.randint(0, 53, (2, 7))
    tgt = torch.full((2, 7), -100)
    _, lf = ref(ids, tgt)
    _, lp = plain(ids, tgt)
    assert lf.item() == 0.0
    assert torch.isfinite(lp)


@pytest.mark.xfail(strict=True, reason="REVIEW-B5: rotation_sandeepkunkunuru seeds its scenarios with hash(str), "
                                       "which PYTHONHASHSEED randomizes: inputs differ on every run")
def test_rotation_scenarios_are_reproducible_across_processes():
    code = ("import sys; sys.path.insert(0, %r); import torch\n"
            "from correctness.rotation_sandeepkunkunuru import _make_scenario\n"
            "x, *_ = _make_scenario('tail33', torch.device('cpu')); print(float(x.detach().sum()))") % str(ROOT)
    outs = set()
    for seed in ("1", "2"):
        env = dict(os.environ, PYTHONHASHSEED=seed)
        outs.add(subprocess.run([sys.executable, "-c", code], env=env, capture_output=True, text=True,
                                check=True, cwd=ROOT).stdout.strip())
    assert len(outs) == 1, outs


# ============================================================================ CPU: contracts and cross-team pins

def test_microbatch_mean_needs_rescale_to_match_g5_full_batch_normalisation():
    """G5 train_week2 divides each microbatch's summed NLL by the FULL batch target count. Every G6 ce_impl returns a
    per-call mean, so plain accumulation of G6 losses weights microbatches unequally; loss * n_local / n_total fixes it."""
    torch.manual_seed(3)
    x, w = torch.randn(12, 8), torch.randn(20, 8)
    y = torch.randint(0, 20, (12,))
    y[:5] = -100                                         # microbatch 1 has 1 target, microbatch 2 has 6
    parts = [(x[:6], y[:6]), (x[6:], y[6:])]
    total = int((y != -100).sum())
    g5 = sum(F.cross_entropy(a @ w.T, t, ignore_index=-100, reduction="sum") for a, t in parts) / total
    naive = sum(linear_cross_entropy_cached(a, w, t, token_chunk=4) for a, t in parts)
    fixed = sum(linear_cross_entropy_cached(a, w, t, token_chunk=4) * int((t != -100).sum()) / total for a, t in parts)
    assert not torch.allclose(naive, g5)
    torch.testing.assert_close(fixed, g5)


@pytest.mark.parametrize("impl", ["cached", "cce"])
def test_portable_paths_match_fp64_with_ignored_rows_and_uneven_chunks(impl):
    torch.manual_seed(7)
    n, h, v = 37, 13, 101
    x = torch.randn(n, h, requires_grad=True)
    w = torch.randn(v, h, requires_grad=True)
    y = torch.randint(0, v, (n,))
    y[::4] = -100
    got = (linear_cross_entropy_cached(x, w, y, token_chunk=5) if impl == "cached"
           else linear_cross_entropy_cce(x, w, y, vocab_chunk=17))
    xr, wr = x.detach().double().requires_grad_(), w.detach().double().requires_grad_()
    ref = _ref_fp64(xr, wr, y)
    torch.testing.assert_close(got.double(), ref, atol=1e-5, rtol=1e-5)
    for a, b in zip(_grads(got, (x, w)), _grads(ref, (xr, wr))):
        assert _rel(a, b) < 1e-5
        assert (a[y == -100].abs().max() == 0) if a.shape[0] == n else True   # ignored rows: exact zero dX


# ============================================================================ CUDA: confirmed defects

@needs_cuda
@pytest.mark.xfail(strict=True, reason="REVIEW-B1: triton_ce returns NaN when one 128-column vocab tile is entirely "
                                       "-inf for a row (max=-inf, exp(-inf - -inf)=NaN); torch is finite")
def test_triton_fully_masked_vocab_tile_is_finite():
    torch.manual_seed(0)
    x, w = torch.randn(5, 16, device="cuda"), torch.randn(256, 16, device="cuda")
    b = torch.zeros(256, device="cuda")
    b[128:] = -float("inf")                              # e.g. a -inf pad bias over a whole BV tile
    y = torch.randint(0, 128, (5,), device="cuda")
    ref = F.cross_entropy(F.linear(x, w, b), y)
    assert torch.isfinite(ref)
    got = linear_cross_entropy_fused_triton(x, w, y, bias=b)
    torch.testing.assert_close(got, ref, atol=1e-5, rtol=1e-5)


# ============================================================================ CUDA: edge cases that hold today

@needs_cuda
@pytest.mark.parametrize("backward_impl", ["vocab", "chunked", "recompute"])
def test_triton_real_vocab_forced_forward_chunks_matches_fp64(backward_impl):
    """V=131072 (frozen tokenizer), scratch_mb=1 forces 85-row forward chunks, rows not multiple of BM, eos target."""
    torch.manual_seed(11)
    n, h, v = 200, 16, 131072
    x = torch.randn(n, h, device="cuda", requires_grad=True)
    w = (torch.randn(v, h, device="cuda") * 0.1).requires_grad_()
    y = torch.randint(0, v, (n,), device="cuda")
    y[::7] = -100
    y[1], y[2], y[-1] = 130822, v - 1, 0                 # eos id, last class, first class
    assert ce.forward_chunk_rows(n, ce.triton.cdiv(v, ce.BV), 1024**2) < n
    got = linear_cross_entropy_fused_triton(x, w, y, scratch_mb=1, backward_impl=backward_impl, token_chunk=33)
    xr, wr = x.detach().double().requires_grad_(), w.detach().double().requires_grad_()
    ref = _ref_fp64(xr, wr, y)
    torch.testing.assert_close(got.double(), ref, atol=1e-5, rtol=1e-5)
    gx, gw = _grads(got, (x, w))
    rx, rw = _grads(ref, (xr, wr))
    assert _rel(gx, rx) < 1e-5 and _rel(gw, rw) < 1e-5
    assert gx[y == -100].abs().max() == 0


@needs_cuda
def test_triton_huge_logits_are_stable():
    torch.manual_seed(13)
    x = (torch.randn(37, 16, device="cuda") * 100).requires_grad_()
    w = (torch.randn(300, 16, device="cuda") * 10).requires_grad_()
    y = torch.randint(0, 300, (37,), device="cuda")
    assert F.linear(x, w).abs().max() > 5e3
    got = linear_cross_entropy_fused_triton(x, w, y)
    xr, wr = x.detach().double().requires_grad_(), w.detach().double().requires_grad_()
    ref = _ref_fp64(xr, wr, y)
    torch.testing.assert_close(got.double(), ref, rtol=1e-5, atol=1e-3)
    for a, b in zip(_grads(got, (x, w)), _grads(ref, (xr, wr))):
        assert torch.isfinite(a).all() and _rel(a, b) < 1e-4


@needs_cuda
def test_triton_bf16_autocast_real_vocab_error_no_worse_than_torch():
    if not torch.cuda.is_bf16_supported():
        pytest.skip("no bf16")
    torch.manual_seed(17)
    n, h, v = 64, 64, 131072
    x = torch.randn(n, h, device="cuda", requires_grad=True)
    w = (torch.randn(v, h, device="cuda") * 0.05).requires_grad_()
    y = torch.randint(0, v, (n,), device="cuda")
    y[::3] = -100
    xr, wr = x.detach().double().requires_grad_(), w.detach().double().requires_grad_()
    ref = _ref_fp64(xr, wr, y)
    rg = _grads(ref, (xr, wr))
    xt, wt = x.detach().clone().requires_grad_(), w.detach().clone().requires_grad_()
    with torch.autocast("cuda", dtype=torch.bfloat16):
        lt = F.cross_entropy(F.linear(xt, wt).float(), y)
        lg = linear_cross_entropy_fused_triton(x, w, y)
    tg, gg = _grads(lt, (xt, wt)), _grads(lg, (x, w))
    assert abs(lg.double() - ref).item() <= 2 * abs(lt.double() - ref).item() + 1e-4
    for a, t, r in zip(gg, tg, rg):
        assert _rel(a, r) <= 2 * _rel(t, r) + 1e-4


@needs_cuda
@pytest.mark.parametrize("mode", ["mask", "slice"])
@pytest.mark.parametrize("mtp", [False, True])
def test_triton_ce_padded_tied_head_matches_torch(mode, mtp):
    """test_vocab_pad.py leaves triton_ce out of its memory-bounded list: padded (53->64) + tied head + MTP here."""
    cfg = dict(vocab_size=53, vocab_pad_multiple=64, vocab_pad_mode=mode, block_size=8, n_layer=1, n_head=2,
               n_embd=32, tie_embeddings=True, mtp=mtp)
    torch.manual_seed(19)
    ref = GPT(ModelConfig(**cfg, ce_impl="torch")).cuda()
    got = GPT(ModelConfig(**cfg, ce_impl="triton_ce", ce_triton_chunk=3)).cuda()
    got.load_state_dict(ref.state_dict())
    ids = torch.randint(0, 53, (2, 8), device="cuda")
    tgt = torch.randint(0, 53, (2, 8), device="cuda")
    tgt[0, 3] = -100
    _, lr = ref(ids, tgt)
    _, lg = got(ids, tgt)
    lr.backward()
    lg.backward()
    torch.testing.assert_close(lg, lr, atol=1e-5, rtol=1e-5)
    assert got.head.weight is got.tok.weight
    assert got.head.weight.grad[53:].abs().max() == 0
    for (name, p), (_, q) in zip(ref.named_parameters(), got.named_parameters()):
        torch.testing.assert_close(q.grad, p.grad, atol=5e-5, rtol=5e-5, msg=name)


@needs_cuda
def test_triton_n_times_v_beyond_int32():
    """N*V >= 2**31 logits (never materialised): loss and dX against a row-chunked fp32 reference."""
    torch.manual_seed(23)
    n, h, v = 16400, 16, 131072
    assert n * v >= 2**31
    x = torch.randn(n, h, device="cuda", dtype=torch.bfloat16, requires_grad=True)
    w = (torch.randn(v, h, device="cuda") * 0.1).to(torch.bfloat16).requires_grad_()
    y = torch.randint(0, v, (n,), device="cuda")
    y[-1] = v - 1
    loss = linear_cross_entropy_fused_triton(x, w, y)
    (gx,) = torch.autograd.grad(loss, (x,))
    total, dx = torch.zeros((), device="cuda", dtype=torch.float64), torch.empty(n, h, device="cuda")
    w32 = w.detach().float()
    for s in range(0, n, 2048):
        lg = x.detach()[s:s + 2048].float() @ w32.T
        total += F.cross_entropy(lg, y[s:s + 2048], reduction="sum").double()
        p = lg.softmax(-1)
        p[torch.arange(p.shape[0]), y[s:s + 2048]] -= 1
        dx[s:s + 2048] = (p @ w32) / n
        del lg, p
    torch.testing.assert_close(loss.double(), total / n, atol=1e-3, rtol=1e-4)
    assert torch.isfinite(gx).all()
    assert _rel(gx[-2048:].float(), dx[-2048:]) < 2e-2      # tail rows, where 64-bit offsets matter


# ---------------------------------------------------------------------------- LayerNorm

@needs_cuda
@pytest.mark.parametrize("d,dtype", [(8192, torch.bfloat16), (8192, torch.float32), (4097, torch.float32),
                                     (6000, torch.float16), (3, torch.float32)])
@pytest.mark.parametrize("case", ["randn", "zero_var", "offset"])
def test_layer_norm_error_no_worse_than_torch(d, dtype, case):
    if d == 3 and case != "randn":
        # D=3: the fp32 mean of a constant/offset row is off by an ulp in both backends (torch shows the same at
        # D=1000); times rstd=1/sqrt(eps) that is ~1e-3 in the output for either. Not a kernel defect.
        pytest.skip("rounding-dominated at D=3")
    from kernels.layer_norm import layer_norm_triton
    torch.manual_seed(29)
    x = torch.randn(37, d, device="cuda")
    if case == "zero_var":
        x[::2] = 3.0                                     # constant rows: var = 0, rstd = 1/sqrt(eps)
    elif case == "offset":
        x = 100.0 + x * 1e-2                             # large mean, small spread
    x = x.to(dtype)
    w, b = torch.randn(d, device="cuda", dtype=dtype), torch.randn(d, device="cuda", dtype=dtype)
    g = torch.randn_like(x)
    r = [t.detach().double().requires_grad_() for t in (x, w, b)]
    yr = F.layer_norm(r[0], (d,), r[1], r[2], 1e-5)
    rg = torch.autograd.grad(yr, r, g.double())
    a = [t.detach().clone().requires_grad_() for t in (x, w, b)]
    ya = layer_norm_triton(*a, 1e-5)
    ag = torch.autograd.grad(ya, a, g)
    t = [t.detach().clone().requires_grad_() for t in (x, w, b)]
    yt = F.layer_norm(t[0], (d,), t[1], t[2], 1e-5)
    tg = torch.autograd.grad(yt, t, g)

    def err(u, v):
        return ((u.double() - v).abs().max() / v.abs().max().clamp_min(1.0)).item()

    assert err(ya, yr) <= 2 * err(yt, yr) + 1e-6
    for got, tor, ref in zip(ag, tg, rg):
        assert torch.isfinite(got).all()
        assert err(got, ref) <= 2 * err(tor, ref) + 1e-6
