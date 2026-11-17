"""Week-3 review, area C: optimizer, data loading and checkpointing (adversarial).

Every confirmed bug is a strict xfail with reason "REVIEW-C<n>: ..." (see review_C.md for the write-up), so the test
turns red the day the bug is fixed and the marker must come off. The other tests pin behaviour the review checked and
found correct (edge cases nobody had a test for).
"""
from __future__ import annotations

import importlib.util
import io
import json
import subprocess
from pathlib import Path
from unittest.mock import patch

import numpy as np
import pytest
import torch

from dataio import loader as loader_mod
from dataio.loader import HEADER_BYTES, MAGIC, VERSION, Loader, open_shard
from models.config import ModelConfig
from models.gpt import GPT
from models.optim import (Muon, MuonAdamW, build_optimizer, zeropower_via_newtonschulz5,
                          zeropower_via_newtonschulz5_batched)
from perfkit.bench import _to_cpu

ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT.parents[1]
P1536_SHA256 = "e6b93a93a60520d7b1af2e9242485f443b5596a1e116b8f8798d83bbad25a64b"   # G3 release/README.md
P1536_EOS = 130822                                                                       # G3 release/README.md


class _StubTokenizer:
    def __init__(self, _path=None):
        self.vocab_size = 131072


def _write_raw_shard(path: Path, tokens, count=None):
    header = np.zeros(256, dtype="<i4")
    header[:3] = [MAGIC, VERSION, len(tokens) if count is None else count]
    with path.open("wb") as f:
        header.tofile(f)
        np.asarray(tokens, dtype="<u4").tofile(f)


def _fineweb_dir(tmp_path: Path, shards: dict) -> Path:
    for name, toks in shards.items():
        _write_raw_shard(tmp_path / name, toks)
    (tmp_path / "tokenizer.json.meta").write_text(json.dumps(
        {"revision": loader_mod.REVISION, "sha256": loader_mod.SHA256, "vocab_size": 131072}))
    return tmp_path


def _loader(**kw):
    with patch("dataio.loader.BrahmicTokenizer", _StubTokenizer):
        return Loader(**kw)


# ----------------------------------------------------------------------------------------------- Newton-Schulz edges

@pytest.mark.parametrize("shape", [(8, 16), (16, 8), (1, 32), (32, 1)])
def test_newton_schulz_zero_matrix_gives_zero_not_nan(shape):
    """A zero gradient must give a zero update (eps keeps 0/0 out), on the loop and the batched path."""
    z = torch.zeros(shape)
    for out in (zeropower_via_newtonschulz5(z), zeropower_via_newtonschulz5_batched(z[None])[0]):
        assert torch.isfinite(out.float()).all()
        assert out.float().abs().max().item() == 0.0


def test_polar_muon_zero_grad_first_step_is_finite_and_only_decays():
    """Polar Express path with a zero gradient on a fresh state: no NaN from the 1e-6/1e-10 clamps; with cautious
    weight decay the mask (0 * p >= 0) is all True, so only the decay moves the weight. Note (review C-N2): the decay
    uses the shape-scaled lr (lr * sqrt(max(1, rows/cols))), unlike plain Muon, which decays with the group lr."""
    for impl in ("loop", "batched"):
        p = torch.nn.Parameter(torch.randn(6, 4))
        p0 = p.detach().clone()
        opt = MuonAdamW([dict(params=[p], kind="muon", lr=0.02, momentum=0.95, beta2=0.95, ns_steps=5,
                              weight_decay=0.1, impl=impl)])
        p.grad = torch.zeros_like(p)
        opt.step()
        assert torch.isfinite(p).all()
        torch.testing.assert_close(p.detach(), p0 * (1 - 0.02 * (6 / 4) ** 0.5 * 0.1), rtol=1e-6, atol=1e-7)


def test_newton_schulz_rank_one_and_extreme_aspect_ratios():
    """Rank-1 input: the top singular value lands in the NS5 band. Observed (review note C-N1): in bf16 the rounding
    noise of the other directions is amplified to O(1) too (NS5 multiplies small singular values by ~3.4 per step), so
    the update is not rank-1. Pinned here so a change to the NS dtype is noticed.
    1 x N and N x 1: the result is the unit vector (singular value in the NS5 band)."""
    torch.manual_seed(0)
    g = torch.outer(torch.randn(16), torch.randn(32))
    s = torch.linalg.svdvals(zeropower_via_newtonschulz5(g).float())
    assert 0.6 < s[0] < 1.3
    assert s[1] > 0.1, "bf16 noise directions are no longer amplified: update review note C-N1"
    for shape in [(1, 512), (512, 1)]:
        s = torch.linalg.svdvals(zeropower_via_newtonschulz5(torch.randn(shape)).float())
        assert 0.6 < s[0] < 1.3


