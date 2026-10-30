# Bench report — pr29_a100real7_normal-run2

**GPU:** NVIDIA A100-SXM4-40GB  |  **dtype:** bf16  |  **B x T:** 16 x 256  |  **torch:** 2.15.0+cu132
**commit:** `dc0b1703d7d0c51b152bd37d81f6fc2b3ddcf64d`  |  **tag:** pr29_a100real7_normal-run2

## Step (clean)

- median: 68.068 ms
- p10..p90: 65.941 .. 69.778 ms
- tokens/s: 60,175
- MFU: 4.8%  |  HFU: 5.3%

## Diagnostics

### CUDA timing-event allocations

- [OK] clean: events_created_during_steps=0
- [OK] layer: events_created_during_steps=0
- [OK] layer.inner_pass: events_created_during_steps=0

### Benchmark warnings

- [warn] recorder overhead 2.1% > 2.0%: layer numbers are flagged
- [warn] 5 gated part(s) have p10..p90 spread > 10%, so may miss the 5% check: data, fwd:block2, opt, opt:opt.polar_muon_adamw, opt:opt.muon

## Regions

| part | median ms | p90 | % of step | level |
| :--- | ---: | ---: | ---: | ---: |
| data | 0.778 | 0.853 | 1.1 | 1 |
| fwd | 17.506 | 17.812 | 25.7 | 1 |
| fwd:embed | 0.705 | 0.739 | 1.0 | 2 |
| fwd:embed.ke | 0.658 | 0.687 | 1.0 | 3 |
| fwd:stack | 6.207 | 6.492 | 9.1 | 1 |
| fwd:block0 | 1.183 | 1.243 | 1.7 | 2 |
| fwd:block0.ln1 | 0.070 | 0.079 | 0.1 | 3 |
| fwd:block0.attn.qkv | 0.196 | 0.225 | 0.3 | 3 |
| fwd:block0.attn.sdpa | 0.465 | 0.505 | 0.7 | 3 |
| fwd:block0.attn.proj | 0.135 | 0.155 | 0.2 | 3 |
| fwd:block0.ln2 | 0.053 | 0.069 | 0.1 | 3 |
| fwd:block0.mlp | 0.200 | 0.221 | 0.3 | 3 |
| fwd:block1 | 0.962 | 1.025 | 1.4 | 2 |
| fwd:block1.ln1 | 0.052 | 0.057 | 0.1 | 3 |
| fwd:block1.attn.qkv | 0.147 | 0.165 | 0.2 | 3 |
| fwd:block1.attn.sdpa | 0.402 | 0.427 | 0.6 | 3 |
| fwd:block1.attn.proj | 0.115 | 0.136 | 0.2 | 3 |
| fwd:block1.ln2 | 0.051 | 0.057 | 0.1 | 3 |
| fwd:block1.mlp | 0.186 | 0.218 | 0.3 | 3 |
| fwd:block2 | 0.943 | 1.018 | 1.4 | 2 |
| fwd:block2.ln1 | 0.051 | 0.055 | 0.1 | 3 |
| fwd:block2.attn.qkv | 0.145 | 0.167 | 0.2 | 3 |
| fwd:block2.attn.sdpa | 0.399 | 0.422 | 0.6 | 3 |
| fwd:block2.attn.proj | 0.110 | 0.134 | 0.2 | 3 |
| fwd:block2.ln2 | 0.050 | 0.052 | 0.1 | 3 |
| fwd:block2.mlp | 0.184 | 0.208 | 0.3 | 3 |
| fwd:block3 | 0.934 | 0.977 | 1.4 | 2 |
| fwd:block3.ln1 | 0.050 | 0.052 | 0.1 | 3 |
| fwd:block3.attn.qkv | 0.144 | 0.166 | 0.2 | 3 |
| fwd:block3.attn.sdpa | 0.397 | 0.421 | 0.6 | 3 |
| fwd:block3.attn.proj | 0.105 | 0.130 | 0.2 | 3 |
| fwd:block3.ln2 | 0.050 | 0.052 | 0.1 | 3 |
| fwd:block3.mlp | 0.182 | 0.210 | 0.3 | 3 |
| fwd:block4 | 0.933 | 0.967 | 1.4 | 2 |
| fwd:block4.ln1 | 0.050 | 0.056 | 0.1 | 3 |
| fwd:block4.attn.qkv | 0.145 | 0.171 | 0.2 | 3 |
| fwd:block4.attn.sdpa | 0.396 | 0.419 | 0.6 | 3 |
| fwd:block4.attn.proj | 0.104 | 0.131 | 0.2 | 3 |
| fwd:block4.ln2 | 0.050 | 0.053 | 0.1 | 3 |
| fwd:block4.mlp | 0.185 | 0.208 | 0.3 | 3 |
| fwd:block5 | 0.925 | 0.951 | 1.4 | 2 |
| fwd:block5.ln1 | 0.050 | 0.065 | 0.1 | 3 |
| fwd:block5.attn.qkv | 0.143 | 0.167 | 0.2 | 3 |
| fwd:block5.attn.sdpa | 0.395 | 0.420 | 0.6 | 3 |
| fwd:block5.attn.proj | 0.103 | 0.132 | 0.2 | 3 |
| fwd:block5.ln2 | 0.050 | 0.055 | 0.1 | 3 |
| fwd:block5.mlp | 0.184 | 0.211 | 0.3 | 3 |
| fwd:head+loss | 10.437 | 10.450 | 15.3 | 2 |
| bwd | 23.405 | 23.418 | 34.4 | 1 |
| bwd:head+loss | 12.281 | 12.296 | 18.0 | 2 |
| bwd:stack | 10.794 | 10.806 | 15.9 | 1 |
| bwd:block5 | 1.789 | 1.794 | 2.6 | 2 |
| bwd.invert:block5 | 0.538 | 0.548 | 0.8 | 3 |
| bwd.invert:block5.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block5.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block5.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.invert:block5.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block5.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block5.mlp | 0.084 | 0.086 | 0.1 | 3 |
| bwd.recompute:block5 | 0.539 | 0.547 | 0.8 | 3 |
| bwd.recompute:block5.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block5.attn.qkv | 0.033 | 0.034 | 0.0 | 3 |
| bwd.recompute:block5.attn.sdpa | 0.284 | 0.286 | 0.4 | 3 |
| bwd.recompute:block5.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block5.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block5.mlp | 0.085 | 0.085 | 0.1 | 3 |
| bwd:block5.grad | 0.822 | 0.826 | 1.2 | 3 |
| bwd:block4 | 1.795 | 1.801 | 2.6 | 2 |
| bwd.invert:block4 | 0.539 | 0.546 | 0.8 | 3 |
| bwd.invert:block4.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block4.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block4.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.invert:block4.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block4.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block4.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd.recompute:block4 | 0.542 | 0.551 | 0.8 | 3 |
| bwd.recompute:block4.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block4.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block4.attn.sdpa | 0.286 | 0.290 | 0.4 | 3 |
| bwd.recompute:block4.attn.proj | 0.031 | 0.033 | 0.0 | 3 |
| bwd.recompute:block4.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block4.mlp | 0.086 | 0.087 | 0.1 | 3 |
| bwd:block4.grad | 0.821 | 0.826 | 1.2 | 3 |
| bwd:block3 | 1.791 | 1.795 | 2.6 | 2 |
| bwd.invert:block3 | 0.538 | 0.546 | 0.8 | 3 |
| bwd.invert:block3.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block3.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block3.attn.sdpa | 0.285 | 0.288 | 0.4 | 3 |
| bwd.invert:block3.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block3.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block3.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd.recompute:block3 | 0.539 | 0.545 | 0.8 | 3 |
| bwd.recompute:block3.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block3.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block3.attn.sdpa | 0.284 | 0.286 | 0.4 | 3 |
| bwd.recompute:block3.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block3.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block3.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block3.grad | 0.822 | 0.826 | 1.2 | 3 |
| bwd:block2 | 1.787 | 1.794 | 2.6 | 2 |
| bwd.invert:block2 | 0.539 | 0.548 | 0.8 | 3 |
| bwd.invert:block2.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block2.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block2.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.invert:block2.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block2.ln2 | 0.019 | 0.021 | 0.0 | 3 |
| bwd.invert:block2.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd.recompute:block2 | 0.542 | 0.551 | 0.8 | 3 |
| bwd.recompute:block2.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block2.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block2.attn.sdpa | 0.287 | 0.290 | 0.4 | 3 |
| bwd.recompute:block2.attn.proj | 0.031 | 0.033 | 0.0 | 3 |
| bwd.recompute:block2.ln2 | 0.020 | 0.023 | 0.0 | 3 |
| bwd.recompute:block2.mlp | 0.085 | 0.087 | 0.1 | 3 |
| bwd:block2.grad | 0.819 | 0.823 | 1.2 | 3 |
| bwd:block1 | 1.797 | 1.802 | 2.6 | 2 |
| bwd.invert:block1 | 0.543 | 0.554 | 0.8 | 3 |
| bwd.invert:block1.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block1.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block1.attn.sdpa | 0.286 | 0.289 | 0.4 | 3 |
| bwd.invert:block1.attn.proj | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block1.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block1.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd.recompute:block1 | 0.542 | 0.555 | 0.8 | 3 |
| bwd.recompute:block1.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block1.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block1.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.recompute:block1.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block1.ln2 | 0.019 | 0.022 | 0.0 | 3 |
| bwd.recompute:block1.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block1.grad | 0.823 | 0.829 | 1.2 | 3 |
| bwd:block0 | 1.791 | 1.796 | 2.6 | 2 |
| bwd.invert:block0 | 0.539 | 0.549 | 0.8 | 3 |
| bwd.invert:block0.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block0.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block0.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.invert:block0.attn.proj | 0.029 | 0.030 | 0.0 | 3 |
| bwd.invert:block0.ln2 | 0.019 | 0.022 | 0.0 | 3 |
| bwd.invert:block0.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd.recompute:block0 | 0.540 | 0.550 | 0.8 | 3 |
| bwd.recompute:block0.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block0.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block0.attn.sdpa | 0.287 | 0.289 | 0.4 | 3 |
| bwd.recompute:block0.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block0.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block0.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block0.grad | 0.821 | 0.825 | 1.2 | 3 |
| bwd:embed | 0.317 | 0.321 | 0.5 | 2 |
| opt | 28.775 | 30.708 | 42.3 | 1 |
| opt:opt.clip | 0.410 | 0.415 | 0.6 | 2 |
| opt:opt.polar_muon_adamw | 28.050 | 30.003 | 41.2 | 2 |
| opt:opt.muon | 22.745 | 24.649 | 33.4 | 2 |
| opt:opt.muon.ns | 25.444 | 27.058 | 37.4 | 3 |
| opt:opt.adamw | 5.161 | 5.272 | 7.6 | 2 |
| opt:opt.moe_bias | 0.014 | 0.015 | 0.0 | 3 |
| opt:opt.zero_grad | 0.249 | 0.290 | 0.4 | 3 |

