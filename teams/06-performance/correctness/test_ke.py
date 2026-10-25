"""Kronecker Embedding v1 against an fp64 codec built byte by byte.  [STUB]

Reference: for each token, put 1/sqrt(L) at index b_p * P + p for its L bytes, z-normalise
(models/ke1.py docstring), then multiply by proj.weight^T in fp64. Use models.ke1.token_bytes_random (already
implemented). One pair per KE mode in models.ke1.MODES ("ke1.dynamic", "ke1.cached"; later "ke1.sparse"); the projection
gradient is checked too. Also test token_bytes_from_tiktoken on known GPT-2 tokens: id of " the" ->
b" the"; 50256 -> b"<|endoftext|>"; a token that is part of a UTF-8 character keeps its raw bytes;
padding rows (>= 50257) are one byte 0; every length is 1..max_pos.
KE2 is not covered yet.
"""


def test_todo():
    raise NotImplementedError("test_ke.py")