def test_batched_muon_groups_mixed_shapes_and_skips_none():
    """Different shapes in one group are bucketed separately; a None-grad param is untouched (and gets no state)."""
    torch.manual_seed(0)
    ps = [torch.nn.Parameter(torch.randn(s)) for s in [(8, 4), (4, 8), (8, 4), (5, 5)]]
    ref = [torch.nn.Parameter(p.detach().clone()) for p in ps]
    o_b, o_l = Muon(ps, lr=0.02, impl="batched"), Muon(ref, lr=0.02, impl="loop")
    for i, (p, r) in enumerate(zip(ps, ref)):
        g = None if i == 3 else torch.randn_like(p)
        p.grad, r.grad = g, (None if g is None else g.clone())
    o_b.step()
    o_l.step()
    for p, r in zip(ps, ref):
        torch.testing.assert_close(p, r, rtol=0, atol=2e-3)
    assert "buf" not in o_b.state[ps[3]]


# ------------------------------------------------------------------------- idle experts: None grad vs zero grad

def _moe_model(dispatch):
    torch.manual_seed(0)
    cfg = ModelConfig(vocab_size=64, block_size=8, n_layer=1, n_head=2, n_embd=16, ffn="moe",
                      moe=dict(num_experts=8, top_k=2, num_shared=0, bias_gamma=0.0, dispatch=dispatch,
                               ffn_hidden=None))
    return GPT(cfg)


def test_fast_moe_dispatch_gives_zero_grads_where_loop_gives_none():
    """Fact the C1 finding rests on: an expert that got no token has grad None under dispatch=loop and an all-zero
    grad under sorted/grouped. The optimizers treat the two differently (None = skipped)."""
    ids = torch.tensor([[1, 2]])
    seen = {}
    for dispatch in ("loop", "sorted", "grouped"):
        m = _moe_model(dispatch)
        _, loss = m(ids[:, :-1], ids[:, 1:])
        loss.backward()
        seen[dispatch] = [m.blocks[0].ffn.experts[e].c_fc.weight.grad for e in range(8)]
    idle = [e for e, g in enumerate(seen["loop"]) if g is None]
    assert idle, "the 1-token batch should leave some of 8 experts idle"
    for e in idle:
        for d in ("sorted", "grouped"):
            assert seen[d][e] is not None and seen[d][e].abs().max().item() == 0.0


@pytest.mark.xfail(strict=True, reason="REVIEW-C1: idle expert is skipped (grad None) under dispatch=loop but keeps "
                                       "moving on its stale momentum (zero grad) under sorted/grouped; the dispatch "
                                       "switch changes the training trajectory")
@pytest.mark.parametrize("fast", ["sorted", "grouped"])
def test_moe_dispatch_does_not_change_optimizer_trajectory(fast):
    """dispatch is documented as an execution switch. Step 1 uses every expert (momentum is built), step 2 leaves
    experts idle. After step 2 the loop-dispatch and fast-dispatch models must still hold the same weights."""
    torch.manual_seed(1)
    big = torch.randint(64, (4, 9))
    tiny = torch.tensor([[3, 4]])
    models = {d: _moe_model(d) for d in ("loop", fast)}
    opts = {d: build_optimizer(m, dict(name="muon", lr=1e-3, muon_lr=0.02, weight_decay=0.0, muon_impl="loop"))
            for d, m in models.items()}
    for ids in (big, tiny):
        for d, m in models.items():
            opts[d].zero_grad()
            _, loss = m(ids[:, :-1], ids[:, 1:])
            loss.backward()
            opts[d].step()
    for (n, a), (_, b) in zip(models["loop"].named_parameters(), models[fast].named_parameters()):
        torch.testing.assert_close(a, b, rtol=0, atol=1e-3, msg=lambda m: f"{n}: {m}")


