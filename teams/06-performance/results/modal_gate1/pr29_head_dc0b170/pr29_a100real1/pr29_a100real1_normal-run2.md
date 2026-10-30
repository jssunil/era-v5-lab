# Bench report — pr29_a100real1_normal-run2

**GPU:** NVIDIA A100-SXM4-40GB  |  **dtype:** bf16  |  **B x T:** 16 x 256  |  **torch:** 2.15.0+cu132
**commit:** `dc0b1703d7d0c51b152bd37d81f6fc2b3ddcf64d`  |  **tag:** pr29_a100real1_normal-run2

## Step (clean)

- median: 81.770 ms
- p10..p90: 80.461 .. 83.361 ms
- tokens/s: 50,092
- MFU: 4.0%  |  HFU: 4.4%

## Diagnostics

### CUDA timing-event allocations

- [OK] clean: events_created_during_steps=0
- [OK] layer: events_created_during_steps=0
- [OK] layer.inner_pass: events_created_during_steps=0

### Benchmark warnings

- [warn] recorder overhead 2.0% > 2.0%: layer numbers are flagged
- [warn] 13 gated part(s) have p10..p90 spread > 10%, so may miss the 5% check: data, fwd:embed, fwd:stack, fwd:block0, fwd:block1, fwd:block2 (+7 more)

## Regions

