"""Kronecker Embedding v1 against an fp64 codec built byte by byte.  [STUB]

Reference: for each token, put 1/sqrt(L) at index b_p * P + p for its L bytes, z-normalise
(models/ke1.py docstring), then multiply by proj.weight^T in fp64. Use models.ke1.token_bytes_random (already
implemented). One pair per KE mode in models.ke1.MODES ("ke1.dynamic", "ke1.cached"; later "ke1.sparse"); the projection
gradient is checked too. Source tokenizer byte-table coverage lives in
test_tokenizer_optimizer.py: all 131072 rows, special tokens and partial UTF-8.
KE2 is not covered yet.
"""


def test_todo():
    raise NotImplementedError("test_ke.py")
