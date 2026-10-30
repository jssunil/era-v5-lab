# Bench report — pr29_a100n2_normal-run2

**GPU:** NVIDIA A100-SXM4-40GB  |  **dtype:** bf16  |  **B x T:** 16 x 256  |  **torch:** 2.15.0+cu132
**commit:** `dc0b1703d7d0c51b152bd37d81f6fc2b3ddcf64d`  |  **tag:** pr29_a100n2_normal-run2

## Step (clean)

- median: 64.819 ms
- p10..p90: 63.269 .. 67.008 ms
- tokens/s: 63,192
- MFU: 5.0%  |  HFU: 5.6%

## Diagnostics

### CUDA timing-event allocations

- [OK] clean: events_created_during_steps=0
- [OK] layer: events_created_during_steps=0
- [OK] layer.inner_pass: events_created_during_steps=0

### Benchmark warnings

- [warn] 9 gated part(s) have p10..p90 spread > 10%, so may miss the 5% check: data, fwd:embed, fwd:stack, fwd:block0, fwd:block1, fwd:block2 (+3 more)

## Regions

| part | median ms | p90 | % of step | level |
| :--- | ---: | ---: | ---: | ---: |
| data | 0.431 | 0.525 | 0.7 | 1 |
| fwd | 17.126 | 17.650 | 26.4 | 1 |
| fwd:embed | 0.667 | 0.705 | 1.0 | 2 |
| fwd:embed.ke | 0.646 | 0.685 | 1.0 | 3 |
| fwd:stack | 5.847 | 6.321 | 9.0 | 1 |
| fwd:block0 | 1.081 | 1.215 | 1.7 | 2 |
| fwd:block0.ln1 | 0.071 | 0.079 | 0.1 | 3 |
| fwd:block0.attn.qkv | 0.182 | 0.217 | 0.3 | 3 |
| fwd:block0.attn.sdpa | 0.452 | 0.506 | 0.7 | 3 |
| fwd:block0.attn.proj | 0.134 | 0.157 | 0.2 | 3 |
| fwd:block0.ln2 | 0.052 | 0.057 | 0.1 | 3 |
| fwd:block0.mlp | 0.195 | 0.222 | 0.3 | 3 |
| fwd:block1 | 0.920 | 0.983 | 1.4 | 2 |
| fwd:block1.ln1 | 0.052 | 0.057 | 0.1 | 3 |
| fwd:block1.attn.qkv | 0.144 | 0.165 | 0.2 | 3 |
| fwd:block1.attn.sdpa | 0.401 | 0.426 | 0.6 | 3 |
| fwd:block1.attn.proj | 0.105 | 0.134 | 0.2 | 3 |
| fwd:block1.ln2 | 0.050 | 0.053 | 0.1 | 3 |
| fwd:block1.mlp | 0.180 | 0.210 | 0.3 | 3 |
| fwd:block2 | 0.905 | 0.967 | 1.4 | 2 |
| fwd:block2.ln1 | 0.050 | 0.053 | 0.1 | 3 |
| fwd:block2.attn.qkv | 0.142 | 0.167 | 0.2 | 3 |
| fwd:block2.attn.sdpa | 0.395 | 0.418 | 0.6 | 3 |
| fwd:block2.attn.proj | 0.098 | 0.129 | 0.2 | 3 |
| fwd:block2.ln2 | 0.049 | 0.052 | 0.1 | 3 |
| fwd:block2.mlp | 0.179 | 0.207 | 0.3 | 3 |
| fwd:block3 | 0.899 | 0.955 | 1.4 | 2 |
| fwd:block3.ln1 | 0.049 | 0.053 | 0.1 | 3 |
| fwd:block3.attn.qkv | 0.143 | 0.168 | 0.2 | 3 |
| fwd:block3.attn.sdpa | 0.395 | 0.423 | 0.6 | 3 |
| fwd:block3.attn.proj | 0.098 | 0.124 | 0.2 | 3 |
| fwd:block3.ln2 | 0.049 | 0.051 | 0.1 | 3 |
| fwd:block3.mlp | 0.179 | 0.208 | 0.3 | 3 |
| fwd:block4 | 0.897 | 0.941 | 1.4 | 2 |
| fwd:block4.ln1 | 0.050 | 0.060 | 0.1 | 3 |
| fwd:block4.attn.qkv | 0.142 | 0.164 | 0.2 | 3 |
| fwd:block4.attn.sdpa | 0.394 | 0.417 | 0.6 | 3 |
| fwd:block4.attn.proj | 0.098 | 0.126 | 0.2 | 3 |
| fwd:block4.ln2 | 0.049 | 0.060 | 0.1 | 3 |
| fwd:block4.mlp | 0.182 | 0.209 | 0.3 | 3 |
| fwd:block5 | 0.893 | 0.937 | 1.4 | 2 |
| fwd:block5.ln1 | 0.050 | 0.062 | 0.1 | 3 |
| fwd:block5.attn.qkv | 0.140 | 0.164 | 0.2 | 3 |
| fwd:block5.attn.sdpa | 0.393 | 0.417 | 0.6 | 3 |
| fwd:block5.attn.proj | 0.098 | 0.127 | 0.2 | 3 |
| fwd:block5.ln2 | 0.050 | 0.067 | 0.1 | 3 |
| fwd:block5.mlp | 0.181 | 0.207 | 0.3 | 3 |
| fwd:head+loss | 10.476 | 10.489 | 16.2 | 2 |
| bwd | 23.534 | 23.551 | 36.3 | 1 |
| bwd:head+loss | 12.363 | 12.372 | 19.1 | 2 |
| bwd:stack | 10.824 | 10.837 | 16.7 | 1 |
| bwd:block5 | 1.795 | 1.800 | 2.8 | 2 |
| bwd.invert:block5 | 0.539 | 0.541 | 0.8 | 3 |
| bwd.invert:block5.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block5.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block5.attn.sdpa | 0.287 | 0.289 | 0.4 | 3 |
| bwd.invert:block5.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block5.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block5.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd.recompute:block5 | 0.541 | 0.543 | 0.8 | 3 |
| bwd.recompute:block5.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block5.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block5.attn.sdpa | 0.286 | 0.287 | 0.4 | 3 |
| bwd.recompute:block5.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block5.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block5.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd:block5.grad | 0.823 | 0.825 | 1.3 | 3 |
| bwd:block4 | 1.798 | 1.802 | 2.8 | 2 |
| bwd.invert:block4 | 0.540 | 0.542 | 0.8 | 3 |
| bwd.invert:block4.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block4.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block4.attn.sdpa | 0.286 | 0.287 | 0.4 | 3 |
| bwd.invert:block4.attn.proj | 0.031 | 0.031 | 0.0 | 3 |
| bwd.invert:block4.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block4.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd.recompute:block4 | 0.542 | 0.544 | 0.8 | 3 |
| bwd.recompute:block4.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block4.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block4.attn.sdpa | 0.287 | 0.289 | 0.4 | 3 |
| bwd.recompute:block4.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block4.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block4.mlp | 0.085 | 0.087 | 0.1 | 3 |
| bwd:block4.grad | 0.824 | 0.826 | 1.3 | 3 |
| bwd:block3 | 1.792 | 1.796 | 2.8 | 2 |
| bwd.invert:block3 | 0.538 | 0.540 | 0.8 | 3 |
| bwd.invert:block3.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block3.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block3.attn.sdpa | 0.284 | 0.286 | 0.4 | 3 |
| bwd.invert:block3.attn.proj | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block3.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block3.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd.recompute:block3 | 0.541 | 0.543 | 0.8 | 3 |
| bwd.recompute:block3.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block3.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block3.attn.sdpa | 0.284 | 0.285 | 0.4 | 3 |
| bwd.recompute:block3.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block3.ln2 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block3.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block3.grad | 0.823 | 0.826 | 1.3 | 3 |
| bwd:block2 | 1.797 | 1.801 | 2.8 | 2 |
| bwd.invert:block2 | 0.538 | 0.540 | 0.8 | 3 |
| bwd.invert:block2.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block2.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block2.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.invert:block2.attn.proj | 0.031 | 0.031 | 0.0 | 3 |
| bwd.invert:block2.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block2.mlp | 0.084 | 0.084 | 0.1 | 3 |
| bwd.recompute:block2 | 0.542 | 0.545 | 0.8 | 3 |
| bwd.recompute:block2.ln1 | 0.022 | 0.022 | 0.0 | 3 |
| bwd.recompute:block2.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block2.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.recompute:block2.attn.proj | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block2.ln2 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block2.mlp | 0.086 | 0.087 | 0.1 | 3 |
| bwd:block2.grad | 0.826 | 0.828 | 1.3 | 3 |
| bwd:block1 | 1.801 | 1.804 | 2.8 | 2 |
| bwd.invert:block1 | 0.542 | 0.545 | 0.8 | 3 |
| bwd.invert:block1.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block1.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block1.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.invert:block1.attn.proj | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block1.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block1.mlp | 0.086 | 0.087 | 0.1 | 3 |
| bwd.recompute:block1 | 0.543 | 0.547 | 0.8 | 3 |
| bwd.recompute:block1.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block1.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block1.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.recompute:block1.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block1.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block1.mlp | 0.085 | 0.085 | 0.1 | 3 |
| bwd:block1.grad | 0.827 | 0.830 | 1.3 | 3 |
| bwd:block0 | 1.796 | 1.802 | 2.8 | 2 |
| bwd.invert:block0 | 0.539 | 0.542 | 0.8 | 3 |
| bwd.invert:block0.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block0.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block0.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.invert:block0.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block0.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block0.mlp | 0.084 | 0.084 | 0.1 | 3 |
| bwd.recompute:block0 | 0.541 | 0.543 | 0.8 | 3 |
| bwd.recompute:block0.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block0.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block0.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.recompute:block0.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block0.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block0.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block0.grad | 0.826 | 0.829 | 1.3 | 3 |
| bwd:embed | 0.338 | 0.341 | 0.5 | 2 |
| opt | 25.802 | 30.897 | 39.8 | 1 |
| opt:opt.clip | 0.412 | 0.415 | 0.6 | 2 |
| opt:opt.polar_muon_adamw | 25.136 | 30.139 | 38.8 | 2 |
| opt:opt.muon | 19.980 | 24.515 | 30.8 | 2 |
| opt:opt.muon.ns | 23.960 | 26.075 | 37.0 | 3 |
| opt:opt.adamw | 4.922 | 5.204 | 7.6 | 2 |
| opt:opt.moe_bias | 0.015 | 0.016 | 0.0 | 3 |
| opt:opt.zero_grad | 0.224 | 0.269 | 0.3 | 3 |

