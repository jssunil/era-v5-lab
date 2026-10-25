"""MoE: every dispatch in models.moe.DISPATCH against a token-by-token fp64 reference.  [STUB]

Reference: per token, fp64 router -> softmax -> top-k on (scores + router_bias) -> renormalised gates ->
sum gate * expert(token) + shared experts (the lab uses 1 shared). Read the weights from the module attributes listed in
models/moe.py. Routing replay (deterministic): (1) replay_routing(moe, idx) gives exactly the normal forward's output
when idx is what record_routing captured. (2) Near tie: set router row 2 = row 1 + 1e-6 * random, so
experts 1 and 2 almost tie; record on x, then run x + 1e-4 * noise: without replay some token's top-k
changes, with replay_routing(recorded) none does, and gates still come from the router (gradient flows). Use a large router init (clear top-k margins, so fp32 vs fp64 never picks different
experts) and a non-zero router_bias. Loop over DISPATCH so a new fast dispatch is tested automatically.
Property tests (no pair): router_bias changes selection but not gate values; update_bias() moves the
bias by +-gamma toward balance and clears the counts; no counts in eval mode; shared experts run on every
token; with the lab init (models/moe.py) f is on the dense model's scale.
"""


def test_todo():
    raise NotImplementedError("test_moe.py")
