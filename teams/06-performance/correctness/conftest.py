"""pytest setup for the correctness tests.

  * Puts teams/06-performance on sys.path, so `pytest teams/06-performance/correctness` works from the
    repo root (the Gate 1 command) as well as from teams/06-performance.
  * `device` fixture: cuda if available, else cpu.
  * A test that hits a stub (NotImplementedError) is reported as SKIPPED with the stub's name, not failed.
    `pytest -rs` lists them. At Gate 1 no skip may be left.
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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if call.excinfo is not None and call.excinfo.errisinstance(NotImplementedError):
        rep.outcome = "skipped"
        rep.longrepr = (str(item.path), item.location[1] or 0, f"stub: {call.excinfo.value}")
