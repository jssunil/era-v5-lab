# Bench report — pr29_a100real3_normal

**GPU:** NVIDIA A100-SXM4-80GB  |  **dtype:** bf16  |  **B x T:** 16 x 256  |  **torch:** 2.15.0+cu132
**commit:** `dc0b1703d7d0c51b152bd37d81f6fc2b3ddcf64d`  |  **tag:** pr29_a100real3_normal

## Step (clean)

- median: 84.054 ms
- p10..p90: 81.993 .. 86.325 ms
- tokens/s: 48,731
- MFU: 3.9%  |  HFU: 4.3%

## Diagnostics

### CUDA timing-event allocations

- [OK] clean: events_created_during_steps=0
- [OK] layer: events_created_during_steps=0
- [OK] layer.inner_pass: events_created_during_steps=0

### Benchmark warnings

- [warn] recorder overhead 2.2% > 2.0%: layer numbers are flagged
- [warn] 9 gated part(s) have p10..p90 spread > 10%, so may miss the 5% check: data, fwd:embed, fwd:stack, fwd:block0, fwd:block1, bwd:stack (+3 more)

## Regions

| part | median ms | p90 | % of step | level |
| :--- | ---: | ---: | ---: | ---: |
| data | 0.852 | 0.949 | 1.0 | 1 |
| fwd | 17.469 | 18.010 | 20.8 | 1 |
| fwd:embed | 0.751 | 0.813 | 0.9 | 2 |
| fwd:embed.ke | 0.716 | 0.769 | 0.9 | 3 |
| fwd:stack | 7.819 | 8.283 | 9.3 | 1 |
| fwd:block0 | 1.408 | 1.604 | 1.7 | 2 |
| fwd:block0.ln1 | 0.086 | 0.101 | 0.1 | 3 |
| fwd:block0.attn.qkv | 0.228 | 0.277 | 0.3 | 3 |
| fwd:block0.attn.sdpa | 0.552 | 0.633 | 0.7 | 3 |
| fwd:block0.attn.proj | 0.190 | 0.222 | 0.2 | 3 |
| fwd:block0.ln2 | 0.072 | 0.082 | 0.1 | 3 |
| fwd:block0.mlp | 0.250 | 0.289 | 0.3 | 3 |
| fwd:block1 | 1.240 | 1.312 | 1.5 | 2 |
| fwd:block1.ln1 | 0.071 | 0.082 | 0.1 | 3 |
| fwd:block1.attn.qkv | 0.190 | 0.224 | 0.2 | 3 |
| fwd:block1.attn.sdpa | 0.492 | 0.537 | 0.6 | 3 |
| fwd:block1.attn.proj | 0.182 | 0.214 | 0.2 | 3 |
| fwd:block1.ln2 | 0.067 | 0.084 | 0.1 | 3 |
| fwd:block1.mlp | 0.235 | 0.273 | 0.3 | 3 |
| fwd:block2 | 1.189 | 1.251 | 1.4 | 2 |
| fwd:block2.ln1 | 0.067 | 0.083 | 0.1 | 3 |
| fwd:block2.attn.qkv | 0.188 | 0.219 | 0.2 | 3 |
| fwd:block2.attn.sdpa | 0.477 | 0.510 | 0.6 | 3 |
| fwd:block2.attn.proj | 0.178 | 0.205 | 0.2 | 3 |
| fwd:block2.ln2 | 0.065 | 0.080 | 0.1 | 3 |
| fwd:block2.mlp | 0.236 | 0.275 | 0.3 | 3 |
| fwd:block3 | 1.193 | 1.233 | 1.4 | 2 |
| fwd:block3.ln1 | 0.067 | 0.077 | 0.1 | 3 |
| fwd:block3.attn.qkv | 0.185 | 0.218 | 0.2 | 3 |
| fwd:block3.attn.sdpa | 0.477 | 0.503 | 0.6 | 3 |
| fwd:block3.attn.proj | 0.179 | 0.213 | 0.2 | 3 |
| fwd:block3.ln2 | 0.066 | 0.073 | 0.1 | 3 |
| fwd:block3.mlp | 0.231 | 0.269 | 0.3 | 3 |
| fwd:block4 | 1.196 | 1.227 | 1.4 | 2 |
| fwd:block4.ln1 | 0.067 | 0.085 | 0.1 | 3 |
| fwd:block4.attn.qkv | 0.187 | 0.222 | 0.2 | 3 |
| fwd:block4.attn.sdpa | 0.473 | 0.505 | 0.6 | 3 |
| fwd:block4.attn.proj | 0.176 | 0.210 | 0.2 | 3 |
| fwd:block4.ln2 | 0.065 | 0.084 | 0.1 | 3 |
| fwd:block4.mlp | 0.235 | 0.273 | 0.3 | 3 |
| fwd:block5 | 1.184 | 1.229 | 1.4 | 2 |
| fwd:block5.ln1 | 0.067 | 0.082 | 0.1 | 3 |
| fwd:block5.attn.qkv | 0.183 | 0.211 | 0.2 | 3 |
| fwd:block5.attn.sdpa | 0.473 | 0.503 | 0.6 | 3 |
| fwd:block5.attn.proj | 0.177 | 0.211 | 0.2 | 3 |
| fwd:block5.ln2 | 0.066 | 0.077 | 0.1 | 3 |
| fwd:block5.mlp | 0.230 | 0.270 | 0.3 | 3 |
| fwd:head+loss | 8.722 | 8.740 | 10.4 | 2 |
| bwd | 21.728 | 23.011 | 25.9 | 1 |
| bwd:head+loss | 10.262 | 10.298 | 12.2 | 2 |
| bwd:stack | 10.787 | 12.050 | 12.8 | 1 |
| bwd:block5 | 1.666 | 1.696 | 2.0 | 2 |
| bwd.invert:block5 | 0.501 | 0.539 | 0.6 | 3 |
| bwd.invert:block5.ln1 | 0.020 | 0.024 | 0.0 | 3 |
| bwd.invert:block5.attn.qkv | 0.031 | 0.035 | 0.0 | 3 |
| bwd.invert:block5.attn.sdpa | 0.260 | 0.264 | 0.3 | 3 |
| bwd.invert:block5.attn.proj | 0.029 | 0.032 | 0.0 | 3 |
| bwd.invert:block5.ln2 | 0.019 | 0.026 | 0.0 | 3 |
| bwd.invert:block5.mlp | 0.083 | 0.092 | 0.1 | 3 |
| bwd.recompute:block5 | 0.504 | 0.532 | 0.6 | 3 |
| bwd.recompute:block5.ln1 | 0.020 | 0.025 | 0.0 | 3 |
| bwd.recompute:block5.attn.qkv | 0.031 | 0.034 | 0.0 | 3 |
| bwd.recompute:block5.attn.sdpa | 0.259 | 0.263 | 0.3 | 3 |
| bwd.recompute:block5.attn.proj | 0.029 | 0.034 | 0.0 | 3 |
| bwd.recompute:block5.ln2 | 0.019 | 0.024 | 0.0 | 3 |
| bwd.recompute:block5.mlp | 0.082 | 0.090 | 0.1 | 3 |
| bwd:block5.grad | 0.755 | 0.770 | 0.9 | 3 |
| bwd:block4 | 1.673 | 1.703 | 2.0 | 2 |
| bwd.invert:block4 | 0.505 | 0.535 | 0.6 | 3 |
| bwd.invert:block4.ln1 | 0.020 | 0.027 | 0.0 | 3 |
| bwd.invert:block4.attn.qkv | 0.031 | 0.035 | 0.0 | 3 |
| bwd.invert:block4.attn.sdpa | 0.260 | 0.264 | 0.3 | 3 |
| bwd.invert:block4.attn.proj | 0.030 | 0.033 | 0.0 | 3 |
| bwd.invert:block4.ln2 | 0.019 | 0.024 | 0.0 | 3 |
| bwd.invert:block4.mlp | 0.083 | 0.089 | 0.1 | 3 |
| bwd.recompute:block4 | 0.505 | 0.538 | 0.6 | 3 |
| bwd.recompute:block4.ln1 | 0.019 | 0.023 | 0.0 | 3 |
| bwd.recompute:block4.attn.qkv | 0.031 | 0.034 | 0.0 | 3 |
| bwd.recompute:block4.attn.sdpa | 0.261 | 0.266 | 0.3 | 3 |
| bwd.recompute:block4.attn.proj | 0.031 | 0.036 | 0.0 | 3 |
| bwd.recompute:block4.ln2 | 0.019 | 0.024 | 0.0 | 3 |
| bwd.recompute:block4.mlp | 0.083 | 0.090 | 0.1 | 3 |
| bwd:block4.grad | 0.757 | 0.777 | 0.9 | 3 |
| bwd:block3 | 1.667 | 1.695 | 2.0 | 2 |
| bwd.invert:block3 | 0.500 | 0.533 | 0.6 | 3 |
| bwd.invert:block3.ln1 | 0.019 | 0.025 | 0.0 | 3 |
| bwd.invert:block3.attn.qkv | 0.031 | 0.034 | 0.0 | 3 |
| bwd.invert:block3.attn.sdpa | 0.259 | 0.263 | 0.3 | 3 |
| bwd.invert:block3.attn.proj | 0.030 | 0.035 | 0.0 | 3 |
| bwd.invert:block3.ln2 | 0.019 | 0.025 | 0.0 | 3 |
| bwd.invert:block3.mlp | 0.083 | 0.088 | 0.1 | 3 |
| bwd.recompute:block3 | 0.502 | 0.535 | 0.6 | 3 |
| bwd.recompute:block3.ln1 | 0.020 | 0.023 | 0.0 | 3 |
| bwd.recompute:block3.attn.qkv | 0.031 | 0.036 | 0.0 | 3 |
| bwd.recompute:block3.attn.sdpa | 0.259 | 0.264 | 0.3 | 3 |
| bwd.recompute:block3.attn.proj | 0.030 | 0.034 | 0.0 | 3 |
| bwd.recompute:block3.ln2 | 0.019 | 0.025 | 0.0 | 3 |
| bwd.recompute:block3.mlp | 0.083 | 0.087 | 0.1 | 3 |
| bwd:block3.grad | 0.755 | 0.772 | 0.9 | 3 |
| bwd:block2 | 1.667 | 1.697 | 2.0 | 2 |
| bwd.invert:block2 | 0.502 | 0.532 | 0.6 | 3 |
| bwd.invert:block2.ln1 | 0.020 | 0.024 | 0.0 | 3 |
| bwd.invert:block2.attn.qkv | 0.031 | 0.034 | 0.0 | 3 |
| bwd.invert:block2.attn.sdpa | 0.261 | 0.264 | 0.3 | 3 |
| bwd.invert:block2.attn.proj | 0.030 | 0.034 | 0.0 | 3 |
| bwd.invert:block2.ln2 | 0.019 | 0.024 | 0.0 | 3 |
| bwd.invert:block2.mlp | 0.082 | 0.085 | 0.1 | 3 |
| bwd.recompute:block2 | 0.504 | 0.539 | 0.6 | 3 |
| bwd.recompute:block2.ln1 | 0.019 | 0.023 | 0.0 | 3 |
| bwd.recompute:block2.attn.qkv | 0.030 | 0.037 | 0.0 | 3 |
| bwd.recompute:block2.attn.sdpa | 0.261 | 0.267 | 0.3 | 3 |
| bwd.recompute:block2.attn.proj | 0.031 | 0.036 | 0.0 | 3 |
| bwd.recompute:block2.ln2 | 0.019 | 0.024 | 0.0 | 3 |
| bwd.recompute:block2.mlp | 0.083 | 0.090 | 0.1 | 3 |
| bwd:block2.grad | 0.753 | 0.773 | 0.9 | 3 |
| bwd:block1 | 1.672 | 1.706 | 2.0 | 2 |
| bwd.invert:block1 | 0.510 | 0.553 | 0.6 | 3 |
| bwd.invert:block1.ln1 | 0.019 | 0.023 | 0.0 | 3 |
| bwd.invert:block1.attn.qkv | 0.031 | 0.036 | 0.0 | 3 |
| bwd.invert:block1.attn.sdpa | 0.260 | 0.267 | 0.3 | 3 |
| bwd.invert:block1.attn.proj | 0.031 | 0.037 | 0.0 | 3 |
| bwd.invert:block1.ln2 | 0.019 | 0.028 | 0.0 | 3 |
| bwd.invert:block1.mlp | 0.084 | 0.092 | 0.1 | 3 |
| bwd.recompute:block1 | 0.534 | 1.706 | 0.6 | 3 |
| bwd.recompute:block1.ln1 | 0.020 | 0.070 | 0.0 | 3 |
| bwd.recompute:block1.attn.qkv | 0.031 | 0.208 | 0.0 | 3 |
| bwd.recompute:block1.attn.sdpa | 0.261 | 0.535 | 0.3 | 3 |
| bwd.recompute:block1.attn.proj | 0.030 | 0.215 | 0.0 | 3 |
| bwd.recompute:block1.ln2 | 0.019 | 0.075 | 0.0 | 3 |
| bwd.recompute:block1.mlp | 0.087 | 0.263 | 0.1 | 3 |
| bwd:block1.grad | 1.722 | 2.122 | 2.0 | 3 |
| bwd:block0 | 2.224 | 3.566 | 2.6 | 2 |
| bwd.invert:block0 | 1.593 | 1.651 | 1.9 | 3 |
| bwd.invert:block0.ln1 | 0.075 | 0.085 | 0.1 | 3 |
| bwd.invert:block0.attn.qkv | 0.200 | 0.227 | 0.2 | 3 |
| bwd.invert:block0.attn.sdpa | 0.478 | 0.508 | 0.6 | 3 |
| bwd.invert:block0.attn.proj | 0.180 | 0.217 | 0.2 | 3 |
| bwd.invert:block0.ln2 | 0.066 | 0.077 | 0.1 | 3 |
| bwd.invert:block0.mlp | 0.233 | 0.274 | 0.3 | 3 |
| bwd.recompute:block0 | 1.712 | 1.781 | 2.0 | 3 |
| bwd.recompute:block0.ln1 | 0.079 | 0.090 | 0.1 | 3 |
| bwd.recompute:block0.attn.qkv | 0.208 | 0.239 | 0.2 | 3 |
| bwd.recompute:block0.attn.sdpa | 0.526 | 0.557 | 0.6 | 3 |
| bwd.recompute:block0.attn.proj | 0.193 | 0.229 | 0.2 | 3 |
| bwd.recompute:block0.ln2 | 0.073 | 0.097 | 0.1 | 3 |
| bwd.recompute:block0.mlp | 0.249 | 0.288 | 0.3 | 3 |
| bwd:block0.grad | 2.023 | 2.120 | 2.4 | 3 |
| bwd:embed | 0.649 | 0.710 | 0.8 | 2 |
| opt | 45.235 | 46.096 | 53.8 | 1 |
| opt:opt.clip | 1.342 | 1.482 | 1.6 | 2 |
| opt:opt.polar_muon_adamw | 43.511 | 44.260 | 51.8 | 2 |
| opt:opt.muon | 37.508 | 38.128 | 44.6 | 2 |
| opt:opt.muon.ns | 38.391 | 39.512 | 45.7 | 3 |
| opt:opt.adamw | 5.847 | 5.949 | 7.0 | 2 |
| opt:opt.moe_bias | 0.018 | 0.020 | 0.0 | 3 |
| opt:opt.zero_grad | 0.264 | 0.327 | 0.3 | 3 |

