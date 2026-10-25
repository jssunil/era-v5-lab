"""Step timing that does not change what it measures.  [STUB]

MVP
  * StepTimer(device): start() / stop() put one CUDA event pair around a step (no sync);
    times_ms() synchronizes ONCE and returns every step's ms. CPU and MPS: sync(device) + perf_counter
    (MPS has no timing events we rely on).
  * stats(xs) -> {"median", "p10", "p90", "iqr", "min", "max", "n"}  (perfkit.schema.STATS must be a subset;
    p10 / p90 / iqr from sorted data, e.g. numpy.percentile; n = len(xs)).
  * sync(device): cuda / mps / cpu synchronize.
Done when: stats() returns every key above and bench clean mode runs end to end on CPU and CUDA.
Extra: Buckets(device): wall-clock seconds per named bucket (startup, eval, checkpoint...) for goodput.
Rules: no synchronize / .item() / print inside a timed step; medians, never means.
"""
from __future__ import annotations

import torch


def sync(device: torch.device):
    raise NotImplementedError("sync")


class StepTimer:
    def __init__(self, device: torch.device):
        raise NotImplementedError("StepTimer")

    def start(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError

    def times_ms(self):
        raise NotImplementedError


def stats(xs) -> dict:
    raise NotImplementedError("stats")
