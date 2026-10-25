"""Run JSON -> Markdown, two-run comparison, baseline and slowest-parts files.  [STUB]

Build it against perfkit.schema.example_run(); no need to wait for bench.

    python -m perfkit.report results/runs/<tag>.json
    python -m perfkit.report run1.json --compare run2.json --baseline results/baseline_v0.md --slowest results/slowest5_v0.md

MVP
  * render(run) -> Markdown: header (GPU, dtype, B x T, torch, commit), step stats, MFU, per-region table
    (ms, p90, % of step, level), "time by part type" (sum over layers), five slowest leaf parts.
  * compare(a, b, tol_pct=5, gate_level=2) -> (rows, ok, problems): the whole step plus every region with
    level <= gate_level must be within tol_pct. NO exemption for small parts. Refuse runs on different
    GPUs or with different configs. Level-3 rows are listed as information only.
  * baseline_md(...): GPU name, commit, config, PASS/FAIL, the comparison table.
  * slowest_md(run): five slowest parts, each: ms and % of step, why (bound + evidence), trace reference,
    one week-2 idea.
Extra: roofline predictions (perfkit/roofline.py), per-part trace files cut from the full trace.
"""
from __future__ import annotations

import argparse


def render(run: dict) -> str:
    raise NotImplementedError("render")


def compare(a: dict, b: dict, tol_pct: float = 5.0, gate_level: int = 2):
    raise NotImplementedError("compare")


def baseline_md(a: dict, b: dict, rows, ok, problems) -> str:
    raise NotImplementedError("baseline_md")


def slowest_md(run: dict) -> str:
    raise NotImplementedError("slowest_md")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("run")
    ap.add_argument("--compare")
    ap.add_argument("--baseline")
    ap.add_argument("--slowest")
    ap.parse_args()
    raise NotImplementedError("report CLI")