## Time by part type (sum over layers)

| part type | median ms sum | % of step |
| :--- | ---: | ---: |
| opt | 45.235 | 53.8 |
| opt:opt.polar_muon_adamw | 43.511 | 51.8 |
| opt:opt.muon.ns | 38.391 | 45.7 |
| opt:opt.muon | 37.508 | 44.6 |
| bwd | 21.728 | 25.9 |
| fwd | 17.469 | 20.8 |
| bwd:stack | 10.787 | 12.8 |
| bwd:block* | 10.568 | 12.6 |
| bwd:head+loss | 10.262 | 12.2 |
| fwd:head+loss | 8.722 | 10.4 |
| fwd:stack | 7.819 | 9.3 |
| fwd:block* | 7.410 | 8.8 |
| bwd:block*.grad | 6.765 | 8.0 |
| opt:opt.adamw | 5.847 | 7.0 |
| bwd.recompute:block* | 4.260 | 5.1 |
| bwd.invert:block* | 4.110 | 4.9 |
| fwd:block*.attn.sdpa | 2.943 | 3.5 |
| bwd.recompute:block*.attn.sdpa | 1.828 | 2.2 |
| bwd.invert:block*.attn.sdpa | 1.779 | 2.1 |
| fwd:block*.mlp | 1.418 | 1.7 |
| opt:opt.clip | 1.342 | 1.6 |
| fwd:block*.attn.qkv | 1.163 | 1.4 |
| fwd:block*.attn.proj | 1.082 | 1.3 |
| data | 0.852 | 1.0 |
| fwd:embed | 0.751 | 0.9 |
| fwd:embed.ke | 0.716 | 0.9 |
| bwd.recompute:block*.mlp | 0.667 | 0.8 |
| bwd:embed | 0.649 | 0.8 |
| bwd.invert:block*.mlp | 0.648 | 0.8 |
| fwd:block*.ln1 | 0.424 | 0.5 |
| fwd:block*.ln2 | 0.398 | 0.5 |
| bwd.recompute:block*.attn.qkv | 0.361 | 0.4 |
| bwd.invert:block*.attn.qkv | 0.353 | 0.4 |
| bwd.recompute:block*.attn.proj | 0.343 | 0.4 |
| bwd.invert:block*.attn.proj | 0.329 | 0.4 |
| opt:opt.zero_grad | 0.264 | 0.3 |
| bwd.recompute:block*.ln1 | 0.180 | 0.2 |
| bwd.invert:block*.ln1 | 0.175 | 0.2 |
| bwd.recompute:block*.ln2 | 0.170 | 0.2 |
| bwd.invert:block*.ln2 | 0.163 | 0.2 |
| opt:opt.moe_bias | 0.018 | 0.0 |

## Five slowest leaf parts

1. `opt:opt.muon.ns` — 38.391 ms (45.7% of step)
2. `bwd:block0.grad` — 2.023 ms (2.4% of step)
3. `bwd:block1.grad` — 1.722 ms (2.0% of step)
4. `bwd:block4.grad` — 0.757 ms (0.9% of step)
5. `bwd:block5.grad` — 0.755 ms (0.9% of step)
