"""perfkit/report.py.

  * compare(): refuses a baseline pair that does not time the same committed code (other commit, dirty or unknown
    tree) or that changes a MoE setting other than dispatch; accepts and labels A/B a pair that differs only in
    optim.muon_impl or model.moe.dispatch.
  * render(): the CUDA timing-event allocation diagnostics per stage and the run's warnings, word for word.
  * compare() applies the 5% / abs_tol_ms rule (report.gate); the checkpoint copy GPU -> CPU is gated, the disk
    write is information only; report.report_settings() fills in keys an older run JSON lacks.
"""
from __future__ import annotations

import copy
import json

import pytest

from perfkit import report
from perfkit.schema import example_run


def _pair(**b_meta):
    a = example_run()
    b = copy.deepcopy(a)
    b["meta"].update(tag="b", **b_meta)
    return a, b


def test_same_clean_commit_passes():
    _, ok, problems = report.compare(*_pair(), 5.0, 2, 0.0)
    assert ok and problems == []


def test_same_commit_muon_implementation_variants_can_be_compared():
    a, b = _pair()
    a["config"]["optim"].update(name="muon", muon_impl="loop")
    b["config"]["optim"].update(name="muon", muon_impl="batched")
    _, ok, problems = report.compare(a, b, 5.0, 2, 0.0)
    assert ok and problems == []


def test_same_commit_moe_dispatch_variants_can_be_compared():
    a, b = _pair()
    a["config"]["model"]["moe"] = {"dispatch": "loop", "num_experts": 8}
    b["config"]["model"]["moe"] = {"dispatch": "sorted", "num_experts": 8}
    _, ok, problems = report.compare(a, b, 5.0, 2, 0.0)
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
    _, ok, problems = report.compare(a, b, 5.0, 2, 0.0)
    assert not ok and "different model config" in problems


def test_different_commit_is_refused():
    _, ok, problems = report.compare(*_pair(commit="1" * 40), 5.0, 2, 0.0)
    assert not ok and any("different commit" in p for p in problems)


def test_dirty_or_unknown_tree_is_refused():
    for dirty in (True, None):
        _, ok, problems = report.compare(*_pair(dirty=dirty), 5.0, 2, 0.0)
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
    assert "[WARN] communication.max_rank: events_created_during_steps=3" in md
    assert "[warn] 9 CUDA timing events were created during measured steps" in md


def test_render_preserves_exact_warning_text_and_no_false_ke_claim():
    run = example_run()
    run["warnings"] = ["recorder overhead 3.2% > 2.0%: layer numbers are flagged"]
    md = report.render(run)
    assert "[warn] recorder overhead 3.2% > 2.0%: layer numbers are flagged" in md
    assert md.count("[warn] recorder overhead 3.2%") == 1


# Sunil PR24 review regression: distinct pool-counter diagnostics
def test_render_flags_inner_pool_allocation_when_timer_count_is_zero():
    run = example_run()
    run["layer"] = {"events_created_during_steps": 0,
                    "inner_pass": {"events_created_during_steps": 0,
                                   "events_created_while_measuring": 57}}
    run["warnings"] = ["57 recorder-pool CUDA events were created during layer.inner_pass measured steps"]
    md = report.render(run)
    assert "[OK] layer: events_created_during_steps=0" in md
    assert "[WARN] layer.inner_pass.recorder_pool: events_created_while_measuring=57" in md
    assert "[warn] 57 recorder-pool CUDA events" in md


def _with_part(run, name, ms):
    run["layer"]["regions"][name] = dict(next(iter(run["layer"]["regions"].values())), median=ms, level=1)
    return run


@pytest.mark.parametrize("x, y, abs_tol, verdict", [
    (0.031, 0.035, 0.05, "ok_abs"),        # 12.9% apart but 0.004 ms
    (0.031, 0.035, 0.0, "FAIL"),           # no floor: the 5% rule alone
    (20.0, 20.9, 0.05, "ok"),              # 4.5%
    (20.0, 21.2, 0.05, "FAIL"),            # 6%
    (1.0, 1.06, 0.05, "FAIL"),             # 6% and 0.06 ms: just over the floor
    (0.569, 0.031, 0.05, "FAIL"),
])
def test_compare_applies_the_5_percent_or_abs_tol_rule(x, y, abs_tol, verdict):
    a, b = _pair()
    _with_part(a, "data", x)
    _with_part(b, "data", y)
    rows, ok, _ = report.compare(a, b, 5.0, 2, abs_tol)
    row = next(r for r in rows if r[0] == "data")
    assert row[1:3] == (x, y) and row[4] == verdict
    assert ok == (verdict != "FAIL")


def test_compare_checkpoint_copy_is_gated_and_disk_write_is_information_only():
    a, b = _pair()
    mk = lambda copy_ms, write_ms: {"save_ms": {"median": copy_ms + write_ms}, "to_cpu_ms": {"median": copy_ms},
                                    "write_ms": {"median": write_ms}}
    a["checkpoint"], b["checkpoint"] = mk(37.0, 300.0), mk(37.0, 450.0)
    rows, ok, _ = report.compare(a, b, 5.0, 2, 0.05)
    verdict = {r[0]: r[4] for r in rows}
    assert ok and verdict[report.CKPT_COPY] == "ok" and verdict[report.CKPT_WRITE] == "info"
    b["checkpoint"] = mk(60.0, 300.0)                                   # the copy moved 62%: that does fail
    rows, ok, _ = report.compare(a, b, 5.0, 2, 0.05)
    assert not ok and {r[0]: r[4] for r in rows}[report.CKPT_COPY] == "FAIL"


def test_compare_lines_report_both_times_for_parts_that_pass_on_the_floor():
    a, b = _pair()
    _with_part(a, "data", 0.031)
    _with_part(b, "data", 0.035)
    rows, ok, problems = report.compare(a, b, 5.0, 2, 0.05)
    text = "\n".join(report.compare_lines(rows, ok, problems, None, 5.0, 2, 0.05))
    assert "0.031" in text and "0.035" in text and "0.004" in text and "ok (< 0.05 ms)" in text
    assert "(1 by the 0.05 ms rule)" in text


def test_report_cli_works_on_a_run_json_written_before_abs_tol_ms(tmp_path, capsys):
    """Run JSONs from before the 0.05 ms rule have no report.abs_tol_ms; report --compare must still work."""
    a = example_run()
    del a["config"]["report"]["abs_tol_ms"], a["config"]["report"]["min_compare_steps"]
    b = copy.deepcopy(a)
    b["meta"]["tag"] = "b"
    pa, pb = tmp_path / "a.json", tmp_path / "b.json"
    pa.write_text(json.dumps(a))
    pb.write_text(json.dumps(b))
    assert report.report_settings(a)["abs_tol_ms"] == 0.05
    assert report.main([str(pa), "--compare", str(pb)]) == 0
    assert "PASS" in capsys.readouterr().out
