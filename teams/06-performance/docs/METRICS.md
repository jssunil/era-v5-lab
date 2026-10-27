# METRICS — MFU / HFU formulas for G8

Source of truth for the numbers: `perfkit/metrics.py`. Bench writes them into the run JSON
(`perfkit/schema.py` `REQUIRED["metrics"]`); report and G8 read the same fields. Do not invent
constants here — change `metrics.py` first.

## FLOPs per token

`T` = sequence length, `L` = layers, `d` = width, `N_active` from `GPT.param_counts`.

```text
model_flops_per_token = 6 * N_active + 12 * L * d * T
                        (PaLM; attention scores counted non-causal)

hw_flops_per_token    = model
                      + 2 forwards of the stack when reversible (invert + recompute)
                      + 2 * head again when ce_impl=chunked (it recomputes the head)
                      + optimizer FLOPs per step (Muon Newton-Schulz) / tokens per step
```

## MFU and HFU

```text
model_tflops_per_s = tokens_per_s * model_flops_per_token / 1e12
MFU                = model_tflops_per_s / peak_tflops

HFU                = tokens_per_s * hw_flops_per_token / 1e12 / peak_tflops
```

MFU uses model FLOPs; HFU uses hardware FLOPs. Both divide by the **dense** vendor peak for the
dtype the run used (`peak_tflops` in the run JSON).

## Peak table (`PEAKS` in `metrics.py`)

`gpu_peak(device_name)` / `peak_tflops(device_name, dtype)` walk a substring table (B200, H200,
H100, A100, L40S, …). First match wins, so specific names come first.

- Known GPU, known dtype peak → `peak_tflops` is set; MFU/HFU can be computed.
- Known GPU, empty peak entry, or unknown GPU → peak is missing; **leave MFU empty** and say so
  in the run (or pass `--peak-tflops` on the bench CLI).

## Tokens per second

`tokens_per_s` comes from the clean median step time and `tokens_per_step` (batch × sequence).
Report and G8 must use the value already stored in the run JSON, not recompute a different one.

## Dirty commit

`meta.dirty` is true when the working tree under `teams/06-performance` (outside `results/`)
differs from `meta.commit`. A dirty run is not a named commit: treat baselines from dirty trees
as non-authoritative until the tree is clean.

## Shared run JSON

`perfkit.schema.REQUIRED` lists every field report and G8 expect under `meta`, `config`, `clean`,
and `metrics` (plus `layer` / `trace` when those modes ran). Renaming or removing a required key
breaks consumers — agree it before changing.
