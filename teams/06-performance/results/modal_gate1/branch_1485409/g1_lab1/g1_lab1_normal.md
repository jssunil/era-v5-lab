# Bench report — g1_lab1_normal

**GPU:** NVIDIA A100-SXM4-40GB  |  **dtype:** bf16  |  **B x T:** 32 x 512  |  **torch:** 2.15.0+cu132
**commit:** `14854097c57056f326efd0c7a40cc036a73bbc94`  |  **tag:** g1_lab1_normal

## Step (clean)

- median: 406.141 ms
- p10..p90: 398.733 .. 416.681 ms
- tokens/s: 40,341
- MFU: 4.2%  |  HFU: 5.3%

## Diagnostics

### CUDA timing-event allocations

- [OK] clean: events_created_during_steps=0
- [OK] layer: events_created_during_steps=0
- [OK] layer.inner_pass: events_created_during_steps=0

### Benchmark warnings

- [warn] 5 gated part(s) have p10..p90 spread > 10%, so may miss the 5% check: data, bwd:block8, bwd:embed, opt:opt.clip, opt:opt.adamw

## Regions

| part | median ms | p90 | % of step | level |
| :--- | ---: | ---: | ---: | ---: |
| data | 0.691 | 0.794 | 0.2 | 1 |
| fwd | 84.119 | 86.246 | 20.7 | 1 |
| fwd:embed | 4.260 | 4.354 | 1.0 | 2 |
| fwd:embed.ke | 4.180 | 4.270 | 1.0 | 3 |
| fwd:stack | 38.901 | 40.881 | 9.6 | 1 |
| fwd:block0 | 4.287 | 4.523 | 1.1 | 2 |
| fwd:block0.ln1 | 0.052 | 0.053 | 0.0 | 3 |
| fwd:block0.attn.qkv | 0.050 | 0.051 | 0.0 | 3 |
| fwd:block0.attn.sdpa | 0.082 | 0.084 | 0.0 | 3 |
| fwd:block0.attn.proj | 0.039 | 0.040 | 0.0 | 3 |
| fwd:block0.ln2 | 0.053 | 0.054 | 0.0 | 3 |
| fwd:block0.moe.router | 0.137 | 0.140 | 0.0 | 3 |
| fwd:block0.moe.dispatch | 3.839 | 4.024 | 0.9 | 3 |
| fwd:block0.moe.dispatch.expert0 | 0.457 | 0.544 | 0.1 | 3 |
| fwd:block0.moe.dispatch.expert1 | 0.459 | 0.489 | 0.1 | 3 |
| fwd:block0.moe.dispatch.expert2 | 0.472 | 0.494 | 0.1 | 3 |
| fwd:block0.moe.dispatch.expert3 | 0.453 | 0.477 | 0.1 | 3 |
| fwd:block0.moe.dispatch.expert4 | 0.465 | 0.481 | 0.1 | 3 |
| fwd:block0.moe.dispatch.expert5 | 0.450 | 0.474 | 0.1 | 3 |
| fwd:block0.moe.dispatch.expert6 | 0.449 | 0.470 | 0.1 | 3 |
| fwd:block0.moe.dispatch.expert7 | 0.446 | 0.466 | 0.1 | 3 |
| fwd:block0.moe.shared | 0.300 | 0.307 | 0.1 | 3 |
| fwd:block1 | 4.381 | 4.597 | 1.1 | 2 |
| fwd:block1.ln1 | 0.078 | 0.080 | 0.0 | 3 |
| fwd:block1.attn.qkv | 0.131 | 0.140 | 0.0 | 3 |
| fwd:block1.attn.sdpa | 0.112 | 0.114 | 0.0 | 3 |
| fwd:block1.attn.proj | 0.070 | 0.078 | 0.0 | 3 |
| fwd:block1.ln2 | 0.057 | 0.059 | 0.0 | 3 |
| fwd:block1.moe.router | 0.216 | 0.227 | 0.1 | 3 |
| fwd:block1.moe.dispatch | 3.882 | 3.978 | 1.0 | 3 |
| fwd:block1.moe.dispatch.expert0 | 0.456 | 0.478 | 0.1 | 3 |
| fwd:block1.moe.dispatch.expert1 | 0.462 | 0.479 | 0.1 | 3 |
| fwd:block1.moe.dispatch.expert2 | 0.450 | 0.473 | 0.1 | 3 |
| fwd:block1.moe.dispatch.expert3 | 0.454 | 0.473 | 0.1 | 3 |
| fwd:block1.moe.dispatch.expert4 | 0.449 | 0.469 | 0.1 | 3 |
| fwd:block1.moe.dispatch.expert5 | 0.442 | 0.467 | 0.1 | 3 |
| fwd:block1.moe.dispatch.expert6 | 0.449 | 0.467 | 0.1 | 3 |
| fwd:block1.moe.dispatch.expert7 | 0.446 | 0.466 | 0.1 | 3 |
| fwd:block1.moe.shared | 0.298 | 0.302 | 0.1 | 3 |
| fwd:block2 | 4.332 | 4.545 | 1.1 | 2 |
| fwd:block2.ln1 | 0.078 | 0.079 | 0.0 | 3 |
| fwd:block2.attn.qkv | 0.129 | 0.137 | 0.0 | 3 |
| fwd:block2.attn.sdpa | 0.112 | 0.114 | 0.0 | 3 |
| fwd:block2.attn.proj | 0.069 | 0.080 | 0.0 | 3 |
| fwd:block2.ln2 | 0.057 | 0.059 | 0.0 | 3 |
| fwd:block2.moe.router | 0.214 | 0.225 | 0.1 | 3 |
| fwd:block2.moe.dispatch | 3.835 | 3.970 | 0.9 | 3 |
| fwd:block2.moe.dispatch.expert0 | 0.456 | 0.475 | 0.1 | 3 |
| fwd:block2.moe.dispatch.expert1 | 0.445 | 0.467 | 0.1 | 3 |
| fwd:block2.moe.dispatch.expert2 | 0.459 | 0.475 | 0.1 | 3 |
| fwd:block2.moe.dispatch.expert3 | 0.456 | 0.471 | 0.1 | 3 |
| fwd:block2.moe.dispatch.expert4 | 0.438 | 0.462 | 0.1 | 3 |
| fwd:block2.moe.dispatch.expert5 | 0.438 | 0.464 | 0.1 | 3 |
| fwd:block2.moe.dispatch.expert6 | 0.446 | 0.465 | 0.1 | 3 |
| fwd:block2.moe.dispatch.expert7 | 0.440 | 0.464 | 0.1 | 3 |
| fwd:block2.moe.shared | 0.297 | 0.303 | 0.1 | 3 |
| fwd:block3 | 4.323 | 4.501 | 1.1 | 2 |
| fwd:block3.ln1 | 0.078 | 0.079 | 0.0 | 3 |
| fwd:block3.attn.qkv | 0.127 | 0.137 | 0.0 | 3 |
| fwd:block3.attn.sdpa | 0.111 | 0.113 | 0.0 | 3 |
| fwd:block3.attn.proj | 0.068 | 0.076 | 0.0 | 3 |
| fwd:block3.ln2 | 0.056 | 0.058 | 0.0 | 3 |
| fwd:block3.moe.router | 0.209 | 0.221 | 0.1 | 3 |
| fwd:block3.moe.dispatch | 3.829 | 3.947 | 0.9 | 3 |
| fwd:block3.moe.dispatch.expert0 | 0.460 | 0.473 | 0.1 | 3 |
| fwd:block3.moe.dispatch.expert1 | 0.444 | 0.465 | 0.1 | 3 |
| fwd:block3.moe.dispatch.expert2 | 0.454 | 0.470 | 0.1 | 3 |
| fwd:block3.moe.dispatch.expert3 | 0.440 | 0.464 | 0.1 | 3 |
| fwd:block3.moe.dispatch.expert4 | 0.440 | 0.463 | 0.1 | 3 |
| fwd:block3.moe.dispatch.expert5 | 0.451 | 0.466 | 0.1 | 3 |
| fwd:block3.moe.dispatch.expert6 | 0.443 | 0.465 | 0.1 | 3 |
| fwd:block3.moe.dispatch.expert7 | 0.438 | 0.461 | 0.1 | 3 |
| fwd:block3.moe.shared | 0.297 | 0.302 | 0.1 | 3 |
| fwd:block4 | 4.335 | 4.524 | 1.1 | 2 |
| fwd:block4.ln1 | 0.078 | 0.079 | 0.0 | 3 |
| fwd:block4.attn.qkv | 0.127 | 0.135 | 0.0 | 3 |
| fwd:block4.attn.sdpa | 0.111 | 0.113 | 0.0 | 3 |
| fwd:block4.attn.proj | 0.067 | 0.076 | 0.0 | 3 |
| fwd:block4.ln2 | 0.056 | 0.058 | 0.0 | 3 |
| fwd:block4.moe.router | 0.209 | 0.222 | 0.1 | 3 |
| fwd:block4.moe.dispatch | 3.841 | 3.948 | 0.9 | 3 |
| fwd:block4.moe.dispatch.expert0 | 0.456 | 0.474 | 0.1 | 3 |
| fwd:block4.moe.dispatch.expert1 | 0.448 | 0.467 | 0.1 | 3 |
| fwd:block4.moe.dispatch.expert2 | 0.452 | 0.470 | 0.1 | 3 |
| fwd:block4.moe.dispatch.expert3 | 0.445 | 0.465 | 0.1 | 3 |
| fwd:block4.moe.dispatch.expert4 | 0.449 | 0.465 | 0.1 | 3 |
| fwd:block4.moe.dispatch.expert5 | 0.443 | 0.465 | 0.1 | 3 |
| fwd:block4.moe.dispatch.expert6 | 0.451 | 0.471 | 0.1 | 3 |
| fwd:block4.moe.dispatch.expert7 | 0.441 | 0.462 | 0.1 | 3 |
| fwd:block4.moe.shared | 0.297 | 0.302 | 0.1 | 3 |
| fwd:block5 | 4.314 | 4.502 | 1.1 | 2 |
| fwd:block5.ln1 | 0.078 | 0.079 | 0.0 | 3 |
| fwd:block5.attn.qkv | 0.125 | 0.135 | 0.0 | 3 |
| fwd:block5.attn.sdpa | 0.111 | 0.113 | 0.0 | 3 |
| fwd:block5.attn.proj | 0.067 | 0.076 | 0.0 | 3 |
| fwd:block5.ln2 | 0.057 | 0.060 | 0.0 | 3 |
| fwd:block5.moe.router | 0.209 | 0.221 | 0.1 | 3 |
| fwd:block5.moe.dispatch | 3.808 | 3.925 | 0.9 | 3 |
| fwd:block5.moe.dispatch.expert0 | 0.458 | 0.472 | 0.1 | 3 |
| fwd:block5.moe.dispatch.expert1 | 0.442 | 0.465 | 0.1 | 3 |
| fwd:block5.moe.dispatch.expert2 | 0.442 | 0.462 | 0.1 | 3 |
| fwd:block5.moe.dispatch.expert3 | 0.445 | 0.465 | 0.1 | 3 |
| fwd:block5.moe.dispatch.expert4 | 0.442 | 0.461 | 0.1 | 3 |
| fwd:block5.moe.dispatch.expert5 | 0.444 | 0.462 | 0.1 | 3 |
| fwd:block5.moe.dispatch.expert6 | 0.438 | 0.457 | 0.1 | 3 |
| fwd:block5.moe.dispatch.expert7 | 0.438 | 0.460 | 0.1 | 3 |
| fwd:block5.moe.shared | 0.297 | 0.302 | 0.1 | 3 |
| fwd:block6 | 4.311 | 4.507 | 1.1 | 2 |
| fwd:block6.ln1 | 0.078 | 0.080 | 0.0 | 3 |
| fwd:block6.attn.qkv | 0.125 | 0.135 | 0.0 | 3 |
| fwd:block6.attn.sdpa | 0.111 | 0.113 | 0.0 | 3 |
| fwd:block6.attn.proj | 0.067 | 0.076 | 0.0 | 3 |
| fwd:block6.ln2 | 0.056 | 0.058 | 0.0 | 3 |
| fwd:block6.moe.router | 0.208 | 0.219 | 0.1 | 3 |
| fwd:block6.moe.dispatch | 3.818 | 3.941 | 0.9 | 3 |
| fwd:block6.moe.dispatch.expert0 | 0.455 | 0.471 | 0.1 | 3 |
| fwd:block6.moe.dispatch.expert1 | 0.450 | 0.469 | 0.1 | 3 |
| fwd:block6.moe.dispatch.expert2 | 0.449 | 0.463 | 0.1 | 3 |
| fwd:block6.moe.dispatch.expert3 | 0.445 | 0.466 | 0.1 | 3 |
| fwd:block6.moe.dispatch.expert4 | 0.444 | 0.462 | 0.1 | 3 |
| fwd:block6.moe.dispatch.expert5 | 0.444 | 0.465 | 0.1 | 3 |
| fwd:block6.moe.dispatch.expert6 | 0.443 | 0.461 | 0.1 | 3 |
| fwd:block6.moe.dispatch.expert7 | 0.443 | 0.461 | 0.1 | 3 |
| fwd:block6.moe.shared | 0.297 | 0.301 | 0.1 | 3 |
| fwd:block7 | 4.281 | 4.499 | 1.1 | 2 |
| fwd:block7.ln1 | 0.077 | 0.079 | 0.0 | 3 |
| fwd:block7.attn.qkv | 0.124 | 0.134 | 0.0 | 3 |
| fwd:block7.attn.sdpa | 0.111 | 0.113 | 0.0 | 3 |
| fwd:block7.attn.proj | 0.065 | 0.077 | 0.0 | 3 |
| fwd:block7.ln2 | 0.056 | 0.058 | 0.0 | 3 |
| fwd:block7.moe.router | 0.208 | 0.218 | 0.1 | 3 |
| fwd:block7.moe.dispatch | 3.811 | 3.927 | 0.9 | 3 |
| fwd:block7.moe.dispatch.expert0 | 0.450 | 0.468 | 0.1 | 3 |
| fwd:block7.moe.dispatch.expert1 | 0.442 | 0.465 | 0.1 | 3 |
| fwd:block7.moe.dispatch.expert2 | 0.446 | 0.464 | 0.1 | 3 |
| fwd:block7.moe.dispatch.expert3 | 0.449 | 0.462 | 0.1 | 3 |
| fwd:block7.moe.dispatch.expert4 | 0.439 | 0.459 | 0.1 | 3 |
| fwd:block7.moe.dispatch.expert5 | 0.446 | 0.463 | 0.1 | 3 |
| fwd:block7.moe.dispatch.expert6 | 0.442 | 0.460 | 0.1 | 3 |
| fwd:block7.moe.dispatch.expert7 | 0.447 | 0.462 | 0.1 | 3 |
| fwd:block7.moe.shared | 0.297 | 0.302 | 0.1 | 3 |
| fwd:block8 | 4.300 | 4.494 | 1.1 | 2 |
| fwd:block8.ln1 | 0.077 | 0.080 | 0.0 | 3 |
| fwd:block8.attn.qkv | 0.124 | 0.136 | 0.0 | 3 |
| fwd:block8.attn.sdpa | 0.111 | 0.114 | 0.0 | 3 |
| fwd:block8.attn.proj | 0.067 | 0.079 | 0.0 | 3 |
| fwd:block8.ln2 | 0.056 | 0.059 | 0.0 | 3 |
| fwd:block8.moe.router | 0.209 | 0.218 | 0.1 | 3 |
| fwd:block8.moe.dispatch | 3.827 | 3.929 | 0.9 | 3 |
| fwd:block8.moe.dispatch.expert0 | 0.446 | 0.472 | 0.1 | 3 |
| fwd:block8.moe.dispatch.expert1 | 0.455 | 0.470 | 0.1 | 3 |
| fwd:block8.moe.dispatch.expert2 | 0.448 | 0.466 | 0.1 | 3 |
| fwd:block8.moe.dispatch.expert3 | 0.443 | 0.460 | 0.1 | 3 |
| fwd:block8.moe.dispatch.expert4 | 0.445 | 0.461 | 0.1 | 3 |
| fwd:block8.moe.dispatch.expert5 | 0.440 | 0.461 | 0.1 | 3 |
| fwd:block8.moe.dispatch.expert6 | 0.444 | 0.462 | 0.1 | 3 |
| fwd:block8.moe.dispatch.expert7 | 0.450 | 0.464 | 0.1 | 3 |
| fwd:block8.moe.shared | 0.298 | 0.301 | 0.1 | 3 |
| fwd:head+loss | 40.844 | 40.876 | 10.1 | 2 |
| bwd | 187.204 | 194.259 | 46.1 | 1 |
| bwd:head+loss | 48.138 | 48.155 | 11.9 | 2 |
| bwd:stack | 138.709 | 145.713 | 34.2 | 1 |
| bwd:block8 | 15.516 | 17.461 | 3.8 | 2 |
| bwd.invert:block8 | 4.487 | 5.255 | 1.1 | 3 |
| bwd.invert:block8.ln1 | 0.053 | 0.054 | 0.0 | 3 |
| bwd.invert:block8.attn.qkv | 0.050 | 0.051 | 0.0 | 3 |
| bwd.invert:block8.attn.sdpa | 0.082 | 0.083 | 0.0 | 3 |
| bwd.invert:block8.attn.proj | 0.039 | 0.040 | 0.0 | 3 |
| bwd.invert:block8.ln2 | 0.053 | 0.054 | 0.0 | 3 |
| bwd.invert:block8.moe.router | 0.067 | 0.068 | 0.0 | 3 |
| bwd.invert:block8.moe.dispatch | 3.670 | 4.361 | 0.9 | 3 |
| bwd.invert:block8.moe.dispatch.expert0 | 0.437 | 0.710 | 0.1 | 3 |
| bwd.invert:block8.moe.dispatch.expert1 | 0.446 | 0.500 | 0.1 | 3 |
| bwd.invert:block8.moe.dispatch.expert2 | 0.437 | 0.465 | 0.1 | 3 |
| bwd.invert:block8.moe.dispatch.expert3 | 0.434 | 0.462 | 0.1 | 3 |
| bwd.invert:block8.moe.dispatch.expert4 | 0.432 | 0.458 | 0.1 | 3 |
| bwd.invert:block8.moe.dispatch.expert5 | 0.432 | 0.463 | 0.1 | 3 |
| bwd.invert:block8.moe.dispatch.expert6 | 0.432 | 0.455 | 0.1 | 3 |
| bwd.invert:block8.moe.dispatch.expert7 | 0.430 | 0.465 | 0.1 | 3 |
| bwd.invert:block8.moe.shared | 0.299 | 0.313 | 0.1 | 3 |
| bwd.recompute:block8 | 5.171 | 5.609 | 1.3 | 3 |
| bwd.recompute:block8.ln1 | 0.086 | 0.113 | 0.0 | 3 |
| bwd.recompute:block8.attn.qkv | 0.142 | 0.184 | 0.0 | 3 |
| bwd.recompute:block8.attn.sdpa | 0.126 | 0.164 | 0.0 | 3 |
| bwd.recompute:block8.attn.proj | 0.079 | 0.096 | 0.0 | 3 |
| bwd.recompute:block8.ln2 | 0.063 | 0.073 | 0.0 | 3 |
| bwd.recompute:block8.moe.router | 0.181 | 0.242 | 0.0 | 3 |
| bwd.recompute:block8.moe.dispatch | 3.928 | 4.194 | 1.0 | 3 |
| bwd.recompute:block8.moe.dispatch.expert0 | 0.462 | 0.502 | 0.1 | 3 |
| bwd.recompute:block8.moe.dispatch.expert1 | 0.463 | 0.493 | 0.1 | 3 |
| bwd.recompute:block8.moe.dispatch.expert2 | 0.457 | 0.485 | 0.1 | 3 |
| bwd.recompute:block8.moe.dispatch.expert3 | 0.456 | 0.477 | 0.1 | 3 |
| bwd.recompute:block8.moe.dispatch.expert4 | 0.455 | 0.479 | 0.1 | 3 |
| bwd.recompute:block8.moe.dispatch.expert5 | 0.455 | 0.479 | 0.1 | 3 |
| bwd.recompute:block8.moe.dispatch.expert6 | 0.455 | 0.476 | 0.1 | 3 |
| bwd.recompute:block8.moe.dispatch.expert7 | 0.455 | 0.481 | 0.1 | 3 |
| bwd.recompute:block8.moe.shared | 0.303 | 0.310 | 0.1 | 3 |
| bwd:block8.grad | 6.962 | 7.410 | 1.7 | 3 |
| bwd:block7 | 15.496 | 16.293 | 3.8 | 2 |
| bwd.invert:block7 | 4.914 | 5.196 | 1.2 | 3 |
| bwd.invert:block7.ln1 | 0.073 | 0.083 | 0.0 | 3 |
| bwd.invert:block7.attn.qkv | 0.133 | 0.149 | 0.0 | 3 |
| bwd.invert:block7.attn.sdpa | 0.112 | 0.114 | 0.0 | 3 |
| bwd.invert:block7.attn.proj | 0.070 | 0.081 | 0.0 | 3 |
| bwd.invert:block7.ln2 | 0.058 | 0.061 | 0.0 | 3 |
| bwd.invert:block7.moe.router | 0.165 | 0.178 | 0.0 | 3 |
| bwd.invert:block7.moe.dispatch | 3.767 | 3.897 | 0.9 | 3 |
| bwd.invert:block7.moe.dispatch.expert0 | 0.450 | 0.469 | 0.1 | 3 |
| bwd.invert:block7.moe.dispatch.expert1 | 0.443 | 0.462 | 0.1 | 3 |
| bwd.invert:block7.moe.dispatch.expert2 | 0.436 | 0.450 | 0.1 | 3 |
| bwd.invert:block7.moe.dispatch.expert3 | 0.436 | 0.455 | 0.1 | 3 |
| bwd.invert:block7.moe.dispatch.expert4 | 0.432 | 0.449 | 0.1 | 3 |
| bwd.invert:block7.moe.dispatch.expert5 | 0.432 | 0.451 | 0.1 | 3 |
| bwd.invert:block7.moe.dispatch.expert6 | 0.431 | 0.444 | 0.1 | 3 |
| bwd.invert:block7.moe.dispatch.expert7 | 0.431 | 0.447 | 0.1 | 3 |
| bwd.invert:block7.moe.shared | 0.299 | 0.308 | 0.1 | 3 |
| bwd.recompute:block7 | 5.149 | 5.303 | 1.3 | 3 |
| bwd.recompute:block7.ln1 | 0.085 | 0.087 | 0.0 | 3 |
| bwd.recompute:block7.attn.qkv | 0.143 | 0.154 | 0.0 | 3 |
| bwd.recompute:block7.attn.sdpa | 0.120 | 0.122 | 0.0 | 3 |
| bwd.recompute:block7.attn.proj | 0.077 | 0.087 | 0.0 | 3 |
| bwd.recompute:block7.ln2 | 0.063 | 0.066 | 0.0 | 3 |
| bwd.recompute:block7.moe.router | 0.177 | 0.189 | 0.0 | 3 |
| bwd.recompute:block7.moe.dispatch | 3.926 | 4.039 | 1.0 | 3 |
| bwd.recompute:block7.moe.dispatch.expert0 | 0.461 | 0.471 | 0.1 | 3 |
| bwd.recompute:block7.moe.dispatch.expert1 | 0.461 | 0.474 | 0.1 | 3 |
| bwd.recompute:block7.moe.dispatch.expert2 | 0.456 | 0.468 | 0.1 | 3 |
| bwd.recompute:block7.moe.dispatch.expert3 | 0.457 | 0.470 | 0.1 | 3 |
| bwd.recompute:block7.moe.dispatch.expert4 | 0.453 | 0.469 | 0.1 | 3 |
| bwd.recompute:block7.moe.dispatch.expert5 | 0.455 | 0.469 | 0.1 | 3 |
| bwd.recompute:block7.moe.dispatch.expert6 | 0.453 | 0.470 | 0.1 | 3 |
| bwd.recompute:block7.moe.dispatch.expert7 | 0.456 | 0.471 | 0.1 | 3 |
| bwd.recompute:block7.moe.shared | 0.303 | 0.309 | 0.1 | 3 |
| bwd:block7.grad | 6.906 | 7.081 | 1.7 | 3 |
| bwd:block6 | 15.396 | 16.063 | 3.8 | 2 |
| bwd.invert:block6 | 4.869 | 5.091 | 1.2 | 3 |
| bwd.invert:block6.ln1 | 0.054 | 0.081 | 0.0 | 3 |
| bwd.invert:block6.attn.qkv | 0.124 | 0.141 | 0.0 | 3 |
| bwd.invert:block6.attn.sdpa | 0.112 | 0.114 | 0.0 | 3 |
| bwd.invert:block6.attn.proj | 0.070 | 0.082 | 0.0 | 3 |
| bwd.invert:block6.ln2 | 0.058 | 0.062 | 0.0 | 3 |
| bwd.invert:block6.moe.router | 0.164 | 0.175 | 0.0 | 3 |
| bwd.invert:block6.moe.dispatch | 3.760 | 3.880 | 0.9 | 3 |
| bwd.invert:block6.moe.dispatch.expert0 | 0.450 | 0.470 | 0.1 | 3 |
| bwd.invert:block6.moe.dispatch.expert1 | 0.441 | 0.457 | 0.1 | 3 |
| bwd.invert:block6.moe.dispatch.expert2 | 0.436 | 0.453 | 0.1 | 3 |
| bwd.invert:block6.moe.dispatch.expert3 | 0.435 | 0.451 | 0.1 | 3 |
| bwd.invert:block6.moe.dispatch.expert4 | 0.433 | 0.446 | 0.1 | 3 |
| bwd.invert:block6.moe.dispatch.expert5 | 0.434 | 0.453 | 0.1 | 3 |
| bwd.invert:block6.moe.dispatch.expert6 | 0.431 | 0.443 | 0.1 | 3 |
| bwd.invert:block6.moe.dispatch.expert7 | 0.428 | 0.445 | 0.1 | 3 |
| bwd.invert:block6.moe.shared | 0.298 | 0.304 | 0.1 | 3 |
| bwd.recompute:block6 | 5.137 | 5.292 | 1.3 | 3 |
| bwd.recompute:block6.ln1 | 0.085 | 0.090 | 0.0 | 3 |
| bwd.recompute:block6.attn.qkv | 0.138 | 0.147 | 0.0 | 3 |
| bwd.recompute:block6.attn.sdpa | 0.124 | 0.126 | 0.0 | 3 |
| bwd.recompute:block6.attn.proj | 0.077 | 0.089 | 0.0 | 3 |
| bwd.recompute:block6.ln2 | 0.062 | 0.066 | 0.0 | 3 |
| bwd.recompute:block6.moe.router | 0.175 | 0.185 | 0.0 | 3 |
| bwd.recompute:block6.moe.dispatch | 3.923 | 4.040 | 1.0 | 3 |
| bwd.recompute:block6.moe.dispatch.expert0 | 0.456 | 0.470 | 0.1 | 3 |
| bwd.recompute:block6.moe.dispatch.expert1 | 0.456 | 0.467 | 0.1 | 3 |
| bwd.recompute:block6.moe.dispatch.expert2 | 0.453 | 0.468 | 0.1 | 3 |
| bwd.recompute:block6.moe.dispatch.expert3 | 0.452 | 0.464 | 0.1 | 3 |
| bwd.recompute:block6.moe.dispatch.expert4 | 0.452 | 0.465 | 0.1 | 3 |
| bwd.recompute:block6.moe.dispatch.expert5 | 0.457 | 0.472 | 0.1 | 3 |
| bwd.recompute:block6.moe.dispatch.expert6 | 0.458 | 0.474 | 0.1 | 3 |
| bwd.recompute:block6.moe.dispatch.expert7 | 0.458 | 0.474 | 0.1 | 3 |
| bwd.recompute:block6.moe.shared | 0.302 | 0.307 | 0.1 | 3 |
| bwd:block6.grad | 6.913 | 7.082 | 1.7 | 3 |
| bwd:block5 | 15.359 | 15.969 | 3.8 | 2 |
| bwd.invert:block5 | 4.861 | 5.034 | 1.2 | 3 |
| bwd.invert:block5.ln1 | 0.054 | 0.075 | 0.0 | 3 |
| bwd.invert:block5.attn.qkv | 0.123 | 0.141 | 0.0 | 3 |
| bwd.invert:block5.attn.sdpa | 0.112 | 0.114 | 0.0 | 3 |
| bwd.invert:block5.attn.proj | 0.069 | 0.079 | 0.0 | 3 |
| bwd.invert:block5.ln2 | 0.058 | 0.062 | 0.0 | 3 |
| bwd.invert:block5.moe.router | 0.164 | 0.176 | 0.0 | 3 |
| bwd.invert:block5.moe.dispatch | 3.750 | 3.863 | 0.9 | 3 |
| bwd.invert:block5.moe.dispatch.expert0 | 0.445 | 0.464 | 0.1 | 3 |
| bwd.invert:block5.moe.dispatch.expert1 | 0.439 | 0.453 | 0.1 | 3 |
| bwd.invert:block5.moe.dispatch.expert2 | 0.436 | 0.450 | 0.1 | 3 |
| bwd.invert:block5.moe.dispatch.expert3 | 0.434 | 0.447 | 0.1 | 3 |
| bwd.invert:block5.moe.dispatch.expert4 | 0.433 | 0.450 | 0.1 | 3 |
| bwd.invert:block5.moe.dispatch.expert5 | 0.432 | 0.445 | 0.1 | 3 |
| bwd.invert:block5.moe.dispatch.expert6 | 0.433 | 0.446 | 0.1 | 3 |
| bwd.invert:block5.moe.dispatch.expert7 | 0.429 | 0.442 | 0.1 | 3 |
| bwd.invert:block5.moe.shared | 0.299 | 0.307 | 0.1 | 3 |
| bwd.recompute:block5 | 5.149 | 5.295 | 1.3 | 3 |
| bwd.recompute:block5.ln1 | 0.085 | 0.087 | 0.0 | 3 |
| bwd.recompute:block5.attn.qkv | 0.140 | 0.150 | 0.0 | 3 |
| bwd.recompute:block5.attn.sdpa | 0.119 | 0.121 | 0.0 | 3 |
| bwd.recompute:block5.attn.proj | 0.076 | 0.085 | 0.0 | 3 |
| bwd.recompute:block5.ln2 | 0.062 | 0.065 | 0.0 | 3 |
| bwd.recompute:block5.moe.router | 0.175 | 0.187 | 0.0 | 3 |
| bwd.recompute:block5.moe.dispatch | 3.932 | 4.041 | 1.0 | 3 |
| bwd.recompute:block5.moe.dispatch.expert0 | 0.457 | 0.468 | 0.1 | 3 |
| bwd.recompute:block5.moe.dispatch.expert1 | 0.458 | 0.470 | 0.1 | 3 |
| bwd.recompute:block5.moe.dispatch.expert2 | 0.455 | 0.464 | 0.1 | 3 |
| bwd.recompute:block5.moe.dispatch.expert3 | 0.456 | 0.469 | 0.1 | 3 |
| bwd.recompute:block5.moe.dispatch.expert4 | 0.457 | 0.470 | 0.1 | 3 |
| bwd.recompute:block5.moe.dispatch.expert5 | 0.458 | 0.474 | 0.1 | 3 |
| bwd.recompute:block5.moe.dispatch.expert6 | 0.459 | 0.475 | 0.1 | 3 |
| bwd.recompute:block5.moe.dispatch.expert7 | 0.457 | 0.473 | 0.1 | 3 |
| bwd.recompute:block5.moe.shared | 0.303 | 0.310 | 0.1 | 3 |
| bwd:block5.grad | 6.873 | 7.032 | 1.7 | 3 |
| bwd:block4 | 15.328 | 16.013 | 3.8 | 2 |
| bwd.invert:block4 | 4.855 | 5.060 | 1.2 | 3 |
| bwd.invert:block4.ln1 | 0.054 | 0.078 | 0.0 | 3 |
| bwd.invert:block4.attn.qkv | 0.125 | 0.141 | 0.0 | 3 |
| bwd.invert:block4.attn.sdpa | 0.112 | 0.113 | 0.0 | 3 |
| bwd.invert:block4.attn.proj | 0.069 | 0.080 | 0.0 | 3 |
| bwd.invert:block4.ln2 | 0.058 | 0.061 | 0.0 | 3 |
| bwd.invert:block4.moe.router | 0.163 | 0.175 | 0.0 | 3 |
| bwd.invert:block4.moe.dispatch | 3.742 | 3.880 | 0.9 | 3 |
| bwd.invert:block4.moe.dispatch.expert0 | 0.447 | 0.462 | 0.1 | 3 |
| bwd.invert:block4.moe.dispatch.expert1 | 0.438 | 0.453 | 0.1 | 3 |
| bwd.invert:block4.moe.dispatch.expert2 | 0.436 | 0.449 | 0.1 | 3 |
| bwd.invert:block4.moe.dispatch.expert3 | 0.431 | 0.449 | 0.1 | 3 |
| bwd.invert:block4.moe.dispatch.expert4 | 0.431 | 0.450 | 0.1 | 3 |
| bwd.invert:block4.moe.dispatch.expert5 | 0.429 | 0.445 | 0.1 | 3 |
| bwd.invert:block4.moe.dispatch.expert6 | 0.433 | 0.448 | 0.1 | 3 |
| bwd.invert:block4.moe.dispatch.expert7 | 0.429 | 0.446 | 0.1 | 3 |
| bwd.invert:block4.moe.shared | 0.298 | 0.303 | 0.1 | 3 |
| bwd.recompute:block4 | 5.151 | 5.322 | 1.3 | 3 |
| bwd.recompute:block4.ln1 | 0.085 | 0.086 | 0.0 | 3 |
| bwd.recompute:block4.attn.qkv | 0.138 | 0.148 | 0.0 | 3 |
| bwd.recompute:block4.attn.sdpa | 0.122 | 0.125 | 0.0 | 3 |
| bwd.recompute:block4.attn.proj | 0.076 | 0.088 | 0.0 | 3 |
| bwd.recompute:block4.ln2 | 0.062 | 0.066 | 0.0 | 3 |
| bwd.recompute:block4.moe.router | 0.174 | 0.185 | 0.0 | 3 |
| bwd.recompute:block4.moe.dispatch | 3.932 | 4.068 | 1.0 | 3 |
| bwd.recompute:block4.moe.dispatch.expert0 | 0.457 | 0.469 | 0.1 | 3 |
| bwd.recompute:block4.moe.dispatch.expert1 | 0.456 | 0.468 | 0.1 | 3 |
| bwd.recompute:block4.moe.dispatch.expert2 | 0.459 | 0.474 | 0.1 | 3 |
| bwd.recompute:block4.moe.dispatch.expert3 | 0.459 | 0.476 | 0.1 | 3 |
| bwd.recompute:block4.moe.dispatch.expert4 | 0.458 | 0.474 | 0.1 | 3 |
| bwd.recompute:block4.moe.dispatch.expert5 | 0.456 | 0.471 | 0.1 | 3 |
| bwd.recompute:block4.moe.dispatch.expert6 | 0.454 | 0.471 | 0.1 | 3 |
| bwd.recompute:block4.moe.dispatch.expert7 | 0.457 | 0.474 | 0.1 | 3 |
| bwd.recompute:block4.moe.shared | 0.303 | 0.312 | 0.1 | 3 |
| bwd:block4.grad | 6.871 | 7.099 | 1.7 | 3 |
| bwd:block3 | 15.354 | 16.054 | 3.8 | 2 |
| bwd.invert:block3 | 4.867 | 5.047 | 1.2 | 3 |
| bwd.invert:block3.ln1 | 0.054 | 0.082 | 0.0 | 3 |
| bwd.invert:block3.attn.qkv | 0.126 | 0.141 | 0.0 | 3 |
| bwd.invert:block3.attn.sdpa | 0.112 | 0.114 | 0.0 | 3 |
| bwd.invert:block3.attn.proj | 0.069 | 0.082 | 0.0 | 3 |
| bwd.invert:block3.ln2 | 0.058 | 0.062 | 0.0 | 3 |
| bwd.invert:block3.moe.router | 0.164 | 0.176 | 0.0 | 3 |
| bwd.invert:block3.moe.dispatch | 3.752 | 3.884 | 0.9 | 3 |
| bwd.invert:block3.moe.dispatch.expert0 | 0.447 | 0.463 | 0.1 | 3 |
| bwd.invert:block3.moe.dispatch.expert1 | 0.440 | 0.452 | 0.1 | 3 |
| bwd.invert:block3.moe.dispatch.expert2 | 0.435 | 0.452 | 0.1 | 3 |
| bwd.invert:block3.moe.dispatch.expert3 | 0.432 | 0.447 | 0.1 | 3 |
| bwd.invert:block3.moe.dispatch.expert4 | 0.431 | 0.447 | 0.1 | 3 |
| bwd.invert:block3.moe.dispatch.expert5 | 0.434 | 0.445 | 0.1 | 3 |
| bwd.invert:block3.moe.dispatch.expert6 | 0.430 | 0.448 | 0.1 | 3 |
| bwd.invert:block3.moe.dispatch.expert7 | 0.431 | 0.447 | 0.1 | 3 |
| bwd.invert:block3.moe.shared | 0.299 | 0.306 | 0.1 | 3 |
| bwd.recompute:block3 | 5.158 | 5.285 | 1.3 | 3 |
| bwd.recompute:block3.ln1 | 0.085 | 0.086 | 0.0 | 3 |
| bwd.recompute:block3.attn.qkv | 0.138 | 0.150 | 0.0 | 3 |
| bwd.recompute:block3.attn.sdpa | 0.123 | 0.126 | 0.0 | 3 |
| bwd.recompute:block3.attn.proj | 0.077 | 0.087 | 0.0 | 3 |
| bwd.recompute:block3.ln2 | 0.062 | 0.065 | 0.0 | 3 |
| bwd.recompute:block3.moe.router | 0.175 | 0.185 | 0.0 | 3 |
| bwd.recompute:block3.moe.dispatch | 3.936 | 4.034 | 1.0 | 3 |
| bwd.recompute:block3.moe.dispatch.expert0 | 0.459 | 0.472 | 0.1 | 3 |
| bwd.recompute:block3.moe.dispatch.expert1 | 0.460 | 0.471 | 0.1 | 3 |
| bwd.recompute:block3.moe.dispatch.expert2 | 0.457 | 0.469 | 0.1 | 3 |
| bwd.recompute:block3.moe.dispatch.expert3 | 0.459 | 0.472 | 0.1 | 3 |
| bwd.recompute:block3.moe.dispatch.expert4 | 0.454 | 0.466 | 0.1 | 3 |
| bwd.recompute:block3.moe.dispatch.expert5 | 0.457 | 0.474 | 0.1 | 3 |
| bwd.recompute:block3.moe.dispatch.expert6 | 0.454 | 0.468 | 0.1 | 3 |
| bwd.recompute:block3.moe.dispatch.expert7 | 0.460 | 0.479 | 0.1 | 3 |
| bwd.recompute:block3.moe.shared | 0.303 | 0.309 | 0.1 | 3 |
| bwd:block3.grad | 6.849 | 7.011 | 1.7 | 3 |
| bwd:block2 | 15.293 | 15.851 | 3.8 | 2 |
| bwd.invert:block2 | 4.865 | 5.034 | 1.2 | 3 |
| bwd.invert:block2.ln1 | 0.054 | 0.077 | 0.0 | 3 |
| bwd.invert:block2.attn.qkv | 0.127 | 0.140 | 0.0 | 3 |
| bwd.invert:block2.attn.sdpa | 0.111 | 0.113 | 0.0 | 3 |
| bwd.invert:block2.attn.proj | 0.069 | 0.079 | 0.0 | 3 |
| bwd.invert:block2.ln2 | 0.057 | 0.060 | 0.0 | 3 |
| bwd.invert:block2.moe.router | 0.164 | 0.175 | 0.0 | 3 |
| bwd.invert:block2.moe.dispatch | 3.756 | 3.880 | 0.9 | 3 |
| bwd.invert:block2.moe.dispatch.expert0 | 0.447 | 0.462 | 0.1 | 3 |
| bwd.invert:block2.moe.dispatch.expert1 | 0.438 | 0.456 | 0.1 | 3 |
| bwd.invert:block2.moe.dispatch.expert2 | 0.437 | 0.452 | 0.1 | 3 |
| bwd.invert:block2.moe.dispatch.expert3 | 0.435 | 0.450 | 0.1 | 3 |
| bwd.invert:block2.moe.dispatch.expert4 | 0.432 | 0.449 | 0.1 | 3 |
| bwd.invert:block2.moe.dispatch.expert5 | 0.432 | 0.447 | 0.1 | 3 |
| bwd.invert:block2.moe.dispatch.expert6 | 0.431 | 0.450 | 0.1 | 3 |
| bwd.invert:block2.moe.dispatch.expert7 | 0.431 | 0.443 | 0.1 | 3 |
| bwd.invert:block2.moe.shared | 0.299 | 0.308 | 0.1 | 3 |
| bwd.recompute:block2 | 5.154 | 5.269 | 1.3 | 3 |
| bwd.recompute:block2.ln1 | 0.084 | 0.086 | 0.0 | 3 |
| bwd.recompute:block2.attn.qkv | 0.137 | 0.147 | 0.0 | 3 |
| bwd.recompute:block2.attn.sdpa | 0.125 | 0.127 | 0.0 | 3 |
| bwd.recompute:block2.attn.proj | 0.076 | 0.087 | 0.0 | 3 |
| bwd.recompute:block2.ln2 | 0.062 | 0.066 | 0.0 | 3 |
| bwd.recompute:block2.moe.router | 0.174 | 0.185 | 0.0 | 3 |
| bwd.recompute:block2.moe.dispatch | 3.933 | 4.020 | 1.0 | 3 |
| bwd.recompute:block2.moe.dispatch.expert0 | 0.459 | 0.472 | 0.1 | 3 |
| bwd.recompute:block2.moe.dispatch.expert1 | 0.456 | 0.471 | 0.1 | 3 |
| bwd.recompute:block2.moe.dispatch.expert2 | 0.458 | 0.470 | 0.1 | 3 |
| bwd.recompute:block2.moe.dispatch.expert3 | 0.458 | 0.471 | 0.1 | 3 |
| bwd.recompute:block2.moe.dispatch.expert4 | 0.458 | 0.475 | 0.1 | 3 |
| bwd.recompute:block2.moe.dispatch.expert5 | 0.455 | 0.467 | 0.1 | 3 |
| bwd.recompute:block2.moe.dispatch.expert6 | 0.458 | 0.472 | 0.1 | 3 |
| bwd.recompute:block2.moe.dispatch.expert7 | 0.455 | 0.473 | 0.1 | 3 |
| bwd.recompute:block2.moe.shared | 0.302 | 0.306 | 0.1 | 3 |
| bwd:block2.grad | 6.815 | 7.004 | 1.7 | 3 |
| bwd:block1 | 15.295 | 15.911 | 3.8 | 2 |
| bwd.invert:block1 | 4.866 | 5.029 | 1.2 | 3 |
| bwd.invert:block1.ln1 | 0.054 | 0.079 | 0.0 | 3 |
| bwd.invert:block1.attn.qkv | 0.129 | 0.141 | 0.0 | 3 |
| bwd.invert:block1.attn.sdpa | 0.112 | 0.114 | 0.0 | 3 |
| bwd.invert:block1.attn.proj | 0.069 | 0.079 | 0.0 | 3 |
| bwd.invert:block1.ln2 | 0.058 | 0.061 | 0.0 | 3 |
| bwd.invert:block1.moe.router | 0.163 | 0.174 | 0.0 | 3 |
| bwd.invert:block1.moe.dispatch | 3.750 | 3.873 | 0.9 | 3 |
| bwd.invert:block1.moe.dispatch.expert0 | 0.445 | 0.458 | 0.1 | 3 |
| bwd.invert:block1.moe.dispatch.expert1 | 0.442 | 0.456 | 0.1 | 3 |
| bwd.invert:block1.moe.dispatch.expert2 | 0.437 | 0.452 | 0.1 | 3 |
| bwd.invert:block1.moe.dispatch.expert3 | 0.435 | 0.448 | 0.1 | 3 |
| bwd.invert:block1.moe.dispatch.expert4 | 0.434 | 0.453 | 0.1 | 3 |
| bwd.invert:block1.moe.dispatch.expert5 | 0.433 | 0.447 | 0.1 | 3 |
| bwd.invert:block1.moe.dispatch.expert6 | 0.431 | 0.447 | 0.1 | 3 |
| bwd.invert:block1.moe.dispatch.expert7 | 0.429 | 0.443 | 0.1 | 3 |
| bwd.invert:block1.moe.shared | 0.299 | 0.309 | 0.1 | 3 |
| bwd.recompute:block1 | 5.145 | 5.288 | 1.3 | 3 |
| bwd.recompute:block1.ln1 | 0.085 | 0.086 | 0.0 | 3 |
| bwd.recompute:block1.attn.qkv | 0.138 | 0.148 | 0.0 | 3 |
| bwd.recompute:block1.attn.sdpa | 0.126 | 0.128 | 0.0 | 3 |
| bwd.recompute:block1.attn.proj | 0.077 | 0.085 | 0.0 | 3 |
| bwd.recompute:block1.ln2 | 0.062 | 0.065 | 0.0 | 3 |
| bwd.recompute:block1.moe.router | 0.174 | 0.187 | 0.0 | 3 |
| bwd.recompute:block1.moe.dispatch | 3.925 | 4.043 | 1.0 | 3 |
| bwd.recompute:block1.moe.dispatch.expert0 | 0.457 | 0.469 | 0.1 | 3 |
| bwd.recompute:block1.moe.dispatch.expert1 | 0.460 | 0.470 | 0.1 | 3 |
| bwd.recompute:block1.moe.dispatch.expert2 | 0.457 | 0.476 | 0.1 | 3 |
| bwd.recompute:block1.moe.dispatch.expert3 | 0.458 | 0.470 | 0.1 | 3 |
| bwd.recompute:block1.moe.dispatch.expert4 | 0.456 | 0.470 | 0.1 | 3 |
| bwd.recompute:block1.moe.dispatch.expert5 | 0.456 | 0.472 | 0.1 | 3 |
| bwd.recompute:block1.moe.dispatch.expert6 | 0.452 | 0.470 | 0.1 | 3 |
| bwd.recompute:block1.moe.dispatch.expert7 | 0.456 | 0.473 | 0.1 | 3 |
| bwd.recompute:block1.moe.shared | 0.302 | 0.307 | 0.1 | 3 |
| bwd:block1.grad | 6.838 | 7.000 | 1.7 | 3 |
| bwd:block0 | 15.256 | 15.820 | 3.8 | 2 |
| bwd.invert:block0 | 4.892 | 5.084 | 1.2 | 3 |
| bwd.invert:block0.ln1 | 0.054 | 0.083 | 0.0 | 3 |
| bwd.invert:block0.attn.qkv | 0.131 | 0.144 | 0.0 | 3 |
| bwd.invert:block0.attn.sdpa | 0.112 | 0.114 | 0.0 | 3 |
| bwd.invert:block0.attn.proj | 0.068 | 0.077 | 0.0 | 3 |
| bwd.invert:block0.ln2 | 0.058 | 0.062 | 0.0 | 3 |
| bwd.invert:block0.moe.router | 0.164 | 0.175 | 0.0 | 3 |
| bwd.invert:block0.moe.dispatch | 3.774 | 3.897 | 0.9 | 3 |
| bwd.invert:block0.moe.dispatch.expert0 | 0.445 | 0.462 | 0.1 | 3 |
| bwd.invert:block0.moe.dispatch.expert1 | 0.443 | 0.460 | 0.1 | 3 |
| bwd.invert:block0.moe.dispatch.expert2 | 0.440 | 0.458 | 0.1 | 3 |
| bwd.invert:block0.moe.dispatch.expert3 | 0.436 | 0.455 | 0.1 | 3 |
| bwd.invert:block0.moe.dispatch.expert4 | 0.436 | 0.452 | 0.1 | 3 |
| bwd.invert:block0.moe.dispatch.expert5 | 0.436 | 0.453 | 0.1 | 3 |
| bwd.invert:block0.moe.dispatch.expert6 | 0.432 | 0.446 | 0.1 | 3 |
| bwd.invert:block0.moe.dispatch.expert7 | 0.432 | 0.449 | 0.1 | 3 |
| bwd.invert:block0.moe.shared | 0.300 | 0.307 | 0.1 | 3 |
| bwd.recompute:block0 | 5.144 | 5.259 | 1.3 | 3 |
| bwd.recompute:block0.ln1 | 0.085 | 0.087 | 0.0 | 3 |
| bwd.recompute:block0.attn.qkv | 0.137 | 0.148 | 0.0 | 3 |
| bwd.recompute:block0.attn.sdpa | 0.127 | 0.129 | 0.0 | 3 |
| bwd.recompute:block0.attn.proj | 0.077 | 0.087 | 0.0 | 3 |
| bwd.recompute:block0.ln2 | 0.062 | 0.066 | 0.0 | 3 |
| bwd.recompute:block0.moe.router | 0.175 | 0.187 | 0.0 | 3 |
| bwd.recompute:block0.moe.dispatch | 3.922 | 4.017 | 1.0 | 3 |
| bwd.recompute:block0.moe.dispatch.expert0 | 0.457 | 0.472 | 0.1 | 3 |
| bwd.recompute:block0.moe.dispatch.expert1 | 0.458 | 0.468 | 0.1 | 3 |
| bwd.recompute:block0.moe.dispatch.expert2 | 0.457 | 0.469 | 0.1 | 3 |
| bwd.recompute:block0.moe.dispatch.expert3 | 0.459 | 0.475 | 0.1 | 3 |
| bwd.recompute:block0.moe.dispatch.expert4 | 0.454 | 0.470 | 0.1 | 3 |
| bwd.recompute:block0.moe.dispatch.expert5 | 0.457 | 0.471 | 0.1 | 3 |
| bwd.recompute:block0.moe.dispatch.expert6 | 0.452 | 0.466 | 0.1 | 3 |
| bwd.recompute:block0.moe.dispatch.expert7 | 0.455 | 0.469 | 0.1 | 3 |
| bwd.recompute:block0.moe.shared | 0.302 | 0.306 | 0.1 | 3 |
| bwd:block0.grad | 6.811 | 6.986 | 1.7 | 3 |
| bwd:embed | 0.344 | 0.404 | 0.1 | 2 |
| opt | 135.655 | 140.758 | 33.4 | 1 |
| opt:opt.clip | 3.176 | 4.582 | 0.8 | 2 |
| opt:opt.muon | 129.320 | 133.585 | 31.8 | 2 |
| opt:opt.muon.ns | 122.677 | 125.343 | 30.2 | 3 |
| opt:opt.adamw | 1.261 | 1.820 | 0.3 | 2 |
| opt:opt.moe_bias | 0.701 | 0.801 | 0.2 | 3 |
| opt:opt.zero_grad | 0.598 | 1.157 | 0.1 | 3 |

