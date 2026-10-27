"""The framework must catch broken code.

Checks, for EVERY registered pair:

  * import every correctness/test_*.py so all pairs are registered
  * for each pair below the drill tolerance (every fp32 pair): check(pair, device, fast_override=scaled(1.01))
    must raise AssertionError
  * a toy pair: correct passes; wrong gradient (x1.01 in backward only) fails; NaN fails; wrong shape fails
  * rel_err(x * 1.01, x) == 0.01
  * check on model-like cases: two outputs through a backward that may run only once (the reversible stack),
    a parameter with no gradient on both sides (an MoE expert with no tokens), a detached fast output fails
  * tolerances: fp32 defaults from TOLERANCES, fp32 >= 1e-2 refused, bf16 pairs are kept out of the drill
"""
from __future__ import annotations

import importlib
from pathlib import Path

import pytest
import torch

from correctness.framework import Case, PAIRS, Pair, check, pair, rel_err, scaled

parametrize = pytest.mark.parametrize


def _import_all_test_modules() -> None:
    here = Path(__file__).resolve().parent
    for path in sorted(here.glob("test_*.py")):
        if path.name == Path(__file__).name:
            continue
        importlib.import_module(path.stem)


_import_all_test_modules()


@pair("_framework.toy", tol=1e-4)
def _toy_pair(device):
    def ref_fn(x):
        return x * 2

    def fast_fn(x):
        return x * 2

    x = torch.randn(3, 3, device=device, dtype=torch.float32, requires_grad=True)
    return Case(ref=ref_fn, fast=fast_fn, inputs=[x], grads=True)


class _ScaleBwd(torch.autograd.Function):
    @staticmethod
    def forward(ctx, y, k):
        ctx.k = k
        return y

    @staticmethod
    def backward(ctx, g):
        return g * ctx.k, None


def test_rel_err_one_percent():
    x = torch.randn(8, 8, dtype=torch.float64)
    err = rel_err(x * 1.01, x)
    assert abs(err - 0.01) < 1e-9


def test_rel_err_shape_mismatch():
    with pytest.raises(AssertionError, match="shape"):
        rel_err(torch.zeros(2), torch.zeros(3))


def test_rel_err_nan():
    a = torch.tensor([1.0, float("nan")])
    b = torch.tensor([1.0, 1.0])
    with pytest.raises(AssertionError, match="NaN/Inf"):
        rel_err(a, b)


def test_toy_correct_passes(device):
    errors = check(PAIRS["_framework.toy"], device)
    assert "out[0]" in errors
    assert errors["out[0]"] < 1e-4


def test_toy_scaled_fails(device):
    with pytest.raises(AssertionError):
        check(PAIRS["_framework.toy"], device, fast_override=scaled(1.01))


def test_wrong_gradient_fails(device):
    def build(dev):
        def ref_fn(x):
            return x * 2

        def fast_fn(x):
            return _ScaleBwd.apply(x * 2, 1.01)

        x = torch.randn(5, device=dev, dtype=torch.float32, requires_grad=True)
        return Case(ref=ref_fn, fast=fast_fn, inputs=[x], grads=True)

    p = Pair("_framework.bad_grad", build, tol=1e-4)
    with pytest.raises(AssertionError, match="grad"):
        check(p, device)


def test_nan_output_fails(device):
    def build(dev):
        def ref_fn(x):
            return x * 2

        def fast_fn(x):
            return x * 2 + torch.nan

        x = torch.randn(2, 2, device=dev, dtype=torch.float32, requires_grad=True)
        return Case(ref=ref_fn, fast=fast_fn, inputs=[x], grads=False)

    p = Pair("_framework.nan", build, tol=1e-4)
    with pytest.raises(AssertionError, match="NaN/Inf"):
        check(p, device)


def test_wrong_shape_fails(device):
    def build(dev):
        def ref_fn(x):
            return x * 2

        def fast_fn(x):
            return (x * 2).flatten()

        x = torch.randn(2, 2, device=dev, dtype=torch.float32, requires_grad=True)
        return Case(ref=ref_fn, fast=fast_fn, inputs=[x], grads=False)

    p = Pair("_framework.shape", build, tol=1e-4)
    with pytest.raises(AssertionError, match="shape"):
        check(p, device)


@parametrize("name", sorted(n for n, p in PAIRS.items() if p.drill))
def test_every_registered_pair_scaled_fails(name, device):
    with pytest.raises(AssertionError):
        check(PAIRS[name], device, fast_override=scaled(1.01))


class _OnceBackward(torch.autograd.Function):
    """Like ReversibleStack: the backward frees its state, so a second backward fails."""

    @staticmethod
    def forward(ctx, x):
        ctx.state = "saved"
        return x * 2

    @staticmethod
    def backward(ctx, g):
        assert ctx.state is not None, "backward ran twice"
        ctx.state = None
        return g * 2


def test_two_outputs_one_backward(device):
    def build(dev):
        def ref_fn(x):
            y = x * 2
            return y, y.sum()

        def fast_fn(x):
            y = _OnceBackward.apply(x)
            return y, y.sum()

        x = torch.randn(4, device=dev, dtype=torch.float32, requires_grad=True)
        return Case(ref=ref_fn, fast=fast_fn, inputs=[x])

    errors = check(Pair("_framework.two_outputs", build), device)
    assert {"out[0]", "out[1]", "grad_in[0]"} <= set(errors)


