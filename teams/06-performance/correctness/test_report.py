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


def test_same_commit_muon_implementation_variants_can_be_compared():
    a, b = _pair()
    a["config"]["optim"].update(name="muon", muon_impl="loop")
    b["config"]["optim"].update(name="muon", muon_impl="batched")
    _, ok, problems = report.compare(a, b)
    assert ok and problems == []


def test_same_commit_moe_dispatch_variants_can_be_compared():
    a, b = _pair()
    a["config"]["model"]["moe"] = {"dispatch": "loop", "num_experts": 8}
    b["config"]["model"]["moe"] = {"dispatch": "sorted", "num_experts": 8}
    _, ok, problems = report.compare(a, b)
    assert ok and problems == []
    assert "model.moe.dispatch: loop vs sorted" in report.ab_note(a, b)
    assert "A/B" in report.baseline_md(a, b, [], ok, problems)


def test_same_implementation_is_not_labelled_ab():
    a, b = _pair()
    assert report.ab_note(a, b) is None
    assert "A/B" not in report.baseline_md(a, b, [], True, [])


def test_moe_setting_other_than_dispatch_is_still_refused():
    a, b = _pair()
    a["config"]["model"]["moe"] = {"dispatch": "loop", "num_experts": 8}
    b["config"]["model"]["moe"] = {"dispatch": "sorted", "num_experts": 4}
    _, ok, problems = report.compare(a, b)
    assert not ok and "different model config" in problems


def test_different_commit_is_refused():
    _, ok, problems = report.compare(*_pair(commit="1" * 40))
    assert not ok and any("different commit" in p for p in problems)


def test_dirty_or_unknown_tree_is_refused():
    for dirty in (True, None):
        _, ok, problems = report.compare(*_pair(dirty=dirty))
        assert not ok and any(f"dirty={dirty}" in p for p in problems)
