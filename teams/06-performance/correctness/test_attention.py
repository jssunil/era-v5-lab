"""Attention: models.gpt.GQAttention against a naive fp64 attention.  [STUB]

Reference (write it yourself, from the definition): from the module's c_attn / c_proj weights,
q, k, v (GQA: k, v have n_kv_head heads; query head h uses kv head h // (n_head / n_kv_head)) -> softmax(q k^T / sqrt(d_head) + causal mask) v -> c_proj. Register @pair("attention.causal").
Check outputs and gradients (input and all parameters). Try a T that is not a power of 2 (e.g. 37), and n_kv_head in {n_head, n_head/2, 1}.
Cover both GQA code paths: SDPA enable_gqa (torch >= 2.5) and the repeat_interleave fallback (monkeypatch
models.gpt._SDPA_GQA = False).
"""


def test_todo():
    raise NotImplementedError("test_attention.py")
