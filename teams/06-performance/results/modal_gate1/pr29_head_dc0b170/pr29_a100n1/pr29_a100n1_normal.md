# Bench report — pr29_a100n1_normal

**GPU:** NVIDIA A100-SXM4-40GB  |  **dtype:** bf16  |  **B x T:** 16 x 256  |  **torch:** 2.15.0+cu132
**commit:** `dc0b1703d7d0c51b152bd37d81f6fc2b3ddcf64d`  |  **tag:** pr29_a100n1_normal

## Step (clean)

- median: 60.899 ms
- p10..p90: 59.265 .. 62.818 ms
- tokens/s: 67,259
- MFU: 5.3%  |  HFU: 5.9%

## Diagnostics

### CUDA timing-event allocations

- [OK] clean: events_created_during_steps=0
- [OK] layer: events_created_during_steps=0
- [OK] layer.inner_pass: events_created_during_steps=0

### Benchmark warnings

- [warn] recorder overhead 2.3% > 2.0%: layer numbers are flagged
- [warn] 7 gated part(s) have p10..p90 spread > 10%, so may miss the 5% check: data, fwd:embed, fwd:stack, fwd:block0, opt, opt:opt.polar_muon_adamw (+1 more)

## Regions

| part | median ms | p90 | % of step | level |
| :--- | ---: | ---: | ---: | ---: |
| data | 0.346 | 0.455 | 0.6 | 1 |
| fwd | 16.365 | 16.954 | 26.9 | 1 |
| fwd:embed | 0.611 | 0.702 | 1.0 | 2 |
| fwd:embed.ke | 0.614 | 0.690 | 1.0 | 3 |
| fwd:stack | 5.231 | 5.676 | 8.6 | 1 |
| fwd:block0 | 0.850 | 1.112 | 1.4 | 2 |
| fwd:block0.ln1 | 0.065 | 0.087 | 0.1 | 3 |
| fwd:block0.attn.qkv | 0.160 | 0.203 | 0.3 | 3 |
| fwd:block0.attn.sdpa | 0.417 | 0.511 | 0.7 | 3 |
| fwd:block0.attn.proj | 0.111 | 0.150 | 0.2 | 3 |
| fwd:block0.ln2 | 0.051 | 0.063 | 0.1 | 3 |
| fwd:block0.mlp | 0.185 | 0.210 | 0.3 | 3 |
| fwd:block1 | 0.843 | 0.876 | 1.4 | 2 |
| fwd:block1.ln1 | 0.051 | 0.056 | 0.1 | 3 |
| fwd:block1.attn.qkv | 0.135 | 0.146 | 0.2 | 3 |
| fwd:block1.attn.sdpa | 0.389 | 0.407 | 0.6 | 3 |
| fwd:block1.attn.proj | 0.094 | 0.111 | 0.2 | 3 |
| fwd:block1.ln2 | 0.049 | 0.052 | 0.1 | 3 |
| fwd:block1.mlp | 0.179 | 0.193 | 0.3 | 3 |
| fwd:block2 | 0.832 | 0.858 | 1.4 | 2 |
| fwd:block2.ln1 | 0.050 | 0.054 | 0.1 | 3 |
| fwd:block2.attn.qkv | 0.132 | 0.142 | 0.2 | 3 |
| fwd:block2.attn.sdpa | 0.383 | 0.396 | 0.6 | 3 |
| fwd:block2.attn.proj | 0.093 | 0.109 | 0.2 | 3 |
| fwd:block2.ln2 | 0.048 | 0.051 | 0.1 | 3 |
| fwd:block2.mlp | 0.176 | 0.186 | 0.3 | 3 |
| fwd:block3 | 0.828 | 0.855 | 1.4 | 2 |
| fwd:block3.ln1 | 0.049 | 0.052 | 0.1 | 3 |
| fwd:block3.attn.qkv | 0.133 | 0.142 | 0.2 | 3 |
| fwd:block3.attn.sdpa | 0.383 | 0.395 | 0.6 | 3 |
| fwd:block3.attn.proj | 0.090 | 0.103 | 0.1 | 3 |
| fwd:block3.ln2 | 0.049 | 0.051 | 0.1 | 3 |
| fwd:block3.mlp | 0.175 | 0.187 | 0.3 | 3 |
| fwd:block4 | 0.829 | 0.854 | 1.4 | 2 |
| fwd:block4.ln1 | 0.049 | 0.052 | 0.1 | 3 |
| fwd:block4.attn.qkv | 0.132 | 0.140 | 0.2 | 3 |
| fwd:block4.attn.sdpa | 0.381 | 0.392 | 0.6 | 3 |
| fwd:block4.attn.proj | 0.093 | 0.108 | 0.2 | 3 |
| fwd:block4.ln2 | 0.048 | 0.051 | 0.1 | 3 |
| fwd:block4.mlp | 0.176 | 0.186 | 0.3 | 3 |
| fwd:block5 | 0.824 | 0.847 | 1.4 | 2 |
| fwd:block5.ln1 | 0.049 | 0.051 | 0.1 | 3 |
| fwd:block5.attn.qkv | 0.131 | 0.142 | 0.2 | 3 |
| fwd:block5.attn.sdpa | 0.381 | 0.392 | 0.6 | 3 |
| fwd:block5.attn.proj | 0.089 | 0.104 | 0.1 | 3 |
| fwd:block5.ln2 | 0.048 | 0.050 | 0.1 | 3 |
| fwd:block5.mlp | 0.176 | 0.191 | 0.3 | 3 |
| fwd:head+loss | 10.429 | 10.439 | 17.1 | 2 |
| bwd | 23.435 | 23.473 | 38.5 | 1 |
| bwd:head+loss | 12.292 | 12.325 | 20.2 | 2 |
| bwd:stack | 10.804 | 10.829 | 17.7 | 1 |
| bwd:block5 | 1.790 | 1.794 | 2.9 | 2 |
| bwd.invert:block5 | 0.536 | 0.538 | 0.9 | 3 |
| bwd.invert:block5.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block5.attn.qkv | 0.031 | 0.032 | 0.1 | 3 |
| bwd.invert:block5.attn.sdpa | 0.287 | 0.289 | 0.5 | 3 |
| bwd.invert:block5.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block5.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block5.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd.recompute:block5 | 0.536 | 0.539 | 0.9 | 3 |
| bwd.recompute:block5.ln1 | 0.021 | 0.022 | 0.0 | 3 |
| bwd.recompute:block5.attn.qkv | 0.032 | 0.033 | 0.1 | 3 |
| bwd.recompute:block5.attn.sdpa | 0.285 | 0.286 | 0.5 | 3 |
| bwd.recompute:block5.attn.proj | 0.030 | 0.030 | 0.0 | 3 |
| bwd.recompute:block5.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.recompute:block5.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd:block5.grad | 0.821 | 0.825 | 1.3 | 3 |
| bwd:block4 | 1.798 | 1.805 | 3.0 | 2 |
| bwd.invert:block4 | 0.539 | 0.541 | 0.9 | 3 |
| bwd.invert:block4.ln1 | 0.021 | 0.023 | 0.0 | 3 |
| bwd.invert:block4.attn.qkv | 0.032 | 0.033 | 0.1 | 3 |
| bwd.invert:block4.attn.sdpa | 0.287 | 0.288 | 0.5 | 3 |
| bwd.invert:block4.attn.proj | 0.030 | 0.030 | 0.0 | 3 |
| bwd.invert:block4.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block4.mlp | 0.085 | 0.085 | 0.1 | 3 |
| bwd.recompute:block4 | 0.540 | 0.543 | 0.9 | 3 |
| bwd.recompute:block4.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block4.attn.qkv | 0.031 | 0.032 | 0.1 | 3 |
| bwd.recompute:block4.attn.sdpa | 0.288 | 0.290 | 0.5 | 3 |
| bwd.recompute:block4.attn.proj | 0.031 | 0.032 | 0.1 | 3 |
| bwd.recompute:block4.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block4.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block4.grad | 0.822 | 0.825 | 1.4 | 3 |
| bwd:block3 | 1.791 | 1.798 | 2.9 | 2 |
| bwd.invert:block3 | 0.536 | 0.539 | 0.9 | 3 |
| bwd.invert:block3.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block3.attn.qkv | 0.031 | 0.031 | 0.1 | 3 |
| bwd.invert:block3.attn.sdpa | 0.286 | 0.288 | 0.5 | 3 |
| bwd.invert:block3.attn.proj | 0.031 | 0.032 | 0.1 | 3 |
| bwd.invert:block3.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block3.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd.recompute:block3 | 0.538 | 0.542 | 0.9 | 3 |
| bwd.recompute:block3.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block3.attn.qkv | 0.032 | 0.033 | 0.1 | 3 |
| bwd.recompute:block3.attn.sdpa | 0.285 | 0.287 | 0.5 | 3 |
| bwd.recompute:block3.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block3.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.recompute:block3.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block3.grad | 0.821 | 0.824 | 1.3 | 3 |
| bwd:block2 | 1.789 | 1.796 | 2.9 | 2 |
| bwd.invert:block2 | 0.536 | 0.539 | 0.9 | 3 |
| bwd.invert:block2.ln1 | 0.022 | 0.022 | 0.0 | 3 |
| bwd.invert:block2.attn.qkv | 0.032 | 0.033 | 0.1 | 3 |
| bwd.invert:block2.attn.sdpa | 0.285 | 0.287 | 0.5 | 3 |
| bwd.invert:block2.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block2.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block2.mlp | 0.084 | 0.084 | 0.1 | 3 |
| bwd.recompute:block2 | 0.539 | 0.542 | 0.9 | 3 |
| bwd.recompute:block2.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block2.attn.qkv | 0.031 | 0.032 | 0.1 | 3 |
| bwd.recompute:block2.attn.sdpa | 0.286 | 0.289 | 0.5 | 3 |
| bwd.recompute:block2.attn.proj | 0.031 | 0.032 | 0.1 | 3 |
| bwd.recompute:block2.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block2.mlp | 0.086 | 0.087 | 0.1 | 3 |
| bwd:block2.grad | 0.817 | 0.821 | 1.3 | 3 |
| bwd:block1 | 1.798 | 1.804 | 3.0 | 2 |
| bwd.invert:block1 | 0.540 | 0.544 | 0.9 | 3 |
| bwd.invert:block1.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block1.attn.qkv | 0.031 | 0.032 | 0.1 | 3 |
| bwd.invert:block1.attn.sdpa | 0.286 | 0.288 | 0.5 | 3 |
| bwd.invert:block1.attn.proj | 0.031 | 0.032 | 0.1 | 3 |
| bwd.invert:block1.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block1.mlp | 0.086 | 0.087 | 0.1 | 3 |
| bwd.recompute:block1 | 0.540 | 0.543 | 0.9 | 3 |
| bwd.recompute:block1.ln1 | 0.022 | 0.022 | 0.0 | 3 |
| bwd.recompute:block1.attn.qkv | 0.032 | 0.033 | 0.1 | 3 |
| bwd.recompute:block1.attn.sdpa | 0.287 | 0.288 | 0.5 | 3 |
| bwd.recompute:block1.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block1.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block1.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block1.grad | 0.824 | 0.828 | 1.4 | 3 |
| bwd:block0 | 1.794 | 1.798 | 2.9 | 2 |
| bwd.invert:block0 | 0.537 | 0.540 | 0.9 | 3 |
| bwd.invert:block0.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block0.attn.qkv | 0.032 | 0.033 | 0.1 | 3 |
| bwd.invert:block0.attn.sdpa | 0.285 | 0.287 | 0.5 | 3 |
| bwd.invert:block0.attn.proj | 0.030 | 0.030 | 0.0 | 3 |
| bwd.invert:block0.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.invert:block0.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd.recompute:block0 | 0.538 | 0.540 | 0.9 | 3 |
| bwd.recompute:block0.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block0.attn.qkv | 0.031 | 0.032 | 0.1 | 3 |
| bwd.recompute:block0.attn.sdpa | 0.286 | 0.288 | 0.5 | 3 |
| bwd.recompute:block0.attn.proj | 0.031 | 0.032 | 0.1 | 3 |
| bwd.recompute:block0.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block0.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block0.grad | 0.823 | 0.827 | 1.4 | 3 |
| bwd:embed | 0.328 | 0.329 | 0.5 | 2 |
| opt | 21.990 | 23.729 | 36.1 | 1 |
| opt:opt.clip | 0.406 | 0.410 | 0.7 | 2 |
| opt:opt.polar_muon_adamw | 21.422 | 23.089 | 35.2 | 2 |
| opt:opt.muon | 16.738 | 18.383 | 27.5 | 2 |
| opt:opt.muon.ns | 21.731 | 24.151 | 35.7 | 3 |
| opt:opt.adamw | 4.477 | 4.709 | 7.4 | 2 |
| opt:opt.moe_bias | 0.015 | 0.019 | 0.0 | 3 |
| opt:opt.zero_grad | 0.190 | 0.291 | 0.3 | 3 |

