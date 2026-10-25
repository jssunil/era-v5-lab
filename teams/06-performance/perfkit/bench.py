"""Time each part of the training step and write the run JSON.  [STUB]

    cd teams/06-performance
    python -m perfkit.bench --config configs/lab_small.yaml [--tag name] [key=value ...]

MVP
  1. load_config + model_config; pick the device; seed everything.
  2. Build Loader (data.source, data.dir, data.tokenizer_path, vocab_size=model.vocab_size); validate
     the pinned GitHub tokenizer's actual vocabulary even for synthetic timing runs. Build model
     (models.gpt.GPT with loader.token_bytes(ke_max_pos) when
     embedding == "ke1"), optimizer (models.optim.build_optimizer),
     autocast for bf16/fp16, GradScaler for fp16. run.dtype bf16 on a GPU without bf16 (T4 / P100 / V100)
     falls back to fp16 and says so in meta (DECISIONS B3). run.device auto: cuda, else mps, else cpu.
  3. One training step = phases at level 1, no sync and no .item() inside:
        with region("fwd", 1), phase("fwd"), autocast:    loss = model(x, y)[1]
        with region("bwd", 1), phase("bwd"):              point("__bwd_start__"); loss.backward(); point("__bwd_end__")
        with region("opt", 1), phase("opt"):              see the order below
     Data: in layer mode the fetch is region("data", 1) around loader.next_batch().
     Optimizer order (fp16 needs it): opt.unscale(scaler) if scaler, region("opt.clip", 2) clip_grad_norm_,
     opt.step(scaler), scaler.update(), region("opt.moe_bias", 3) update_bias() on each model.moe_layers(),
     opt.zero_grad(). With ce_impl chunked the model returns logits=None: use only [1].
  4. If cfg.model.reversible: models.reversible.reconstruction_error on one batch, under the run dtype,
     into the run JSON (meta.reconstruction_err); warn above 1e-3. Then warmup bench.warmup steps.
  5. clean: StepTimer around each step; the data fetch timed on the host (perf_counter, no sync).
  6. layer: EventRecorder(max_level=bench.level). Steps ALTERNATE recorder off / on (both under a
     StepTimer) -> overhead_pct from neighbouring steps. Backward segments from the recorded points, cut
     per level: a point of level L closes the segment "bwd:<point name>", which starts at the previous
     point of level <= L (or "__bwd_start__"). "__bwd_end__" closes "bwd:embed", which starts at "stack".
     Plain stack, points in backward order: head+loss (1), block8 .. block0 (2), stack (1). That gives
         bwd:head+loss  __bwd_start__ -> head+loss       bwd:block8  head+loss -> block8
         bwd:block{i}   block{i+1} -> block{i}           bwd:stack   head+loss -> stack  (all blocks)
         bwd:embed      stack -> __bwd_end__
     The ~0 ms gap block0 -> stack (two identity marks back to back) is not a segment.
     Reversible stack: points head+loss and stack only, so bwd:head+loss, bwd:stack and bwd:embed are cut
     the same way; its backward opens bwd:block{i} (level 2) and bwd.invert / bwd.recompute / .grad
     (level 3) as regions itself. So bwd:stack is the whole stack backward in both stacks, like fwd:stack.
     A segment takes the level of the forward region with the same name: head+loss 2, stack 1,
     block{i} 2, embed 2. Both stacks give the same names and levels, so report.compare works on either.
     A region can be recorded from
     the autograd thread (CUDA backward): the recorder must not assume the main thread.
     Keep each region's level in the JSON (report.compare uses it).
  7. Metrics via perfkit.metrics; write results/runs/<tag>.json (perfkit/schema.py) and the
     Markdown from perfkit.report.render. perfkit.schema.validate_run must return [].
Extra: trace mode (torch.profiler + ProfilerRecorder, Chrome trace to ~/.cache/era-perf/traces/, outside the repo), host-sync
detection (torch.cuda.set_sync_debug_mode), checkpoint and tokenizer timing, goodput loop.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from models.config import load_config, model_config  # noqa: E402


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", required=True)
    ap.add_argument("--tag", default=None)
    ap.add_argument("overrides", nargs="*", help="key=value, e.g. run.batch_size=16")
    a = ap.parse_args(argv)
    cfg = load_config(a.config, a.overrides)
    model_config(cfg)                       # fail early on a bad config
    raise NotImplementedError("bench")


if __name__ == "__main__":
    main()
