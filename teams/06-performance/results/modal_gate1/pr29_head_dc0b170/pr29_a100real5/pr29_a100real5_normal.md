# Bench report — pr29_a100real5_normal

**GPU:** NVIDIA A100-SXM4-40GB  |  **dtype:** bf16  |  **B x T:** 16 x 256  |  **torch:** 2.15.0+cu132
**commit:** `dc0b1703d7d0c51b152bd37d81f6fc2b3ddcf64d`  |  **tag:** pr29_a100real5_normal

## Step (clean)

- median: 85.645 ms
- p10..p90: 83.794 .. 89.414 ms
- tokens/s: 47,825
- MFU: 3.8%  |  HFU: 4.2%

## Diagnostics

### CUDA timing-event allocations

- [OK] clean: events_created_during_steps=0
- [OK] layer: events_created_during_steps=0
- [OK] layer.inner_pass: events_created_during_steps=0

### Benchmark warnings

- [warn] recorder overhead 2.4% > 2.0%: layer numbers are flagged
- [warn] 10 gated part(s) have p10..p90 spread > 10%, so may miss the 5% check: data, fwd:embed, fwd:block0, fwd:block2, fwd:block3, fwd:block5 (+4 more)

## Regions

| part | median ms | p90 | % of step | level |
| :--- | ---: | ---: | ---: | ---: |
| data | 0.984 | 1.110 | 1.1 | 1 |
| fwd | 19.702 | 20.321 | 23.0 | 1 |
| fwd:embed | 0.809 | 0.888 | 0.9 | 2 |
| fwd:embed.ke | 0.788 | 0.877 | 0.9 | 3 |
| fwd:stack | 8.226 | 8.725 | 9.6 | 1 |
| fwd:block0 | 1.548 | 1.718 | 1.8 | 2 |
| fwd:block0.ln1 | 0.104 | 0.120 | 0.1 | 3 |
| fwd:block0.attn.qkv | 0.284 | 0.338 | 0.3 | 3 |
| fwd:block0.attn.sdpa | 0.654 | 0.751 | 0.8 | 3 |
| fwd:block0.attn.proj | 0.210 | 0.237 | 0.2 | 3 |
| fwd:block0.ln2 | 0.074 | 0.092 | 0.1 | 3 |
| fwd:block0.mlp | 0.287 | 0.313 | 0.3 | 3 |
| fwd:block1 | 1.276 | 1.341 | 1.5 | 2 |
| fwd:block1.ln1 | 0.074 | 0.084 | 0.1 | 3 |
| fwd:block1.attn.qkv | 0.207 | 0.238 | 0.2 | 3 |
| fwd:block1.attn.sdpa | 0.521 | 0.575 | 0.6 | 3 |
| fwd:block1.attn.proj | 0.196 | 0.217 | 0.2 | 3 |
| fwd:block1.ln2 | 0.070 | 0.085 | 0.1 | 3 |
| fwd:block1.mlp | 0.263 | 0.287 | 0.3 | 3 |
| fwd:block2 | 1.251 | 1.328 | 1.5 | 2 |
| fwd:block2.ln1 | 0.071 | 0.091 | 0.1 | 3 |
| fwd:block2.attn.qkv | 0.201 | 0.221 | 0.2 | 3 |
| fwd:block2.attn.sdpa | 0.508 | 0.550 | 0.6 | 3 |
| fwd:block2.attn.proj | 0.195 | 0.219 | 0.2 | 3 |
| fwd:block2.ln2 | 0.067 | 0.081 | 0.1 | 3 |
| fwd:block2.mlp | 0.255 | 0.291 | 0.3 | 3 |
| fwd:block3 | 1.237 | 1.309 | 1.4 | 2 |
| fwd:block3.ln1 | 0.069 | 0.083 | 0.1 | 3 |
| fwd:block3.attn.qkv | 0.203 | 0.227 | 0.2 | 3 |
| fwd:block3.attn.sdpa | 0.504 | 0.550 | 0.6 | 3 |
| fwd:block3.attn.proj | 0.190 | 0.213 | 0.2 | 3 |
| fwd:block3.ln2 | 0.068 | 0.087 | 0.1 | 3 |
| fwd:block3.mlp | 0.257 | 0.296 | 0.3 | 3 |
| fwd:block4 | 1.244 | 1.287 | 1.5 | 2 |
| fwd:block4.ln1 | 0.068 | 0.078 | 0.1 | 3 |
| fwd:block4.attn.qkv | 0.202 | 0.225 | 0.2 | 3 |
| fwd:block4.attn.sdpa | 0.506 | 0.544 | 0.6 | 3 |
| fwd:block4.attn.proj | 0.192 | 0.212 | 0.2 | 3 |
| fwd:block4.ln2 | 0.067 | 0.078 | 0.1 | 3 |
| fwd:block4.mlp | 0.257 | 0.285 | 0.3 | 3 |
| fwd:block5 | 1.241 | 1.302 | 1.4 | 2 |
| fwd:block5.ln1 | 0.070 | 0.085 | 0.1 | 3 |
| fwd:block5.attn.qkv | 0.201 | 0.225 | 0.2 | 3 |
| fwd:block5.attn.sdpa | 0.498 | 0.534 | 0.6 | 3 |
| fwd:block5.attn.proj | 0.193 | 0.216 | 0.2 | 3 |
| fwd:block5.ln2 | 0.068 | 0.081 | 0.1 | 3 |
| fwd:block5.mlp | 0.253 | 0.282 | 0.3 | 3 |
| fwd:head+loss | 10.463 | 10.487 | 12.2 | 2 |
| bwd | 23.354 | 23.433 | 27.3 | 1 |
| bwd:head+loss | 12.280 | 12.290 | 14.3 | 2 |
| bwd:stack | 10.747 | 10.778 | 12.5 | 1 |
| bwd:block5 | 1.781 | 1.789 | 2.1 | 2 |
| bwd.invert:block5 | 0.529 | 0.531 | 0.6 | 3 |
| bwd.invert:block5.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block5.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block5.attn.sdpa | 0.285 | 0.286 | 0.3 | 3 |
| bwd.invert:block5.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block5.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block5.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd.recompute:block5 | 0.528 | 0.531 | 0.6 | 3 |
| bwd.recompute:block5.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block5.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block5.attn.sdpa | 0.282 | 0.285 | 0.3 | 3 |
| bwd.recompute:block5.attn.proj | 0.029 | 0.030 | 0.0 | 3 |
| bwd.recompute:block5.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.recompute:block5.mlp | 0.084 | 0.084 | 0.1 | 3 |
| bwd:block5.grad | 0.819 | 0.821 | 1.0 | 3 |
| bwd:block4 | 1.787 | 1.792 | 2.1 | 2 |
| bwd.invert:block4 | 0.531 | 0.534 | 0.6 | 3 |
| bwd.invert:block4.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block4.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block4.attn.sdpa | 0.285 | 0.287 | 0.3 | 3 |
| bwd.invert:block4.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block4.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.invert:block4.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd.recompute:block4 | 0.534 | 0.536 | 0.6 | 3 |
| bwd.recompute:block4.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block4.attn.qkv | 0.031 | 0.031 | 0.0 | 3 |
| bwd.recompute:block4.attn.sdpa | 0.285 | 0.287 | 0.3 | 3 |
| bwd.recompute:block4.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block4.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block4.mlp | 0.084 | 0.086 | 0.1 | 3 |
| bwd:block4.grad | 0.817 | 0.820 | 1.0 | 3 |
| bwd:block3 | 1.782 | 1.790 | 2.1 | 2 |
| bwd.invert:block3 | 0.529 | 0.532 | 0.6 | 3 |
| bwd.invert:block3.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block3.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block3.attn.sdpa | 0.284 | 0.286 | 0.3 | 3 |
| bwd.invert:block3.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block3.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block3.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd.recompute:block3 | 0.531 | 0.534 | 0.6 | 3 |
| bwd.recompute:block3.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block3.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block3.attn.sdpa | 0.284 | 0.285 | 0.3 | 3 |
| bwd.recompute:block3.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block3.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.recompute:block3.mlp | 0.084 | 0.084 | 0.1 | 3 |
| bwd:block3.grad | 0.818 | 0.820 | 1.0 | 3 |
| bwd:block2 | 1.782 | 1.787 | 2.1 | 2 |
| bwd.invert:block2 | 0.531 | 0.534 | 0.6 | 3 |
| bwd.invert:block2.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block2.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block2.attn.sdpa | 0.286 | 0.288 | 0.3 | 3 |
| bwd.invert:block2.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block2.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.invert:block2.mlp | 0.083 | 0.083 | 0.1 | 3 |
| bwd.recompute:block2 | 0.532 | 0.535 | 0.6 | 3 |
| bwd.recompute:block2.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block2.attn.qkv | 0.031 | 0.031 | 0.0 | 3 |
| bwd.recompute:block2.attn.sdpa | 0.286 | 0.288 | 0.3 | 3 |
| bwd.recompute:block2.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block2.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block2.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd:block2.grad | 0.816 | 0.819 | 1.0 | 3 |
| bwd:block1 | 1.789 | 1.795 | 2.1 | 2 |
| bwd.invert:block1 | 0.532 | 0.536 | 0.6 | 3 |
| bwd.invert:block1.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block1.attn.qkv | 0.031 | 0.031 | 0.0 | 3 |
| bwd.invert:block1.attn.sdpa | 0.285 | 0.287 | 0.3 | 3 |
| bwd.invert:block1.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block1.ln2 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block1.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd.recompute:block1 | 0.532 | 0.539 | 0.6 | 3 |
| bwd.recompute:block1.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block1.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block1.attn.sdpa | 0.285 | 0.287 | 0.3 | 3 |
| bwd.recompute:block1.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block1.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.recompute:block1.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd:block1.grad | 0.822 | 1.490 | 1.0 | 3 |
| bwd:block0 | 1.786 | 1.790 | 2.1 | 2 |
| bwd.invert:block0 | 0.533 | 1.781 | 0.6 | 3 |
| bwd.invert:block0.ln1 | 0.022 | 0.084 | 0.0 | 3 |
| bwd.invert:block0.attn.qkv | 0.032 | 0.230 | 0.0 | 3 |
| bwd.invert:block0.attn.sdpa | 0.285 | 0.533 | 0.3 | 3 |
| bwd.invert:block0.attn.proj | 0.030 | 0.211 | 0.0 | 3 |
| bwd.invert:block0.ln2 | 0.019 | 0.073 | 0.0 | 3 |
| bwd.invert:block0.mlp | 0.083 | 0.276 | 0.1 | 3 |
| bwd.recompute:block0 | 1.656 | 1.918 | 1.9 | 3 |
| bwd.recompute:block0.ln1 | 0.020 | 0.090 | 0.0 | 3 |
| bwd.recompute:block0.attn.qkv | 0.188 | 0.246 | 0.2 | 3 |
| bwd.recompute:block0.attn.sdpa | 0.531 | 0.597 | 0.6 | 3 |
| bwd.recompute:block0.attn.proj | 0.202 | 0.234 | 0.2 | 3 |
| bwd.recompute:block0.ln2 | 0.073 | 0.088 | 0.1 | 3 |
| bwd.recompute:block0.mlp | 0.270 | 0.298 | 0.3 | 3 |
| bwd:block0.grad | 2.111 | 2.311 | 2.5 | 3 |
| bwd:embed | 0.315 | 0.336 | 0.4 | 2 |
| opt | 44.613 | 48.617 | 52.1 | 1 |
| opt:opt.clip | 0.409 | 1.607 | 0.5 | 2 |
| opt:opt.polar_muon_adamw | 43.746 | 46.612 | 51.1 | 2 |
| opt:opt.muon | 37.446 | 40.105 | 43.7 | 2 |
| opt:opt.muon.ns | 40.133 | 42.049 | 46.9 | 3 |
| opt:opt.adamw | 6.140 | 6.384 | 7.2 | 2 |
| opt:opt.moe_bias | 0.018 | 0.022 | 0.0 | 3 |
| opt:opt.zero_grad | 0.369 | 0.410 | 0.4 | 3 |

