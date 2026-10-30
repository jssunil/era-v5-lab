# Bench report — pr29_a100real2_normal

**GPU:** NVIDIA A100-SXM4-40GB  |  **dtype:** bf16  |  **B x T:** 16 x 256  |  **torch:** 2.15.0+cu132
**commit:** `dc0b1703d7d0c51b152bd37d81f6fc2b3ddcf64d`  |  **tag:** pr29_a100real2_normal

## Step (clean)

- median: 63.874 ms
- p10..p90: 62.707 .. 84.013 ms
- tokens/s: 64,126
- MFU: 5.1%  |  HFU: 5.7%

## Diagnostics

### CUDA timing-event allocations

- [OK] clean: events_created_during_steps=0
- [OK] layer: events_created_during_steps=0
- [OK] layer.inner_pass: events_created_during_steps=0

### Benchmark warnings

- [warn] 3 gated part(s) have p10..p90 spread > 10%, so may miss the 5% check: data, fwd:embed, fwd:block0

## Regions

| part | median ms | p90 | % of step | level |
| :--- | ---: | ---: | ---: | ---: |
| data | 0.506 | 0.664 | 0.8 | 1 |
| fwd | 16.694 | 17.003 | 26.1 | 1 |
| fwd:embed | 0.623 | 0.671 | 1.0 | 2 |
| fwd:embed.ke | 0.613 | 0.654 | 1.0 | 3 |
| fwd:stack | 5.498 | 5.727 | 8.6 | 1 |
| fwd:block0 | 0.862 | 1.037 | 1.3 | 2 |
| fwd:block0.ln1 | 0.055 | 0.070 | 0.1 | 3 |
| fwd:block0.attn.qkv | 0.162 | 0.191 | 0.3 | 3 |
| fwd:block0.attn.sdpa | 0.412 | 0.457 | 0.6 | 3 |
| fwd:block0.attn.proj | 0.116 | 0.144 | 0.2 | 3 |
| fwd:block0.ln2 | 0.049 | 0.053 | 0.1 | 3 |
| fwd:block0.mlp | 0.181 | 0.216 | 0.3 | 3 |
| fwd:block1 | 0.886 | 0.908 | 1.4 | 2 |
| fwd:block1.ln1 | 0.049 | 0.059 | 0.1 | 3 |
| fwd:block1.attn.qkv | 0.140 | 0.165 | 0.2 | 3 |
| fwd:block1.attn.sdpa | 0.390 | 0.415 | 0.6 | 3 |
| fwd:block1.attn.proj | 0.099 | 0.123 | 0.2 | 3 |
| fwd:block1.ln2 | 0.048 | 0.051 | 0.1 | 3 |
| fwd:block1.mlp | 0.178 | 0.206 | 0.3 | 3 |
| fwd:block2 | 0.883 | 0.898 | 1.4 | 2 |
| fwd:block2.ln1 | 0.048 | 0.055 | 0.1 | 3 |
| fwd:block2.attn.qkv | 0.139 | 0.161 | 0.2 | 3 |
| fwd:block2.attn.sdpa | 0.390 | 0.414 | 0.6 | 3 |
| fwd:block2.attn.proj | 0.099 | 0.125 | 0.2 | 3 |
| fwd:block2.ln2 | 0.048 | 0.054 | 0.1 | 3 |
| fwd:block2.mlp | 0.176 | 0.206 | 0.3 | 3 |
| fwd:block3 | 0.876 | 0.892 | 1.4 | 2 |
| fwd:block3.ln1 | 0.048 | 0.064 | 0.1 | 3 |
| fwd:block3.attn.qkv | 0.138 | 0.165 | 0.2 | 3 |
| fwd:block3.attn.sdpa | 0.389 | 0.412 | 0.6 | 3 |
| fwd:block3.attn.proj | 0.098 | 0.123 | 0.2 | 3 |
| fwd:block3.ln2 | 0.048 | 0.054 | 0.1 | 3 |
| fwd:block3.mlp | 0.175 | 0.203 | 0.3 | 3 |
| fwd:block4 | 0.876 | 0.892 | 1.4 | 2 |
| fwd:block4.ln1 | 0.047 | 0.053 | 0.1 | 3 |
| fwd:block4.attn.qkv | 0.139 | 0.163 | 0.2 | 3 |
| fwd:block4.attn.sdpa | 0.388 | 0.415 | 0.6 | 3 |
| fwd:block4.attn.proj | 0.096 | 0.121 | 0.2 | 3 |
| fwd:block4.ln2 | 0.048 | 0.055 | 0.1 | 3 |
| fwd:block4.mlp | 0.177 | 0.206 | 0.3 | 3 |
| fwd:block5 | 0.876 | 0.891 | 1.4 | 2 |
| fwd:block5.ln1 | 0.048 | 0.053 | 0.1 | 3 |
| fwd:block5.attn.qkv | 0.139 | 0.164 | 0.2 | 3 |
| fwd:block5.attn.sdpa | 0.388 | 0.414 | 0.6 | 3 |
| fwd:block5.attn.proj | 0.095 | 0.122 | 0.1 | 3 |
| fwd:block5.ln2 | 0.048 | 0.054 | 0.1 | 3 |
| fwd:block5.mlp | 0.177 | 0.204 | 0.3 | 3 |
| fwd:head+loss | 10.477 | 10.486 | 16.4 | 2 |
| bwd | 23.474 | 23.499 | 36.8 | 1 |
| bwd:head+loss | 12.393 | 12.405 | 19.4 | 2 |
| bwd:stack | 10.755 | 10.770 | 16.8 | 1 |
| bwd:block5 | 1.780 | 1.785 | 2.8 | 2 |
| bwd.invert:block5 | 0.534 | 0.536 | 0.8 | 3 |
| bwd.invert:block5.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block5.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block5.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.invert:block5.attn.proj | 0.030 | 0.032 | 0.0 | 3 |
| bwd.invert:block5.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block5.mlp | 0.083 | 0.085 | 0.1 | 3 |
| bwd.recompute:block5 | 0.534 | 0.537 | 0.8 | 3 |
| bwd.recompute:block5.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block5.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block5.attn.sdpa | 0.282 | 0.284 | 0.4 | 3 |
| bwd.recompute:block5.attn.proj | 0.030 | 0.030 | 0.0 | 3 |
| bwd.recompute:block5.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block5.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd:block5.grad | 0.820 | 0.822 | 1.3 | 3 |
| bwd:block4 | 1.788 | 1.793 | 2.8 | 2 |
| bwd.invert:block4 | 0.536 | 0.539 | 0.8 | 3 |
| bwd.invert:block4.ln1 | 0.022 | 0.022 | 0.0 | 3 |
| bwd.invert:block4.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block4.attn.sdpa | 0.284 | 0.286 | 0.4 | 3 |
| bwd.invert:block4.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block4.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.invert:block4.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd.recompute:block4 | 0.539 | 0.541 | 0.8 | 3 |
| bwd.recompute:block4.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block4.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block4.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.recompute:block4.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block4.ln2 | 0.020 | 0.021 | 0.0 | 3 |
| bwd.recompute:block4.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block4.grad | 0.820 | 0.823 | 1.3 | 3 |
| bwd:block3 | 1.783 | 1.787 | 2.8 | 2 |
| bwd.invert:block3 | 0.536 | 0.539 | 0.8 | 3 |
| bwd.invert:block3.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block3.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block3.attn.sdpa | 0.284 | 0.287 | 0.4 | 3 |
| bwd.invert:block3.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block3.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block3.mlp | 0.084 | 0.086 | 0.1 | 3 |
| bwd.recompute:block3 | 0.538 | 0.541 | 0.8 | 3 |
| bwd.recompute:block3.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block3.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block3.attn.sdpa | 0.284 | 0.285 | 0.4 | 3 |
| bwd.recompute:block3.attn.proj | 0.031 | 0.031 | 0.0 | 3 |
| bwd.recompute:block3.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block3.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd:block3.grad | 0.819 | 0.821 | 1.3 | 3 |
| bwd:block2 | 1.783 | 1.787 | 2.8 | 2 |
| bwd.invert:block2 | 0.536 | 0.539 | 0.8 | 3 |
| bwd.invert:block2.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block2.attn.qkv | 0.031 | 0.033 | 0.0 | 3 |
| bwd.invert:block2.attn.sdpa | 0.286 | 0.287 | 0.4 | 3 |
| bwd.invert:block2.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block2.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block2.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd.recompute:block2 | 0.541 | 0.544 | 0.8 | 3 |
| bwd.recompute:block2.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block2.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block2.attn.sdpa | 0.286 | 0.289 | 0.4 | 3 |
| bwd.recompute:block2.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block2.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block2.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block2.grad | 0.818 | 0.821 | 1.3 | 3 |
| bwd:block1 | 1.790 | 1.795 | 2.8 | 2 |
| bwd.invert:block1 | 0.538 | 0.541 | 0.8 | 3 |
| bwd.invert:block1.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block1.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block1.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.invert:block1.attn.proj | 0.031 | 0.033 | 0.0 | 3 |
| bwd.invert:block1.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block1.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd.recompute:block1 | 0.539 | 0.543 | 0.8 | 3 |
| bwd.recompute:block1.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block1.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block1.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.recompute:block1.attn.proj | 0.031 | 0.031 | 0.0 | 3 |
| bwd.recompute:block1.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block1.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd:block1.grad | 0.824 | 0.826 | 1.3 | 3 |
| bwd:block0 | 1.788 | 1.791 | 2.8 | 2 |
| bwd.invert:block0 | 0.537 | 0.540 | 0.8 | 3 |
| bwd.invert:block0.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block0.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block0.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.invert:block0.attn.proj | 0.030 | 0.030 | 0.0 | 3 |
| bwd.invert:block0.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block0.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd.recompute:block0 | 0.539 | 0.542 | 0.8 | 3 |
| bwd.recompute:block0.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block0.attn.qkv | 0.031 | 0.031 | 0.0 | 3 |
| bwd.recompute:block0.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.recompute:block0.attn.proj | 0.030 | 0.032 | 0.0 | 3 |
| bwd.recompute:block0.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block0.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block0.grad | 0.820 | 0.823 | 1.3 | 3 |
| bwd:embed | 0.317 | 0.319 | 0.5 | 2 |
| opt | 24.235 | 25.146 | 37.9 | 1 |
| opt:opt.clip | 0.409 | 0.412 | 0.6 | 2 |
| opt:opt.polar_muon_adamw | 23.650 | 24.553 | 37.0 | 2 |
| opt:opt.muon | 18.726 | 19.617 | 29.3 | 2 |
| opt:opt.muon.ns | 22.777 | 24.773 | 35.7 | 3 |
| opt:opt.adamw | 4.857 | 4.904 | 7.6 | 2 |
| opt:opt.moe_bias | 0.014 | 0.016 | 0.0 | 3 |
| opt:opt.zero_grad | 0.181 | 0.249 | 0.3 | 3 |

