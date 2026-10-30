# Bench report — pr29_a100real3_normal-run2

**GPU:** NVIDIA A100-SXM4-80GB  |  **dtype:** bf16  |  **B x T:** 16 x 256  |  **torch:** 2.15.0+cu132
**commit:** `dc0b1703d7d0c51b152bd37d81f6fc2b3ddcf64d`  |  **tag:** pr29_a100real3_normal-run2

## Step (clean)

- median: 85.872 ms
- p10..p90: 82.802 .. 89.293 ms
- tokens/s: 47,699
- MFU: 3.8%  |  HFU: 4.2%

## Diagnostics

### CUDA timing-event allocations

- [OK] clean: events_created_during_steps=0
- [OK] layer: events_created_during_steps=0
- [OK] layer.inner_pass: events_created_during_steps=0

### Benchmark warnings

- [warn] recorder overhead 2.4% > 2.0%: layer numbers are flagged
- [warn] 21 gated part(s) have p10..p90 spread > 10%, so may miss the 5% check: data, fwd, fwd:embed, fwd:stack, fwd:block0, fwd:block1 (+15 more)

## Regions

| part | median ms | p90 | % of step | level |
| :--- | ---: | ---: | ---: | ---: |
| data | 0.924 | 1.162 | 1.1 | 1 |
| fwd | 17.934 | 20.544 | 20.9 | 1 |
| fwd:embed | 0.796 | 0.991 | 0.9 | 2 |
| fwd:embed.ke | 0.786 | 0.837 | 0.9 | 3 |
| fwd:stack | 8.198 | 10.515 | 9.5 | 1 |
| fwd:block0 | 1.544 | 2.077 | 1.8 | 2 |
| fwd:block0.ln1 | 0.105 | 0.130 | 0.1 | 3 |
| fwd:block0.attn.qkv | 0.279 | 0.330 | 0.3 | 3 |
| fwd:block0.attn.sdpa | 0.663 | 0.765 | 0.8 | 3 |
| fwd:block0.attn.proj | 0.216 | 0.258 | 0.3 | 3 |
| fwd:block0.ln2 | 0.081 | 0.096 | 0.1 | 3 |
| fwd:block0.mlp | 0.275 | 0.313 | 0.3 | 3 |
| fwd:block1 | 1.288 | 1.640 | 1.5 | 2 |
| fwd:block1.ln1 | 0.077 | 0.095 | 0.1 | 3 |
| fwd:block1.attn.qkv | 0.207 | 0.242 | 0.2 | 3 |
| fwd:block1.attn.sdpa | 0.546 | 0.595 | 0.6 | 3 |
| fwd:block1.attn.proj | 0.195 | 0.228 | 0.2 | 3 |
| fwd:block1.ln2 | 0.070 | 0.081 | 0.1 | 3 |
| fwd:block1.mlp | 0.249 | 0.286 | 0.3 | 3 |
| fwd:block2 | 1.245 | 1.567 | 1.4 | 2 |
| fwd:block2.ln1 | 0.072 | 0.095 | 0.1 | 3 |
| fwd:block2.attn.qkv | 0.202 | 0.232 | 0.2 | 3 |
| fwd:block2.attn.sdpa | 0.504 | 0.553 | 0.6 | 3 |
| fwd:block2.attn.proj | 0.189 | 0.224 | 0.2 | 3 |
| fwd:block2.ln2 | 0.068 | 0.078 | 0.1 | 3 |
| fwd:block2.mlp | 0.252 | 0.293 | 0.3 | 3 |
| fwd:block3 | 1.228 | 1.619 | 1.4 | 2 |
| fwd:block3.ln1 | 0.069 | 0.081 | 0.1 | 3 |
| fwd:block3.attn.qkv | 0.198 | 0.237 | 0.2 | 3 |
| fwd:block3.attn.sdpa | 0.508 | 0.545 | 0.6 | 3 |
| fwd:block3.attn.proj | 0.185 | 0.209 | 0.2 | 3 |
| fwd:block3.ln2 | 0.067 | 0.077 | 0.1 | 3 |
| fwd:block3.mlp | 0.253 | 0.289 | 0.3 | 3 |
| fwd:block4 | 1.228 | 1.589 | 1.4 | 2 |
| fwd:block4.ln1 | 0.069 | 0.082 | 0.1 | 3 |
| fwd:block4.attn.qkv | 0.196 | 0.216 | 0.2 | 3 |
| fwd:block4.attn.sdpa | 0.504 | 0.540 | 0.6 | 3 |
| fwd:block4.attn.proj | 0.188 | 0.220 | 0.2 | 3 |
| fwd:block4.ln2 | 0.067 | 0.077 | 0.1 | 3 |
| fwd:block4.mlp | 0.246 | 0.284 | 0.3 | 3 |
| fwd:block5 | 1.223 | 1.457 | 1.4 | 2 |
| fwd:block5.ln1 | 0.070 | 0.089 | 0.1 | 3 |
| fwd:block5.attn.qkv | 0.198 | 0.224 | 0.2 | 3 |
| fwd:block5.attn.sdpa | 0.497 | 0.546 | 0.6 | 3 |
| fwd:block5.attn.proj | 0.186 | 0.222 | 0.2 | 3 |
| fwd:block5.ln2 | 0.068 | 0.086 | 0.1 | 3 |
| fwd:block5.mlp | 0.248 | 0.286 | 0.3 | 3 |
| fwd:head+loss | 8.733 | 8.797 | 10.2 | 2 |
| bwd | 22.820 | 33.436 | 26.6 | 1 |
| bwd:head+loss | 10.264 | 10.289 | 12.0 | 2 |
| bwd:stack | 11.843 | 22.256 | 13.8 | 1 |
| bwd:block5 | 1.649 | 1.692 | 1.9 | 2 |
| bwd.invert:block5 | 0.501 | 0.526 | 0.6 | 3 |
| bwd.invert:block5.ln1 | 0.019 | 0.023 | 0.0 | 3 |
| bwd.invert:block5.attn.qkv | 0.031 | 0.037 | 0.0 | 3 |
| bwd.invert:block5.attn.sdpa | 0.259 | 0.264 | 0.3 | 3 |
| bwd.invert:block5.attn.proj | 0.029 | 0.034 | 0.0 | 3 |
| bwd.invert:block5.ln2 | 0.019 | 0.025 | 0.0 | 3 |
| bwd.invert:block5.mlp | 0.081 | 0.086 | 0.1 | 3 |
| bwd.recompute:block5 | 0.503 | 0.526 | 0.6 | 3 |
| bwd.recompute:block5.ln1 | 0.020 | 0.025 | 0.0 | 3 |
| bwd.recompute:block5.attn.qkv | 0.031 | 0.036 | 0.0 | 3 |
| bwd.recompute:block5.attn.sdpa | 0.258 | 0.261 | 0.3 | 3 |
| bwd.recompute:block5.attn.proj | 0.029 | 0.033 | 0.0 | 3 |
| bwd.recompute:block5.ln2 | 0.019 | 0.023 | 0.0 | 3 |
| bwd.recompute:block5.mlp | 0.081 | 0.086 | 0.1 | 3 |
| bwd:block5.grad | 0.751 | 0.763 | 0.9 | 3 |
| bwd:block4 | 1.657 | 1.705 | 1.9 | 2 |
| bwd.invert:block4 | 0.504 | 0.527 | 0.6 | 3 |
| bwd.invert:block4.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block4.attn.qkv | 0.031 | 0.034 | 0.0 | 3 |
| bwd.invert:block4.attn.sdpa | 0.258 | 0.262 | 0.3 | 3 |
| bwd.invert:block4.attn.proj | 0.029 | 0.033 | 0.0 | 3 |
| bwd.invert:block4.ln2 | 0.019 | 0.026 | 0.0 | 3 |
| bwd.invert:block4.mlp | 0.082 | 0.087 | 0.1 | 3 |
| bwd.recompute:block4 | 0.502 | 0.536 | 0.6 | 3 |
| bwd.recompute:block4.ln1 | 0.019 | 0.026 | 0.0 | 3 |
| bwd.recompute:block4.attn.qkv | 0.030 | 0.036 | 0.0 | 3 |
| bwd.recompute:block4.attn.sdpa | 0.259 | 0.263 | 0.3 | 3 |
| bwd.recompute:block4.attn.proj | 0.030 | 0.035 | 0.0 | 3 |
| bwd.recompute:block4.ln2 | 0.019 | 0.025 | 0.0 | 3 |
| bwd.recompute:block4.mlp | 0.083 | 0.087 | 0.1 | 3 |
| bwd:block4.grad | 0.753 | 0.766 | 0.9 | 3 |
| bwd:block3 | 1.651 | 1.709 | 1.9 | 2 |
| bwd.invert:block3 | 0.498 | 0.526 | 0.6 | 3 |
| bwd.invert:block3.ln1 | 0.019 | 0.024 | 0.0 | 3 |
| bwd.invert:block3.attn.qkv | 0.030 | 0.034 | 0.0 | 3 |
| bwd.invert:block3.attn.sdpa | 0.258 | 0.265 | 0.3 | 3 |
| bwd.invert:block3.attn.proj | 0.030 | 0.035 | 0.0 | 3 |
| bwd.invert:block3.ln2 | 0.019 | 0.023 | 0.0 | 3 |
| bwd.invert:block3.mlp | 0.082 | 0.086 | 0.1 | 3 |
| bwd.recompute:block3 | 0.502 | 0.528 | 0.6 | 3 |
| bwd.recompute:block3.ln1 | 0.020 | 0.026 | 0.0 | 3 |
| bwd.recompute:block3.attn.qkv | 0.031 | 0.035 | 0.0 | 3 |
| bwd.recompute:block3.attn.sdpa | 0.257 | 0.261 | 0.3 | 3 |
| bwd.recompute:block3.attn.proj | 0.029 | 0.033 | 0.0 | 3 |
| bwd.recompute:block3.ln2 | 0.018 | 0.023 | 0.0 | 3 |
| bwd.recompute:block3.mlp | 0.082 | 0.088 | 0.1 | 3 |
| bwd:block3.grad | 0.752 | 0.767 | 0.9 | 3 |
| bwd:block2 | 1.651 | 4.900 | 1.9 | 2 |
| bwd.invert:block2 | 0.503 | 0.527 | 0.6 | 3 |
| bwd.invert:block2.ln1 | 0.020 | 0.026 | 0.0 | 3 |
| bwd.invert:block2.attn.qkv | 0.031 | 0.035 | 0.0 | 3 |
| bwd.invert:block2.attn.sdpa | 0.260 | 0.264 | 0.3 | 3 |
| bwd.invert:block2.attn.proj | 0.029 | 0.033 | 0.0 | 3 |
| bwd.invert:block2.ln2 | 0.018 | 0.022 | 0.0 | 3 |
| bwd.invert:block2.mlp | 0.081 | 0.084 | 0.1 | 3 |
| bwd.recompute:block2 | 0.507 | 0.532 | 0.6 | 3 |
| bwd.recompute:block2.ln1 | 0.019 | 0.024 | 0.0 | 3 |
| bwd.recompute:block2.attn.qkv | 0.030 | 0.034 | 0.0 | 3 |
| bwd.recompute:block2.attn.sdpa | 0.260 | 0.265 | 0.3 | 3 |
| bwd.recompute:block2.attn.proj | 0.030 | 0.035 | 0.0 | 3 |
| bwd.recompute:block2.ln2 | 0.019 | 0.024 | 0.0 | 3 |
| bwd.recompute:block2.mlp | 0.083 | 0.088 | 0.1 | 3 |
| bwd:block2.grad | 0.754 | 1.368 | 0.9 | 3 |
| bwd:block1 | 1.655 | 5.847 | 1.9 | 2 |
| bwd.invert:block1 | 0.865 | 1.815 | 1.0 | 3 |
| bwd.invert:block1.ln1 | 0.023 | 0.089 | 0.0 | 3 |
| bwd.invert:block1.attn.qkv | 0.034 | 0.239 | 0.0 | 3 |
| bwd.invert:block1.attn.sdpa | 0.261 | 0.561 | 0.3 | 3 |
| bwd.invert:block1.attn.proj | 0.039 | 0.215 | 0.0 | 3 |
| bwd.invert:block1.ln2 | 0.060 | 0.075 | 0.1 | 3 |
| bwd.invert:block1.mlp | 0.238 | 0.276 | 0.3 | 3 |
| bwd.recompute:block1 | 1.779 | 1.916 | 2.1 | 3 |
| bwd.recompute:block1.ln1 | 0.081 | 0.090 | 0.1 | 3 |
| bwd.recompute:block1.attn.qkv | 0.213 | 0.252 | 0.2 | 3 |
| bwd.recompute:block1.attn.sdpa | 0.544 | 0.609 | 0.6 | 3 |
| bwd.recompute:block1.attn.proj | 0.200 | 0.228 | 0.2 | 3 |
| bwd.recompute:block1.ln2 | 0.074 | 0.097 | 0.1 | 3 |
| bwd.recompute:block1.mlp | 0.259 | 0.298 | 0.3 | 3 |
| bwd:block1.grad | 2.149 | 2.274 | 2.5 | 3 |
| bwd:block0 | 3.371 | 6.051 | 3.9 | 2 |
| bwd.invert:block0 | 1.685 | 1.764 | 2.0 | 3 |
| bwd.invert:block0.ln1 | 0.081 | 0.093 | 0.1 | 3 |
| bwd.invert:block0.attn.qkv | 0.209 | 0.241 | 0.2 | 3 |
| bwd.invert:block0.attn.sdpa | 0.499 | 0.542 | 0.6 | 3 |
| bwd.invert:block0.attn.proj | 0.190 | 0.224 | 0.2 | 3 |
| bwd.invert:block0.ln2 | 0.068 | 0.077 | 0.1 | 3 |
| bwd.invert:block0.mlp | 0.244 | 0.285 | 0.3 | 3 |
| bwd.recompute:block0 | 1.787 | 1.898 | 2.1 | 3 |
| bwd.recompute:block0.ln1 | 0.083 | 0.097 | 0.1 | 3 |
| bwd.recompute:block0.attn.qkv | 0.223 | 0.250 | 0.3 | 3 |
| bwd.recompute:block0.attn.sdpa | 0.545 | 0.589 | 0.6 | 3 |
| bwd.recompute:block0.attn.proj | 0.202 | 0.233 | 0.2 | 3 |
| bwd.recompute:block0.ln2 | 0.075 | 0.088 | 0.1 | 3 |
| bwd.recompute:block0.mlp | 0.260 | 0.297 | 0.3 | 3 |
| bwd:block0.grad | 2.146 | 2.284 | 2.5 | 3 |
| bwd:embed | 0.686 | 0.897 | 0.8 | 2 |
| opt | 46.473 | 54.149 | 54.1 | 1 |
| opt:opt.clip | 1.433 | 2.067 | 1.7 | 2 |
| opt:opt.polar_muon_adamw | 44.627 | 52.134 | 52.0 | 2 |
| opt:opt.muon | 38.426 | 45.505 | 44.7 | 2 |
| opt:opt.muon.ns | 40.018 | 41.410 | 46.6 | 3 |
| opt:opt.adamw | 6.063 | 6.685 | 7.1 | 2 |
| opt:opt.moe_bias | 0.020 | 0.025 | 0.0 | 3 |
| opt:opt.zero_grad | 0.326 | 0.373 | 0.4 | 3 |