| part | median ms | p90 | % of step | level |
| :--- | ---: | ---: | ---: | ---: |
| data | 0.901 | 0.996 | 1.1 | 1 |
| fwd | 19.252 | 19.741 | 23.5 | 1 |
| fwd:embed | 0.784 | 0.833 | 1.0 | 2 |
| fwd:embed.ke | 0.718 | 0.767 | 0.9 | 3 |
| fwd:stack | 7.803 | 8.264 | 9.5 | 1 |
| fwd:block0 | 1.431 | 1.551 | 1.8 | 2 |
| fwd:block0.ln1 | 0.085 | 0.106 | 0.1 | 3 |
| fwd:block0.attn.qkv | 0.221 | 0.260 | 0.3 | 3 |
| fwd:block0.attn.sdpa | 0.532 | 0.594 | 0.7 | 3 |
| fwd:block0.attn.proj | 0.184 | 0.215 | 0.2 | 3 |
| fwd:block0.ln2 | 0.068 | 0.083 | 0.1 | 3 |
| fwd:block0.mlp | 0.248 | 0.281 | 0.3 | 3 |
| fwd:block1 | 1.218 | 1.298 | 1.5 | 2 |
| fwd:block1.ln1 | 0.068 | 0.081 | 0.1 | 3 |
| fwd:block1.attn.qkv | 0.187 | 0.216 | 0.2 | 3 |
| fwd:block1.attn.sdpa | 0.474 | 0.510 | 0.6 | 3 |
| fwd:block1.attn.proj | 0.180 | 0.203 | 0.2 | 3 |
| fwd:block1.ln2 | 0.061 | 0.073 | 0.1 | 3 |
| fwd:block1.mlp | 0.233 | 0.277 | 0.3 | 3 |
| fwd:block2 | 1.182 | 1.261 | 1.4 | 2 |
| fwd:block2.ln1 | 0.066 | 0.084 | 0.1 | 3 |
| fwd:block2.attn.qkv | 0.181 | 0.206 | 0.2 | 3 |
| fwd:block2.attn.sdpa | 0.467 | 0.515 | 0.6 | 3 |
| fwd:block2.attn.proj | 0.176 | 0.197 | 0.2 | 3 |
| fwd:block2.ln2 | 0.062 | 0.079 | 0.1 | 3 |
| fwd:block2.mlp | 0.233 | 0.265 | 0.3 | 3 |
| fwd:block3 | 1.180 | 1.268 | 1.4 | 2 |
| fwd:block3.ln1 | 0.062 | 0.076 | 0.1 | 3 |
| fwd:block3.attn.qkv | 0.185 | 0.211 | 0.2 | 3 |
| fwd:block3.attn.sdpa | 0.465 | 0.498 | 0.6 | 3 |
| fwd:block3.attn.proj | 0.175 | 0.196 | 0.2 | 3 |
| fwd:block3.ln2 | 0.062 | 0.081 | 0.1 | 3 |
| fwd:block3.mlp | 0.232 | 0.266 | 0.3 | 3 |
| fwd:block4 | 1.185 | 1.266 | 1.4 | 2 |
| fwd:block4.ln1 | 0.062 | 0.083 | 0.1 | 3 |
| fwd:block4.attn.qkv | 0.182 | 0.212 | 0.2 | 3 |
| fwd:block4.attn.sdpa | 0.464 | 0.504 | 0.6 | 3 |
| fwd:block4.attn.proj | 0.173 | 0.199 | 0.2 | 3 |
| fwd:block4.ln2 | 0.060 | 0.075 | 0.1 | 3 |
| fwd:block4.mlp | 0.232 | 0.266 | 0.3 | 3 |
| fwd:block5 | 1.183 | 1.255 | 1.4 | 2 |
| fwd:block5.ln1 | 0.063 | 0.073 | 0.1 | 3 |
| fwd:block5.attn.qkv | 0.179 | 0.207 | 0.2 | 3 |
| fwd:block5.attn.sdpa | 0.468 | 0.512 | 0.6 | 3 |
| fwd:block5.attn.proj | 0.172 | 0.200 | 0.2 | 3 |
| fwd:block5.ln2 | 0.063 | 0.080 | 0.1 | 3 |
| fwd:block5.mlp | 0.234 | 0.263 | 0.3 | 3 |
| fwd:head+loss | 10.463 | 10.484 | 12.8 | 2 |
| bwd | 23.380 | 23.401 | 28.6 | 1 |
| bwd:head+loss | 12.292 | 12.311 | 15.0 | 2 |
| bwd:stack | 10.754 | 10.770 | 13.2 | 1 |
| bwd:block5 | 1.784 | 1.789 | 2.2 | 2 |
| bwd.invert:block5 | 0.532 | 0.537 | 0.7 | 3 |
| bwd.invert:block5.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block5.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block5.attn.sdpa | 0.287 | 0.289 | 0.4 | 3 |
| bwd.invert:block5.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block5.ln2 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block5.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd.recompute:block5 | 0.531 | 0.538 | 0.6 | 3 |
| bwd.recompute:block5.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block5.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block5.attn.sdpa | 0.284 | 0.287 | 0.3 | 3 |
| bwd.recompute:block5.attn.proj | 0.029 | 0.030 | 0.0 | 3 |
| bwd.recompute:block5.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.recompute:block5.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd:block5.grad | 0.818 | 0.822 | 1.0 | 3 |
| bwd:block4 | 1.786 | 1.794 | 2.2 | 2 |
| bwd.invert:block4 | 0.531 | 0.537 | 0.6 | 3 |
| bwd.invert:block4.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block4.attn.qkv | 0.031 | 0.033 | 0.0 | 3 |
| bwd.invert:block4.attn.sdpa | 0.285 | 0.287 | 0.3 | 3 |
| bwd.invert:block4.attn.proj | 0.029 | 0.030 | 0.0 | 3 |
| bwd.invert:block4.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.invert:block4.mlp | 0.084 | 0.084 | 0.1 | 3 |
| bwd.recompute:block4 | 0.534 | 0.539 | 0.7 | 3 |
| bwd.recompute:block4.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block4.attn.qkv | 0.031 | 0.031 | 0.0 | 3 |
| bwd.recompute:block4.attn.sdpa | 0.286 | 0.288 | 0.3 | 3 |
| bwd.recompute:block4.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block4.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block4.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block4.grad | 0.816 | 0.819 | 1.0 | 3 |
| bwd:block3 | 1.784 | 1.789 | 2.2 | 2 |
| bwd.invert:block3 | 0.529 | 0.532 | 0.6 | 3 |
| bwd.invert:block3.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block3.attn.qkv | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block3.attn.sdpa | 0.285 | 0.287 | 0.3 | 3 |
| bwd.invert:block3.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block3.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block3.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd.recompute:block3 | 0.532 | 0.535 | 0.7 | 3 |
| bwd.recompute:block3.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block3.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block3.attn.sdpa | 0.284 | 0.286 | 0.3 | 3 |
| bwd.recompute:block3.attn.proj | 0.030 | 0.030 | 0.0 | 3 |
| bwd.recompute:block3.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.recompute:block3.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd:block3.grad | 0.819 | 0.824 | 1.0 | 3 |
| bwd:block2 | 1.784 | 1.791 | 2.2 | 2 |
| bwd.invert:block2 | 0.530 | 0.535 | 0.6 | 3 |
| bwd.invert:block2.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block2.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block2.attn.sdpa | 0.285 | 0.287 | 0.3 | 3 |
| bwd.invert:block2.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block2.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.invert:block2.mlp | 0.082 | 0.083 | 0.1 | 3 |
| bwd.recompute:block2 | 0.534 | 0.537 | 0.7 | 3 |
| bwd.recompute:block2.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block2.attn.qkv | 0.031 | 0.031 | 0.0 | 3 |
| bwd.recompute:block2.attn.sdpa | 0.286 | 0.288 | 0.3 | 3 |
| bwd.recompute:block2.attn.proj | 0.030 | 0.032 | 0.0 | 3 |
| bwd.recompute:block2.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block2.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block2.grad | 0.818 | 0.824 | 1.0 | 3 |
| bwd:block1 | 1.788 | 1.796 | 2.2 | 2 |
| bwd.invert:block1 | 0.532 | 0.539 | 0.7 | 3 |
| bwd.invert:block1.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block1.attn.qkv | 0.031 | 0.031 | 0.0 | 3 |
| bwd.invert:block1.attn.sdpa | 0.285 | 0.287 | 0.3 | 3 |
| bwd.invert:block1.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block1.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block1.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd.recompute:block1 | 0.532 | 0.539 | 0.7 | 3 |
| bwd.recompute:block1.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block1.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block1.attn.sdpa | 0.285 | 0.287 | 0.3 | 3 |
| bwd.recompute:block1.attn.proj | 0.030 | 0.030 | 0.0 | 3 |
| bwd.recompute:block1.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.recompute:block1.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd:block1.grad | 0.820 | 0.825 | 1.0 | 3 |
| bwd:block0 | 1.785 | 1.790 | 2.2 | 2 |
| bwd.invert:block0 | 0.531 | 0.536 | 0.6 | 3 |
| bwd.invert:block0.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block0.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block0.attn.sdpa | 0.284 | 0.287 | 0.3 | 3 |
| bwd.invert:block0.attn.proj | 0.029 | 0.030 | 0.0 | 3 |
| bwd.invert:block0.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.invert:block0.mlp | 0.084 | 0.084 | 0.1 | 3 |
| bwd.recompute:block0 | 0.531 | 0.536 | 0.6 | 3 |
| bwd.recompute:block0.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block0.attn.qkv | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block0.attn.sdpa | 0.285 | 0.288 | 0.3 | 3 |
| bwd.recompute:block0.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block0.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block0.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd:block0.grad | 0.819 | 0.849 | 1.0 | 3 |
| bwd:embed | 0.325 | 0.328 | 0.4 | 2 |
| opt | 40.858 | 46.046 | 50.0 | 1 |
| opt:opt.clip | 0.410 | 0.414 | 0.5 | 2 |
| opt:opt.polar_muon_adamw | 40.112 | 45.274 | 49.1 | 2 |
| opt:opt.muon | 33.896 | 38.568 | 41.5 | 2 |
| opt:opt.muon.ns | 37.554 | 38.544 | 45.9 | 3 |
| opt:opt.adamw | 6.011 | 6.368 | 7.4 | 2 |
| opt:opt.moe_bias | 0.017 | 0.019 | 0.0 | 3 |
| opt:opt.zero_grad | 0.280 | 0.323 | 0.3 | 3 |

