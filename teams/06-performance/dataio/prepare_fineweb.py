"""Download FineWeb 10B, already tokenized with GPT-2 (kjj0/fineweb10B-gpt2 on the Hugging Face Hub).  [implemented]

    python -m dataio.prepare_fineweb                       # val shard + 1 train shard (100M tokens, ~200 MB)
    python -m dataio.prepare_fineweb --train-shards 4

Shard format (modded-nanogpt): a 1024-byte header of 256 int32 (magic 20240520, version 1, number of
tokens), then the tokens as uint16. Files: fineweb_val_000000.bin, fineweb_train_000001.bin .. 000103.bin
(100M tokens each). One train shard is far more than the timing runs read.
Data stays out of git (pr-guard rejects .bin files).
"""
from __future__ import annotations

import argparse
from pathlib import Path

REPO = "kjj0/fineweb10B-gpt2"
DEFAULT_DIR = "~/.cache/era-perf/fineweb10B-gpt2"


def shard_names(train_shards: int):
    return ["fineweb_val_000000.bin"] + [f"fineweb_train_{i:06d}.bin" for i in range(1, train_shards + 1)]


def prepare(out: str = DEFAULT_DIR, train_shards: int = 1):
    from huggingface_hub import hf_hub_download
    out = Path(out).expanduser()
    out.mkdir(parents=True, exist_ok=True)
    for name in shard_names(train_shards):
        if not (out / name).exists():
            hf_hub_download(repo_id=REPO, filename=name, repo_type="dataset", local_dir=out)
        print(out / name)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=DEFAULT_DIR)
    ap.add_argument("--train-shards", type=int, default=1, help="1..103, 100M tokens each")
    a = ap.parse_args()
    prepare(a.out, a.train_shards)