## Time by part type (sum over layers)

| part type | median ms sum | % of step |
| :--- | ---: | ---: |
| opt | 44.613 | 52.1 |
| opt:opt.polar_muon_adamw | 43.746 | 51.1 |
| opt:opt.muon.ns | 40.133 | 46.9 |
| opt:opt.muon | 37.446 | 43.7 |
| bwd | 23.354 | 27.3 |
| fwd | 19.702 | 23.0 |
| bwd:head+loss | 12.280 | 14.3 |
| bwd:stack | 10.747 | 12.5 |
| bwd:block* | 10.706 | 12.5 |
| fwd:head+loss | 10.463 | 12.2 |
| fwd:stack | 8.226 | 9.6 |
| fwd:block* | 7.796 | 9.1 |
| bwd:block*.grad | 6.204 | 7.2 |
| opt:opt.adamw | 6.140 | 7.2 |
| bwd.recompute:block* | 4.315 | 5.0 |
| fwd:block*.attn.sdpa | 3.191 | 3.7 |
| bwd.invert:block* | 3.187 | 3.7 |
| bwd.recompute:block*.attn.sdpa | 1.952 | 2.3 |
| bwd.invert:block*.attn.sdpa | 1.708 | 2.0 |
| fwd:block*.mlp | 1.571 | 1.8 |
| fwd:block*.attn.qkv | 1.297 | 1.5 |
| fwd:block*.attn.proj | 1.176 | 1.4 |
| data | 0.984 | 1.1 |
| fwd:embed | 0.809 | 0.9 |
| fwd:embed.ke | 0.788 | 0.9 |
| bwd.recompute:block*.mlp | 0.689 | 0.8 |
| bwd.invert:block*.mlp | 0.500 | 0.6 |
| fwd:block*.ln1 | 0.455 | 0.5 |
| fwd:block*.ln2 | 0.412 | 0.5 |
| opt:opt.clip | 0.409 | 0.5 |
| opt:opt.zero_grad | 0.369 | 0.4 |
| bwd.recompute:block*.attn.proj | 0.351 | 0.4 |
| bwd.recompute:block*.attn.qkv | 0.342 | 0.4 |
| bwd:embed | 0.315 | 0.4 |
| bwd.invert:block*.attn.qkv | 0.185 | 0.2 |
| bwd.invert:block*.attn.proj | 0.180 | 0.2 |
| bwd.recompute:block*.ln2 | 0.170 | 0.2 |
| bwd.invert:block*.ln1 | 0.124 | 0.1 |
| bwd.recompute:block*.ln1 | 0.123 | 0.1 |
| bwd.invert:block*.ln2 | 0.118 | 0.1 |
| opt:opt.moe_bias | 0.018 | 0.0 |

## Five slowest leaf parts

1. `opt:opt.muon.ns` — 40.133 ms (46.9% of step)
2. `bwd:block0.grad` — 2.111 ms (2.5% of step)
3. `bwd:block1.grad` — 0.822 ms (1.0% of step)
4. `bwd:block5.grad` — 0.819 ms (1.0% of step)
5. `bwd:block3.grad` — 0.818 ms (1.0% of step)
