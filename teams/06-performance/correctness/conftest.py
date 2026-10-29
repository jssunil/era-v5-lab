"""pytest setup for the correctness tests.

  * Puts teams/06-performance on sys.path, so `pytest teams/06-performance/correctness` works from the
    repo root (the Gate 1 command) as well as from teams/06-performance.
  * `device` fixture: cuda if available, else cpu.
  * A test that hits a stub (NotImplementedError) is reported as SKIPPED with the stub's name, not failed.
    `pytest -rs` lists them. At Gate 1 no stub skip may be left (skips for missing CUDA / bf16 are expected
    on a laptop).
  * At the end of the run: one row per pair, grouped by area: the worst output and gradient error, how much
    of the tolerance it uses, whether two runs were bit-identical, and PASS/FAIL with the first failure line.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest
import torch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


@pytest.fixture
def device():
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


FAILED_PAIRS: dict = {}              # pair name -> first line of its failure (filled by the hook below)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if call.excinfo is not None and call.excinfo.errisinstance(NotImplementedError):
        rep.outcome = "skipped"
        rep.longrepr = (str(item.path), item.location[1] or 0, f"stub: {call.excinfo.value}")
    elif rep.failed and call.excinfo is not None:
        name = getattr(item, "callspec", None) and item.callspec.params.get("name")
        if isinstance(name, str):
            first = str(call.excinfo.value).strip().splitlines()[0] if str(call.excinfo.value).strip() else ""
            FAILED_PAIRS[name] = first.removeprefix(f"{name}: ")


def _used(err, tol) -> str:
    """How much of the tolerance the error uses: '3%' (fine) ... '100%+' (over)."""
    if err is None:
        return ""
    pct = 100 * err / tol
    return "<1%" if pct < 1 else f"{pct:.0f}%"


def pytest_terminal_summary(terminalreporter):
    """Each pair's worst error against its tolerance (the Instructor asked for every test's error)."""
    from correctness.framework import RESULTS, TOLERANCES
    names = sorted(set(RESULTS) | set(FAILED_PAIRS))
    if not names:
        return
    tr = terminalreporter
    tr.section("correctness: every pair, fast vs fp64 reference (worst relative error)")
    tr.write_line("used = error / tolerance. repeat = two runs of the fast code are bit-identical.")
    head = f"{'pair':32s} {'dtype':9s} {'output':>9s} {'used':>5s}   {'gradient':>9s} {'used':>5s}   {'repeat':10s} result"
    tr.write_line(head)
    tr.write_line("-" * len(head))
    area = None
    for name in names:
        if area is not None and name.split(".")[0] != area:
            tr.write_line("")
        area = name.split(".")[0]
        if name in FAILED_PAIRS:
            tr.write_line(f"{name:32s} {'':9s} {'':>9s} {'':>5s}   {'':>9s} {'':>5s}   {'':10s} FAIL  {FAILED_PAIRS[name]}",
                          red=True)
            continue
        r = RESULTS[name]
        grad = "-" if r["grad"] is None else f"{r['grad']:.2e}"
        tr.write_line(f"{name:32s} {r['dtype']:9s} {r['out']:9.2e} {_used(r['out'], r['tol']):>5s}   "
                      f"{grad:>9s} {_used(r['grad'], r['grad_tol']):>5s}   {r.get('repeat', ''):10s} PASS")
    tr.write_line("-" * len(head))
    tol = ", ".join(f"{str(d).replace('torch.', '')} {o:g} / {g:g}" for d, (o, g) in TOLERANCES.items())
    failed = len(FAILED_PAIRS)
    tr.write_line(f"{len(names)} pairs: {len(names) - failed} PASS, {failed} FAIL.   tolerance (output / gradient): {tol}",
                  red=bool(failed), green=not failed)
