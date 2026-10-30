# Bench report — pr29_a100real5_normal-run2

**GPU:** NVIDIA A100-SXM4-40GB  |  **dtype:** bf16  |  **B x T:** 16 x 256  |  **torch:** 2.15.0+cu132
**commit:** `dc0b1703d7d0c51b152bd37d81f6fc2b3ddcf64d`  |  **tag:** pr29_a100real5_normal-run2

## Step (clean)

- median: 90.163 ms
- p10..p90: 88.350 .. 93.015 ms
- tokens/s: 45,429
- MFU: 3.6%  |  HFU: 4.0%

## Diagnostics

### CUDA timing-event allocations

- [OK] clean: events_created_during_steps=0
- [OK] layer: events_created_during_steps=0
- [OK] layer.inner_pass: events_created_during_steps=0

### Benchmark warnings

- [warn] recorder overhead 2.6% > 2.0%: layer numbers are flagged
- [warn] 18 gated part(s) have p10..p90 spread > 10%, so may miss the 5% check: data, fwd:embed, fwd:stack, fwd:block0, fwd:block1, fwd:block2 (+12 more)

## Regions

| part | median ms | p90 | % of step | level |
| :--- | ---: | ---: | ---: | ---: |
| data | 1.018 | 1.151 | 1.1 | 1 |
| fwd | 19.911 | 20.748 | 22.1 | 1 |
| fwd:embed | 0.827 | 0.923 | 0.9 | 2 |
| fwd:embed.ke | 0.799 | 0.854 | 0.9 | 3 |
| fwd:stack | 8.377 | 9.127 | 9.3 | 1 |
| fwd:block0 | 1.602 | 1.791 | 1.8 | 2 |
| fwd:block0.ln1 | 0.102 | 0.117 | 0.1 | 3 |
| fwd:block0.attn.qkv | 0.285 | 0.324 | 0.3 | 3 |
| fwd:block0.attn.sdpa | 0.651 | 0.716 | 0.7 | 3 |
| fwd:block0.attn.proj | 0.209 | 0.238 | 0.2 | 3 |
| fwd:block0.ln2 | 0.073 | 0.090 | 0.1 | 3 |
| fwd:block0.mlp | 0.271 | 0.300 | 0.3 | 3 |
| fwd:block1 | 1.297 | 1.450 | 1.4 | 2 |
| fwd:block1.ln1 | 0.073 | 0.089 | 0.1 | 3 |
| fwd:block1.attn.qkv | 0.208 | 0.233 | 0.2 | 3 |
| fwd:block1.attn.sdpa | 0.516 | 0.557 | 0.6 | 3 |
| fwd:block1.attn.proj | 0.197 | 0.225 | 0.2 | 3 |
| fwd:block1.ln2 | 0.068 | 0.086 | 0.1 | 3 |
| fwd:block1.mlp | 0.261 | 0.292 | 0.3 | 3 |
| fwd:block2 | 1.272 | 1.414 | 1.4 | 2 |
| fwd:block2.ln1 | 0.070 | 0.083 | 0.1 | 3 |
| fwd:block2.attn.qkv | 0.201 | 0.227 | 0.2 | 3 |
| fwd:block2.attn.sdpa | 0.506 | 0.536 | 0.6 | 3 |
| fwd:block2.attn.proj | 0.198 | 0.224 | 0.2 | 3 |
| fwd:block2.ln2 | 0.067 | 0.080 | 0.1 | 3 |
| fwd:block2.mlp | 0.256 | 0.286 | 0.3 | 3 |
| fwd:block3 | 1.253 | 1.358 | 1.4 | 2 |
| fwd:block3.ln1 | 0.069 | 0.091 | 0.1 | 3 |
| fwd:block3.attn.qkv | 0.200 | 0.226 | 0.2 | 3 |
| fwd:block3.attn.sdpa | 0.506 | 0.545 | 0.6 | 3 |
| fwd:block3.attn.proj | 0.194 | 0.216 | 0.2 | 3 |
| fwd:block3.ln2 | 0.068 | 0.080 | 0.1 | 3 |
| fwd:block3.mlp | 0.248 | 0.278 | 0.3 | 3 |
| fwd:block4 | 1.246 | 1.338 | 1.4 | 2 |
| fwd:block4.ln1 | 0.069 | 0.093 | 0.1 | 3 |
| fwd:block4.attn.qkv | 0.198 | 0.220 | 0.2 | 3 |
| fwd:block4.attn.sdpa | 0.498 | 0.537 | 0.6 | 3 |
| fwd:block4.attn.proj | 0.193 | 0.222 | 0.2 | 3 |
| fwd:block4.ln2 | 0.067 | 0.080 | 0.1 | 3 |
| fwd:block4.mlp | 0.255 | 0.287 | 0.3 | 3 |
| fwd:block5 | 1.240 | 1.334 | 1.4 | 2 |
| fwd:block5.ln1 | 0.069 | 0.082 | 0.1 | 3 |
| fwd:block5.attn.qkv | 0.196 | 0.226 | 0.2 | 3 |
| fwd:block5.attn.sdpa | 0.499 | 0.535 | 0.6 | 3 |
| fwd:block5.attn.proj | 0.193 | 0.212 | 0.2 | 3 |
| fwd:block5.ln2 | 0.067 | 0.088 | 0.1 | 3 |
| fwd:block5.mlp | 0.253 | 0.281 | 0.3 | 3 |
| fwd:head+loss | 10.464 | 10.484 | 11.6 | 2 |
| bwd | 23.416 | 25.982 | 26.0 | 1 |
| bwd:head+loss | 12.280 | 12.293 | 13.6 | 2 |
| bwd:stack | 10.809 | 12.786 | 12.0 | 1 |
| bwd:block5 | 1.790 | 1.795 | 2.0 | 2 |
| bwd.invert:block5 | 0.531 | 0.534 | 0.6 | 3 |
| bwd.invert:block5.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block5.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block5.attn.sdpa | 0.285 | 0.287 | 0.3 | 3 |
| bwd.invert:block5.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block5.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block5.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd.recompute:block5 | 0.531 | 0.534 | 0.6 | 3 |
| bwd.recompute:block5.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block5.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block5.attn.sdpa | 0.283 | 0.285 | 0.3 | 3 |
| bwd.recompute:block5.attn.proj | 0.030 | 0.030 | 0.0 | 3 |
| bwd.recompute:block5.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.recompute:block5.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd:block5.grad | 0.823 | 0.826 | 0.9 | 3 |
| bwd:block4 | 1.796 | 1.801 | 2.0 | 2 |
| bwd.invert:block4 | 0.532 | 0.536 | 0.6 | 3 |
| bwd.invert:block4.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block4.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block4.attn.sdpa | 0.285 | 0.287 | 0.3 | 3 |
| bwd.invert:block4.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block4.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.invert:block4.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd.recompute:block4 | 0.536 | 0.539 | 0.6 | 3 |
| bwd.recompute:block4.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block4.attn.qkv | 0.031 | 0.031 | 0.0 | 3 |
| bwd.recompute:block4.attn.sdpa | 0.286 | 0.289 | 0.3 | 3 |
| bwd.recompute:block4.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block4.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block4.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block4.grad | 0.822 | 0.825 | 0.9 | 3 |
| bwd:block3 | 1.792 | 1.796 | 2.0 | 2 |
| bwd.invert:block3 | 0.532 | 0.535 | 0.6 | 3 |
| bwd.invert:block3.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block3.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block3.attn.sdpa | 0.285 | 0.287 | 0.3 | 3 |
| bwd.invert:block3.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block3.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block3.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd.recompute:block3 | 0.535 | 0.538 | 0.6 | 3 |
| bwd.recompute:block3.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block3.attn.qkv | 0.031 | 0.033 | 0.0 | 3 |
| bwd.recompute:block3.attn.sdpa | 0.284 | 0.286 | 0.3 | 3 |
| bwd.recompute:block3.attn.proj | 0.031 | 0.031 | 0.0 | 3 |
| bwd.recompute:block3.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block3.mlp | 0.085 | 0.085 | 0.1 | 3 |
| bwd:block3.grad | 0.822 | 0.825 | 0.9 | 3 |
| bwd:block2 | 1.792 | 1.797 | 2.0 | 2 |
| bwd.invert:block2 | 0.532 | 0.536 | 0.6 | 3 |
| bwd.invert:block2.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block2.attn.qkv | 0.031 | 0.033 | 0.0 | 3 |
| bwd.invert:block2.attn.sdpa | 0.286 | 0.288 | 0.3 | 3 |
| bwd.invert:block2.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block2.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.invert:block2.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd.recompute:block2 | 0.536 | 0.541 | 0.6 | 3 |
| bwd.recompute:block2.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block2.attn.qkv | 0.031 | 0.031 | 0.0 | 3 |
| bwd.recompute:block2.attn.sdpa | 0.287 | 0.290 | 0.3 | 3 |
| bwd.recompute:block2.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block2.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block2.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block2.grad | 0.821 | 0.826 | 0.9 | 3 |
| bwd:block1 | 1.799 | 1.814 | 2.0 | 2 |
| bwd.invert:block1 | 0.535 | 0.537 | 0.6 | 3 |
| bwd.invert:block1.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block1.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block1.attn.sdpa | 0.286 | 0.288 | 0.3 | 3 |
| bwd.invert:block1.attn.proj | 0.031 | 0.033 | 0.0 | 3 |
| bwd.invert:block1.ln2 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block1.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd.recompute:block1 | 0.536 | 0.538 | 0.6 | 3 |
| bwd.recompute:block1.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block1.attn.qkv | 0.031 | 0.033 | 0.0 | 3 |
| bwd.recompute:block1.attn.sdpa | 0.285 | 0.287 | 0.3 | 3 |
| bwd.recompute:block1.attn.proj | 0.031 | 0.031 | 0.0 | 3 |
| bwd.recompute:block1.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.recompute:block1.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd:block1.grad | 0.825 | 1.489 | 0.9 | 3 |
| bwd:block0 | 1.797 | 3.638 | 2.0 | 2 |
| bwd.invert:block0 | 0.535 | 1.759 | 0.6 | 3 |
| bwd.invert:block0.ln1 | 0.022 | 0.083 | 0.0 | 3 |
| bwd.invert:block0.attn.qkv | 0.032 | 0.222 | 0.0 | 3 |
| bwd.invert:block0.attn.sdpa | 0.286 | 0.531 | 0.3 | 3 |
| bwd.invert:block0.attn.proj | 0.030 | 0.210 | 0.0 | 3 |
| bwd.invert:block0.ln2 | 0.019 | 0.072 | 0.0 | 3 |
| bwd.invert:block0.mlp | 0.084 | 0.274 | 0.1 | 3 |
| bwd.recompute:block0 | 1.514 | 1.890 | 1.7 | 3 |
| bwd.recompute:block0.ln1 | 0.020 | 0.090 | 0.0 | 3 |
| bwd.recompute:block0.attn.qkv | 0.082 | 0.250 | 0.1 | 3 |
| bwd.recompute:block0.attn.sdpa | 0.510 | 0.585 | 0.6 | 3 |
| bwd.recompute:block0.attn.proj | 0.203 | 0.232 | 0.2 | 3 |
| bwd.recompute:block0.ln2 | 0.073 | 0.095 | 0.1 | 3 |
| bwd.recompute:block0.mlp | 0.259 | 0.298 | 0.3 | 3 |
| bwd:block0.grad | 2.086 | 2.229 | 2.3 | 3 |
| bwd:embed | 0.318 | 0.887 | 0.4 | 2 |
| opt | 45.488 | 51.422 | 50.5 | 1 |
| opt:opt.clip | 0.409 | 1.852 | 0.5 | 2 |
| opt:opt.polar_muon_adamw | 44.652 | 49.047 | 49.5 | 2 |
| opt:opt.muon | 38.232 | 42.158 | 42.4 | 2 |
| opt:opt.muon.ns | 39.923 | 42.270 | 44.3 | 3 |
| opt:opt.adamw | 6.184 | 6.712 | 6.9 | 2 |
| opt:opt.moe_bias | 0.022 | 0.025 | 0.0 | 3 |
| opt:opt.zero_grad | 0.357 | 0.422 | 0.4 | 3 |