## Time by part type (sum over layers)

| part type | median ms sum | % of step |
| :--- | ---: | ---: |
| opt | 24.235 | 37.9 |
| opt:opt.polar_muon_adamw | 23.650 | 37.0 |
| bwd | 23.474 | 36.8 |
| opt:opt.muon.ns | 22.777 | 35.7 |
| opt:opt.muon | 18.726 | 29.3 |
| fwd | 16.694 | 26.1 |
| bwd:head+loss | 12.393 | 19.4 |
| bwd:stack | 10.755 | 16.8 |
| bwd:block* | 10.712 | 16.8 |
| fwd:head+loss | 10.477 | 16.4 |
| fwd:stack | 5.498 | 8.6 |
| fwd:block* | 5.258 | 8.2 |
| bwd:block*.grad | 4.922 | 7.7 |
| opt:opt.adamw | 4.857 | 7.6 |
| bwd.recompute:block* | 3.228 | 5.1 |
| bwd.invert:block* | 3.214 | 5.0 |
| fwd:block*.attn.sdpa | 2.357 | 3.7 |
| bwd.invert:block*.attn.sdpa | 1.708 | 2.7 |
| bwd.recompute:block*.attn.sdpa | 1.706 | 2.7 |
| fwd:block*.mlp | 1.065 | 1.7 |
| fwd:block*.attn.qkv | 0.858 | 1.3 |
| fwd:embed | 0.623 | 1.0 |
| fwd:embed.ke | 0.613 | 1.0 |
| fwd:block*.attn.proj | 0.604 | 0.9 |
| data | 0.506 | 0.8 |
| bwd.recompute:block*.mlp | 0.506 | 0.8 |
| bwd.invert:block*.mlp | 0.502 | 0.8 |
| opt:opt.clip | 0.409 | 0.6 |
| bwd:embed | 0.317 | 0.5 |
| fwd:block*.ln1 | 0.295 | 0.5 |
| fwd:block*.ln2 | 0.290 | 0.5 |
| bwd.recompute:block*.attn.qkv | 0.187 | 0.3 |
| bwd.invert:block*.attn.qkv | 0.187 | 0.3 |
| bwd.recompute:block*.attn.proj | 0.182 | 0.3 |
| bwd.invert:block*.attn.proj | 0.181 | 0.3 |
| opt:opt.zero_grad | 0.181 | 0.3 |
| bwd.invert:block*.ln1 | 0.126 | 0.2 |
| bwd.recompute:block*.ln1 | 0.126 | 0.2 |
| bwd.recompute:block*.ln2 | 0.121 | 0.2 |
| bwd.invert:block*.ln2 | 0.120 | 0.2 |
| opt:opt.moe_bias | 0.014 | 0.0 |

## Five slowest leaf parts

1. `opt:opt.muon.ns` — 22.777 ms (35.7% of step)
2. `bwd:block1.grad` — 0.824 ms (1.3% of step)
3. `bwd:block5.grad` — 0.820 ms (1.3% of step)
4. `bwd:block4.grad` — 0.820 ms (1.3% of step)
5. `bwd:block0.grad` — 0.820 ms (1.3% of step)
