# Bench report — g1_lab1_normal-run2

**GPU:** NVIDIA A100-SXM4-40GB  |  **dtype:** bf16  |  **B x T:** 32 x 512  |  **torch:** 2.15.0+cu132
**commit:** `14854097c57056f326efd0c7a40cc036a73bbc94`  |  **tag:** g1_lab1_normal-run2

## Step (clean)

- median: 400.159 ms
- p10..p90: 395.006 .. 412.674 ms
- tokens/s: 40,944
- MFU: 4.2%  |  HFU: 5.4%

## Diagnostics

### CUDA timing-event allocations

- [OK] clean: events_created_during_steps=0
- [OK] layer: events_created_during_steps=0
- [OK] layer.inner_pass: events_created_during_steps=0

### Benchmark warnings

- [warn] 4 gated part(s) have p10..p90 spread > 10%, so may miss the 5% check: data, bwd:block8, opt:opt.clip, opt:opt.adamw

## Regions

| part | median ms | p90 | % of step | level |
| :--- | ---: | ---: | ---: | ---: |
| data | 0.537 | 0.795 | 0.1 | 1 |
| fwd | 83.190 | 84.799 | 20.8 | 1 |
| fwd:embed | 4.216 | 4.321 | 1.1 | 2 |
| fwd:embed.ke | 4.183 | 4.267 | 1.0 | 3 |
| fwd:stack | 38.062 | 39.554 | 9.5 | 1 |
| fwd:block0 | 4.150 | 4.337 | 1.0 | 2 |
| fwd:block0.ln1 | 0.052 | 0.053 | 0.0 | 3 |
| fwd:block0.attn.qkv | 0.050 | 0.051 | 0.0 | 3 |
| fwd:block0.attn.sdpa | 0.082 | 0.084 | 0.0 | 3 |
| fwd:block0.attn.proj | 0.038 | 0.039 | 0.0 | 3 |
| fwd:block0.ln2 | 0.053 | 0.054 | 0.0 | 3 |
| fwd:block0.moe.router | 0.145 | 0.148 | 0.0 | 3 |
| fwd:block0.moe.dispatch | 3.766 | 3.988 | 0.9 | 3 |
| fwd:block0.moe.dispatch.expert0 | 0.454 | 0.540 | 0.1 | 3 |
| fwd:block0.moe.dispatch.expert1 | 0.455 | 0.497 | 0.1 | 3 |
| fwd:block0.moe.dispatch.expert2 | 0.457 | 0.487 | 0.1 | 3 |
| fwd:block0.moe.dispatch.expert3 | 0.443 | 0.477 | 0.1 | 3 |
| fwd:block0.moe.dispatch.expert4 | 0.449 | 0.475 | 0.1 | 3 |
| fwd:block0.moe.dispatch.expert5 | 0.440 | 0.469 | 0.1 | 3 |
| fwd:block0.moe.dispatch.expert6 | 0.443 | 0.470 | 0.1 | 3 |
| fwd:block0.moe.dispatch.expert7 | 0.440 | 0.471 | 0.1 | 3 |
| fwd:block0.moe.shared | 0.300 | 0.310 | 0.1 | 3 |
| fwd:block1 | 4.271 | 4.445 | 1.1 | 2 |
| fwd:block1.ln1 | 0.078 | 0.080 | 0.0 | 3 |
| fwd:block1.attn.qkv | 0.127 | 0.145 | 0.0 | 3 |
| fwd:block1.attn.sdpa | 0.112 | 0.122 | 0.0 | 3 |
| fwd:block1.attn.proj | 0.068 | 0.081 | 0.0 | 3 |
| fwd:block1.ln2 | 0.055 | 0.061 | 0.0 | 3 |
| fwd:block1.moe.router | 0.219 | 0.243 | 0.1 | 3 |
| fwd:block1.moe.dispatch | 3.841 | 4.016 | 1.0 | 3 |
| fwd:block1.moe.dispatch.expert0 | 0.451 | 0.479 | 0.1 | 3 |
| fwd:block1.moe.dispatch.expert1 | 0.465 | 0.492 | 0.1 | 3 |
| fwd:block1.moe.dispatch.expert2 | 0.446 | 0.470 | 0.1 | 3 |
| fwd:block1.moe.dispatch.expert3 | 0.445 | 0.467 | 0.1 | 3 |
| fwd:block1.moe.dispatch.expert4 | 0.459 | 0.485 | 0.1 | 3 |
| fwd:block1.moe.dispatch.expert5 | 0.443 | 0.463 | 0.1 | 3 |
| fwd:block1.moe.dispatch.expert6 | 0.443 | 0.467 | 0.1 | 3 |
| fwd:block1.moe.dispatch.expert7 | 0.434 | 0.466 | 0.1 | 3 |
| fwd:block1.moe.shared | 0.298 | 0.307 | 0.1 | 3 |
| fwd:block2 | 4.243 | 4.420 | 1.1 | 2 |
| fwd:block2.ln1 | 0.077 | 0.081 | 0.0 | 3 |
| fwd:block2.attn.qkv | 0.126 | 0.142 | 0.0 | 3 |
| fwd:block2.attn.sdpa | 0.111 | 0.115 | 0.0 | 3 |
| fwd:block2.attn.proj | 0.066 | 0.080 | 0.0 | 3 |
| fwd:block2.ln2 | 0.056 | 0.059 | 0.0 | 3 |
| fwd:block2.moe.router | 0.209 | 0.224 | 0.1 | 3 |
| fwd:block2.moe.dispatch | 3.807 | 4.021 | 1.0 | 3 |
| fwd:block2.moe.dispatch.expert0 | 0.457 | 0.485 | 0.1 | 3 |
| fwd:block2.moe.dispatch.expert1 | 0.441 | 0.465 | 0.1 | 3 |
| fwd:block2.moe.dispatch.expert2 | 0.448 | 0.471 | 0.1 | 3 |
| fwd:block2.moe.dispatch.expert3 | 0.455 | 0.475 | 0.1 | 3 |
| fwd:block2.moe.dispatch.expert4 | 0.434 | 0.463 | 0.1 | 3 |
| fwd:block2.moe.dispatch.expert5 | 0.441 | 0.469 | 0.1 | 3 |
| fwd:block2.moe.dispatch.expert6 | 0.440 | 0.464 | 0.1 | 3 |
| fwd:block2.moe.dispatch.expert7 | 0.440 | 0.464 | 0.1 | 3 |
| fwd:block2.moe.shared | 0.297 | 0.305 | 0.1 | 3 |
| fwd:block3 | 4.248 | 4.385 | 1.1 | 2 |
| fwd:block3.ln1 | 0.078 | 0.080 | 0.0 | 3 |
| fwd:block3.attn.qkv | 0.125 | 0.138 | 0.0 | 3 |
| fwd:block3.attn.sdpa | 0.111 | 0.114 | 0.0 | 3 |
| fwd:block3.attn.proj | 0.065 | 0.077 | 0.0 | 3 |
| fwd:block3.ln2 | 0.055 | 0.058 | 0.0 | 3 |
| fwd:block3.moe.router | 0.209 | 0.220 | 0.1 | 3 |
| fwd:block3.moe.dispatch | 3.816 | 3.974 | 1.0 | 3 |
| fwd:block3.moe.dispatch.expert0 | 0.459 | 0.479 | 0.1 | 3 |
| fwd:block3.moe.dispatch.expert1 | 0.442 | 0.467 | 0.1 | 3 |
| fwd:block3.moe.dispatch.expert2 | 0.441 | 0.463 | 0.1 | 3 |
| fwd:block3.moe.dispatch.expert3 | 0.451 | 0.471 | 0.1 | 3 |
| fwd:block3.moe.dispatch.expert4 | 0.446 | 0.463 | 0.1 | 3 |
| fwd:block3.moe.dispatch.expert5 | 0.445 | 0.466 | 0.1 | 3 |
| fwd:block3.moe.dispatch.expert6 | 0.440 | 0.463 | 0.1 | 3 |
| fwd:block3.moe.dispatch.expert7 | 0.434 | 0.455 | 0.1 | 3 |
| fwd:block3.moe.shared | 0.297 | 0.306 | 0.1 | 3 |
| fwd:block4 | 4.258 | 4.402 | 1.1 | 2 |
| fwd:block4.ln1 | 0.077 | 0.079 | 0.0 | 3 |
| fwd:block4.attn.qkv | 0.126 | 0.136 | 0.0 | 3 |
| fwd:block4.attn.sdpa | 0.111 | 0.114 | 0.0 | 3 |
| fwd:block4.attn.proj | 0.065 | 0.075 | 0.0 | 3 |
| fwd:block4.ln2 | 0.055 | 0.057 | 0.0 | 3 |
| fwd:block4.moe.router | 0.207 | 0.223 | 0.1 | 3 |
| fwd:block4.moe.dispatch | 3.804 | 3.969 | 1.0 | 3 |
| fwd:block4.moe.dispatch.expert0 | 0.453 | 0.477 | 0.1 | 3 |
| fwd:block4.moe.dispatch.expert1 | 0.450 | 0.469 | 0.1 | 3 |
| fwd:block4.moe.dispatch.expert2 | 0.442 | 0.464 | 0.1 | 3 |
| fwd:block4.moe.dispatch.expert3 | 0.444 | 0.465 | 0.1 | 3 |
| fwd:block4.moe.dispatch.expert4 | 0.445 | 0.463 | 0.1 | 3 |
| fwd:block4.moe.dispatch.expert5 | 0.437 | 0.462 | 0.1 | 3 |
| fwd:block4.moe.dispatch.expert6 | 0.450 | 0.470 | 0.1 | 3 |
| fwd:block4.moe.dispatch.expert7 | 0.437 | 0.462 | 0.1 | 3 |
| fwd:block4.moe.shared | 0.297 | 0.303 | 0.1 | 3 |
| fwd:block5 | 4.224 | 4.380 | 1.1 | 2 |
| fwd:block5.ln1 | 0.077 | 0.079 | 0.0 | 3 |
| fwd:block5.attn.qkv | 0.125 | 0.136 | 0.0 | 3 |
| fwd:block5.attn.sdpa | 0.111 | 0.113 | 0.0 | 3 |
| fwd:block5.attn.proj | 0.063 | 0.076 | 0.0 | 3 |
| fwd:block5.ln2 | 0.055 | 0.059 | 0.0 | 3 |
| fwd:block5.moe.router | 0.207 | 0.222 | 0.1 | 3 |
| fwd:block5.moe.dispatch | 3.794 | 3.986 | 0.9 | 3 |
| fwd:block5.moe.dispatch.expert0 | 0.453 | 0.472 | 0.1 | 3 |
| fwd:block5.moe.dispatch.expert1 | 0.442 | 0.467 | 0.1 | 3 |
| fwd:block5.moe.dispatch.expert2 | 0.440 | 0.463 | 0.1 | 3 |
| fwd:block5.moe.dispatch.expert3 | 0.446 | 0.464 | 0.1 | 3 |
| fwd:block5.moe.dispatch.expert4 | 0.439 | 0.465 | 0.1 | 3 |
| fwd:block5.moe.dispatch.expert5 | 0.445 | 0.469 | 0.1 | 3 |
| fwd:block5.moe.dispatch.expert6 | 0.441 | 0.461 | 0.1 | 3 |
| fwd:block5.moe.dispatch.expert7 | 0.439 | 0.463 | 0.1 | 3 |
| fwd:block5.moe.shared | 0.297 | 0.303 | 0.1 | 3 |
| fwd:block6 | 4.237 | 4.390 | 1.1 | 2 |
| fwd:block6.ln1 | 0.078 | 0.080 | 0.0 | 3 |
| fwd:block6.attn.qkv | 0.124 | 0.135 | 0.0 | 3 |
| fwd:block6.attn.sdpa | 0.111 | 0.114 | 0.0 | 3 |
| fwd:block6.attn.proj | 0.065 | 0.077 | 0.0 | 3 |
| fwd:block6.ln2 | 0.055 | 0.059 | 0.0 | 3 |
| fwd:block6.moe.router | 0.207 | 0.221 | 0.1 | 3 |
| fwd:block6.moe.dispatch | 3.812 | 3.986 | 1.0 | 3 |
| fwd:block6.moe.dispatch.expert0 | 0.453 | 0.475 | 0.1 | 3 |
| fwd:block6.moe.dispatch.expert1 | 0.449 | 0.464 | 0.1 | 3 |
| fwd:block6.moe.dispatch.expert2 | 0.449 | 0.467 | 0.1 | 3 |
| fwd:block6.moe.dispatch.expert3 | 0.443 | 0.468 | 0.1 | 3 |
| fwd:block6.moe.dispatch.expert4 | 0.442 | 0.464 | 0.1 | 3 |
| fwd:block6.moe.dispatch.expert5 | 0.445 | 0.471 | 0.1 | 3 |
| fwd:block6.moe.dispatch.expert6 | 0.443 | 0.460 | 0.1 | 3 |
| fwd:block6.moe.dispatch.expert7 | 0.443 | 0.465 | 0.1 | 3 |
| fwd:block6.moe.shared | 0.297 | 0.305 | 0.1 | 3 |
| fwd:block7 | 4.222 | 4.379 | 1.1 | 2 |
| fwd:block7.ln1 | 0.077 | 0.080 | 0.0 | 3 |
| fwd:block7.attn.qkv | 0.124 | 0.137 | 0.0 | 3 |
| fwd:block7.attn.sdpa | 0.111 | 0.114 | 0.0 | 3 |
| fwd:block7.attn.proj | 0.063 | 0.075 | 0.0 | 3 |
| fwd:block7.ln2 | 0.055 | 0.057 | 0.0 | 3 |
| fwd:block7.moe.router | 0.205 | 0.220 | 0.1 | 3 |
| fwd:block7.moe.dispatch | 3.794 | 3.958 | 0.9 | 3 |
| fwd:block7.moe.dispatch.expert0 | 0.451 | 0.477 | 0.1 | 3 |
| fwd:block7.moe.dispatch.expert1 | 0.436 | 0.460 | 0.1 | 3 |
| fwd:block7.moe.dispatch.expert2 | 0.445 | 0.467 | 0.1 | 3 |
| fwd:block7.moe.dispatch.expert3 | 0.446 | 0.465 | 0.1 | 3 |
| fwd:block7.moe.dispatch.expert4 | 0.440 | 0.463 | 0.1 | 3 |
| fwd:block7.moe.dispatch.expert5 | 0.439 | 0.460 | 0.1 | 3 |
| fwd:block7.moe.dispatch.expert6 | 0.444 | 0.461 | 0.1 | 3 |
| fwd:block7.moe.dispatch.expert7 | 0.437 | 0.458 | 0.1 | 3 |
| fwd:block7.moe.shared | 0.298 | 0.303 | 0.1 | 3 |
| fwd:block8 | 4.227 | 4.394 | 1.1 | 2 |
| fwd:block8.ln1 | 0.077 | 0.080 | 0.0 | 3 |
| fwd:block8.attn.qkv | 0.124 | 0.136 | 0.0 | 3 |
| fwd:block8.attn.sdpa | 0.111 | 0.113 | 0.0 | 3 |
| fwd:block8.attn.proj | 0.064 | 0.075 | 0.0 | 3 |
| fwd:block8.ln2 | 0.055 | 0.058 | 0.0 | 3 |
| fwd:block8.moe.router | 0.208 | 0.220 | 0.1 | 3 |
| fwd:block8.moe.dispatch | 3.804 | 3.999 | 1.0 | 3 |
| fwd:block8.moe.dispatch.expert0 | 0.449 | 0.471 | 0.1 | 3 |
| fwd:block8.moe.dispatch.expert1 | 0.446 | 0.472 | 0.1 | 3 |
| fwd:block8.moe.dispatch.expert2 | 0.443 | 0.467 | 0.1 | 3 |
| fwd:block8.moe.dispatch.expert3 | 0.442 | 0.460 | 0.1 | 3 |
| fwd:block8.moe.dispatch.expert4 | 0.442 | 0.470 | 0.1 | 3 |
| fwd:block8.moe.dispatch.expert5 | 0.440 | 0.459 | 0.1 | 3 |
| fwd:block8.moe.dispatch.expert6 | 0.444 | 0.461 | 0.1 | 3 |
| fwd:block8.moe.dispatch.expert7 | 0.444 | 0.470 | 0.1 | 3 |
| fwd:block8.moe.shared | 0.298 | 0.308 | 0.1 | 3 |
| fwd:head+loss | 40.842 | 40.855 | 10.2 | 2 |
| bwd | 184.884 | 191.177 | 46.2 | 1 |
| bwd:head+loss | 48.137 | 48.158 | 12.0 | 2 |
| bwd:stack | 136.389 | 142.628 | 34.1 | 1 |
| bwd:block8 | 15.195 | 16.606 | 3.8 | 2 |
| bwd.invert:block8 | 4.481 | 5.446 | 1.1 | 3 |
| bwd.invert:block8.ln1 | 0.053 | 0.054 | 0.0 | 3 |
| bwd.invert:block8.attn.qkv | 0.050 | 0.052 | 0.0 | 3 |
| bwd.invert:block8.attn.sdpa | 0.082 | 0.084 | 0.0 | 3 |
| bwd.invert:block8.attn.proj | 0.038 | 0.038 | 0.0 | 3 |
| bwd.invert:block8.ln2 | 0.053 | 0.054 | 0.0 | 3 |
| bwd.invert:block8.moe.router | 0.067 | 0.068 | 0.0 | 3 |
| bwd.invert:block8.moe.dispatch | 3.660 | 4.504 | 0.9 | 3 |
| bwd.invert:block8.moe.dispatch.expert0 | 0.442 | 0.992 | 0.1 | 3 |
| bwd.invert:block8.moe.dispatch.expert1 | 0.444 | 0.532 | 0.1 | 3 |
| bwd.invert:block8.moe.dispatch.expert2 | 0.435 | 0.471 | 0.1 | 3 |
| bwd.invert:block8.moe.dispatch.expert3 | 0.433 | 0.462 | 0.1 | 3 |
| bwd.invert:block8.moe.dispatch.expert4 | 0.430 | 0.458 | 0.1 | 3 |
| bwd.invert:block8.moe.dispatch.expert5 | 0.431 | 0.453 | 0.1 | 3 |
| bwd.invert:block8.moe.dispatch.expert6 | 0.428 | 0.459 | 0.1 | 3 |
| bwd.invert:block8.moe.dispatch.expert7 | 0.432 | 0.467 | 0.1 | 3 |
| bwd.invert:block8.moe.shared | 0.300 | 0.311 | 0.1 | 3 |
| bwd.recompute:block8 | 5.145 | 5.771 | 1.3 | 3 |
| bwd.recompute:block8.ln1 | 0.085 | 0.120 | 0.0 | 3 |
| bwd.recompute:block8.attn.qkv | 0.146 | 0.190 | 0.0 | 3 |
| bwd.recompute:block8.attn.sdpa | 0.130 | 0.193 | 0.0 | 3 |
| bwd.recompute:block8.attn.proj | 0.081 | 0.101 | 0.0 | 3 |
| bwd.recompute:block8.ln2 | 0.063 | 0.072 | 0.0 | 3 |
| bwd.recompute:block8.moe.router | 0.183 | 0.265 | 0.0 | 3 |
| bwd.recompute:block8.moe.dispatch | 3.910 | 4.213 | 1.0 | 3 |
| bwd.recompute:block8.moe.dispatch.expert0 | 0.467 | 0.518 | 0.1 | 3 |
| bwd.recompute:block8.moe.dispatch.expert1 | 0.462 | 0.497 | 0.1 | 3 |
| bwd.recompute:block8.moe.dispatch.expert2 | 0.457 | 0.490 | 0.1 | 3 |
| bwd.recompute:block8.moe.dispatch.expert3 | 0.454 | 0.481 | 0.1 | 3 |
| bwd.recompute:block8.moe.dispatch.expert4 | 0.453 | 0.479 | 0.1 | 3 |
| bwd.recompute:block8.moe.dispatch.expert5 | 0.451 | 0.476 | 0.1 | 3 |
| bwd.recompute:block8.moe.dispatch.expert6 | 0.451 | 0.477 | 0.1 | 3 |
| bwd.recompute:block8.moe.dispatch.expert7 | 0.455 | 0.484 | 0.1 | 3 |
| bwd.recompute:block8.moe.shared | 0.303 | 0.313 | 0.1 | 3 |
| bwd:block8.grad | 7.029 | 7.484 | 1.8 | 3 |
| bwd:block7 | 15.208 | 16.011 | 3.8 | 2 |
| bwd.invert:block7 | 4.876 | 5.278 | 1.2 | 3 |
| bwd.invert:block7.ln1 | 0.078 | 0.087 | 0.0 | 3 |
| bwd.invert:block7.attn.qkv | 0.141 | 0.165 | 0.0 | 3 |
| bwd.invert:block7.attn.sdpa | 0.112 | 0.124 | 0.0 | 3 |
| bwd.invert:block7.attn.proj | 0.069 | 0.081 | 0.0 | 3 |
| bwd.invert:block7.ln2 | 0.057 | 0.063 | 0.0 | 3 |
| bwd.invert:block7.moe.router | 0.163 | 0.197 | 0.0 | 3 |
| bwd.invert:block7.moe.dispatch | 3.716 | 3.900 | 0.9 | 3 |
| bwd.invert:block7.moe.dispatch.expert0 | 0.441 | 0.467 | 0.1 | 3 |
| bwd.invert:block7.moe.dispatch.expert1 | 0.436 | 0.456 | 0.1 | 3 |
| bwd.invert:block7.moe.dispatch.expert2 | 0.431 | 0.450 | 0.1 | 3 |
| bwd.invert:block7.moe.dispatch.expert3 | 0.431 | 0.449 | 0.1 | 3 |
| bwd.invert:block7.moe.dispatch.expert4 | 0.425 | 0.443 | 0.1 | 3 |
| bwd.invert:block7.moe.dispatch.expert5 | 0.428 | 0.446 | 0.1 | 3 |
| bwd.invert:block7.moe.dispatch.expert6 | 0.425 | 0.448 | 0.1 | 3 |
| bwd.invert:block7.moe.dispatch.expert7 | 0.425 | 0.447 | 0.1 | 3 |
| bwd.invert:block7.moe.shared | 0.300 | 0.311 | 0.1 | 3 |
| bwd.recompute:block7 | 5.093 | 5.420 | 1.3 | 3 |
| bwd.recompute:block7.ln1 | 0.084 | 0.091 | 0.0 | 3 |
| bwd.recompute:block7.attn.qkv | 0.141 | 0.155 | 0.0 | 3 |
| bwd.recompute:block7.attn.sdpa | 0.120 | 0.128 | 0.0 | 3 |
| bwd.recompute:block7.attn.proj | 0.076 | 0.090 | 0.0 | 3 |
| bwd.recompute:block7.ln2 | 0.062 | 0.069 | 0.0 | 3 |
| bwd.recompute:block7.moe.router | 0.176 | 0.196 | 0.0 | 3 |
| bwd.recompute:block7.moe.dispatch | 3.877 | 4.057 | 1.0 | 3 |
| bwd.recompute:block7.moe.dispatch.expert0 | 0.456 | 0.477 | 0.1 | 3 |
| bwd.recompute:block7.moe.dispatch.expert1 | 0.456 | 0.472 | 0.1 | 3 |
| bwd.recompute:block7.moe.dispatch.expert2 | 0.450 | 0.469 | 0.1 | 3 |
| bwd.recompute:block7.moe.dispatch.expert3 | 0.453 | 0.475 | 0.1 | 3 |
| bwd.recompute:block7.moe.dispatch.expert4 | 0.449 | 0.466 | 0.1 | 3 |
| bwd.recompute:block7.moe.dispatch.expert5 | 0.452 | 0.466 | 0.1 | 3 |
| bwd.recompute:block7.moe.dispatch.expert6 | 0.447 | 0.470 | 0.1 | 3 |
| bwd.recompute:block7.moe.dispatch.expert7 | 0.450 | 0.465 | 0.1 | 3 |
| bwd.recompute:block7.moe.shared | 0.302 | 0.312 | 0.1 | 3 |
| bwd:block7.grad | 6.894 | 7.212 | 1.7 | 3 |
| bwd:block6 | 15.184 | 15.702 | 3.8 | 2 |
| bwd.invert:block6 | 4.817 | 5.083 | 1.2 | 3 |
| bwd.invert:block6.ln1 | 0.054 | 0.084 | 0.0 | 3 |
| bwd.invert:block6.attn.qkv | 0.124 | 0.145 | 0.0 | 3 |
| bwd.invert:block6.attn.sdpa | 0.112 | 0.118 | 0.0 | 3 |
| bwd.invert:block6.attn.proj | 0.068 | 0.079 | 0.0 | 3 |
| bwd.invert:block6.ln2 | 0.057 | 0.059 | 0.0 | 3 |
| bwd.invert:block6.moe.router | 0.163 | 0.176 | 0.0 | 3 |
| bwd.invert:block6.moe.dispatch | 3.710 | 3.847 | 0.9 | 3 |
| bwd.invert:block6.moe.dispatch.expert0 | 0.449 | 0.470 | 0.1 | 3 |
| bwd.invert:block6.moe.dispatch.expert1 | 0.436 | 0.452 | 0.1 | 3 |
| bwd.invert:block6.moe.dispatch.expert2 | 0.429 | 0.448 | 0.1 | 3 |
| bwd.invert:block6.moe.dispatch.expert3 | 0.428 | 0.440 | 0.1 | 3 |
| bwd.invert:block6.moe.dispatch.expert4 | 0.425 | 0.440 | 0.1 | 3 |
| bwd.invert:block6.moe.dispatch.expert5 | 0.428 | 0.448 | 0.1 | 3 |
| bwd.invert:block6.moe.dispatch.expert6 | 0.424 | 0.438 | 0.1 | 3 |
| bwd.invert:block6.moe.dispatch.expert7 | 0.422 | 0.436 | 0.1 | 3 |
| bwd.invert:block6.moe.shared | 0.298 | 0.306 | 0.1 | 3 |
| bwd.recompute:block6 | 5.067 | 5.235 | 1.3 | 3 |
| bwd.recompute:block6.ln1 | 0.084 | 0.087 | 0.0 | 3 |
| bwd.recompute:block6.attn.qkv | 0.136 | 0.148 | 0.0 | 3 |
| bwd.recompute:block6.attn.sdpa | 0.124 | 0.131 | 0.0 | 3 |
| bwd.recompute:block6.attn.proj | 0.074 | 0.085 | 0.0 | 3 |
| bwd.recompute:block6.ln2 | 0.062 | 0.065 | 0.0 | 3 |
| bwd.recompute:block6.moe.router | 0.172 | 0.186 | 0.0 | 3 |
| bwd.recompute:block6.moe.dispatch | 3.858 | 3.983 | 1.0 | 3 |
| bwd.recompute:block6.moe.dispatch.expert0 | 0.450 | 0.470 | 0.1 | 3 |
| bwd.recompute:block6.moe.dispatch.expert1 | 0.452 | 0.463 | 0.1 | 3 |
| bwd.recompute:block6.moe.dispatch.expert2 | 0.448 | 0.466 | 0.1 | 3 |
| bwd.recompute:block6.moe.dispatch.expert3 | 0.445 | 0.462 | 0.1 | 3 |
| bwd.recompute:block6.moe.dispatch.expert4 | 0.448 | 0.467 | 0.1 | 3 |
| bwd.recompute:block6.moe.dispatch.expert5 | 0.449 | 0.463 | 0.1 | 3 |
| bwd.recompute:block6.moe.dispatch.expert6 | 0.451 | 0.468 | 0.1 | 3 |
| bwd.recompute:block6.moe.dispatch.expert7 | 0.450 | 0.462 | 0.1 | 3 |
| bwd.recompute:block6.moe.shared | 0.301 | 0.308 | 0.1 | 3 |
| bwd:block6.grad | 6.919 | 7.145 | 1.7 | 3 |
| bwd:block5 | 15.144 | 15.711 | 3.8 | 2 |
| bwd.invert:block5 | 4.808 | 5.066 | 1.2 | 3 |
| bwd.invert:block5.ln1 | 0.054 | 0.083 | 0.0 | 3 |
| bwd.invert:block5.attn.qkv | 0.117 | 0.140 | 0.0 | 3 |
| bwd.invert:block5.attn.sdpa | 0.112 | 0.115 | 0.0 | 3 |
| bwd.invert:block5.attn.proj | 0.067 | 0.080 | 0.0 | 3 |
| bwd.invert:block5.ln2 | 0.057 | 0.060 | 0.0 | 3 |
| bwd.invert:block5.moe.router | 0.160 | 0.181 | 0.0 | 3 |
| bwd.invert:block5.moe.dispatch | 3.707 | 3.831 | 0.9 | 3 |
| bwd.invert:block5.moe.dispatch.expert0 | 0.444 | 0.465 | 0.1 | 3 |
| bwd.invert:block5.moe.dispatch.expert1 | 0.433 | 0.452 | 0.1 | 3 |
| bwd.invert:block5.moe.dispatch.expert2 | 0.429 | 0.444 | 0.1 | 3 |
| bwd.invert:block5.moe.dispatch.expert3 | 0.431 | 0.448 | 0.1 | 3 |
| bwd.invert:block5.moe.dispatch.expert4 | 0.428 | 0.440 | 0.1 | 3 |
| bwd.invert:block5.moe.dispatch.expert5 | 0.425 | 0.442 | 0.1 | 3 |
| bwd.invert:block5.moe.dispatch.expert6 | 0.424 | 0.440 | 0.1 | 3 |
| bwd.invert:block5.moe.dispatch.expert7 | 0.423 | 0.440 | 0.1 | 3 |
| bwd.invert:block5.moe.shared | 0.298 | 0.307 | 0.1 | 3 |
| bwd.recompute:block5 | 5.079 | 5.271 | 1.3 | 3 |
| bwd.recompute:block5.ln1 | 0.084 | 0.086 | 0.0 | 3 |
| bwd.recompute:block5.attn.qkv | 0.138 | 0.151 | 0.0 | 3 |
| bwd.recompute:block5.attn.sdpa | 0.119 | 0.123 | 0.0 | 3 |
| bwd.recompute:block5.attn.proj | 0.074 | 0.086 | 0.0 | 3 |
| bwd.recompute:block5.ln2 | 0.061 | 0.067 | 0.0 | 3 |
| bwd.recompute:block5.moe.router | 0.172 | 0.186 | 0.0 | 3 |
| bwd.recompute:block5.moe.dispatch | 3.880 | 4.010 | 1.0 | 3 |
| bwd.recompute:block5.moe.dispatch.expert0 | 0.454 | 0.467 | 0.1 | 3 |
| bwd.recompute:block5.moe.dispatch.expert1 | 0.452 | 0.470 | 0.1 | 3 |
| bwd.recompute:block5.moe.dispatch.expert2 | 0.450 | 0.462 | 0.1 | 3 |
| bwd.recompute:block5.moe.dispatch.expert3 | 0.452 | 0.471 | 0.1 | 3 |
| bwd.recompute:block5.moe.dispatch.expert4 | 0.452 | 0.470 | 0.1 | 3 |
| bwd.recompute:block5.moe.dispatch.expert5 | 0.451 | 0.474 | 0.1 | 3 |
| bwd.recompute:block5.moe.dispatch.expert6 | 0.455 | 0.472 | 0.1 | 3 |
| bwd.recompute:block5.moe.dispatch.expert7 | 0.452 | 0.470 | 0.1 | 3 |
| bwd.recompute:block5.moe.shared | 0.302 | 0.312 | 0.1 | 3 |
| bwd:block5.grad | 6.867 | 7.148 | 1.7 | 3 |
| bwd:block4 | 15.131 | 15.672 | 3.8 | 2 |
| bwd.invert:block4 | 4.784 | 5.013 | 1.2 | 3 |
| bwd.invert:block4.ln1 | 0.054 | 0.085 | 0.0 | 3 |
| bwd.invert:block4.attn.qkv | 0.119 | 0.145 | 0.0 | 3 |
| bwd.invert:block4.attn.sdpa | 0.112 | 0.119 | 0.0 | 3 |
| bwd.invert:block4.attn.proj | 0.066 | 0.078 | 0.0 | 3 |
| bwd.invert:block4.ln2 | 0.057 | 0.062 | 0.0 | 3 |
| bwd.invert:block4.moe.router | 0.161 | 0.183 | 0.0 | 3 |
| bwd.invert:block4.moe.dispatch | 3.694 | 3.828 | 0.9 | 3 |
| bwd.invert:block4.moe.dispatch.expert0 | 0.443 | 0.465 | 0.1 | 3 |
| bwd.invert:block4.moe.dispatch.expert1 | 0.431 | 0.445 | 0.1 | 3 |
| bwd.invert:block4.moe.dispatch.expert2 | 0.429 | 0.450 | 0.1 | 3 |
| bwd.invert:block4.moe.dispatch.expert3 | 0.424 | 0.440 | 0.1 | 3 |
| bwd.invert:block4.moe.dispatch.expert4 | 0.425 | 0.444 | 0.1 | 3 |
| bwd.invert:block4.moe.dispatch.expert5 | 0.423 | 0.437 | 0.1 | 3 |
| bwd.invert:block4.moe.dispatch.expert6 | 0.427 | 0.455 | 0.1 | 3 |
| bwd.invert:block4.moe.dispatch.expert7 | 0.420 | 0.435 | 0.1 | 3 |
| bwd.invert:block4.moe.shared | 0.299 | 0.305 | 0.1 | 3 |
| bwd.recompute:block4 | 5.074 | 5.219 | 1.3 | 3 |
| bwd.recompute:block4.ln1 | 0.083 | 0.087 | 0.0 | 3 |
| bwd.recompute:block4.attn.qkv | 0.136 | 0.149 | 0.0 | 3 |
| bwd.recompute:block4.attn.sdpa | 0.122 | 0.126 | 0.0 | 3 |
| bwd.recompute:block4.attn.proj | 0.073 | 0.085 | 0.0 | 3 |
| bwd.recompute:block4.ln2 | 0.061 | 0.066 | 0.0 | 3 |
| bwd.recompute:block4.moe.router | 0.172 | 0.184 | 0.0 | 3 |
| bwd.recompute:block4.moe.dispatch | 3.877 | 3.996 | 1.0 | 3 |
| bwd.recompute:block4.moe.dispatch.expert0 | 0.452 | 0.465 | 0.1 | 3 |
| bwd.recompute:block4.moe.dispatch.expert1 | 0.451 | 0.468 | 0.1 | 3 |
| bwd.recompute:block4.moe.dispatch.expert2 | 0.453 | 0.468 | 0.1 | 3 |
| bwd.recompute:block4.moe.dispatch.expert3 | 0.451 | 0.466 | 0.1 | 3 |
| bwd.recompute:block4.moe.dispatch.expert4 | 0.452 | 0.466 | 0.1 | 3 |
| bwd.recompute:block4.moe.dispatch.expert5 | 0.448 | 0.463 | 0.1 | 3 |
| bwd.recompute:block4.moe.dispatch.expert6 | 0.454 | 0.475 | 0.1 | 3 |
| bwd.recompute:block4.moe.dispatch.expert7 | 0.449 | 0.466 | 0.1 | 3 |
| bwd.recompute:block4.moe.shared | 0.302 | 0.308 | 0.1 | 3 |
| bwd:block4.grad | 6.867 | 7.102 | 1.7 | 3 |
| bwd:block3 | 15.107 | 15.670 | 3.8 | 2 |
| bwd.invert:block3 | 4.794 | 5.018 | 1.2 | 3 |
| bwd.invert:block3.ln1 | 0.054 | 0.082 | 0.0 | 3 |
| bwd.invert:block3.attn.qkv | 0.120 | 0.149 | 0.0 | 3 |
| bwd.invert:block3.attn.sdpa | 0.112 | 0.123 | 0.0 | 3 |
| bwd.invert:block3.attn.proj | 0.068 | 0.081 | 0.0 | 3 |
| bwd.invert:block3.ln2 | 0.056 | 0.067 | 0.0 | 3 |
| bwd.invert:block3.moe.router | 0.160 | 0.181 | 0.0 | 3 |
| bwd.invert:block3.moe.dispatch | 3.704 | 3.817 | 0.9 | 3 |
| bwd.invert:block3.moe.dispatch.expert0 | 0.444 | 0.461 | 0.1 | 3 |
| bwd.invert:block3.moe.dispatch.expert1 | 0.432 | 0.445 | 0.1 | 3 |
| bwd.invert:block3.moe.dispatch.expert2 | 0.429 | 0.446 | 0.1 | 3 |
| bwd.invert:block3.moe.dispatch.expert3 | 0.430 | 0.445 | 0.1 | 3 |
| bwd.invert:block3.moe.dispatch.expert4 | 0.428 | 0.440 | 0.1 | 3 |
| bwd.invert:block3.moe.dispatch.expert5 | 0.424 | 0.438 | 0.1 | 3 |
| bwd.invert:block3.moe.dispatch.expert6 | 0.425 | 0.440 | 0.1 | 3 |
| bwd.invert:block3.moe.dispatch.expert7 | 0.424 | 0.438 | 0.1 | 3 |
| bwd.invert:block3.moe.shared | 0.299 | 0.306 | 0.1 | 3 |
| bwd.recompute:block3 | 5.067 | 5.225 | 1.3 | 3 |
| bwd.recompute:block3.ln1 | 0.084 | 0.086 | 0.0 | 3 |
| bwd.recompute:block3.attn.qkv | 0.137 | 0.151 | 0.0 | 3 |
| bwd.recompute:block3.attn.sdpa | 0.122 | 0.126 | 0.0 | 3 |
| bwd.recompute:block3.attn.proj | 0.074 | 0.087 | 0.0 | 3 |
| bwd.recompute:block3.ln2 | 0.061 | 0.065 | 0.0 | 3 |
| bwd.recompute:block3.moe.router | 0.171 | 0.182 | 0.0 | 3 |
| bwd.recompute:block3.moe.dispatch | 3.871 | 3.977 | 1.0 | 3 |
| bwd.recompute:block3.moe.dispatch.expert0 | 0.455 | 0.470 | 0.1 | 3 |
| bwd.recompute:block3.moe.dispatch.expert1 | 0.454 | 0.466 | 0.1 | 3 |
| bwd.recompute:block3.moe.dispatch.expert2 | 0.452 | 0.470 | 0.1 | 3 |
| bwd.recompute:block3.moe.dispatch.expert3 | 0.449 | 0.465 | 0.1 | 3 |
| bwd.recompute:block3.moe.dispatch.expert4 | 0.452 | 0.471 | 0.1 | 3 |
| bwd.recompute:block3.moe.dispatch.expert5 | 0.446 | 0.463 | 0.1 | 3 |
| bwd.recompute:block3.moe.dispatch.expert6 | 0.450 | 0.472 | 0.1 | 3 |
| bwd.recompute:block3.moe.dispatch.expert7 | 0.447 | 0.465 | 0.1 | 3 |
| bwd.recompute:block3.moe.shared | 0.302 | 0.312 | 0.1 | 3 |
| bwd:block3.grad | 6.838 | 7.095 | 1.7 | 3 |
| bwd:block2 | 15.108 | 15.646 | 3.8 | 2 |
| bwd.invert:block2 | 4.794 | 5.054 | 1.2 | 3 |
| bwd.invert:block2.ln1 | 0.054 | 0.084 | 0.0 | 3 |
| bwd.invert:block2.attn.qkv | 0.124 | 0.140 | 0.0 | 3 |
| bwd.invert:block2.attn.sdpa | 0.111 | 0.123 | 0.0 | 3 |
| bwd.invert:block2.attn.proj | 0.067 | 0.079 | 0.0 | 3 |
| bwd.invert:block2.ln2 | 0.056 | 0.058 | 0.0 | 3 |
| bwd.invert:block2.moe.router | 0.159 | 0.180 | 0.0 | 3 |
| bwd.invert:block2.moe.dispatch | 3.696 | 3.829 | 0.9 | 3 |
| bwd.invert:block2.moe.dispatch.expert0 | 0.441 | 0.458 | 0.1 | 3 |
| bwd.invert:block2.moe.dispatch.expert1 | 0.433 | 0.456 | 0.1 | 3 |
| bwd.invert:block2.moe.dispatch.expert2 | 0.430 | 0.442 | 0.1 | 3 |
| bwd.invert:block2.moe.dispatch.expert3 | 0.428 | 0.448 | 0.1 | 3 |
| bwd.invert:block2.moe.dispatch.expert4 | 0.426 | 0.445 | 0.1 | 3 |
| bwd.invert:block2.moe.dispatch.expert5 | 0.427 | 0.443 | 0.1 | 3 |
| bwd.invert:block2.moe.dispatch.expert6 | 0.424 | 0.446 | 0.1 | 3 |
| bwd.invert:block2.moe.dispatch.expert7 | 0.425 | 0.440 | 0.1 | 3 |
| bwd.invert:block2.moe.shared | 0.299 | 0.309 | 0.1 | 3 |
| bwd.recompute:block2 | 5.069 | 5.240 | 1.3 | 3 |
| bwd.recompute:block2.ln1 | 0.083 | 0.087 | 0.0 | 3 |
| bwd.recompute:block2.attn.qkv | 0.135 | 0.147 | 0.0 | 3 |
| bwd.recompute:block2.attn.sdpa | 0.125 | 0.133 | 0.0 | 3 |
| bwd.recompute:block2.attn.proj | 0.074 | 0.086 | 0.0 | 3 |
| bwd.recompute:block2.ln2 | 0.061 | 0.071 | 0.0 | 3 |
| bwd.recompute:block2.moe.router | 0.171 | 0.185 | 0.0 | 3 |
| bwd.recompute:block2.moe.dispatch | 3.873 | 4.000 | 1.0 | 3 |
| bwd.recompute:block2.moe.dispatch.expert0 | 0.453 | 0.466 | 0.1 | 3 |
| bwd.recompute:block2.moe.dispatch.expert1 | 0.451 | 0.470 | 0.1 | 3 |
| bwd.recompute:block2.moe.dispatch.expert2 | 0.449 | 0.463 | 0.1 | 3 |
| bwd.recompute:block2.moe.dispatch.expert3 | 0.455 | 0.487 | 0.1 | 3 |
| bwd.recompute:block2.moe.dispatch.expert4 | 0.449 | 0.465 | 0.1 | 3 |
| bwd.recompute:block2.moe.dispatch.expert5 | 0.453 | 0.484 | 0.1 | 3 |
| bwd.recompute:block2.moe.dispatch.expert6 | 0.445 | 0.463 | 0.1 | 3 |
| bwd.recompute:block2.moe.dispatch.expert7 | 0.451 | 0.468 | 0.1 | 3 |
| bwd.recompute:block2.moe.shared | 0.302 | 0.310 | 0.1 | 3 |
| bwd:block2.grad | 6.812 | 7.079 | 1.7 | 3 |
| bwd:block1 | 15.079 | 15.668 | 3.8 | 2 |
| bwd.invert:block1 | 4.800 | 5.047 | 1.2 | 3 |
| bwd.invert:block1.ln1 | 0.054 | 0.083 | 0.0 | 3 |
| bwd.invert:block1.attn.qkv | 0.124 | 0.145 | 0.0 | 3 |
| bwd.invert:block1.attn.sdpa | 0.111 | 0.120 | 0.0 | 3 |
| bwd.invert:block1.attn.proj | 0.067 | 0.081 | 0.0 | 3 |
| bwd.invert:block1.ln2 | 0.056 | 0.059 | 0.0 | 3 |
| bwd.invert:block1.moe.router | 0.160 | 0.179 | 0.0 | 3 |
| bwd.invert:block1.moe.dispatch | 3.699 | 3.843 | 0.9 | 3 |
| bwd.invert:block1.moe.dispatch.expert0 | 0.439 | 0.456 | 0.1 | 3 |
| bwd.invert:block1.moe.dispatch.expert1 | 0.438 | 0.460 | 0.1 | 3 |
| bwd.invert:block1.moe.dispatch.expert2 | 0.427 | 0.442 | 0.1 | 3 |
| bwd.invert:block1.moe.dispatch.expert3 | 0.428 | 0.449 | 0.1 | 3 |
| bwd.invert:block1.moe.dispatch.expert4 | 0.431 | 0.453 | 0.1 | 3 |
| bwd.invert:block1.moe.dispatch.expert5 | 0.425 | 0.442 | 0.1 | 3 |
| bwd.invert:block1.moe.dispatch.expert6 | 0.424 | 0.440 | 0.1 | 3 |
| bwd.invert:block1.moe.dispatch.expert7 | 0.423 | 0.442 | 0.1 | 3 |
| bwd.invert:block1.moe.shared | 0.299 | 0.308 | 0.1 | 3 |
| bwd.recompute:block1 | 5.080 | 5.294 | 1.3 | 3 |
| bwd.recompute:block1.ln1 | 0.084 | 0.086 | 0.0 | 3 |
| bwd.recompute:block1.attn.qkv | 0.137 | 0.151 | 0.0 | 3 |
| bwd.recompute:block1.attn.sdpa | 0.124 | 0.131 | 0.0 | 3 |
| bwd.recompute:block1.attn.proj | 0.074 | 0.085 | 0.0 | 3 |
| bwd.recompute:block1.ln2 | 0.061 | 0.065 | 0.0 | 3 |
| bwd.recompute:block1.moe.router | 0.171 | 0.187 | 0.0 | 3 |
| bwd.recompute:block1.moe.dispatch | 3.878 | 3.998 | 1.0 | 3 |
| bwd.recompute:block1.moe.dispatch.expert0 | 0.450 | 0.465 | 0.1 | 3 |
| bwd.recompute:block1.moe.dispatch.expert1 | 0.457 | 0.472 | 0.1 | 3 |
| bwd.recompute:block1.moe.dispatch.expert2 | 0.453 | 0.470 | 0.1 | 3 |
| bwd.recompute:block1.moe.dispatch.expert3 | 0.451 | 0.468 | 0.1 | 3 |
| bwd.recompute:block1.moe.dispatch.expert4 | 0.455 | 0.477 | 0.1 | 3 |
| bwd.recompute:block1.moe.dispatch.expert5 | 0.448 | 0.464 | 0.1 | 3 |
| bwd.recompute:block1.moe.dispatch.expert6 | 0.445 | 0.468 | 0.1 | 3 |
| bwd.recompute:block1.moe.dispatch.expert7 | 0.447 | 0.465 | 0.1 | 3 |
| bwd.recompute:block1.moe.shared | 0.302 | 0.308 | 0.1 | 3 |
| bwd:block1.grad | 6.828 | 7.038 | 1.7 | 3 |
| bwd:block0 | 15.093 | 15.590 | 3.8 | 2 |
| bwd.invert:block0 | 4.804 | 5.114 | 1.2 | 3 |
| bwd.invert:block0.ln1 | 0.054 | 0.085 | 0.0 | 3 |
| bwd.invert:block0.attn.qkv | 0.127 | 0.147 | 0.0 | 3 |
| bwd.invert:block0.attn.sdpa | 0.111 | 0.114 | 0.0 | 3 |
| bwd.invert:block0.attn.proj | 0.067 | 0.077 | 0.0 | 3 |
| bwd.invert:block0.ln2 | 0.056 | 0.060 | 0.0 | 3 |
| bwd.invert:block0.moe.router | 0.160 | 0.179 | 0.0 | 3 |
| bwd.invert:block0.moe.dispatch | 3.704 | 3.863 | 0.9 | 3 |
| bwd.invert:block0.moe.dispatch.expert0 | 0.439 | 0.463 | 0.1 | 3 |
| bwd.invert:block0.moe.dispatch.expert1 | 0.433 | 0.454 | 0.1 | 3 |
| bwd.invert:block0.moe.dispatch.expert2 | 0.430 | 0.448 | 0.1 | 3 |
| bwd.invert:block0.moe.dispatch.expert3 | 0.427 | 0.454 | 0.1 | 3 |
| bwd.invert:block0.moe.dispatch.expert4 | 0.427 | 0.448 | 0.1 | 3 |
| bwd.invert:block0.moe.dispatch.expert5 | 0.425 | 0.441 | 0.1 | 3 |
| bwd.invert:block0.moe.dispatch.expert6 | 0.425 | 0.438 | 0.1 | 3 |
| bwd.invert:block0.moe.dispatch.expert7 | 0.424 | 0.440 | 0.1 | 3 |
| bwd.invert:block0.moe.shared | 0.299 | 0.310 | 0.1 | 3 |
| bwd.recompute:block0 | 5.067 | 5.280 | 1.3 | 3 |
| bwd.recompute:block0.ln1 | 0.084 | 0.087 | 0.0 | 3 |
| bwd.recompute:block0.attn.qkv | 0.134 | 0.147 | 0.0 | 3 |
| bwd.recompute:block0.attn.sdpa | 0.126 | 0.135 | 0.0 | 3 |
| bwd.recompute:block0.attn.proj | 0.073 | 0.083 | 0.0 | 3 |
| bwd.recompute:block0.ln2 | 0.061 | 0.069 | 0.0 | 3 |
| bwd.recompute:block0.moe.router | 0.171 | 0.188 | 0.0 | 3 |
| bwd.recompute:block0.moe.dispatch | 3.864 | 4.042 | 1.0 | 3 |
| bwd.recompute:block0.moe.dispatch.expert0 | 0.452 | 0.466 | 0.1 | 3 |
| bwd.recompute:block0.moe.dispatch.expert1 | 0.452 | 0.468 | 0.1 | 3 |
| bwd.recompute:block0.moe.dispatch.expert2 | 0.450 | 0.462 | 0.1 | 3 |
| bwd.recompute:block0.moe.dispatch.expert3 | 0.452 | 0.474 | 0.1 | 3 |
| bwd.recompute:block0.moe.dispatch.expert4 | 0.447 | 0.463 | 0.1 | 3 |
| bwd.recompute:block0.moe.dispatch.expert5 | 0.451 | 0.480 | 0.1 | 3 |
| bwd.recompute:block0.moe.dispatch.expert6 | 0.446 | 0.463 | 0.1 | 3 |
| bwd.recompute:block0.moe.dispatch.expert7 | 0.451 | 0.471 | 0.1 | 3 |
| bwd.recompute:block0.moe.shared | 0.301 | 0.311 | 0.1 | 3 |
| bwd:block0.grad | 6.788 | 7.097 | 1.7 | 3 |
| bwd:embed | 0.344 | 0.351 | 0.1 | 2 |
| opt | 132.400 | 137.159 | 33.1 | 1 |
| opt:opt.clip | 2.916 | 4.434 | 0.7 | 2 |
| opt:opt.muon | 127.041 | 130.696 | 31.7 | 2 |
| opt:opt.muon.ns | 121.087 | 124.156 | 30.3 | 3 |
| opt:opt.adamw | 1.135 | 1.473 | 0.3 | 2 |
| opt:opt.moe_bias | 0.713 | 0.802 | 0.2 | 3 |
| opt:opt.zero_grad | 0.691 | 1.122 | 0.2 | 3 |

