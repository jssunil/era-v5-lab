"""Reference-vs-fast checks.  [CONTRACT implemented: Case / Pair / pair registry; checks STUB]

Registering a pair (anyone, in correctness/test_<topic>.py):

    @pair("moe.loop", tol=1e-4, grad_tol=1e-3)
    def _(device):
        ...
        return Case(ref=ref_fn, fast=fast_fn, inputs=[x], params_ref=[...], params_fast=[...])

Rules: the reference is written independently from the definition, in fp64, never by calling the
fast code. tolerances < 1e-2 always (so a 1.01 error fails).

MVP
  * rel_err(fast, ref) = ||fast - ref|| / ||ref|| in fp64; AssertionError on shape mismatch or NaN/Inf.
  * check(pair, device, fast_override=None): build the Case; clone the inputs (fp64 copy for ref);
    compare every output; backpropagate the SAME random cotangent through both; compare the grads of
    inputs that require grad and of params_fast vs params_ref. AssertionError naming the pair, the
    tensor, the error and the tolerance. Returns {name: error}.
  * scaled(k=1.01): wraps a fast function so its outputs are multiplied by k.
Do not use torch.allclose defaults: in bf16 (rtol 1.6e-2) they let a 1% error pass.

Precision: pairs compare the fast code in fp32 against the fp64 reference, so tol < 1e-2 is easy and the
1.01 drill bites. bf16 errors are often larger than 1e-2 / 3 (bf16 has 8 mantissa bits), so do NOT make a
bf16 @pair with a loosened tolerance. Check bf16 behaviour with plain property tests and a stated
threshold (e.g. reversible reconstruction_error < 1e-3), outside the 1.01 drill.
"""
from __future__ import annotations

import copy
from dataclasses import dataclass, field
from typing import Callable

PAIRS: dict = {}
DEFAULT_TOL = 1e-4


@dataclass
class Case:
    ref: Callable
    fast: Callable
    inputs: list
    params_ref: list = field(default_factory=list)
    params_fast: list = field(default_factory=list)
    grads: bool = True


@dataclass
class Pair:
    name: str
    build: Callable          # device -> Case
    tol: float = DEFAULT_TOL
    grad_tol: float | None = None


def pair(name, tol=DEFAULT_TOL, grad_tol=None):
    assert tol < 1e-2 and (grad_tol is None or grad_tol < 1e-2), f"{name}: tolerance must be < 1e-2"

    def deco(fn):
        assert name not in PAIRS, f"duplicate pair {name}"
        PAIRS[name] = Pair(name, fn, tol, grad_tol)
        return fn
    return deco


def pairs_in(module_name):
    """Names of the pairs a test module registered (for pytest.mark.parametrize)."""
    return [n for n, p in PAIRS.items() if p.build.__module__ == module_name]


def to64(module):
    """fp64 deep copy of a module, for references."""
    return copy.deepcopy(module).double()


def rel_err(fast, ref) -> float:
    raise NotImplementedError("rel_err")


def check(p: Pair, device, fast_override=None) -> dict:
    raise NotImplementedError("check")


def scaled(k=1.01):
    raise NotImplementedError("scaled")