## Time by part type (sum over layers)

| part type | median ms sum | % of step |
| :--- | ---: | ---: |
| opt | 28.775 | 42.3 |
| opt:opt.polar_muon_adamw | 28.050 | 41.2 |
| opt:opt.muon.ns | 25.444 | 37.4 |
| bwd | 23.405 | 34.4 |
| opt:opt.muon | 22.745 | 33.4 |
| fwd | 17.506 | 25.7 |
| bwd:head+loss | 12.281 | 18.0 |
| bwd:stack | 10.794 | 15.9 |
| bwd:block* | 10.749 | 15.8 |
| fwd:head+loss | 10.437 | 15.3 |
| fwd:stack | 6.207 | 9.1 |
| fwd:block* | 5.879 | 8.6 |
| opt:opt.adamw | 5.161 | 7.6 |
| bwd:block*.grad | 4.929 | 7.2 |
| bwd.recompute:block* | 3.242 | 4.8 |
| bwd.invert:block* | 3.234 | 4.8 |
| fwd:block*.attn.sdpa | 2.456 | 3.6 |
| bwd.invert:block*.attn.sdpa | 1.713 | 2.5 |
| bwd.recompute:block*.attn.sdpa | 1.713 | 2.5 |
| fwd:block*.mlp | 1.122 | 1.6 |
| fwd:block*.attn.qkv | 0.921 | 1.4 |
| data | 0.778 | 1.1 |
| fwd:embed | 0.705 | 1.0 |
| fwd:block*.attn.proj | 0.672 | 1.0 |
| fwd:embed.ke | 0.658 | 1.0 |
| bwd.recompute:block*.mlp | 0.511 | 0.8 |
| bwd.invert:block*.mlp | 0.504 | 0.7 |
| opt:opt.clip | 0.410 | 0.6 |
| fwd:block*.ln1 | 0.324 | 0.5 |
| bwd:embed | 0.317 | 0.5 |
| fwd:block*.ln2 | 0.305 | 0.4 |
| opt:opt.zero_grad | 0.249 | 0.4 |
| bwd.invert:block*.attn.qkv | 0.189 | 0.3 |
| bwd.recompute:block*.attn.qkv | 0.188 | 0.3 |
| bwd.invert:block*.attn.proj | 0.181 | 0.3 |
| bwd.recompute:block*.attn.proj | 0.180 | 0.3 |
| bwd.invert:block*.ln1 | 0.126 | 0.2 |
| bwd.recompute:block*.ln1 | 0.126 | 0.2 |
| bwd.invert:block*.ln2 | 0.120 | 0.2 |
| bwd.recompute:block*.ln2 | 0.120 | 0.2 |
| opt:opt.moe_bias | 0.014 | 0.0 |

## Five slowest leaf parts

1. `opt:opt.muon.ns` — 25.444 ms (37.4% of step)
2. `bwd:block1.grad` — 0.823 ms (1.2% of step)
3. `bwd:block5.grad` — 0.822 ms (1.2% of step)
4. `bwd:block3.grad` — 0.822 ms (1.2% of step)
5. `bwd:block4.grad` — 0.821 ms (1.2% of step)