def test_unused_param_has_no_grad_on_both_sides(device):
    def build(dev):
        w_fast = torch.randn(3, device=dev, requires_grad=True)
        unused_fast = torch.randn(3, device=dev, requires_grad=True)
        w_ref, unused_ref = (t.detach().double().requires_grad_(True) for t in (w_fast, unused_fast))
        return Case(ref=lambda x: x * w_ref, fast=lambda x: x * w_fast,
                    inputs=[torch.randn(3, device=dev)],
                    params_ref=[w_ref, unused_ref], params_fast=[w_fast, unused_fast])

    errors = check(Pair("_framework.unused_param", build), device)
    assert "grad_param[0]" in errors and "grad_param[1]" not in errors


def test_detached_fast_output_fails(device):
    def build(dev):
        x = torch.randn(3, device=dev, requires_grad=True)
        return Case(ref=lambda x: x * 2, fast=lambda x: (x * 2).detach(), inputs=[x])

    with pytest.raises(AssertionError, match="requires_grad"):
        check(Pair("_framework.detached", build), device)


def test_tolerances_per_dtype():
    from correctness.framework import TOLERANCES
    fp32 = Pair("_framework.fp32", _toy_pair)
    assert (fp32.tol, fp32.gtol) == TOLERANCES[torch.float32] and fp32.drill
    with pytest.raises(AssertionError, match="fp32 tolerance"):
        pair("_framework.too_loose", tol=1e-2)
    bf16 = Pair("_framework.bf16", _toy_pair, *TOLERANCES[torch.bfloat16], dtype=torch.bfloat16)
    assert not bf16.drill
    with pytest.raises(AssertionError, match="no tolerances"):
        pair("_framework.fp8", dtype=torch.float8_e4m3fn)


# ------------------------------------------------------------------------------ determinism (Task 3)
# "Determinism: running the fast version twice gives identical bits." (G6_Team_Task_Plan.md, Task 3)
# The parity tolerance (1e-5) cannot see a kernel that is wrong by 1e-9 from run to run, so these toy pairs
# are wrong by WOBBLE per call: they pass parity and must fail the determinism check.
# WOBBLE = 1e-6 is chosen on purpose: it is above the fp32 resolution of the values used here (about 5e-7, so
# the two runs really differ in their bits) and far below the parity tolerance (1e-5 relative), so parity
# still passes. A smaller wobble such as 1e-9 would be rounded away in fp32 and prove nothing.
WOBBLE = 1e-6

class _CallCounter:
    """Counts how often the fast side runs, so a test can tell one run from two."""

    def __init__(self):
        self.n = 0


def _wobbly_pair(counter, *, deterministic=True, wobble_in="output"):
    """Fast code equals the reference up to a WOBBLE offset that changes on every call."""

    class Noisy(torch.autograd.Function):          # a forward that is exact and a backward that wobbles
        @staticmethod
        def forward(ctx, x):
            return x * 2

        @staticmethod
        def backward(ctx, g):
            counter.n += 1
            return g * 2 + WOBBLE * counter.n

    def build(device):
        x = torch.randn(4, device=device, dtype=torch.float32, requires_grad=True)

        def fast(a):
            counter.n += 1
            if wobble_in == "gradient":
                return Noisy.apply(a)
            return a * 2 + WOBBLE * counter.n          # forward output differs between two runs

        return Case(ref=lambda a: a * 2, fast=fast, inputs=[x])

    return Pair("_framework.wobbly", build, deterministic=deterministic)


def test_a_wobbly_output_passes_parity_but_fails_determinism(device):
    p = _wobbly_pair(_CallCounter())
    with pytest.raises(AssertionError, match="not deterministic"):
        check(p, device)


def test_a_wobbly_gradient_fails_determinism(device):
    p = _wobbly_pair(_CallCounter(), wobble_in="gradient")
    with pytest.raises(AssertionError, match=r"grad_in\[0\].*not deterministic"):
        check(p, device)


def test_deterministic_false_opts_out(device):
    # By design non-deterministic code (for example a CUDA atomic scatter) registers with deterministic=False.
    p = _wobbly_pair(_CallCounter(), deterministic=False)
    assert check(p, device)                       # parity still has to pass


def test_the_fast_side_runs_twice_when_deterministic_and_once_when_not(device):
    for deterministic, runs in ((True, 2), (False, 1)):
        calls = _CallCounter()

        def build(dev, calls=calls):
            x = torch.randn(4, device=dev, requires_grad=True)

            def fast(a):
                calls.n += 1
                return a * 2

            return Case(ref=lambda a: a * 2, fast=fast, inputs=[x], grads=False)

        check(Pair("_framework.runs", build, deterministic=deterministic), device)
        assert calls.n == runs


def test_the_1_01_drill_does_not_run_the_second_pass(device):
    calls = _CallCounter()

    def build(dev):
        x = torch.randn(4, device=dev)

        def fast(a):
            calls.n += 1
            return a * 2

        return Case(ref=lambda a: a * 2, fast=fast, inputs=[x], grads=False)

    with pytest.raises(AssertionError, match="rel_err"):         # it fails on parity, as the drill expects
        check(Pair("_framework.drill", build), device, fast_override=scaled(1.01))
    assert calls.n == 1


def test_pair_decorator_passes_deterministic_to_the_registry():
    @pair("_framework.det_flag", deterministic=False)
    def _(device):
        raise NotImplementedError

    assert PAIRS["_framework.det_flag"].deterministic is False
    assert PAIRS["_framework.toy"].deterministic is True          # the default: every pair is checked
