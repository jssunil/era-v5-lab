"""Named timing regions that cost nothing when timing is off.  [CONTRACT implemented; recorders STUB]

The module-level API (region / phase / point / mark / use_recorder) is the contract every
other file uses: do not change its signatures. The two recorders below are still to be written.

Model code:
    with region("block3.attn", level=2):   ...        # a named piece of work
    x = mark(x, "block3")                             # backward boundary: grad reached x
    with phase("bwd.recompute"):   ...                # prefix region names inside

Names become "<phase>:<name>" (e.g. "fwd:block3.attn.qkv"). Levels: 1 phases (data, fwd, bwd, opt),
2 per layer / big parts, 3 inside a layer. A recorder ignores regions above its max_level.

With no recorder active: region() returns ONE shared no-op context, mark() returns its input
(no autograd node), phase() does nothing.

Recorder protocol:
    rec.max_level: int
    rec.region(full_name, level) -> context manager
    rec.point(name, level)       -> None      (called by point() and by mark() in backward)
"""
from __future__ import annotations

from contextlib import contextmanager, nullcontext

import torch

_NULL = nullcontext()
_REC = None    # active recorder or None
_PHASE = ""    # current phase prefix


def active():
    return _REC


@contextmanager
def use_recorder(rec):
    global _REC
    prev, _REC = _REC, rec
    try:
        yield rec
    finally:
        _REC = prev


@contextmanager
def phase(name: str):
    global _PHASE
    if _REC is None:
        yield
        return
    prev, _PHASE = _PHASE, name
    try:
        yield
    finally:
        _PHASE = prev


def region(name: str, level: int = 2):
    rec = _REC
    if rec is None or level > rec.max_level:
        return _NULL
    return rec.region(f"{_PHASE}:{name}" if _PHASE else name, level)


def point(name: str, level: int = 1):
    rec = _REC
    if rec is not None and level <= rec.max_level:
        rec.point(name, level)


def mark(x: torch.Tensor, name: str, level: int = 1) -> torch.Tensor:
    """Identity in forward; in backward, tells the recorder when the gradient reaches x."""
    rec = _REC
    if rec is None or level > rec.max_level or not x.requires_grad:
        return x
    return _Mark.apply(x, rec, name, level)


class _Mark(torch.autograd.Function):
    @staticmethod
    def forward(ctx, x, rec, name, level):
        ctx.rec, ctx.name, ctx.level = rec, name, level
        return x.view_as(x)

    @staticmethod
    def backward(ctx, g):
        ctx.rec.point(ctx.name, ctx.level)
        return g, None, None, None


# ------------------------------------------------------------------------------ recorders

class EventRecorder:
    """Layer mode. MVP: on CUDA record a torch.cuda.Event at each region start/end and point
    (no sync); on CPU use time.perf_counter. collect() synchronizes ONCE after the step and returns
        spans:  [(full_name, level, ms)]
        points: [(name, level, clock)] in backward order, where clock.ms_since(other_clock) works.
    Overhead is a few microseconds of CPU per event and ~0 GPU."""

    def __init__(self, device: torch.device, max_level: int = 2):
        self.max_level = max_level
        raise NotImplementedError("EventRecorder")

    def region(self, name, level=2):
        raise NotImplementedError

    def point(self, name, level=1):
        raise NotImplementedError

    def collect(self):
        raise NotImplementedError


class ProfilerRecorder:
    """Trace mode. MVP: region() opens torch.profiler.record_function(name) (+ NVTX range on CUDA);
    point() records a zero-length record_function named f"__point__:{name}" so trace tools can
    cut backward segments."""

    def __init__(self, max_level: int = 3):
        self.max_level = max_level
        raise NotImplementedError("ProfilerRecorder")

    def region(self, name, level=2):
        raise NotImplementedError

    def point(self, name, level=1):
        raise NotImplementedError