## Time by part type (sum over layers)

| part type | median ms sum | % of step |
| :--- | ---: | ---: |
| bwd | 184.884 | 46.2 |
| bwd:stack | 136.389 | 34.1 |
| bwd:block* | 136.249 | 34.0 |
| opt | 132.400 | 33.1 |
| opt:opt.muon | 127.041 | 31.7 |
| opt:opt.muon.ns | 121.087 | 30.3 |
| fwd | 83.190 | 20.8 |
| bwd:block*.grad | 61.841 | 15.5 |
| bwd:head+loss | 48.137 | 12.0 |
| bwd.recompute:block* | 45.740 | 11.4 |
| bwd.invert:block* | 42.957 | 10.7 |
| fwd:head+loss | 40.842 | 10.2 |
| fwd:block* | 38.079 | 9.5 |
| fwd:stack | 38.062 | 9.5 |
| bwd.recompute:block*.moe.dispatch | 34.888 | 8.7 |
| fwd:block*.moe.dispatch | 34.238 | 8.6 |
| bwd.invert:block*.moe.dispatch | 33.290 | 8.3 |
| fwd:embed | 4.216 | 1.1 |
| fwd:embed.ke | 4.183 | 1.0 |
| bwd.recompute:block*.moe.dispatch.expert0 | 4.086 | 1.0 |
| bwd.recompute:block*.moe.dispatch.expert1 | 4.084 | 1.0 |
| fwd:block*.moe.dispatch.expert0 | 4.078 | 1.0 |
| bwd.recompute:block*.moe.dispatch.expert3 | 4.060 | 1.0 |
| bwd.recompute:block*.moe.dispatch.expert2 | 4.059 | 1.0 |
| bwd.recompute:block*.moe.dispatch.expert4 | 4.056 | 1.0 |
| bwd.recompute:block*.moe.dispatch.expert7 | 4.050 | 1.0 |
| bwd.recompute:block*.moe.dispatch.expert5 | 4.047 | 1.0 |
| bwd.recompute:block*.moe.dispatch.expert6 | 4.044 | 1.0 |
| fwd:block*.moe.dispatch.expert1 | 4.026 | 1.0 |
| fwd:block*.moe.dispatch.expert3 | 4.017 | 1.0 |
| fwd:block*.moe.dispatch.expert2 | 4.013 | 1.0 |
| fwd:block*.moe.dispatch.expert4 | 3.998 | 1.0 |
| fwd:block*.moe.dispatch.expert6 | 3.989 | 1.0 |
| bwd.invert:block*.moe.dispatch.expert0 | 3.983 | 1.0 |
| fwd:block*.moe.dispatch.expert5 | 3.978 | 1.0 |
| fwd:block*.moe.dispatch.expert7 | 3.950 | 1.0 |
| bwd.invert:block*.moe.dispatch.expert1 | 3.917 | 1.0 |
| bwd.invert:block*.moe.dispatch.expert2 | 3.869 | 1.0 |
| bwd.invert:block*.moe.dispatch.expert3 | 3.860 | 1.0 |
| bwd.invert:block*.moe.dispatch.expert4 | 3.845 | 1.0 |
| bwd.invert:block*.moe.dispatch.expert5 | 3.837 | 1.0 |
| bwd.invert:block*.moe.dispatch.expert6 | 3.826 | 1.0 |
| bwd.invert:block*.moe.dispatch.expert7 | 3.818 | 1.0 |
| opt:opt.clip | 2.916 | 0.7 |
| bwd.recompute:block*.moe.shared | 2.717 | 0.7 |
| bwd.invert:block*.moe.shared | 2.691 | 0.7 |
| fwd:block*.moe.shared | 2.679 | 0.7 |
| fwd:block*.moe.router | 1.816 | 0.5 |
| bwd.recompute:block*.moe.router | 1.560 | 0.4 |
| bwd.invert:block*.moe.router | 1.351 | 0.3 |
| bwd.recompute:block*.attn.qkv | 1.242 | 0.3 |
| opt:opt.adamw | 1.135 | 0.3 |
| bwd.recompute:block*.attn.sdpa | 1.112 | 0.3 |
| fwd:block*.attn.qkv | 1.051 | 0.3 |
| bwd.invert:block*.attn.qkv | 1.046 | 0.3 |
| bwd.invert:block*.attn.sdpa | 0.972 | 0.2 |
| fwd:block*.attn.sdpa | 0.968 | 0.2 |
| bwd.recompute:block*.ln1 | 0.755 | 0.2 |
| opt:opt.moe_bias | 0.713 | 0.2 |
| opt:opt.zero_grad | 0.691 | 0.2 |
| bwd.recompute:block*.attn.proj | 0.671 | 0.2 |
| fwd:block*.ln1 | 0.670 | 0.2 |
| bwd.invert:block*.attn.proj | 0.573 | 0.1 |
| bwd.recompute:block*.ln2 | 0.557 | 0.1 |
| fwd:block*.attn.proj | 0.556 | 0.1 |
| data | 0.537 | 0.1 |
| bwd.invert:block*.ln1 | 0.511 | 0.1 |
| bwd.invert:block*.ln2 | 0.508 | 0.1 |
| fwd:block*.ln2 | 0.497 | 0.1 |
| bwd:embed | 0.344 | 0.1 |

## Five slowest leaf parts

1. `opt:opt.muon.ns` — 121.087 ms (30.3% of step)
2. `bwd:block8.grad` — 7.029 ms (1.8% of step)
3. `bwd:block6.grad` — 6.919 ms (1.7% of step)
4. `bwd:block7.grad` — 6.894 ms (1.7% of step)
5. `bwd:block4.grad` — 6.867 ms (1.7% of step)
