# Bench report — pr29_a100real7_normal

**GPU:** NVIDIA A100-SXM4-40GB  |  **dtype:** bf16  |  **B x T:** 16 x 256  |  **torch:** 2.15.0+cu132
**commit:** `dc0b1703d7d0c51b152bd37d81f6fc2b3ddcf64d`  |  **tag:** pr29_a100real7_normal

## Step (clean)

- median: 68.200 ms
- p10..p90: 66.477 .. 69.949 ms
- tokens/s: 60,059
- MFU: 4.8%  |  HFU: 5.3%

## Diagnostics

### CUDA timing-event allocations

- [OK] clean: events_created_during_steps=0
- [OK] layer: events_created_during_steps=0
- [OK] layer.inner_pass: events_created_during_steps=0

### Benchmark warnings

- [warn] recorder overhead 2.1% > 2.0%: layer numbers are flagged
- [warn] 7 gated part(s) have p10..p90 spread > 10%, so may miss the 5% check: data, fwd:embed, fwd:block0, fwd:block1, opt, opt:opt.polar_muon_adamw (+1 more)

## Regions

| part | median ms | p90 | % of step | level |
| :--- | ---: | ---: | ---: | ---: |
| data | 0.767 | 0.885 | 1.1 | 1 |
| fwd | 17.458 | 17.764 | 25.6 | 1 |
| fwd:embed | 0.697 | 0.743 | 1.0 | 2 |
| fwd:embed.ke | 0.657 | 0.695 | 1.0 | 3 |
| fwd:stack | 6.164 | 6.467 | 9.0 | 1 |
| fwd:block0 | 1.171 | 1.292 | 1.7 | 2 |
| fwd:block0.ln1 | 0.068 | 0.088 | 0.1 | 3 |
| fwd:block0.attn.qkv | 0.191 | 0.227 | 0.3 | 3 |
| fwd:block0.attn.sdpa | 0.466 | 0.520 | 0.7 | 3 |
| fwd:block0.attn.proj | 0.138 | 0.165 | 0.2 | 3 |
| fwd:block0.ln2 | 0.052 | 0.063 | 0.1 | 3 |
| fwd:block0.mlp | 0.197 | 0.236 | 0.3 | 3 |
| fwd:block1 | 0.949 | 1.045 | 1.4 | 2 |
| fwd:block1.ln1 | 0.052 | 0.063 | 0.1 | 3 |
| fwd:block1.attn.qkv | 0.144 | 0.170 | 0.2 | 3 |
| fwd:block1.attn.sdpa | 0.404 | 0.431 | 0.6 | 3 |
| fwd:block1.attn.proj | 0.111 | 0.139 | 0.2 | 3 |
| fwd:block1.ln2 | 0.050 | 0.060 | 0.1 | 3 |
| fwd:block1.mlp | 0.184 | 0.215 | 0.3 | 3 |
| fwd:block2 | 0.935 | 0.992 | 1.4 | 2 |
| fwd:block2.ln1 | 0.049 | 0.060 | 0.1 | 3 |
| fwd:block2.attn.qkv | 0.142 | 0.173 | 0.2 | 3 |
| fwd:block2.attn.sdpa | 0.396 | 0.427 | 0.6 | 3 |
| fwd:block2.attn.proj | 0.108 | 0.140 | 0.2 | 3 |
| fwd:block2.ln2 | 0.049 | 0.056 | 0.1 | 3 |
| fwd:block2.mlp | 0.182 | 0.211 | 0.3 | 3 |
| fwd:block3 | 0.921 | 0.989 | 1.4 | 2 |
| fwd:block3.ln1 | 0.049 | 0.059 | 0.1 | 3 |
| fwd:block3.attn.qkv | 0.143 | 0.166 | 0.2 | 3 |
| fwd:block3.attn.sdpa | 0.396 | 0.429 | 0.6 | 3 |
| fwd:block3.attn.proj | 0.103 | 0.135 | 0.2 | 3 |
| fwd:block3.ln2 | 0.049 | 0.058 | 0.1 | 3 |
| fwd:block3.mlp | 0.181 | 0.209 | 0.3 | 3 |
| fwd:block4 | 0.921 | 0.957 | 1.3 | 2 |
| fwd:block4.ln1 | 0.049 | 0.058 | 0.1 | 3 |
| fwd:block4.attn.qkv | 0.142 | 0.172 | 0.2 | 3 |
| fwd:block4.attn.sdpa | 0.394 | 0.427 | 0.6 | 3 |
| fwd:block4.attn.proj | 0.102 | 0.135 | 0.2 | 3 |
| fwd:block4.ln2 | 0.049 | 0.058 | 0.1 | 3 |
| fwd:block4.mlp | 0.183 | 0.212 | 0.3 | 3 |
| fwd:block5 | 0.919 | 0.977 | 1.3 | 2 |
| fwd:block5.ln1 | 0.049 | 0.054 | 0.1 | 3 |
| fwd:block5.attn.qkv | 0.141 | 0.168 | 0.2 | 3 |
| fwd:block5.attn.sdpa | 0.394 | 0.420 | 0.6 | 3 |
| fwd:block5.attn.proj | 0.102 | 0.136 | 0.2 | 3 |
| fwd:block5.ln2 | 0.049 | 0.057 | 0.1 | 3 |
| fwd:block5.mlp | 0.181 | 0.212 | 0.3 | 3 |
| fwd:head+loss | 10.437 | 10.448 | 15.3 | 2 |
| bwd | 23.365 | 23.389 | 34.3 | 1 |
| bwd:head+loss | 12.279 | 12.291 | 18.0 | 2 |
| bwd:stack | 10.760 | 10.781 | 15.8 | 1 |
| bwd:block5 | 1.780 | 1.785 | 2.6 | 2 |
| bwd.invert:block5 | 0.536 | 0.542 | 0.8 | 3 |
| bwd.invert:block5.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block5.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block5.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.invert:block5.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block5.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block5.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd.recompute:block5 | 0.535 | 0.545 | 0.8 | 3 |
| bwd.recompute:block5.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block5.attn.qkv | 0.031 | 0.033 | 0.0 | 3 |
| bwd.recompute:block5.attn.sdpa | 0.283 | 0.285 | 0.4 | 3 |
| bwd.recompute:block5.attn.proj | 0.029 | 0.030 | 0.0 | 3 |
| bwd.recompute:block5.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block5.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd:block5.grad | 0.818 | 0.823 | 1.2 | 3 |
| bwd:block4 | 1.789 | 1.797 | 2.6 | 2 |
| bwd.invert:block4 | 0.537 | 0.544 | 0.8 | 3 |
| bwd.invert:block4.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block4.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block4.attn.sdpa | 0.285 | 0.288 | 0.4 | 3 |
| bwd.invert:block4.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block4.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block4.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd.recompute:block4 | 0.540 | 0.548 | 0.8 | 3 |
| bwd.recompute:block4.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block4.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block4.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.recompute:block4.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block4.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block4.mlp | 0.085 | 0.087 | 0.1 | 3 |
| bwd:block4.grad | 0.819 | 0.823 | 1.2 | 3 |
| bwd:block3 | 1.783 | 1.788 | 2.6 | 2 |
| bwd.invert:block3 | 0.536 | 0.547 | 0.8 | 3 |
| bwd.invert:block3.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block3.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block3.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.invert:block3.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block3.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block3.mlp | 0.084 | 0.086 | 0.1 | 3 |
| bwd.recompute:block3 | 0.539 | 0.549 | 0.8 | 3 |
| bwd.recompute:block3.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block3.attn.qkv | 0.032 | 0.034 | 0.0 | 3 |
| bwd.recompute:block3.attn.sdpa | 0.284 | 0.286 | 0.4 | 3 |
| bwd.recompute:block3.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block3.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block3.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block3.grad | 0.819 | 0.823 | 1.2 | 3 |
| bwd:block2 | 1.784 | 1.790 | 2.6 | 2 |
| bwd.invert:block2 | 0.537 | 0.544 | 0.8 | 3 |
| bwd.invert:block2.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block2.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block2.attn.sdpa | 0.285 | 0.288 | 0.4 | 3 |
| bwd.invert:block2.attn.proj | 0.030 | 0.030 | 0.0 | 3 |
| bwd.invert:block2.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block2.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd.recompute:block2 | 0.541 | 0.550 | 0.8 | 3 |
| bwd.recompute:block2.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block2.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block2.attn.sdpa | 0.287 | 0.289 | 0.4 | 3 |
| bwd.recompute:block2.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block2.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block2.mlp | 0.085 | 0.087 | 0.1 | 3 |
| bwd:block2.grad | 0.818 | 0.824 | 1.2 | 3 |
| bwd:block1 | 1.790 | 1.796 | 2.6 | 2 |
| bwd.invert:block1 | 0.541 | 0.551 | 0.8 | 3 |
| bwd.invert:block1.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block1.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block1.attn.sdpa | 0.285 | 0.288 | 0.4 | 3 |
| bwd.invert:block1.attn.proj | 0.031 | 0.033 | 0.0 | 3 |
| bwd.invert:block1.ln2 | 0.020 | 0.023 | 0.0 | 3 |
| bwd.invert:block1.mlp | 0.086 | 0.088 | 0.1 | 3 |
| bwd.recompute:block1 | 0.542 | 0.551 | 0.8 | 3 |
| bwd.recompute:block1.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block1.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block1.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.recompute:block1.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block1.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block1.mlp | 0.084 | 0.086 | 0.1 | 3 |
| bwd:block1.grad | 0.822 | 0.826 | 1.2 | 3 |
| bwd:block0 | 1.787 | 1.794 | 2.6 | 2 |
| bwd.invert:block0 | 0.539 | 0.544 | 0.8 | 3 |
| bwd.invert:block0.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block0.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block0.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.invert:block0.attn.proj | 0.029 | 0.030 | 0.0 | 3 |
| bwd.invert:block0.ln2 | 0.019 | 0.022 | 0.0 | 3 |
| bwd.invert:block0.mlp | 0.083 | 0.085 | 0.1 | 3 |
| bwd.recompute:block0 | 0.539 | 0.546 | 0.8 | 3 |
| bwd.recompute:block0.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block0.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block0.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.recompute:block0.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block0.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block0.mlp | 0.084 | 0.087 | 0.1 | 3 |
| bwd:block0.grad | 0.820 | 0.824 | 1.2 | 3 |
| bwd:embed | 0.316 | 0.318 | 0.5 | 2 |
| opt | 28.710 | 30.848 | 42.1 | 1 |
| opt:opt.clip | 0.410 | 0.415 | 0.6 | 2 |
| opt:opt.polar_muon_adamw | 28.028 | 30.150 | 41.1 | 2 |
| opt:opt.muon | 22.784 | 24.908 | 33.4 | 2 |
| opt:opt.muon.ns | 25.449 | 27.445 | 37.3 | 3 |
| opt:opt.adamw | 5.109 | 5.287 | 7.5 | 2 |
| opt:opt.moe_bias | 0.015 | 0.016 | 0.0 | 3 |
| opt:opt.zero_grad | 0.244 | 0.298 | 0.4 | 3 |

