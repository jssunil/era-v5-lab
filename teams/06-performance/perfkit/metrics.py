"""MFU, HFU, goodput, memory, GPU telemetry, run metadata.  [STUB]

MVP
  * PEAKS: dense (no sparsity) vendor peak TFLOPs per dtype + HBM GB/s for T4, P100, V100, L4, A10,
    A100-40/80, H100 PCIe/SXM, B200 (+ a CPU placeholder). Match by substring of the device name.
  * run_metadata(device) -> the "meta" fields of perfkit/schema.py (GPU name, torch, CUDA, driver,
    commit + dirty from git, or the PERF_COMMIT env var when there is no .git, e.g. a Colab upload).
  * flops_per_token(model, T) -> {"model_flops_per_token": 6*N_active + 12*L*d*T, "params_total", "params_active"}
  * mfu(flops, tokens_per_s, peak_tflops) -> {"mfu", "model_tflops_per_s"}
  * memory(device) -> peak allocated / reserved GB.
Extra: HFU (+2 forwards of the stack when reversible, + Muon Newton-Schulz FLOPs), goodput
(time and tokens, badput buckets), NVML sampler thread (util, power, SM clock, temperature).
"""
from __future__ import annotations


def gpu_peak(device_name: str) -> dict:
    raise NotImplementedError("gpu_peak")


def run_metadata(device) -> dict:
    raise NotImplementedError("run_metadata")


def flops_per_token(model, T: int) -> dict:
    raise NotImplementedError("flops_per_token")


def mfu(flops: dict, tokens_per_s: float, peak_tflops: float) -> dict:
    raise NotImplementedError("mfu")


def memory(device) -> dict:
    raise NotImplementedError("memory")
