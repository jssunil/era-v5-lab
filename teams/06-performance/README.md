# Team 06-performance

Put your work in a **topic folder**: `teams/06-performance/<topic>/<file>`, for example `teams/06-performance/harness/run.py`.
The team lead decides the topic names. Do not make personal folders. Do not make new folders under `teams/`.
Open a pull request; the lead reviews and merges it. The pr-guard check must pass.

## What this is

Week-1 performance work for the lab model: a timing harness that times every part of the training step,
a correctness framework that proves fast code gives the right result, and the first baseline.
Everything is driven by config: a new model is a new YAML file in `configs/`, not new code.

## The lab model (`configs/lab_small.yaml`)

| Part | Setting |
|---|---|
| Data | Raw FineWeb sample-10BT retokenized with BrahmicTokenizer-131K, random 512-token windows |
| Tokenizer | [BrahmicTokenizer-131K source repo](https://github.com/theschoolofai/BrahmicTokenizer-131K), exactly 131,072 IDs |
| Embedding | Kronecker Embedding v1: fixed byte codec (256 x 32 = 8192) + `Linear(8192 -> 256)` |
| Attention | GQA: 8 query heads, 2 key/value heads, width 256 |
| MoE | 1 shared + top-2 of 8 routed experts (256 -> 1024 -> 256), bias balancing, fp32 router |
| Stack | Reversible midpoint, 9 layers, pre-LN inside `f`; the backward rebuilds each layer's input |
| Optimizer | Muon on 2D block weights including routers; AdamW on embedding parameters (including KE projection), output head, norm gains and biases |
| Size | Reported from the selected config at runtime with the full 131,072-token vocabulary |

`configs/base.yaml` on its own is the plain NanoGPT comparison model (table embedding, dense MLP, plain stack, AdamW).
`configs/tiny_cpu.yaml` is the lab model shrunk for a laptop.

## Folder layout

```
configs/       base.yaml (every setting; plain NanoGPT on its own), lab_small.yaml, tiny_cpu.yaml
models/        config.py, gpt.py, ke1.py, moe.py, reversible.py, optim.py
dataio/        prepare_fineweb.py, loader.py
perfkit/       regions.py, timer.py, bench.py, metrics.py, report.py, roofline.py, schema.py, smoke.py
correctness/   framework.py and the test files
results/       run JSONs, baseline_v0.md, slowest5_v0.md
docs/          PLAN.md (interfaces, what is done and left), PARTS.md (every part we time)
```

## Status

- **Done:** the lab model and data pipeline (earlier GPT-2 version verified on an A100; Brahmic timings pending), the
  timing-marker API with markers in the model, the run JSON format, the test-pair registry, and a smoke test.
  The test files are stubs: each is reported as skipped until its owner writes it.
- **Left for Gate 1:** the step timer and event recorder, the bench (clean and layer modes), metrics and
  MFU, the report with the 5% two-run comparison, the correctness checks and the four test pairs, then two
  baseline runs and `results/baseline_v0.md`, `results/slowest5_v0.md`.

The full table is in [`docs/PLAN.md`](docs/PLAN.md) section 3. Every part we time is in [`docs/PARTS.md`](docs/PARTS.md).

## How to run

Every command runs from `teams/06-performance/`. Give the GPU name with every timing you share.

**1. Get the code**

```bash
git clone <REPO_URL> era-v5-lab          # the URL of the integration branch is posted in the G6 group
cd era-v5-lab && git checkout g6/dev && cd teams/06-performance
```

**2. Install.** Laptop (venv outside the repo): `python -m venv ~/.venvs/g6 && source ~/.venvs/g6/bin/activate`,
then `pip install -r perfkit/requirements.txt`. Colab (torch is already installed, do not reinstall it):
`pip install -q tokenizers datasets pyyaml pytest`.

**3. Tests** (CPU is fine, ~5 s)

```bash
python -m pytest correctness -q -rs              # all pass; unfinished stubs are SKIPPED and named
```

At Gate 1 no skip may be left (`-rs` lists them).

**4. Tokenizer and data:** the tokenizer is loaded exclusively from `tokenizer.json` in the
[source repo](https://github.com/theschoolofai/BrahmicTokenizer-131K), pinned to commit
`7dfcf398172c825c6689ad578e8b484ca5f57bc9` and verified by SHA-256. It is never loaded from
Hugging Face. The default downloads that GitHub file into `~/.cache/era-perf/BrahmicTokenizer-131K/`.
For an offline run, clone the source repo and set `data.tokenizer_path=/path/to/BrahmicTokenizer-131K/tokenizer.json`.
Tests accept the same path via `BRAHMIC_TOKENIZER_PATH`.

Data preparation streams raw text from FineWeb sample-10BT and encodes it with that artifact.
New shards use uint32 (IDs exceed 65,535) and a tokenizer metadata manifest. Existing GPT-2 shards
are incompatible and must be prepared again. Data stays outside git, by default in
`~/.cache/era-perf/fineweb-brahmic131k/`.

```bash
python -m dataio.prepare_fineweb                 # val + 1 train shard, 1M tokens each (~8 MB total)
# Offline tokenizer: append --tokenizer-path /path/to/source-checkout/tokenizer.json
```

For a quick check without FineWeb, add `data.source=synthetic`. Synthetic runs still use the
real Brahmic vocabulary and KE byte table, including special tokens and raw partial UTF-8 bytes.

**5. Smoke test the model** (not the baseline: Gate 1 numbers come from `perfkit.bench` on committed code)

```bash
python -m perfkit.smoke                                      # lab model: configs/lab_small.yaml
python -m perfkit.smoke --config configs/base.yaml          # plain NanoGPT for comparison
python -m perfkit.smoke --config configs/tiny_cpu.yaml       # laptop, seconds; numbers mean nothing
python -m perfkit.smoke --batch 16 model.ce_impl=chunked     # if out of memory
```

Precision and batch come from the GPU: bf16 and B=32 on A100 / L4 / H100, fp16 and B=8 on T4 / P100 / V100.
`key=value` overrides work for any key of `configs/base.yaml`. A good run: reconstruction error below
1e-3 (`OK`), loss starting at about ln(131072) = 11.78 and falling, p10 / p90 within a few % of the median,
`all weights finite: True`.

**6. Training schedule:** timing runs use a constant learning rate by default. To inspect training
loss with cosine decay and optional linear warmup, add optimizer overrides; schedule duration follows
the run's `--steps` plus timing warmup steps.

```bash
python -m perfkit.smoke --steps 20 --warmup 5 optim.schedule=cosine optim.warmup_steps=3
```

No timing results are published yet for the Brahmic vocabulary. The per-part `perfkit.bench` remains
unimplemented; `perfkit.smoke` reports whole-step timing only.

**Colab in one cell** (Runtime → Change runtime type → GPU):

```python
!git clone -q <REPO_URL> /content/era-v5-lab
%cd /content/era-v5-lab
!git checkout -q g6/dev
%cd teams/06-performance
!pip install -q tokenizers datasets pyyaml pytest
!python -m pytest correctness -q
!python -m dataio.prepare_fineweb
!python -m perfkit.smoke
```

Use `%cd`, not `!cd` (`!cd` changes the folder for that line only). Colab deletes `/content` and the data
cache when the session ends.