## Time by part type (sum over layers)

| part type | median ms sum | % of step |
| :--- | ---: | ---: |
| opt | 25.802 | 39.8 |
| opt:opt.polar_muon_adamw | 25.136 | 38.8 |
| opt:opt.muon.ns | 23.960 | 37.0 |
| bwd | 23.534 | 36.3 |
| opt:opt.muon | 19.980 | 30.8 |
| fwd | 17.126 | 26.4 |
| bwd:head+loss | 12.363 | 19.1 |
| bwd:stack | 10.824 | 16.7 |
| bwd:block* | 10.780 | 16.6 |
| fwd:head+loss | 10.476 | 16.2 |
| fwd:stack | 5.847 | 9.0 |
| fwd:block* | 5.594 | 8.6 |
| bwd:block*.grad | 4.951 | 7.6 |
| opt:opt.adamw | 4.922 | 7.6 |
| bwd.recompute:block* | 3.248 | 5.0 |
| bwd.invert:block* | 3.234 | 5.0 |
| fwd:block*.attn.sdpa | 2.431 | 3.8 |
| bwd.recompute:block*.attn.sdpa | 1.712 | 2.6 |
| bwd.invert:block*.attn.sdpa | 1.712 | 2.6 |
| fwd:block*.mlp | 1.097 | 1.7 |
| fwd:block*.attn.qkv | 0.894 | 1.4 |
| fwd:embed | 0.667 | 1.0 |
| fwd:embed.ke | 0.646 | 1.0 |
| fwd:block*.attn.proj | 0.632 | 1.0 |
| bwd.recompute:block*.mlp | 0.510 | 0.8 |
| bwd.invert:block*.mlp | 0.507 | 0.8 |
| data | 0.431 | 0.7 |
| opt:opt.clip | 0.412 | 0.6 |
| bwd:embed | 0.338 | 0.5 |
| fwd:block*.ln1 | 0.323 | 0.5 |
| fwd:block*.ln2 | 0.300 | 0.5 |
| opt:opt.zero_grad | 0.224 | 0.3 |
| bwd.invert:block*.attn.qkv | 0.187 | 0.3 |
| bwd.recompute:block*.attn.qkv | 0.187 | 0.3 |
| bwd.invert:block*.attn.proj | 0.185 | 0.3 |
| bwd.recompute:block*.attn.proj | 0.184 | 0.3 |
| bwd.recompute:block*.ln1 | 0.127 | 0.2 |
| bwd.invert:block*.ln1 | 0.126 | 0.2 |
| bwd.recompute:block*.ln2 | 0.122 | 0.2 |
| bwd.invert:block*.ln2 | 0.120 | 0.2 |
| opt:opt.moe_bias | 0.015 | 0.0 |

## Five slowest leaf parts

1. `opt:opt.muon.ns` — 23.960 ms (37.0% of step)
2. `bwd:block1.grad` — 0.827 ms (1.3% of step)
3. `bwd:block2.grad` — 0.826 ms (1.3% of step)
4. `bwd:block0.grad` — 0.826 ms (1.3% of step)
5. `bwd:block4.grad` — 0.824 ms (1.3% of step)