## Time by part type (sum over layers)

| part type | median ms sum | % of step |
| :--- | ---: | ---: |
| bwd | 23.435 | 38.5 |
| opt | 21.990 | 36.1 |
| opt:opt.muon.ns | 21.731 | 35.7 |
| opt:opt.polar_muon_adamw | 21.422 | 35.2 |
| opt:opt.muon | 16.738 | 27.5 |
| fwd | 16.365 | 26.9 |
| bwd:head+loss | 12.292 | 20.2 |
| bwd:stack | 10.804 | 17.7 |
| bwd:block* | 10.760 | 17.7 |
| fwd:head+loss | 10.429 | 17.1 |
| fwd:stack | 5.231 | 8.6 |
| fwd:block* | 5.006 | 8.2 |
| bwd:block*.grad | 4.930 | 8.1 |
| opt:opt.adamw | 4.477 | 7.4 |
| bwd.recompute:block* | 3.229 | 5.3 |
| bwd.invert:block* | 3.222 | 5.3 |
| fwd:block*.attn.sdpa | 2.335 | 3.8 |
| bwd.recompute:block*.attn.sdpa | 1.715 | 2.8 |
| bwd.invert:block*.attn.sdpa | 1.714 | 2.8 |
| fwd:block*.mlp | 1.068 | 1.8 |
| fwd:block*.attn.qkv | 0.822 | 1.4 |
| fwd:embed.ke | 0.614 | 1.0 |
| fwd:embed | 0.611 | 1.0 |
| fwd:block*.attn.proj | 0.570 | 0.9 |
| bwd.recompute:block*.mlp | 0.510 | 0.8 |
| bwd.invert:block*.mlp | 0.508 | 0.8 |
| opt:opt.clip | 0.406 | 0.7 |
| data | 0.346 | 0.6 |
| bwd:embed | 0.328 | 0.5 |
| fwd:block*.ln1 | 0.314 | 0.5 |
| fwd:block*.ln2 | 0.294 | 0.5 |
| opt:opt.zero_grad | 0.190 | 0.3 |
| bwd.recompute:block*.attn.qkv | 0.188 | 0.3 |
| bwd.invert:block*.attn.qkv | 0.187 | 0.3 |
| bwd.recompute:block*.attn.proj | 0.181 | 0.3 |
| bwd.invert:block*.attn.proj | 0.180 | 0.3 |
| bwd.invert:block*.ln1 | 0.125 | 0.2 |
| bwd.recompute:block*.ln1 | 0.125 | 0.2 |
| bwd.invert:block*.ln2 | 0.120 | 0.2 |
| bwd.recompute:block*.ln2 | 0.120 | 0.2 |
| opt:opt.moe_bias | 0.015 | 0.0 |

## Five slowest leaf parts

1. `opt:opt.muon.ns` — 21.731 ms (35.7% of step)
2. `bwd:block1.grad` — 0.824 ms (1.4% of step)
3. `bwd:block0.grad` — 0.823 ms (1.4% of step)
4. `bwd:block4.grad` — 0.822 ms (1.4% of step)
5. `bwd:block5.grad` — 0.821 ms (1.3% of step)
