# Modal Gate 1 test logs (A100), 30 Oct 2026

Evidence for the patch on top of PR #29 (`g6/sunil-5pct-stability`, code commit `1485409`). Every folder holds the
console log of one Modal run (`*_log.txt`), the GPU / torch report (`repeat_env.txt`) and, for a pair, the two
generated reports (`*_normal.md`, `*_normal-run2.md`). Nothing here is hand-edited.

Setup: Modal container with one A100-SXM4-40GB for the repeat pairs and one A100-SXM4-80GB for the test suite
(Modal picked the 80GB card for that job; the GPU name is in each `*env.txt`), torch 2.15.0+cu132, 8 vCPUs reserved, real FineWeb sample-10BT
(BrahmicTokenizer-131K shards copied to local disk before the run). Each pair is
`python -m perfkit.bench --tag <tag> --level 3 --repeat 2`, then `python -m perfkit.report <run2>.json --compare <run1>.json`;
the `lab_small` pairs add `--config configs/lab_small.yaml`.

## Test suite (`branch_1485409/g1_suite`)
| Command | Result |
|---|---|
| `pytest correctness -q -rs --all-configs` | 327 passed, 0 failed, 0 skipped, 0 xfailed |
| `pytest correctness -q -rs` | 183 passed, 144 deselected, 0 skipped |

PR #29 head (`dc0b170`) on a Modal H100: 317 passed and 1 xfailed with `--all-configs`.

## 5% repeat pairs
A pair passes when every gated part agrees within 5% or less than 0.05 ms (`report.abs_tol_ms`). The branch
rows use the patched rule (checkpoint copy GPU to CPU gated, disk write information only); the PR #29 rows use
the rule as merged in the PR (`checkpoint save` gated).

| Code | Run | Result | Parts outside 5% and 0.05 ms (run 2 / run 1, ms) |
|---|---|---|---|
| branch_1485409 | g1_base1 | FAIL (3 of 28) | fwd:block0 1.066 0.950 0.117 12.3% slower OUTSIDE, opt 25.695 24.457 1.238 5.1% slower OUTSIDE, opt:opt.muon 19.887 18.911 0.976 5.2% slower OUTSIDE |
| branch_1485409 | g1_base2 | FAIL (4 of 28) | opt 40.504 37.894 2.610 6.9% slower OUTSIDE, opt:opt.polar_muon_adamw 39.766 37.145 2.621 7.1% slower OUTSIDE, opt:opt.muon 33.715 31.389 2.327 7.4% slower OUTSIDE, opt:opt.adamw 5.844 5.553 0.291 5.2% slower OUTSIDE |
| branch_1485409 | g1_lab1 | FAIL (3 of 33) | data 0.537 0.691 0.154 22.3% faster OUTSIDE, opt:opt.clip 2.916 3.176 0.261 8.2% faster OUTSIDE, opt:opt.adamw 1.135 1.261 0.126 10.0% faster OUTSIDE |
| branch_1485409 | g1_lab2 | PASS | - |
| pr29_head_dc0b170 | pr29_a100n1 | FAIL (3 of 28) | opt 20.706 21.990 1.285 5.8% faster OUTSIDE, opt:opt.polar_muon_adamw 20.087 21.422 1.334 6.2% faster OUTSIDE, opt:opt.muon 15.469 16.738 1.269 7.6% faster OUTSIDE |
| pr29_head_dc0b170 | pr29_a100n2 | FAIL (2 of 28) | fwd:block0 1.081 0.999 0.082 8.2% slower OUTSIDE, checkpoint save 386.220 365.263 20.956 5.7% slower OUTSIDE |
| pr29_head_dc0b170 | pr29_a100real1 | PASS | - |
| pr29_head_dc0b170 | pr29_a100real2 | FAIL (1 of 28) | checkpoint save 723.685 805.742 82.057 10.2% faster OUTSIDE |
| pr29_head_dc0b170 | pr29_a100real3 | FAIL (7 of 28) | data 0.924 0.852 0.071 8.3% slower OUTSIDE, fwd:block0 1.544 1.408 0.136 9.7% slower OUTSIDE, bwd 22.820 21.728 1.092 5.0% slower OUTSIDE, bwd:stack 11.843 10.787 1.056 9.8% slower OUTSIDE ... |
| pr29_head_dc0b170 | pr29_a100real4 | FAIL (5 of 28) | opt 25.970 23.962 2.008 8.4% slower OUTSIDE, opt:opt.polar_muon_adamw 25.266 23.271 1.995 8.6% slower OUTSIDE, opt:opt.muon 20.263 18.493 1.770 9.6% slower OUTSIDE, opt:opt.adamw 4.881 4.616 0.265 5.7% slower OUTSIDE ... |
| pr29_head_dc0b170 | pr29_a100real5 | FAIL (1 of 28) | step (clean) 90.163 85.645 4.518 5.3% slower OUTSIDE |
| pr29_head_dc0b170 | pr29_a100real6 | FAIL (7 of 28) | data 0.516 0.697 0.181 25.9% faster OUTSIDE, fwd:embed 0.622 0.672 0.050 7.5% faster OUTSIDE, fwd:stack 5.413 5.805 0.392 6.7% faster OUTSIDE, fwd:block0 0.858 1.068 0.210 19.7% faster OUTSIDE ... |
| pr29_head_dc0b170 | pr29_a100real7 | FAIL (1 of 28) | checkpoint save 364.613 393.634 29.021 7.4% faster OUTSIDE |

Reading: the whole step agrees within 3% in every pair; the parts that move are the optimizer step (thousands of small
launches) and parts under about 2 ms. `lab_small` (B=32, T=512, 400 to 560 ms step) is steadier than `base.yaml`
(B=16, T=256, 65 to 90 ms step).

## What the patch changes
See the PR description. Files: `perfkit/report.py`, `perfkit/bench.py`, `correctness/conftest.py`,
`correctness/test_ke.py`, `correctness/test_report.py`, `correctness/test_bench.py`, `models/ke1.py`,
`configs/lab_small.yaml` (restored), `README.md`, `docs/PARTS.md`.