## Time by part type (sum over layers)

| part type | median ms sum | % of step |
| :--- | ---: | ---: |
| opt | 45.488 | 50.5 |
| opt:opt.polar_muon_adamw | 44.652 | 49.5 |
| opt:opt.muon.ns | 39.923 | 44.3 |
| opt:opt.muon | 38.232 | 42.4 |
| bwd | 23.416 | 26.0 |
| fwd | 19.911 | 22.1 |
| bwd:head+loss | 12.280 | 13.6 |
| bwd:stack | 10.809 | 12.0 |
| bwd:block* | 10.766 | 11.9 |
| fwd:head+loss | 10.464 | 11.6 |
| fwd:stack | 8.377 | 9.3 |
| fwd:block* | 7.910 | 8.8 |
| bwd:block*.grad | 6.200 | 6.9 |
| opt:opt.adamw | 6.184 | 6.9 |
| bwd.recompute:block* | 4.187 | 4.6 |
| bwd.invert:block* | 3.198 | 3.5 |
| fwd:block*.attn.sdpa | 3.175 | 3.5 |
| bwd.recompute:block*.attn.sdpa | 1.933 | 2.1 |
| bwd.invert:block*.attn.sdpa | 1.712 | 1.9 |
| fwd:block*.mlp | 1.544 | 1.7 |
| fwd:block*.attn.qkv | 1.288 | 1.4 |
| fwd:block*.attn.proj | 1.183 | 1.3 |
| data | 1.018 | 1.1 |
| fwd:embed | 0.827 | 0.9 |
| fwd:embed.ke | 0.799 | 0.9 |
| bwd.recompute:block*.mlp | 0.681 | 0.8 |
| bwd.invert:block*.mlp | 0.505 | 0.6 |
| fwd:block*.ln1 | 0.451 | 0.5 |
| opt:opt.clip | 0.409 | 0.5 |
| fwd:block*.ln2 | 0.409 | 0.5 |
| opt:opt.zero_grad | 0.357 | 0.4 |
| bwd.recompute:block*.attn.proj | 0.355 | 0.4 |
| bwd:embed | 0.318 | 0.4 |
| bwd.recompute:block*.attn.qkv | 0.237 | 0.3 |
| bwd.invert:block*.attn.qkv | 0.185 | 0.2 |
| bwd.invert:block*.attn.proj | 0.180 | 0.2 |
| bwd.recompute:block*.ln2 | 0.170 | 0.2 |
| bwd.invert:block*.ln1 | 0.124 | 0.1 |
| bwd.recompute:block*.ln1 | 0.123 | 0.1 |
| bwd.invert:block*.ln2 | 0.117 | 0.1 |
| opt:opt.moe_bias | 0.022 | 0.0 |

## Five slowest leaf parts

1. `opt:opt.muon.ns` — 39.923 ms (44.3% of step)
2. `bwd:block0.grad` — 2.086 ms (2.3% of step)
3. `bwd:block1.grad` — 0.825 ms (0.9% of step)
4. `bwd:block5.grad` — 0.823 ms (0.9% of step)
5. `bwd:block4.grad` — 0.822 ms (0.9% of step)
