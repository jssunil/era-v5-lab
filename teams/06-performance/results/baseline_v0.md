# Baseline v0: lab_small on one A100

**Result: PASS.** Every gated part agrees within 5% between two runs. The largest difference is 2.98% (`fwd:block2`).

| | |
|---|---|
| GPU | NVIDIA A100-SXM4-40GB (compute capability 8.0, 39.5 GB), Colab |
| Commit | `TBD` |
| Software | torch 2.11.0+cu130, CUDA 13.0, driver 580.82.07, Python 3.13 |
| Config | `configs/lab_small.yaml`, no overrides |
| Model | KE v1 embedding, GQA 8/2 heads, MoE 1 shared + top-2 of 8, reversible midpoint stack, 9 layers, width 256, vocabulary 131,072 (BrahmicTokenizer-131K) |
| Run | bf16 autocast, B=32, T=512 (16,384 tokens per step), FineWeb sample-10BT, Muon + AdamW, constant LR |
| Command | `python -m perfkit.bench --config configs/lab_small.yaml --level 3 --repeat 2 --tag z` |
| Runs | `z` and `z-run2`, each in its own Python process, back to back in one Colab session, 2026-10-27 |
| Method | 10 warmup steps, then 150 measured steps per mode. Parts are timed with CUDA events and no host sync inside a step. Each number is the median over the steps. |

## The step

| | Run 1 | Run 2 |
|---|---:|---:|
| Step time, median (ms) | 497.1 | 498.9 |
| p10 .. p90 (ms) | 490.5 .. 505.7 | 493.2 .. 504.4 |
| Tokens per second | 32,958 | 32,838 |
| MFU / HFU (bf16 dense peak 312 TFLOPS) | 3.4% / 4.3% | 3.4% / 4.3% |
| Peak memory allocated / reserved (GB) | 25.1 / 29.4 | 25.1 / 29.4 |
| GPU busy in the trace | 25.1% | 25.1% |
| Kernels per step / host syncs per step | 18,436 / 433 | 18,430 / 433 |
| Recorder overhead (layer mode) | 0.47% | 0.13% |

The model has 79.9M parameters, 51.3M of them active per token (the LM head is 33.5M of those). That makes
322 MFLOP per token for MFU and 410 MFLOP per token for HFU. HFU also counts the reversible stack's two extra
forwards and Muon's Newton-Schulz work. The method is in `docs/METRICS.md`.

Where the step goes (run 1, level-1 parts): forward 101 ms (20%), backward 235 ms (47%), optimizer 159 ms (32%),
data 0.8 ms.

## The 5% check

Rule: the whole step and every part at level 1 or 2 must agree within 5%, with no exemption for small parts.
Diff = slower / faster - 1. Level-3 parts (inside a block) are timed and listed in the run files but not gated.

| Part | Level | Run 1 (ms) | Run 2 (ms) | Diff | |
|---|---:|---:|---:|---:|---|
| `step (clean)` | - | 497.123 | 498.934 | 0.36% | ok |
| `data` | 1 | 0.826 | 0.828 | 0.25% | ok |
| `fwd` | 1 | 101.299 | 101.782 | 0.48% | ok |
| `fwd:embed` | 2 | 4.343 | 4.346 | 0.07% | ok |
| `fwd:stack` | 1 | 54.641 | 55.135 | 0.90% | ok |
| `fwd:block0` | 2 | 5.734 | 5.792 | 1.01% | ok |
| `fwd:block1` | 2 | 6.104 | 6.125 | 0.35% | ok |
| `fwd:block2` | 2 | 6.044 | 6.224 | 2.98% | ok |
| `fwd:block3` | 2 | 6.075 | 6.122 | 0.77% | ok |
| `fwd:block4` | 2 | 6.115 | 6.181 | 1.08% | ok |
| `fwd:block5` | 2 | 6.021 | 6.111 | 1.51% | ok |
| `fwd:block6` | 2 | 6.085 | 6.074 | 0.18% | ok |
| `fwd:block7` | 2 | 5.932 | 6.012 | 1.36% | ok |
| `fwd:block8` | 2 | 6.013 | 6.104 | 1.51% | ok |
| `fwd:head+loss` | 2 | 42.129 | 42.134 | 0.01% | ok |
| `bwd` | 1 | 234.821 | 235.618 | 0.34% | ok |
| `bwd:head+loss` | 2 | 48.175 | 48.185 | 0.02% | ok |
| `bwd:stack` | 1 | 186.163 | 186.927 | 0.41% | ok |
| `bwd:block8` | 2 | 21.040 | 21.145 | 0.50% | ok |
| `bwd:block7` | 2 | 20.864 | 20.941 | 0.37% | ok |
| `bwd:block6` | 2 | 20.801 | 20.690 | 0.53% | ok |
| `bwd:block5` | 2 | 20.621 | 20.728 | 0.52% | ok |
| `bwd:block4` | 2 | 20.675 | 20.822 | 0.71% | ok |
| `bwd:block3` | 2 | 20.540 | 20.602 | 0.30% | ok |
| `bwd:block2` | 2 | 20.464 | 20.749 | 1.39% | ok |
| `bwd:block1` | 2 | 20.409 | 20.560 | 0.74% | ok |
| `bwd:block0` | 2 | 20.426 | 20.408 | 0.09% | ok |
| `bwd:embed` | 2 | 0.482 | 0.480 | 0.43% | ok |
| `opt` | 1 | 158.548 | 159.921 | 0.87% | ok |
| `opt:opt.clip` | 2 | 4.196 | 4.173 | 0.55% | ok |
| `opt:opt.muon` | 2 | 151.078 | 152.210 | 0.75% | ok |
| `opt:opt.adamw` | 2 | 1.547 | 1.560 | 0.79% | ok |
| `checkpoint save` | - | 3278.174 | 3278.279 | 0.00% | ok |

**Watch:** `opt:opt.adamw` (1.5 ms) has a p10..p90 spread of about 10% within a run, and the first blocks'
forward spreads by 10 to 11%. Here they agree within 1 to 3%, but a different Colab machine could move them.

## Also measured

| | Run 1 | Run 2 |
|---|---:|---:|
| Checkpoint save (model + optimizer, 747 MB), median of 10 | 3278 ms | 3278 ms |
| of which copy to CPU / write and fsync | 65 / 3214 ms | 65 / 3214 ms |
| GPU during the clean steps (nvidia-smi, 75 samples): utilization, SM clock, power, temperature | 40%, 1410 MHz, 79 W, 41 C | 40%, 1410 MHz, 86 W, 41 C |
| Clock slowdowns (power or thermal) | none | none |
| Reversible reconstruction error (bf16) | 2.4e-4 | 2.4e-4 |
| MoE all-to-all | not timed: one GPU. Payload 32 MB per call, 72 calls per step (needs `torchrun` on 2 GPUs) | |

## What makes the runs repeatable

- **Each run gets its own Python process.** A second run in the same process as a first one that used the
  profiler was 26% slower on every CPU-bound part, and the same on the GPU-bound ones (the head, the embedding).
  The step is CPU-bound (25% GPU busy), so anything that slows the CPU shows up in the timings.
- **The same GPU, clocks steady.** The SM clock stayed at 1410 MHz with no power or thermal slowdowns in either
  run, so GPU clocks do not explain the remaining 0 to 3%.
- **Other pairs on the same GPU agreed too:** two runs without the profiler within 4.7% (largest `opt.adamw`),
  and another two-run pair within 3.8%.