def test_muon_zero_grad_with_stale_momentum_is_a_full_size_update():
    """Why C1 matters: Newton-Schulz normalises its input, so a zero grad with a decayed momentum buffer still moves
    the weight by about lr * (RMS of an orthogonal matrix), not by a decayed amount."""
    torch.manual_seed(0)
    p = torch.nn.Parameter(torch.randn(16, 8))
    opt = Muon([p], lr=0.02)
    p.grad = torch.randn_like(p)
    opt.step()
    buf0 = opt.state[p]["buf"].norm().item()
    first = None
    for k in range(20):
        p.grad = torch.zeros_like(p)
        before = p.detach().clone()
        opt.step()
        rms = (p.detach() - before).pow(2).mean().sqrt().item()
        first = first or rms
    assert opt.state[p]["buf"].norm().item() < 0.95 ** 20 * buf0 * 1.01      # the buffer decays 0.95 per step
    assert rms > 0.5 * first, f"update after 20 idle steps {rms:.3g} vs first idle step {first:.3g}"


# -------------------------------------------------------------------------------------- state_dict and resume

def _set_grads(model, k):
    g = torch.Generator().manual_seed(k)
    for p in model.parameters():
        p.grad = torch.randn(p.shape, generator=g) * 1e-2


@pytest.mark.parametrize("name,impl", [("muon", "loop"), ("muon", "batched"), ("polar_muon_adamw", "batched")])
def test_save_load_through_bytes_resumes_bit_identically(name, impl):
    """model + optimizer through _to_cpu -> torch.save -> torch.load (the bench checkpoint path), then two more
    steps: identical to the run that never stopped."""
    cfg = ModelConfig(vocab_size=32, block_size=4, n_layer=1, n_head=2, n_embd=8, ffn="moe",
                      moe=dict(num_experts=2, top_k=1, num_shared=1))
    ocfg = dict(name=name, lr=1e-3, muon_lr=0.02, weight_decay=0.01, muon_impl=impl, adamw_impl="foreach")
    torch.manual_seed(0)
    live = GPT(cfg)
    opt = build_optimizer(live, ocfg)
    for k in range(2):
        _set_grads(live, k)
        opt.step()
    buf = io.BytesIO()
    torch.save(_to_cpu({"model": live.state_dict(), "optim": opt.state_dict()}, {}), buf)
    buf.seek(0)
    ck = torch.load(buf, weights_only=True)
    resumed = GPT(cfg)
    resumed.load_state_dict(ck["model"])
    ropt = build_optimizer(resumed, ocfg)
    ropt.load_state_dict(ck["optim"])
    for k in range(2, 4):
        _set_grads(live, k)
        _set_grads(resumed, k)
        opt.step()
        ropt.step()
    for (n, a), (_, b) in zip(live.named_parameters(), resumed.named_parameters()):
        assert torch.equal(a, b), n


def test_checkpoint_holds_every_optimizer_buffer():
    """After one step with all grads present, the saved optimizer state has the Muon momentum for every Muon matrix and
    step/exp_avg/exp_avg_sq for every AdamW parameter, with the parameter's shape."""
    cfg = ModelConfig(vocab_size=32, block_size=4, n_layer=1, n_head=2, n_embd=8, ffn="moe",
                      moe=dict(num_experts=2, top_k=1, num_shared=1))
    m = GPT(cfg)
    opt = build_optimizer(m, dict(name="muon", lr=1e-3, muon_lr=0.02, weight_decay=0.0, muon_impl="batched"))
    _set_grads(m, 0)
    opt.step()
    sd = _to_cpu(opt.state_dict(), {})
    for name, o in opt.named:
        st = sd[name]["state"]
        n_params = sum(len(g["params"]) for g in o.param_groups)
        assert len(st) == n_params
        keys = {"buf"} if name == "opt.muon" else {"step", "exp_avg", "exp_avg_sq"}
        for s in st.values():
            assert keys <= set(s)


@pytest.mark.xfail(strict=True, reason="REVIEW-C2: optimizer load_state_dict restores the saved group settings "
                                       "(impl, lr, initial_lr), so the config of the resumed run is silently ignored")
def test_resume_honours_the_new_runs_muon_impl():
    """PR #34 says checkpoints resume across impls. A run saved with muon_impl=loop and resumed with
    muon_impl=batched must run batched; torch's load_state_dict copies the saved group dict over the new one."""
    cfg = ModelConfig(vocab_size=32, block_size=4, n_layer=1, n_head=2, n_embd=8)
    a = GPT(cfg)
    oa = build_optimizer(a, dict(name="muon", lr=1e-3, muon_lr=0.02, weight_decay=0.0, muon_impl="loop"))
    _set_grads(a, 0)
    oa.step()
    b = GPT(cfg)
    ob = build_optimizer(b, dict(name="muon", lr=1e-3, muon_lr=0.04, weight_decay=0.0, muon_impl="batched"))
    ob.load_state_dict(oa.state_dict())
    group = dict(ob.named)["opt.muon"].param_groups[0]
    assert group["impl"] == "batched" and group["lr"] == 0.04


