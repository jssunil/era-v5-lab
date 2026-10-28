"""perfkit/report.py: compare() refuses a baseline pair that does not time the same committed code."""
from __future__ import annotations

import copy

from perfkit import report
from perfkit.schema import example_run


def _pair(**b_meta):
    a = example_run()
    b = copy.deepcopy(a)
    b["meta"].update(tag="b", **b_meta)
    return a, b


def test_same_clean_commit_passes():
    _, ok, problems = report.compare(*_pair())
    assert ok and problems == []


def test_different_commit_is_refused():
    _, ok, problems = report.compare(*_pair(commit="1" * 40))
    assert not ok and any("different commit" in p for p in problems)


def test_dirty_or_unknown_tree_is_refused():
    for dirty in (True, None):
        _, ok, problems = report.compare(*_pair(dirty=dirty))
        assert not ok and any(f"dirty={dirty}" in p for p in problems)


# ------------------------------------------------------------------------------ exact timing diagnostics in Markdown

def test_render_shows_per_stage_cuda_allocation_diagnostics():
    run = example_run()
    run["clean"]["events_created_during_steps"] = 0
    run["layer"] = {"events_created_during_steps": 2,
                    "inner_pass": {"events_created_during_steps": 4}}
    run["comm"] = {"moe_a2a": {"events_created_during_steps": 3}}
    run["warnings"] = ["9 CUDA timing events were created during measured steps"]
    md = report.render(run)
    assert "[OK] clean: events_created_during_steps=0" in md
    assert "[WARN] layer: events_created_during_steps=2" in md
    assert "[WARN] layer.inner_pass: events_created_during_steps=4" in md
    assert "[WARN] communication: events_created_during_steps=3" in md
    assert "[warn] 9 CUDA timing events were created during measured steps" in md


def test_render_preserves_exact_warning_text_and_no_false_ke_claim():
    run = example_run()
    run["warnings"] = ["recorder overhead 3.2% > 2.0%: layer numbers are flagged"]
    md = report.render(run)
    assert "[warn] recorder overhead 3.2% > 2.0%: layer numbers are flagged" in md
    assert "Consult pytest output" in md
    assert "test_ke.py::" not in md  # not present in benchmark run JSON
