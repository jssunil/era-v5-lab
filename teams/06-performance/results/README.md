# Results

- `runs/<tag>.json` + `<tag>.md`: one bench run each (committed as evidence).
- `runs/<tag>_parts/`: small per-part traces for the slowest five (committed).
- Full profiler traces go to `~/.cache/era-perf/traces/`, outside the repo (too big for git; pr-guard
  rejects files over 5 MB). Never write them under `results/`.
- `baseline_v0.md`, `slowest5_v0.md`: written by `perfkit.report` from two GPU runs.

Every result names its GPU and commit. A number without both does not count.