## Time by part type (sum over layers)

| part type | median ms sum | % of step |
| :--- | ---: | ---: |
| bwd | 187.204 | 46.1 |
| bwd:stack | 138.709 | 34.2 |
| bwd:block* | 138.294 | 34.1 |
| opt | 135.655 | 33.4 |
| opt:opt.muon | 129.320 | 31.8 |
| opt:opt.muon.ns | 122.677 | 30.2 |
| fwd | 84.119 | 20.7 |
| bwd:block*.grad | 61.836 | 15.2 |
| bwd:head+loss | 48.138 | 11.9 |
| bwd.recompute:block* | 46.358 | 11.4 |
| bwd.invert:block* | 43.476 | 10.7 |
| fwd:head+loss | 40.844 | 10.1 |
| fwd:stack | 38.901 | 9.6 |
| fwd:block* | 38.863 | 9.6 |
| bwd.recompute:block*.moe.dispatch | 35.357 | 8.7 |
| fwd:block*.moe.dispatch | 34.491 | 8.5 |
| bwd.invert:block*.moe.dispatch | 33.722 | 8.3 |
| fwd:embed | 4.260 | 1.0 |
| fwd:embed.ke | 4.180 | 1.0 |
| bwd.recompute:block*.moe.dispatch.expert1 | 4.127 | 1.0 |
| bwd.recompute:block*.moe.dispatch.expert0 | 4.124 | 1.0 |
| bwd.recompute:block*.moe.dispatch.expert3 | 4.112 | 1.0 |
| bwd.recompute:block*.moe.dispatch.expert2 | 4.107 | 1.0 |
| bwd.recompute:block*.moe.dispatch.expert7 | 4.106 | 1.0 |
| bwd.recompute:block*.moe.dispatch.expert5 | 4.106 | 1.0 |
| bwd.recompute:block*.moe.dispatch.expert4 | 4.094 | 1.0 |
| bwd.recompute:block*.moe.dispatch.expert6 | 4.094 | 1.0 |
| fwd:block*.moe.dispatch.expert0 | 4.093 | 1.0 |
| fwd:block*.moe.dispatch.expert2 | 4.070 | 1.0 |
| fwd:block*.moe.dispatch.expert1 | 4.046 | 1.0 |
| fwd:block*.moe.dispatch.expert3 | 4.029 | 1.0 |
| bwd.invert:block*.moe.dispatch.expert0 | 4.016 | 1.0 |
| fwd:block*.moe.dispatch.expert4 | 4.012 | 1.0 |
| fwd:block*.moe.dispatch.expert6 | 4.004 | 1.0 |
| fwd:block*.moe.dispatch.expert5 | 3.999 | 1.0 |
| fwd:block*.moe.dispatch.expert7 | 3.990 | 1.0 |
| bwd.invert:block*.moe.dispatch.expert1 | 3.973 | 1.0 |
| bwd.invert:block*.moe.dispatch.expert2 | 3.931 | 1.0 |
| bwd.invert:block*.moe.dispatch.expert3 | 3.910 | 1.0 |
| bwd.invert:block*.moe.dispatch.expert5 | 3.895 | 1.0 |
| bwd.invert:block*.moe.dispatch.expert4 | 3.895 | 1.0 |
| bwd.invert:block*.moe.dispatch.expert6 | 3.884 | 1.0 |
| bwd.invert:block*.moe.dispatch.expert7 | 3.870 | 1.0 |
| opt:opt.clip | 3.176 | 0.8 |
| bwd.recompute:block*.moe.shared | 2.724 | 0.7 |
| bwd.invert:block*.moe.shared | 2.690 | 0.7 |
| fwd:block*.moe.shared | 2.678 | 0.7 |
| fwd:block*.moe.router | 1.818 | 0.4 |
| bwd.recompute:block*.moe.router | 1.581 | 0.4 |
| bwd.invert:block*.moe.router | 1.377 | 0.3 |
| opt:opt.adamw | 1.261 | 0.3 |
| bwd.recompute:block*.attn.qkv | 1.252 | 0.3 |
| bwd.recompute:block*.attn.sdpa | 1.111 | 0.3 |
| bwd.invert:block*.attn.qkv | 1.070 | 0.3 |
| fwd:block*.attn.qkv | 1.062 | 0.3 |
| bwd.invert:block*.attn.sdpa | 0.974 | 0.2 |
| fwd:block*.attn.sdpa | 0.969 | 0.2 |
| bwd.recompute:block*.ln1 | 0.765 | 0.2 |
| opt:opt.moe_bias | 0.701 | 0.2 |
| data | 0.691 | 0.2 |
| bwd.recompute:block*.attn.proj | 0.691 | 0.2 |
| fwd:block*.ln1 | 0.673 | 0.2 |
| opt:opt.zero_grad | 0.598 | 0.1 |
| bwd.invert:block*.attn.proj | 0.589 | 0.1 |
| fwd:block*.attn.proj | 0.575 | 0.1 |
| bwd.recompute:block*.ln2 | 0.564 | 0.1 |
| bwd.invert:block*.ln2 | 0.519 | 0.1 |
| fwd:block*.ln2 | 0.506 | 0.1 |
| bwd.invert:block*.ln1 | 0.506 | 0.1 |
| bwd:embed | 0.344 | 0.1 |

## Five slowest leaf parts

1. `opt:opt.muon.ns` — 122.677 ms (30.2% of step)
2. `bwd:block8.grad` — 6.962 ms (1.7% of step)
3. `bwd:block6.grad` — 6.913 ms (1.7% of step)
4. `bwd:block7.grad` — 6.906 ms (1.7% of step)
5. `bwd:block5.grad` — 6.873 ms (1.7% of step)