## Time by part type (sum over layers)

| part type | median ms sum | % of step |
| :--- | ---: | ---: |
| opt | 40.858 | 50.0 |
| opt:opt.polar_muon_adamw | 40.112 | 49.1 |
| opt:opt.muon.ns | 37.554 | 45.9 |
| opt:opt.muon | 33.896 | 41.5 |
| bwd | 23.380 | 28.6 |
| fwd | 19.252 | 23.5 |
| bwd:head+loss | 12.292 | 15.0 |
| bwd:stack | 10.754 | 13.2 |
| bwd:block* | 10.710 | 13.1 |
| fwd:head+loss | 10.463 | 12.8 |
| fwd:stack | 7.803 | 9.5 |
| fwd:block* | 7.378 | 9.0 |
| opt:opt.adamw | 6.011 | 7.4 |
| bwd:block*.grad | 4.911 | 6.0 |
| bwd.recompute:block* | 3.195 | 3.9 |
| bwd.invert:block* | 3.187 | 3.9 |
| fwd:block*.attn.sdpa | 2.870 | 3.5 |
| bwd.invert:block*.attn.sdpa | 1.709 | 2.1 |
| bwd.recompute:block*.attn.sdpa | 1.708 | 2.1 |
| fwd:block*.mlp | 1.414 | 1.7 |
| fwd:block*.attn.qkv | 1.136 | 1.4 |
| fwd:block*.attn.proj | 1.059 | 1.3 |
| data | 0.901 | 1.1 |
| fwd:embed | 0.784 | 1.0 |
| fwd:embed.ke | 0.718 | 0.9 |
| bwd.recompute:block*.mlp | 0.504 | 0.6 |
| bwd.invert:block*.mlp | 0.502 | 0.6 |
| opt:opt.clip | 0.410 | 0.5 |
| fwd:block*.ln1 | 0.406 | 0.5 |
| fwd:block*.ln2 | 0.377 | 0.5 |
| bwd:embed | 0.325 | 0.4 |
| opt:opt.zero_grad | 0.280 | 0.3 |
| bwd.invert:block*.attn.qkv | 0.184 | 0.2 |
| bwd.recompute:block*.attn.qkv | 0.183 | 0.2 |
| bwd.recompute:block*.attn.proj | 0.178 | 0.2 |
| bwd.invert:block*.attn.proj | 0.176 | 0.2 |
| bwd.invert:block*.ln1 | 0.123 | 0.2 |
| bwd.recompute:block*.ln1 | 0.123 | 0.2 |
| bwd.invert:block*.ln2 | 0.117 | 0.1 |
| bwd.recompute:block*.ln2 | 0.117 | 0.1 |
| opt:opt.moe_bias | 0.017 | 0.0 |

## Five slowest leaf parts

1. `opt:opt.muon.ns` — 37.554 ms (45.9% of step)
2. `bwd:block1.grad` — 0.820 ms (1.0% of step)
3. `bwd:block3.grad` — 0.819 ms (1.0% of step)
4. `bwd:block0.grad` — 0.819 ms (1.0% of step)
5. `bwd:block5.grad` — 0.818 ms (1.0% of step)