def test_tied_embedding_is_owned_once_by_adamw():
    cfg = ModelConfig(vocab_size=32, block_size=4, n_layer=1, n_head=2, n_embd=8, embedding="table")
    m = GPT(cfg)
    opt = build_optimizer(m, dict(name="muon", lr=1e-3, muon_lr=0.02, weight_decay=0.1))
    owned = [p for _, o in opt.named for g in o.param_groups for p in g["params"]]
    assert len(owned) == len({id(p) for p in owned}) == len(list(m.parameters()))
    adamw = dict(opt.named)["opt.adamw"]
    head = m.head.weight
    assert any(head is p for g in adamw.param_groups if g["weight_decay"] > 0 for p in g["params"])


def _g5_optim_module(tmp_path):
    try:
        src = subprocess.run(["git", "show", "upstream/main:teams/05-architecture/harness/week2/optim.py"],
                             cwd=LAB, capture_output=True, text=True, check=True).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        pytest.skip("upstream/main (theschoolofai/era-v5-lab) not fetched")
    path = tmp_path / "g5_week2_optim.py"
    path.write_text(src)
    spec = importlib.util.spec_from_file_location("g5_week2_optim", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_g6_muon_matches_g5_week2_muon(tmp_path):
    """G5 harness/week2/optim.py says its Muon is G6's loop path. Same grads, three steps, mixed shapes and a None
    grad: G6 loop, G6 batched and G5 must agree."""
    g5 = _g5_optim_module(tmp_path)
    torch.manual_seed(0)
    init = [torch.randn(s) for s in [(12, 4), (4, 12), (12, 4), (6, 6)]]
    sets = [[torch.nn.Parameter(t.clone()) for t in init] for _ in range(3)]
    opts = [Muon(sets[0], lr=0.02, weight_decay=0.01, impl="loop"),
            Muon(sets[1], lr=0.02, weight_decay=0.01, impl="batched"),
            g5.Muon(sets[2], lr=0.02, weight_decay=0.01)]
    for step in range(3):
        grads = [None if (step == 1 and i == 2) else torch.randn(t.shape) for i, t in enumerate(init)]
        for ps, o in zip(sets, opts):
            for p, g in zip(ps, grads):
                p.grad = None if g is None else g.clone()
            o.step()
    for i in range(len(init)):
        torch.testing.assert_close(sets[1][i], sets[0][i], rtol=0, atol=3e-3)
        torch.testing.assert_close(sets[2][i], sets[0][i], rtol=0, atol=3e-3)


# ----------------------------------------------------------------------------------------------------- loader

def test_shard_of_exactly_block_plus_one_tokens(tmp_path):
    d = _fineweb_dir(tmp_path, {"fineweb_train_000001.bin": list(range(10, 15))})      # T + 1 = 5 tokens
    ld = _loader(source="fineweb10b", batch_size=3, block_size=4, device="cpu", data_dir=d)
    x, y = ld.next_batch()
    assert x.tolist() == [[10, 11, 12, 13]] * 3 and y.tolist() == [[11, 12, 13, 14]] * 3


def test_shard_shorter_than_block_plus_one_is_refused(tmp_path):
    d = _fineweb_dir(tmp_path, {"fineweb_train_000001.bin": list(range(4))})
    with pytest.raises(ValueError, match="block_size \\+ 1"):
        _loader(source="fineweb10b", batch_size=1, block_size=4, device="cpu", data_dir=d)


def test_token_id_at_or_above_vocab_in_a_shard_is_refused(tmp_path):
    d = _fineweb_dir(tmp_path, {"fineweb_train_000001.bin": [131072] * 6})
    ld = _loader(source="fineweb10b", batch_size=1, block_size=4, device="cpu", data_dir=d)
    with pytest.raises(ValueError, match="outside the Brahmic vocabulary"):
        ld.next_batch()


def test_truncated_shard_is_refused(tmp_path):
    _write_raw_shard(tmp_path / "s.bin", list(range(10)), count=11)
    with pytest.raises(ValueError, match="truncated"):
        open_shard(tmp_path / "s.bin")


def test_every_row_of_a_batch_comes_from_one_shard(tmp_path):
    """Observed design (see review C4): one shard is drawn per batch, not per row. With G1's one-pack-per-shard
    layout every batch would hold one pack/language."""
    d = _fineweb_dir(tmp_path, {"fineweb_train_000001.bin": [1] * 64, "fineweb_train_000002.bin": [2] * 64})
    ld = _loader(source="fineweb10b", batch_size=8, block_size=4, device="cpu", data_dir=d, seed=3)
    for _ in range(20):
        x, _ = ld.next_batch()
        assert len(set(x.flatten().tolist())) == 1


@pytest.mark.xfail(strict=True, reason="REVIEW-C3: Loader has no state_dict/load_state_dict; a resumed run "
                                       "restarts the sample stream from the seed and repeats the first batches")
def test_loader_resumes_its_sample_stream():
    a = _loader(source="synthetic", batch_size=2, block_size=4, device="cpu", seed=7)
    seen = [a.next_batch()[0] for _ in range(3)]
    b = _loader(source="synthetic", batch_size=2, block_size=4, device="cpu", seed=7)
    assert hasattr(a, "state_dict") and hasattr(b, "load_state_dict")
    b.load_state_dict(a.state_dict())
    assert not torch.equal(b.next_batch()[0], seen[0])


@pytest.mark.xfail(strict=True, reason="REVIEW-C4: G6 Loader cannot open a G1 shard-v1 directory (file names, "
                                       "manifest and tokenizer pin differ), although shard_format_v1.md says it can")
def test_loader_reads_g1_shard_v1_directory(tmp_path):
    """G1 shard_format_v1.md: '.bin' is byte-compatible with G6's loader, so 'the perf loader reads our shards with
    no change'. The .bin itself opens (asserted first); the directory does not."""
    toks = [5, 6, 7, 8, P1536_EOS, 9, 10, 11, 12, P1536_EOS]
    _write_raw_shard(tmp_path / "code-go-train-000000.bin", toks)
    np.save(tmp_path / "code-go-train-000000.idx.npy", np.array([0, 5, 10], dtype=np.int64))
    (tmp_path / "code-go-train-000000.json").write_text(json.dumps(
        {"schema_version": "shard-v1", "tokenizer_sha256": P1536_SHA256, "eos_token_id": P1536_EOS}))
    assert open_shard(tmp_path / "code-go-train-000000.bin").tolist() == toks
    ld = _loader(source="fineweb10b", batch_size=1, block_size=4, device="cpu", data_dir=tmp_path)
    assert ld.next_batch()[0].shape == (1, 4)


@pytest.mark.xfail(strict=True, reason="REVIEW-C5: G6 pins BrahmicTokenizer-131K (sha 01d968a7, EOS "
                                       "<|end_of_text|> = 36); G3 froze p1536 (sha e6b93a93, EOS 130822) on 16 Nov")
def test_g6_tokenizer_pin_is_the_frozen_g3_tokenizer():
    from dataio import tokenizer as tk
    path = Path(tk.DEFAULT_PATH).expanduser()
    eos = None
    if path.exists():
        eos = json.loads(path.read_text())["model"]["vocab"].get("<|end_of_text|>")
    assert tk.SHA256 == P1536_SHA256
    assert eos in (None, P1536_EOS)


# ------------------------------------------------------------------------------------------------- checkpoint

def test_to_cpu_saves_a_tied_weight_once():
    w = torch.randn(4, 3)
    state = {"tok.weight": w.detach(), "head.weight": w.detach()}      # two objects, one storage (as state_dict gives)
    out = _to_cpu(state, {})
    assert out["tok.weight"] is out["head.weight"]


@pytest.mark.xfail(strict=True, reason="REVIEW-C6: _to_cpu returns the live tensor for CPU tensors (src.to('cpu') "
                                       "is a no-op), not the 'CPU copy' its docstring promises; to_cpu_ms on CPU "
                                       "measures nothing and an async writer would save a later state")
def test_to_cpu_is_a_snapshot_for_cpu_tensors():
    p = torch.zeros(4)
    snap = _to_cpu({"p": p}, {})
    p.add_(1.0)                       # the optimizer keeps training after the save started
    assert snap["p"].sum().item() == 0.0
