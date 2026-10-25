"""Regression checks for the source tokenizer, shard IDs, and optimizer ownership."""
import json
import os

import numpy as np
import pytest
import torch

from dataio.loader import Loader, open_shard
from dataio.prepare_fineweb import write_shard
from dataio.tokenizer import BrahmicTokenizer, REVISION, SHA256, VOCAB_SIZE
from models.config import ModelConfig
from models.gpt import GPT
from models.optim import build_optimizer


@pytest.fixture(scope="module")
def tokenizer():
    return BrahmicTokenizer(os.environ.get("BRAHMIC_TOKENIZER_PATH"))


def test_source_vocabulary_and_byte_table(tokenizer):
    rows = tokenizer.raw_token_bytes()
    assert len(rows) == VOCAB_SIZE == 131072
    assert min(map(len, rows)) == 1
    assert max(map(len, rows)) == 32
    table, lens = tokenizer.token_bytes()
    assert table.shape == (VOCAB_SIZE, 32)
    for idx, raw in enumerate(rows):
        assert bytes(table[idx, :lens[idx]].tolist()) == raw
    vocab = tokenizer.spec["model"]["vocab"]
    assert rows[vocab["<|end_of_text|>"]] == b"<|end_of_text|>"
    # Retain incomplete UTF-8 bytes instead of decoding them to replacement chars.
    assert b"\x80" in rows
    assert tokenizer.encode("भारत एक देश है") == [66526, 2420, 13092, 732]
    with pytest.raises(ValueError, match="byte positions"):
        tokenizer.token_bytes(31)


def test_untrusted_artifact_rejected(tmp_path):
    path = tmp_path / "tokenizer.json"
    path.write_text("{}")
    with pytest.raises(ValueError, match="checksum"):
        BrahmicTokenizer(path)


def test_uint32_and_synthetic_use_real_vocabulary(tmp_path, tokenizer):
    ids = [0, 65536, 131071, 42, 100000]
    path = tmp_path / "fineweb_train_000001.bin"
    write_shard(path, ids)
    assert open_shard(path).dtype == np.dtype("<u4")
    assert open_shard(path).tolist() == ids
    (tmp_path / "tokenizer.json.meta").write_text(json.dumps(
        {"revision": REVISION, "sha256": SHA256, "vocab_size": VOCAB_SIZE}))
    ld = Loader("fineweb10b", 1, 4, "cpu", data_dir=tmp_path, tokenizer_path=tokenizer.path)
    x, y = ld.next_batch()
    assert x.tolist() == [ids[:-1]]
    assert y.tolist() == [ids[1:]]
    synthetic = Loader("synthetic", 1, 4, "cpu", tokenizer_path=tokenizer.path)
    actual, lens = synthetic.token_bytes(32)
    expected, expected_lens = tokenizer.token_bytes(32)
    assert torch.equal(actual, expected) and torch.equal(lens, expected_lens)
    with pytest.raises(ValueError, match="vocabulary"):
        Loader("synthetic", 1, 4, "cpu", vocab_size=50304, tokenizer_path=tokenizer.path)
    # Old uint16 headers must fail before token IDs can be misinterpreted.
    path.write_bytes(np.array([20240520, 1, 5] + [0] * 253, dtype="<i4").tobytes())
    with pytest.raises(ValueError, match="Brahmic uint32"):
        open_shard(path)


@pytest.mark.parametrize("embedding", ["table", "ke1"])
def test_optimizer_ownership_and_norm_gains(embedding):
    # Small vocabulary here is a unit fixture, never a performance configuration.
    cfg = ModelConfig(vocab_size=16, block_size=4, n_layer=1, n_head=2, n_embd=8,
                      embedding=embedding, ffn="moe",
                      moe=dict(num_experts=2, top_k=1, num_shared=1))
    from models.ke1 import token_bytes_random
    model = GPT(cfg, token_bytes_random(16) if embedding == "ke1" else None)
    opt = build_optimizer(model, dict(name="muon", lr=0.001, muon_lr=0.02, weight_decay=0.01))
    groups = {name: {id(p) for g in o.param_groups for p in g["params"]} for name, o in opt.named}
    muon, adamw = groups["opt.muon"], groups["opt.adamw"]
    assert not muon & adamw
    assert muon | adamw == {id(p) for p in model.parameters() if p.requires_grad}
    for name, p in model.named_parameters():
        expected = muon if name.startswith("blocks.") and p.ndim == 2 else adamw
        assert id(p) in expected, name
    assert id(model.head.weight) in adamw
    norms = [m for m in model.modules() if isinstance(m, torch.nn.LayerNorm)]
    assert norms and all(m.weight.requires_grad and id(m.weight) in adamw for m in norms)
    model(torch.tensor([[1, 2, 3, 4]]), torch.tensor([[2, 3, 4, 5]]))[1].backward()
    assert all(m.weight.grad is not None for m in norms)
    opt.step()
    assert all(torch.isfinite(p).all() for p in model.parameters())
