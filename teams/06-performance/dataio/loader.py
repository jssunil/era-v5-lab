"""Training batches.  [implemented: MVP]

  * Loader(source, batch_size, block_size, device, data_dir=None, vocab_size=50304, seed=0, split="train")
      source "fineweb10b": random windows from the GPT-2 token shards of kjj0/fineweb10B-gpt2
        (dataio/prepare_fineweb.py; np.memmap past the 1024-byte header). "synthetic": random ids.
  * next_batch() -> (x, y) int64 on device, [B, T] each, y = x shifted by one.
      Pinned memory + non_blocking copy on CUDA. No sync.
  * token_bytes(max_pos) -> the KE byte table: GPT-2 bytes from tiktoken for fineweb10b,
      models.ke1.token_bytes_random for synthetic.
  * attributes B, T (the bench reads them for tokens per step).
Extra: background prefetch thread (data.loader: simple -> prefetch, docs/PARTS.md).
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import torch

MAGIC, VERSION, HEADER_BYTES = 20240520, 1, 1024
DEFAULT_DIR = "~/.cache/era-perf/fineweb10B-gpt2"


def open_shard(path: Path) -> np.memmap:
    header = np.fromfile(path, dtype=np.int32, count=256)
    if header[0] != MAGIC or header[1] != VERSION:
        raise ValueError(f"{path}: not a fineweb10B-gpt2 shard (header {header[:3].tolist()})")
    return np.memmap(path, dtype=np.uint16, mode="r", offset=HEADER_BYTES, shape=(int(header[2]),))


class Loader:
    def __init__(self, source, batch_size, block_size, device, data_dir=None, vocab_size=50304, seed=0,
                 split="train"):
        self.B, self.T = batch_size, block_size
        self.source, self.device, self.vocab_size = source, torch.device(device), vocab_size
        self.pin = self.device.type == "cuda"
        self.rng = np.random.default_rng(seed)
        if source == "fineweb10b":
            d = Path(data_dir or DEFAULT_DIR).expanduser()
            paths = sorted(d.glob(f"fineweb_{split}_*.bin"))
            if not paths:
                raise FileNotFoundError(f"no fineweb_{split}_*.bin in {d}: run python -m dataio.prepare_fineweb")
            self.shards = [open_shard(p) for p in paths]
            sizes = np.array([len(s) - block_size - 1 for s in self.shards], dtype=np.float64)
            self.p_shard = sizes / sizes.sum()
        elif source != "synthetic":
            raise ValueError(f"data.source={source!r}: fineweb10b | synthetic")

    def next_batch(self):
        B, T = self.B, self.T
        if self.source == "synthetic":
            buf = torch.from_numpy(self.rng.integers(0, self.vocab_size, (B, T + 1), dtype=np.int64))
        else:
            shard = self.shards[self.rng.choice(len(self.shards), p=self.p_shard)]
            starts = self.rng.integers(0, len(shard) - T - 1, B)
            buf = torch.from_numpy(np.stack([shard[s:s + T + 1] for s in starts]).astype(np.int64))
        if self.pin:
            buf = buf.pin_memory()
        buf = buf.to(self.device, non_blocking=True)
        return buf[:, :-1].contiguous(), buf[:, 1:].contiguous()

    def token_bytes(self, max_pos: int):
        from models.ke1 import token_bytes_from_tiktoken, token_bytes_random
        if self.source == "synthetic":
            return token_bytes_random(self.vocab_size, max_pos)
        return token_bytes_from_tiktoken("gpt2", max_pos, self.vocab_size)
