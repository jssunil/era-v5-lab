"""perfkit/bench.py: the harness runs end to end, writes a valid run JSON, and follows the Instructor's rules.

Everything runs on the CPU with a tiny model and a fake Loader, so the tests need no GPU, no data download and no
network (the real Loader fetches the pinned BrahmicTokenizer-131K artifact). The fake Loader has the same
constructor and attributes as dataio.loader.Loader.

  * build: the Loader gets data.tokenizer_path; dtype fallbacks (B3); the LR-schedule note.
  * run metadata: tokenizer revision and sha256, vocab size (rule 1a).
  * rule_checks: dirty tree, wrong vocabulary (1a), level < 3 (3a), checkpoint / comm not measured (3b).
  * quick_compare: the 5% check on the whole step and every part at level <= gate_level.
  * write_run / _finite: unique file names, NaN and inf become null.
  * main: clean + layer + checkpoint run, validate_run returns [], the parts are there, exit codes 0 and 2.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest
import torch

from models.config import load_config
from models.ke1 import token_bytes_random
from perfkit import bench
from perfkit.schema import example_run, validate_run

ROOT = Path(__file__).resolve().parents[1]
TINY = ROOT / "configs" / "tiny_cpu.yaml"
VOCAB = 512
SEEN = {}


class FakeLoader:
    """Same constructor and attributes as dataio.loader.Loader, random token ids, no tokenizer download."""

    def __init__(self, source, batch_size, block_size, device, data_dir=None, vocab_size=VOCAB, seed=0,
                 split="train", tokenizer_path=None):
        SEEN["tokenizer_path"] = tokenizer_path
        SEEN["source"] = source
        self.B, self.T, self.source, self.vocab_size = batch_size, block_size, source, vocab_size
        self.device = torch.device(device)
        self.g = torch.Generator().manual_seed(seed)

    def next_batch(self):
        buf = torch.randint(0, self.vocab_size, (self.B, self.T + 1), generator=self.g)
        return buf[:, :-1].contiguous(), buf[:, 1:].contiguous()

    def token_bytes(self, max_pos):
        return token_bytes_random(self.vocab_size, max_pos)


@pytest.fixture(autouse=True)
def fake_loader(monkeypatch, tmp_path):
    SEEN.clear()
    monkeypatch.setattr(bench, "Loader", FakeLoader)
    monkeypatch.setattr(bench, "CACHE", tmp_path / "cache")


def tiny_cfg(*overrides):
    return load_config(TINY, ["data.source=synthetic", f"model.vocab_size={VOCAB}", *overrides])


# ------------------------------------------------------------------------------ build

def test_build_passes_tokenizer_path_to_loader():
    cfg = tiny_cfg("data.tokenizer_path=some/tokenizer.json")
    s = bench.build(cfg, torch.device("cpu"))
    assert SEEN["tokenizer_path"] == "some/tokenizer.json"
    assert s.loader.vocab_size == VOCAB and s.mcfg.vocab_size == VOCAB


def test_build_notes_a_schedule_it_ignores():
    s = bench.build(tiny_cfg("optim.schedule=cosine"), torch.device("cpu"))
    assert any("optim.schedule=cosine" in n for n in s.notes)
    assert not any("schedule" in n for n in bench.build(tiny_cfg(), torch.device("cpu")).notes)


def test_choose_dtype_fallbacks(monkeypatch):
    notes = []
    assert bench.choose_dtype("fp16", torch.device("cpu"), notes) == "bf16"          # no fp16 autocast on CPU
    assert notes and "bf16" in notes[0]

    monkeypatch.setattr(bench, "native_bf16", lambda: False)                       # T4 / P100 / V100 (DECISIONS B3)
    notes = []
    assert bench.choose_dtype("bf16", torch.device("cuda"), notes) == "fp16"
    assert "DECISIONS B3" in notes[0]
    monkeypatch.setattr(bench, "native_bf16", lambda: True)
    assert bench.choose_dtype("bf16", torch.device("cuda"), []) == "bf16"
    assert bench.choose_dtype("fp32", torch.device("cpu"), []) == "fp32"
    with pytest.raises(ValueError):
        bench.choose_dtype("fp8", torch.device("cpu"), [])


def test_pick_device_cpu_and_missing_cuda(monkeypatch):
    assert bench.pick_device("cpu").type == "cpu"
    monkeypatch.setattr(torch.cuda, "is_available", lambda: False)
    with pytest.raises(SystemExit):
        bench.pick_device("cuda")


# ------------------------------------------------------------------------------ metadata (rule 1a)

def test_run_metadata_records_the_tokenizer():
    s = bench.build(tiny_cfg(), torch.device("cpu"))
    meta = bench.run_metadata(s, "configs/tiny_cpu.yaml", [], "t")
    assert meta["tokenizer"]["vocab_size"] == VOCAB
    assert meta["tokenizer"]["revision"] == bench.TOKENIZER_REVISION
    assert meta["tokenizer"]["sha256"] == bench.TOKENIZER_SHA256
    assert meta["vocab_size"] == VOCAB and meta["lr_schedule"] == "constant"
    assert meta["batch_size"] == s.loader.B and meta["seq_len"] == s.loader.T


def _checked_run(**meta):
    run = example_run()
    run["meta"].update({"data_source": "synthetic", "vocab_size": bench.BRAHMIC_VOCAB, "dirty": False,
                        "commit": "abc", "device": "cuda",
                        "tokenizer": {"vocab_size": bench.BRAHMIC_VOCAB}, **meta})
    return run


def _cfg(level=3):
    return {"bench": {"level": level}, "run": {}, "report": {"gate_level": 2}}


def test_rule_checks_clean_run_has_no_warnings():
    run = _checked_run()
    for r in run["layer"]["regions"].values():
        r["spread_pct"] = 1.0
    assert bench.rule_checks(run, ["clean", "layer", "checkpoint", "comm"], _cfg()) == []


def test_rule_checks_flag_each_rule():
    run = _checked_run(dirty=True, commit=None, vocab_size=50304, tokenizer={"vocab_size": 50304})
    for r in run["layer"]["regions"].values():
        r["spread_pct"] = 1.0
    out = "\n".join(bench.rule_checks(run, ["clean", "layer"], _cfg(level=2)))
    assert "uncommitted changes" in out
    assert "no commit ID" in out
    assert "rule 1a" in out and "50304" in out                # wrong vocabulary
    assert "rule 3a" in out                                   # parts inside a block not timed
    assert "rule 3b" in out and "checkpoint and comm" in out  # not measured


def test_rule_checks_noisy_gated_part_is_named():
    run = _checked_run()
    for r in run["layer"]["regions"].values():
        r["spread_pct"] = 1.0
    run["layer"]["regions"]["fwd:block0"]["spread_pct"] = 25.0
    out = "\n".join(bench.rule_checks(run, ["clean", "layer", "checkpoint", "comm"], _cfg()))
    assert "fwd:block0" in out and "5% check" in out


# ------------------------------------------------------------------------------ the 5% check

def _two_runs():
    a = example_run()
    return a, copy.deepcopy(a)


def test_quick_compare_identical_runs_pass():
    a, b = _two_runs()
    rows, ok, problems = bench.quick_compare(a, b, 5.0, 2)
    assert ok and not problems
    names = [r[0] for r in rows]
    assert "step (clean)" in names and "fwd:block0" in names
    assert all(r[4] == "ok" for r in rows)


def test_quick_compare_only_gates_levels_up_to_gate_level():
    a, b = _two_runs()
    level3 = [n for n, r in a["layer"]["regions"].items() if r["level"] == 3]
    assert level3, "the example run must have a level-3 part"
    b["layer"]["regions"][level3[0]]["median"] *= 3          # inside a block: reported, not gated
    rows, ok, _ = bench.quick_compare(a, b, 5.0, 2)
    assert ok and level3[0] not in [r[0] for r in rows]


def test_quick_compare_fails_a_part_that_moved_more_than_tol():
    a, b = _two_runs()
    b["layer"]["regions"]["fwd:block1"]["median"] *= 1.10    # a whole block 10% slower
    rows, ok, _ = bench.quick_compare(a, b, 5.0, 2)
    verdict = {r[0]: r[4] for r in rows}
    assert not ok and verdict["fwd:block1"] == "FAIL" and verdict["fwd:block0"] == "ok"
    assert bench.quick_compare(a, b, 12.0, 2)[1]             # a looser tolerance lets it through


def test_quick_compare_5_percent_boundary():
    a, b = _two_runs()
    b["clean"]["step_ms"]["median"] = a["clean"]["step_ms"]["median"] * 1.049
    assert bench.quick_compare(a, b, 5.0, 2)[1]
    b["clean"]["step_ms"]["median"] = a["clean"]["step_ms"]["median"] * 1.06
    assert not bench.quick_compare(a, b, 5.0, 2)[1]


def test_quick_compare_refuses_different_gpu_and_vocab():
    a, b = _two_runs()
    b["meta"]["gpu"] = "OTHER-GPU"
    b["meta"]["vocab_size"] = 50304
    rows, ok, problems = bench.quick_compare(a, b, 5.0, 2)
    assert not ok and any("gpu" in p for p in problems) and any("vocab_size" in p for p in problems)


def test_quick_compare_missing_part_is_a_failure():
    a, b = _two_runs()
    del b["layer"]["regions"]["fwd:block0"]
    rows, ok, _ = bench.quick_compare(a, b, 5.0, 2)
    assert not ok and {r[0]: r[4] for r in rows}["fwd:block0"] == "MISSING"


def test_quick_compare_includes_checkpoint_and_all_to_all_when_both_have_them():
    a, b = _two_runs()
    for r, ms in ((a, 100.0), (b, 130.0)):
        r["checkpoint"] = {"save_ms": {"median": ms}}
        r["comm"] = {"moe_a2a": {"measured": True, "per_step_ms": ms / 10}}
    rows, ok, _ = bench.quick_compare(a, b, 5.0, 2)
    verdict = {r[0]: r[4] for r in rows}
    assert verdict["checkpoint save"] == "FAIL" and verdict["moe all-to-all"] == "FAIL" and not ok


# ------------------------------------------------------------------------------ output helpers

def test_write_run_never_overwrites(tmp_path):
    p1 = bench.write_run({"a": 1}, tmp_path, "run")
    p2 = bench.write_run({"a": 2}, tmp_path, "run")
    p3 = bench.write_run({"a": 3}, tmp_path, "run")
    assert [p.name for p in (p1, p2, p3)] == ["run.json", "run-2.json", "run-3.json"]
    assert json.loads(p1.read_text()) == {"a": 1}


def test_run_json_stays_valid_json_with_nan_and_inf(tmp_path):
    p = bench.write_run({"loss": float("nan"), "xs": [1.0, float("inf")], "n": {"v": -float("inf")}}, tmp_path, "r")
    assert json.loads(p.read_text()) == {"loss": None, "xs": [1.0, None], "n": {"v": None}}


def test_slug():
    assert bench._slug("NVIDIA GeForce RTX 5070 Ti") == "geforce-rtx-5070-ti"
    assert bench._slug("") == "cpu"


def test_parse_turns_flags_into_overrides():
    a, ov = bench.parse(["--config", "c.yaml", "--modes", "clean,layer", "--level", "3", "--steps", "7",
                         "--warmup", "2", "run.batch_size=4"])
    assert ov == ["run.batch_size=4", "bench.modes=[clean,layer]", "bench.level=3", "bench.steps=7", "bench.warmup=2"]


def test_parse_accepts_overrides_on_both_sides_of_the_flags():
    _, ov = bench.parse(["--config", "c.yaml", "run.batch_size=4", "--steps", "7", "report.tol_pct=9"])
    assert ov == ["run.batch_size=4", "report.tol_pct=9", "bench.steps=7"]


# ------------------------------------------------------------------------------ end to end (CPU)

def _run_main(tmp_path, tag, *extra):
    argv = ["--config", str(TINY), "--tag", tag, "--steps", "4", "--warmup", "2",
            "data.source=synthetic", f"model.vocab_size={VOCAB}", f"bench.out_dir={tmp_path / 'runs'}", *extra]
    return bench.main(argv)


@pytest.fixture
def first_run(tmp_path):
    code = _run_main(tmp_path, "first", "--modes", "clean,layer,checkpoint", "--level", "3")
    path = tmp_path / "runs" / "first.json"
    return code, path, json.loads(path.read_text())


def test_main_writes_a_complete_valid_run(first_run):
    code, path, run = first_run
    assert code == 0, "exit code 0 means validate_run found nothing missing"
    assert validate_run(run) == []
    assert run["meta"]["vocab_size"] == VOCAB and run["meta"]["tokenizer"]["revision"] == bench.TOKENIZER_REVISION
    assert run["clean"]["step_ms"]["n"] == 4 and run["clean"]["step_ms"]["median"] > 0
    assert run["metrics"]["tokens_per_s"] > 0 and run["metrics"]["params_total"] >= run["metrics"]["params_active"]


def test_main_times_whole_blocks_and_the_step_parts(first_run):
    _, _, run = first_run
    regions = run["layer"]["regions"]
    for part in ("fwd", "bwd", "opt", "fwd:embed", "fwd:head+loss", "fwd:block0", "fwd:block1",
                 "bwd:head+loss", "bwd:block0", "bwd:block1", "bwd:stack", "bwd:embed", "opt:opt.clip"):
        assert part in regions, f"missing gated part {part}"
        assert regions[part]["level"] <= 2 and regions[part]["median"] >= 0
    assert any(r["level"] == 3 for r in regions.values()), "bench.level=3 must also time the parts inside a block"
    assert run["layer"]["overhead_pct"] is not None


def test_main_measures_checkpoint_save(first_run):
    _, _, run = first_run
    ck = run["checkpoint"]
    assert ck["save_ms"]["median"] > 0 and ck["save_ms"]["n"] >= 1
    assert not list((bench.CACHE / "ckpt").glob("*")) if (bench.CACHE / "ckpt").exists() else True   # deleted after


def test_main_flags_a_run_with_the_wrong_vocabulary(first_run):
    _, _, run = first_run
    assert any("rule 1a" in w for w in run["warnings"])      # the test model uses 512, not 131072
    assert any("rule 3b" in w and "comm" in w for w in run["warnings"])


def test_main_against_exit_codes(tmp_path, first_run, capsys):
    _, path, run = first_run
    # same numbers: every part agrees
    code = _run_main(tmp_path, "same", "--modes", "clean,layer", "--level", "3", "--against", str(path),
                     "report.tol_pct=1000")
    assert code == 0
    assert "PASS" in capsys.readouterr().out
    # the earlier run says the step took a hundredth of the time: this run is far outside tol_pct
    fast = copy.deepcopy(run)
    fast["clean"]["step_ms"]["median"] /= 100
    other = tmp_path / "fast.json"
    other.write_text(json.dumps(fast))
    code = _run_main(tmp_path, "slow", "--modes", "clean,layer", "--level", "3", "--against", str(other))
    assert code == 2
    assert "FAIL" in capsys.readouterr().out


def test_main_rejects_an_unknown_mode(tmp_path):
    with pytest.raises(SystemExit):
        _run_main(tmp_path, "x", "--modes", "clean,nonsense")
