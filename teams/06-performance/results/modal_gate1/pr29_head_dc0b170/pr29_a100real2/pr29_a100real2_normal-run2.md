# Bench report — pr29_a100real2_normal-run2

**GPU:** NVIDIA A100-SXM4-40GB  |  **dtype:** bf16  |  **B x T:** 16 x 256  |  **torch:** 2.15.0+cu132
**commit:** `dc0b1703d7d0c51b152bd37d81f6fc2b3ddcf64d`  |  **tag:** pr29_a100real2_normal-run2

## Step (clean)

- median: 64.770 ms
- p10..p90: 63.634 .. 67.118 ms
- tokens/s: 63,240
- MFU: 5.0%  |  HFU: 5.6%

## Diagnostics

### CUDA timing-event allocations

- [OK] clean: events_created_during_steps=0
- [OK] layer: events_created_during_steps=0
- [OK] layer.inner_pass: events_created_during_steps=0

### Benchmark warnings

- [warn] recorder overhead 2.0% > 2.0%: layer numbers are flagged
- [warn] 4 gated part(s) have p10..p90 spread > 10%, so may miss the 5% check: data, fwd:embed, fwd:block0, opt:opt.muon

## Regions

| part | median ms | p90 | % of step | level |
| :--- | ---: | ---: | ---: | ---: |
| data | 0.551 | 0.726 | 0.9 | 1 |
| fwd | 16.779 | 17.113 | 25.9 | 1 |
| fwd:embed | 0.631 | 0.672 | 1.0 | 2 |
| fwd:embed.ke | 0.610 | 0.676 | 0.9 | 3 |
| fwd:stack | 5.578 | 5.828 | 8.6 | 1 |
| fwd:block0 | 0.901 | 1.073 | 1.4 | 2 |
| fwd:block0.ln1 | 0.055 | 0.076 | 0.1 | 3 |
| fwd:block0.attn.qkv | 0.169 | 0.196 | 0.3 | 3 |
| fwd:block0.attn.sdpa | 0.420 | 0.479 | 0.6 | 3 |
| fwd:block0.attn.proj | 0.119 | 0.144 | 0.2 | 3 |
| fwd:block0.ln2 | 0.050 | 0.055 | 0.1 | 3 |
| fwd:block0.mlp | 0.184 | 0.206 | 0.3 | 3 |
| fwd:block1 | 0.897 | 0.920 | 1.4 | 2 |
| fwd:block1.ln1 | 0.050 | 0.053 | 0.1 | 3 |
| fwd:block1.attn.qkv | 0.139 | 0.161 | 0.2 | 3 |
| fwd:block1.attn.sdpa | 0.392 | 0.414 | 0.6 | 3 |
| fwd:block1.attn.proj | 0.105 | 0.128 | 0.2 | 3 |
| fwd:block1.ln2 | 0.049 | 0.051 | 0.1 | 3 |
| fwd:block1.mlp | 0.180 | 0.203 | 0.3 | 3 |
| fwd:block2 | 0.888 | 0.914 | 1.4 | 2 |
| fwd:block2.ln1 | 0.049 | 0.052 | 0.1 | 3 |
| fwd:block2.attn.qkv | 0.138 | 0.147 | 0.2 | 3 |
| fwd:block2.attn.sdpa | 0.391 | 0.416 | 0.6 | 3 |
| fwd:block2.attn.proj | 0.101 | 0.121 | 0.2 | 3 |
| fwd:block2.ln2 | 0.048 | 0.050 | 0.1 | 3 |
| fwd:block2.mlp | 0.179 | 0.204 | 0.3 | 3 |
| fwd:block3 | 0.885 | 0.905 | 1.4 | 2 |
| fwd:block3.ln1 | 0.048 | 0.051 | 0.1 | 3 |
| fwd:block3.attn.qkv | 0.139 | 0.165 | 0.2 | 3 |
| fwd:block3.attn.sdpa | 0.390 | 0.413 | 0.6 | 3 |
| fwd:block3.attn.proj | 0.101 | 0.123 | 0.2 | 3 |
| fwd:block3.ln2 | 0.049 | 0.051 | 0.1 | 3 |
| fwd:block3.mlp | 0.176 | 0.200 | 0.3 | 3 |
| fwd:block4 | 0.887 | 0.907 | 1.4 | 2 |
| fwd:block4.ln1 | 0.048 | 0.053 | 0.1 | 3 |
| fwd:block4.attn.qkv | 0.138 | 0.158 | 0.2 | 3 |
| fwd:block4.attn.sdpa | 0.389 | 0.412 | 0.6 | 3 |
| fwd:block4.attn.proj | 0.101 | 0.123 | 0.2 | 3 |
| fwd:block4.ln2 | 0.049 | 0.050 | 0.1 | 3 |
| fwd:block4.mlp | 0.177 | 0.207 | 0.3 | 3 |
| fwd:block5 | 0.884 | 0.905 | 1.4 | 2 |
| fwd:block5.ln1 | 0.049 | 0.053 | 0.1 | 3 |
| fwd:block5.attn.qkv | 0.138 | 0.159 | 0.2 | 3 |
| fwd:block5.attn.sdpa | 0.390 | 0.411 | 0.6 | 3 |
| fwd:block5.attn.proj | 0.098 | 0.124 | 0.2 | 3 |
| fwd:block5.ln2 | 0.049 | 0.051 | 0.1 | 3 |
| fwd:block5.mlp | 0.178 | 0.204 | 0.3 | 3 |
| fwd:head+loss | 10.481 | 10.492 | 16.2 | 2 |
| bwd | 23.539 | 23.558 | 36.3 | 1 |
| bwd:head+loss | 12.398 | 12.407 | 19.1 | 2 |
| bwd:stack | 10.812 | 10.827 | 16.7 | 1 |
| bwd:block5 | 1.791 | 1.794 | 2.8 | 2 |
| bwd.invert:block5 | 0.538 | 0.541 | 0.8 | 3 |
| bwd.invert:block5.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block5.attn.qkv | 0.032 | 0.032 | 0.0 | 3 |
| bwd.invert:block5.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.invert:block5.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block5.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block5.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd.recompute:block5 | 0.537 | 0.539 | 0.8 | 3 |
| bwd.recompute:block5.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block5.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block5.attn.sdpa | 0.284 | 0.286 | 0.4 | 3 |
| bwd.recompute:block5.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block5.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block5.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd:block5.grad | 0.824 | 0.826 | 1.3 | 3 |
| bwd:block4 | 1.797 | 1.801 | 2.8 | 2 |
| bwd.invert:block4 | 0.540 | 0.543 | 0.8 | 3 |
| bwd.invert:block4.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block4.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block4.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.invert:block4.attn.proj | 0.031 | 0.031 | 0.0 | 3 |
| bwd.invert:block4.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.invert:block4.mlp | 0.085 | 0.085 | 0.1 | 3 |
| bwd.recompute:block4 | 0.541 | 0.544 | 0.8 | 3 |
| bwd.recompute:block4.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block4.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block4.attn.sdpa | 0.287 | 0.289 | 0.4 | 3 |
| bwd.recompute:block4.attn.proj | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block4.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block4.mlp | 0.085 | 0.087 | 0.1 | 3 |
| bwd:block4.grad | 0.823 | 0.826 | 1.3 | 3 |
| bwd:block3 | 1.793 | 1.796 | 2.8 | 2 |
| bwd.invert:block3 | 0.538 | 0.541 | 0.8 | 3 |
| bwd.invert:block3.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block3.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block3.attn.sdpa | 0.285 | 0.288 | 0.4 | 3 |
| bwd.invert:block3.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block3.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block3.mlp | 0.084 | 0.086 | 0.1 | 3 |
| bwd.recompute:block3 | 0.540 | 0.543 | 0.8 | 3 |
| bwd.recompute:block3.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block3.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block3.attn.sdpa | 0.284 | 0.286 | 0.4 | 3 |
| bwd.recompute:block3.attn.proj | 0.031 | 0.031 | 0.0 | 3 |
| bwd.recompute:block3.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block3.mlp | 0.085 | 0.085 | 0.1 | 3 |
| bwd:block3.grad | 0.823 | 0.826 | 1.3 | 3 |
| bwd:block2 | 1.792 | 1.796 | 2.8 | 2 |
| bwd.invert:block2 | 0.539 | 0.542 | 0.8 | 3 |
| bwd.invert:block2.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block2.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block2.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.invert:block2.attn.proj | 0.031 | 0.031 | 0.0 | 3 |
| bwd.invert:block2.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block2.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd.recompute:block2 | 0.542 | 0.544 | 0.8 | 3 |
| bwd.recompute:block2.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block2.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block2.attn.sdpa | 0.287 | 0.289 | 0.4 | 3 |
| bwd.recompute:block2.attn.proj | 0.031 | 0.033 | 0.0 | 3 |
| bwd.recompute:block2.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block2.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block2.grad | 0.822 | 0.825 | 1.3 | 3 |
| bwd:block1 | 1.800 | 1.804 | 2.8 | 2 |
| bwd.invert:block1 | 0.542 | 0.545 | 0.8 | 3 |
| bwd.invert:block1.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block1.attn.qkv | 0.032 | 0.032 | 0.0 | 3 |
| bwd.invert:block1.attn.sdpa | 0.286 | 0.289 | 0.4 | 3 |
| bwd.invert:block1.attn.proj | 0.033 | 0.033 | 0.1 | 3 |
| bwd.invert:block1.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block1.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd.recompute:block1 | 0.541 | 0.544 | 0.8 | 3 |
| bwd.recompute:block1.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block1.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block1.attn.sdpa | 0.286 | 0.287 | 0.4 | 3 |
| bwd.recompute:block1.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block1.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block1.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd:block1.grad | 0.826 | 0.829 | 1.3 | 3 |
| bwd:block0 | 1.796 | 1.801 | 2.8 | 2 |
| bwd.invert:block0 | 0.539 | 0.542 | 0.8 | 3 |
| bwd.invert:block0.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block0.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block0.attn.sdpa | 0.285 | 0.288 | 0.4 | 3 |
| bwd.invert:block0.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block0.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block0.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd.recompute:block0 | 0.540 | 0.543 | 0.8 | 3 |
| bwd.recompute:block0.ln1 | 0.020 | 0.021 | 0.0 | 3 |
| bwd.recompute:block0.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block0.attn.sdpa | 0.287 | 0.289 | 0.4 | 3 |
| bwd.recompute:block0.attn.proj | 0.030 | 0.032 | 0.0 | 3 |
| bwd.recompute:block0.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block0.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block0.grad | 0.825 | 0.828 | 1.3 | 3 |
| bwd:embed | 0.319 | 0.321 | 0.5 | 2 |
| opt | 24.634 | 25.998 | 38.0 | 1 |
| opt:opt.clip | 0.409 | 0.412 | 0.6 | 2 |
| opt:opt.polar_muon_adamw | 24.022 | 25.355 | 37.1 | 2 |
| opt:opt.muon | 19.007 | 20.279 | 29.3 | 2 |
| opt:opt.muon.ns | 23.079 | 24.701 | 35.6 | 3 |
| opt:opt.adamw | 4.936 | 5.022 | 7.6 | 2 |
| opt:opt.moe_bias | 0.013 | 0.016 | 0.0 | 3 |
| opt:opt.zero_grad | 0.177 | 0.264 | 0.3 | 3 |

