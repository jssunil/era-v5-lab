"""Reversible stack: custom backward against plain autograd, plus inversion.  [STUB]

Pairs: ReversibleStack.apply(x, blocks) (fast) vs models.reversible.plain_forward on an fp64 copy
of the same blocks (ref), for ffn="mlp" and ffn="moe"; gradients of x and of every parameter.
Extra test: run forward, then invert every block in reverse: the input comes back (rel err < 1e-4).
Pairs run in fp32 / fp64 (correctness/framework.py: precision). bf16 is a property test, not a pair:
with ffn="moe" under bf16 autocast, models.reversible.reconstruction_error < 1e-3 at 9 and 24 layers
(measured ~2.5e-4 on CPU and A100), and the custom-backward gradient of x is within 1e-3 of plain_forward's.
This end-to-end check cannot prove the routing replay works: at init few tokens sit near a tie
(measured without replay: 9 layers 3.8e-5, no flips; 24 layers 1.3e-3). The replay itself is tested
deterministically in test_moe.py (near-tie construction).
"""


def test_todo():
    raise NotImplementedError("test_reversible.py")