## Time by part type (sum over layers)

| part type | median ms sum | % of step |
| :--- | ---: | ---: |
| opt | 46.473 | 54.1 |
| opt:opt.polar_muon_adamw | 44.627 | 52.0 |
| opt:opt.muon.ns | 40.018 | 46.6 |
| opt:opt.muon | 38.426 | 44.7 |
| bwd | 22.820 | 26.6 |
| fwd | 17.934 | 20.9 |
| bwd:stack | 11.843 | 13.8 |
| bwd:block* | 11.633 | 13.5 |
| bwd:head+loss | 10.264 | 12.0 |
| fwd:head+loss | 8.733 | 10.2 |
| fwd:stack | 8.198 | 9.5 |
| fwd:block* | 7.755 | 9.0 |
| bwd:block*.grad | 7.305 | 8.5 |
| opt:opt.adamw | 6.063 | 7.1 |
| bwd.recompute:block* | 5.580 | 6.5 |
| bwd.invert:block* | 4.556 | 5.3 |
| fwd:block*.attn.sdpa | 3.222 | 3.8 |
| bwd.recompute:block*.attn.sdpa | 2.124 | 2.5 |
| bwd.invert:block*.attn.sdpa | 1.795 | 2.1 |
| fwd:block*.mlp | 1.523 | 1.8 |
| opt:opt.clip | 1.433 | 1.7 |
| fwd:block*.attn.qkv | 1.278 | 1.5 |
| fwd:block*.attn.proj | 1.158 | 1.3 |
| data | 0.924 | 1.1 |
| bwd.recompute:block*.mlp | 0.847 | 1.0 |
| bwd.invert:block*.mlp | 0.807 | 0.9 |
| fwd:embed | 0.796 | 0.9 |
| fwd:embed.ke | 0.786 | 0.9 |
| bwd:embed | 0.686 | 0.8 |
| bwd.recompute:block*.attn.qkv | 0.557 | 0.6 |
| bwd.recompute:block*.attn.proj | 0.519 | 0.6 |
| fwd:block*.ln1 | 0.461 | 0.5 |
| fwd:block*.ln2 | 0.420 | 0.5 |
| bwd.invert:block*.attn.qkv | 0.365 | 0.4 |
| bwd.invert:block*.attn.proj | 0.345 | 0.4 |
| opt:opt.zero_grad | 0.326 | 0.4 |
| bwd.recompute:block*.ln1 | 0.244 | 0.3 |
| bwd.recompute:block*.ln2 | 0.226 | 0.3 |
| bwd.invert:block*.ln2 | 0.205 | 0.2 |
| bwd.invert:block*.ln1 | 0.183 | 0.2 |
| opt:opt.moe_bias | 0.020 | 0.0 |

## Five slowest leaf parts

1. `opt:opt.muon.ns` — 40.018 ms (46.6% of step)
2. `bwd:block1.grad` — 2.149 ms (2.5% of step)
3. `bwd:block0.grad` — 2.146 ms (2.5% of step)
4. `fwd:embed.ke` — 0.786 ms (0.9% of step)
5. `bwd:block2.grad` — 0.754 ms (0.9% of step)