## Time by part type (sum over layers)

| part type | median ms sum | % of step |
| :--- | ---: | ---: |
| opt | 24.634 | 38.0 |
| opt:opt.polar_muon_adamw | 24.022 | 37.1 |
| bwd | 23.539 | 36.3 |
| opt:opt.muon.ns | 23.079 | 35.6 |
| opt:opt.muon | 19.007 | 29.3 |
| fwd | 16.779 | 25.9 |
| bwd:head+loss | 12.398 | 19.1 |
| bwd:stack | 10.812 | 16.7 |
| bwd:block* | 10.769 | 16.6 |
| fwd:head+loss | 10.481 | 16.2 |
| fwd:stack | 5.578 | 8.6 |
| fwd:block* | 5.342 | 8.2 |
| bwd:block*.grad | 4.945 | 7.6 |
| opt:opt.adamw | 4.936 | 7.6 |
| bwd.recompute:block* | 3.239 | 5.0 |
| bwd.invert:block* | 3.234 | 5.0 |
| fwd:block*.attn.sdpa | 2.373 | 3.7 |
| bwd.invert:block*.attn.sdpa | 1.714 | 2.6 |
| bwd.recompute:block*.attn.sdpa | 1.713 | 2.6 |
| fwd:block*.mlp | 1.074 | 1.7 |
| fwd:block*.attn.qkv | 0.863 | 1.3 |
| fwd:embed | 0.631 | 1.0 |
| fwd:block*.attn.proj | 0.626 | 1.0 |
| fwd:embed.ke | 0.610 | 0.9 |
| data | 0.551 | 0.9 |
| bwd.recompute:block*.mlp | 0.508 | 0.8 |
| bwd.invert:block*.mlp | 0.504 | 0.8 |
| opt:opt.clip | 0.409 | 0.6 |
| bwd:embed | 0.319 | 0.5 |
| fwd:block*.ln1 | 0.300 | 0.5 |
| fwd:block*.ln2 | 0.295 | 0.5 |
| bwd.invert:block*.attn.qkv | 0.189 | 0.3 |
| bwd.recompute:block*.attn.qkv | 0.187 | 0.3 |
| bwd.invert:block*.attn.proj | 0.185 | 0.3 |
| bwd.recompute:block*.attn.proj | 0.183 | 0.3 |
| opt:opt.zero_grad | 0.177 | 0.3 |
| bwd.invert:block*.ln1 | 0.126 | 0.2 |
| bwd.recompute:block*.ln1 | 0.126 | 0.2 |
| bwd.invert:block*.ln2 | 0.120 | 0.2 |
| bwd.recompute:block*.ln2 | 0.120 | 0.2 |
| opt:opt.moe_bias | 0.013 | 0.0 |

## Five slowest leaf parts

1. `opt:opt.muon.ns` — 23.079 ms (35.6% of step)
2. `bwd:block1.grad` — 0.826 ms (1.3% of step)
3. `bwd:block0.grad` — 0.825 ms (1.3% of step)
4. `bwd:block5.grad` — 0.824 ms (1.3% of step)
5. `bwd:block4.grad` — 0.823 ms (1.3% of step)