## Time by part type (sum over layers)

| part type | median ms sum | % of step |
| :--- | ---: | ---: |
| opt | 28.710 | 42.1 |
| opt:opt.polar_muon_adamw | 28.028 | 41.1 |
| opt:opt.muon.ns | 25.449 | 37.3 |
| bwd | 23.365 | 34.3 |
| opt:opt.muon | 22.784 | 33.4 |
| fwd | 17.458 | 25.6 |
| bwd:head+loss | 12.279 | 18.0 |
| bwd:stack | 10.760 | 15.8 |
| bwd:block* | 10.712 | 15.7 |
| fwd:head+loss | 10.437 | 15.3 |
| fwd:stack | 6.164 | 9.0 |
| fwd:block* | 5.816 | 8.5 |
| opt:opt.adamw | 5.109 | 7.5 |
| bwd:block*.grad | 4.917 | 7.2 |
| bwd.recompute:block* | 3.234 | 4.7 |
| bwd.invert:block* | 3.224 | 4.7 |
| fwd:block*.attn.sdpa | 2.451 | 3.6 |
| bwd.recompute:block*.attn.sdpa | 1.709 | 2.5 |
| bwd.invert:block*.attn.sdpa | 1.709 | 2.5 |
| fwd:block*.mlp | 1.109 | 1.6 |
| fwd:block*.attn.qkv | 0.905 | 1.3 |
| data | 0.767 | 1.1 |
| fwd:embed | 0.697 | 1.0 |
| fwd:block*.attn.proj | 0.664 | 1.0 |
| fwd:embed.ke | 0.657 | 1.0 |
| bwd.recompute:block*.mlp | 0.507 | 0.7 |
| bwd.invert:block*.mlp | 0.504 | 0.7 |
| opt:opt.clip | 0.410 | 0.6 |
| fwd:block*.ln1 | 0.316 | 0.5 |
| bwd:embed | 0.316 | 0.5 |
| fwd:block*.ln2 | 0.299 | 0.4 |
| opt:opt.zero_grad | 0.244 | 0.4 |
| bwd.invert:block*.attn.qkv | 0.186 | 0.3 |
| bwd.recompute:block*.attn.qkv | 0.186 | 0.3 |
| bwd.invert:block*.attn.proj | 0.179 | 0.3 |
| bwd.recompute:block*.attn.proj | 0.179 | 0.3 |
| bwd.invert:block*.ln1 | 0.126 | 0.2 |
| bwd.recompute:block*.ln1 | 0.126 | 0.2 |
| bwd.invert:block*.ln2 | 0.120 | 0.2 |
| bwd.recompute:block*.ln2 | 0.120 | 0.2 |
| opt:opt.moe_bias | 0.015 | 0.0 |

## Five slowest leaf parts

1. `opt:opt.muon.ns` — 25.449 ms (37.3% of step)
2. `bwd:block1.grad` — 0.822 ms (1.2% of step)
3. `bwd:block0.grad` — 0.820 ms (1.2% of step)
4. `bwd:block4.grad` — 0.819 ms (1.2% of step)
5. `bwd:block3.grad` — 0.819 ms (1.2% of step)
