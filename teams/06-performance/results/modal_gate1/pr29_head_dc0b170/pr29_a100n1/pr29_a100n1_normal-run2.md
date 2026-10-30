# Bench report — pr29_a100n1_normal-run2

**GPU:** NVIDIA A100-SXM4-40GB  |  **dtype:** bf16  |  **B x T:** 16 x 256  |  **torch:** 2.15.0+cu132
**commit:** `dc0b1703d7d0c51b152bd37d81f6fc2b3ddcf64d`  |  **tag:** pr29_a100n1_normal-run2

## Step (clean)

- median: 60.457 ms
- p10..p90: 58.908 .. 61.878 ms
- tokens/s: 67,750
- MFU: 5.4%  |  HFU: 6.0%

## Diagnostics

### CUDA timing-event allocations

- [OK] clean: events_created_during_steps=0
- [OK] layer: events_created_during_steps=0
- [OK] layer.inner_pass: events_created_during_steps=0

### Benchmark warnings

- [warn] recorder overhead 2.3% > 2.0%: layer numbers are flagged
- [warn] 6 gated part(s) have p10..p90 spread > 10%, so may miss the 5% check: data, fwd:embed, fwd:block0, opt, opt:opt.polar_muon_adamw, opt:opt.muon

## Regions

| part | median ms | p90 | % of step | level |
| :--- | ---: | ---: | ---: | ---: |
| data | 0.296 | 0.398 | 0.5 | 1 |
| fwd | 16.306 | 16.572 | 27.0 | 1 |
| fwd:embed | 0.584 | 0.642 | 1.0 | 2 |
| fwd:embed.ke | 0.567 | 0.662 | 0.9 | 3 |
| fwd:stack | 5.179 | 5.377 | 8.6 | 1 |
| fwd:block0 | 0.837 | 0.955 | 1.4 | 2 |
| fwd:block0.ln1 | 0.056 | 0.077 | 0.1 | 3 |
| fwd:block0.attn.qkv | 0.147 | 0.191 | 0.2 | 3 |
| fwd:block0.attn.sdpa | 0.398 | 0.481 | 0.7 | 3 |
| fwd:block0.attn.proj | 0.101 | 0.132 | 0.2 | 3 |
| fwd:block0.ln2 | 0.051 | 0.054 | 0.1 | 3 |
| fwd:block0.mlp | 0.179 | 0.197 | 0.3 | 3 |
| fwd:block1 | 0.834 | 0.846 | 1.4 | 2 |
| fwd:block1.ln1 | 0.051 | 0.054 | 0.1 | 3 |
| fwd:block1.attn.qkv | 0.131 | 0.141 | 0.2 | 3 |
| fwd:block1.attn.sdpa | 0.381 | 0.393 | 0.6 | 3 |
| fwd:block1.attn.proj | 0.089 | 0.101 | 0.1 | 3 |
| fwd:block1.ln2 | 0.049 | 0.051 | 0.1 | 3 |
| fwd:block1.mlp | 0.174 | 0.185 | 0.3 | 3 |
| fwd:block2 | 0.827 | 0.841 | 1.4 | 2 |
| fwd:block2.ln1 | 0.050 | 0.052 | 0.1 | 3 |
| fwd:block2.attn.qkv | 0.129 | 0.138 | 0.2 | 3 |
| fwd:block2.attn.sdpa | 0.380 | 0.388 | 0.6 | 3 |
| fwd:block2.attn.proj | 0.088 | 0.100 | 0.1 | 3 |
| fwd:block2.ln2 | 0.048 | 0.050 | 0.1 | 3 |
| fwd:block2.mlp | 0.174 | 0.184 | 0.3 | 3 |
| fwd:block3 | 0.823 | 0.841 | 1.4 | 2 |
| fwd:block3.ln1 | 0.049 | 0.051 | 0.1 | 3 |
| fwd:block3.attn.qkv | 0.130 | 0.141 | 0.2 | 3 |
| fwd:block3.attn.sdpa | 0.381 | 0.390 | 0.6 | 3 |
| fwd:block3.attn.proj | 0.085 | 0.098 | 0.1 | 3 |
| fwd:block3.ln2 | 0.048 | 0.051 | 0.1 | 3 |
| fwd:block3.mlp | 0.173 | 0.183 | 0.3 | 3 |
| fwd:block4 | 0.823 | 0.836 | 1.4 | 2 |
| fwd:block4.ln1 | 0.049 | 0.051 | 0.1 | 3 |
| fwd:block4.attn.qkv | 0.129 | 0.137 | 0.2 | 3 |
| fwd:block4.attn.sdpa | 0.379 | 0.391 | 0.6 | 3 |
| fwd:block4.attn.proj | 0.085 | 0.096 | 0.1 | 3 |
| fwd:block4.ln2 | 0.048 | 0.050 | 0.1 | 3 |
| fwd:block4.mlp | 0.173 | 0.184 | 0.3 | 3 |
| fwd:block5 | 0.818 | 0.835 | 1.4 | 2 |
| fwd:block5.ln1 | 0.049 | 0.051 | 0.1 | 3 |
| fwd:block5.attn.qkv | 0.128 | 0.138 | 0.2 | 3 |
| fwd:block5.attn.sdpa | 0.379 | 0.389 | 0.6 | 3 |
| fwd:block5.attn.proj | 0.083 | 0.094 | 0.1 | 3 |
| fwd:block5.ln2 | 0.048 | 0.050 | 0.1 | 3 |
| fwd:block5.mlp | 0.173 | 0.185 | 0.3 | 3 |
| fwd:head+loss | 10.430 | 10.439 | 17.3 | 2 |
| bwd | 23.482 | 23.532 | 38.8 | 1 |
| bwd:head+loss | 12.295 | 12.332 | 20.3 | 2 |
| bwd:stack | 10.845 | 10.868 | 17.9 | 1 |
| bwd:block5 | 1.796 | 1.802 | 3.0 | 2 |
| bwd.invert:block5 | 0.538 | 0.540 | 0.9 | 3 |
| bwd.invert:block5.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block5.attn.qkv | 0.032 | 0.032 | 0.1 | 3 |
| bwd.invert:block5.attn.sdpa | 0.287 | 0.289 | 0.5 | 3 |
| bwd.invert:block5.attn.proj | 0.030 | 0.032 | 0.0 | 3 |
| bwd.invert:block5.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block5.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd.recompute:block5 | 0.540 | 0.543 | 0.9 | 3 |
| bwd.recompute:block5.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block5.attn.qkv | 0.032 | 0.033 | 0.1 | 3 |
| bwd.recompute:block5.attn.sdpa | 0.286 | 0.288 | 0.5 | 3 |
| bwd.recompute:block5.attn.proj | 0.030 | 0.030 | 0.0 | 3 |
| bwd.recompute:block5.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.recompute:block5.mlp | 0.086 | 0.086 | 0.1 | 3 |
| bwd:block5.grad | 0.822 | 0.825 | 1.4 | 3 |
| bwd:block4 | 1.805 | 1.811 | 3.0 | 2 |
| bwd.invert:block4 | 0.540 | 0.543 | 0.9 | 3 |
| bwd.invert:block4.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block4.attn.qkv | 0.032 | 0.033 | 0.1 | 3 |
| bwd.invert:block4.attn.sdpa | 0.288 | 0.289 | 0.5 | 3 |
| bwd.invert:block4.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block4.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block4.mlp | 0.085 | 0.085 | 0.1 | 3 |
| bwd.recompute:block4 | 0.543 | 0.545 | 0.9 | 3 |
| bwd.recompute:block4.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block4.attn.qkv | 0.031 | 0.032 | 0.1 | 3 |
| bwd.recompute:block4.attn.sdpa | 0.288 | 0.290 | 0.5 | 3 |
| bwd.recompute:block4.attn.proj | 0.031 | 0.033 | 0.1 | 3 |
| bwd.recompute:block4.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block4.mlp | 0.086 | 0.087 | 0.1 | 3 |
| bwd:block4.grad | 0.826 | 0.830 | 1.4 | 3 |
| bwd:block3 | 1.799 | 1.803 | 3.0 | 2 |
| bwd.invert:block3 | 0.540 | 0.542 | 0.9 | 3 |
| bwd.invert:block3.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block3.attn.qkv | 0.031 | 0.032 | 0.1 | 3 |
| bwd.invert:block3.attn.sdpa | 0.287 | 0.290 | 0.5 | 3 |
| bwd.invert:block3.attn.proj | 0.031 | 0.032 | 0.1 | 3 |
| bwd.invert:block3.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block3.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd.recompute:block3 | 0.542 | 0.544 | 0.9 | 3 |
| bwd.recompute:block3.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block3.attn.qkv | 0.032 | 0.033 | 0.1 | 3 |
| bwd.recompute:block3.attn.sdpa | 0.287 | 0.289 | 0.5 | 3 |
| bwd.recompute:block3.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block3.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block3.mlp | 0.086 | 0.087 | 0.1 | 3 |
| bwd:block3.grad | 0.825 | 0.828 | 1.4 | 3 |
| bwd:block2 | 1.795 | 1.800 | 3.0 | 2 |
| bwd.invert:block2 | 0.538 | 0.541 | 0.9 | 3 |
| bwd.invert:block2.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block2.attn.qkv | 0.032 | 0.033 | 0.1 | 3 |
| bwd.invert:block2.attn.sdpa | 0.286 | 0.288 | 0.5 | 3 |
| bwd.invert:block2.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block2.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block2.mlp | 0.084 | 0.084 | 0.1 | 3 |
| bwd.recompute:block2 | 0.540 | 0.543 | 0.9 | 3 |
| bwd.recompute:block2.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block2.attn.qkv | 0.031 | 0.032 | 0.1 | 3 |
| bwd.recompute:block2.attn.sdpa | 0.287 | 0.289 | 0.5 | 3 |
| bwd.recompute:block2.attn.proj | 0.031 | 0.032 | 0.1 | 3 |
| bwd.recompute:block2.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block2.mlp | 0.086 | 0.087 | 0.1 | 3 |
| bwd:block2.grad | 0.822 | 0.825 | 1.4 | 3 |
| bwd:block1 | 1.804 | 1.809 | 3.0 | 2 |
| bwd.invert:block1 | 0.543 | 0.545 | 0.9 | 3 |
| bwd.invert:block1.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block1.attn.qkv | 0.032 | 0.033 | 0.1 | 3 |
| bwd.invert:block1.attn.sdpa | 0.288 | 0.290 | 0.5 | 3 |
| bwd.invert:block1.attn.proj | 0.031 | 0.032 | 0.1 | 3 |
| bwd.invert:block1.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block1.mlp | 0.087 | 0.088 | 0.1 | 3 |
| bwd.recompute:block1 | 0.541 | 0.544 | 0.9 | 3 |
| bwd.recompute:block1.ln1 | 0.021 | 0.023 | 0.0 | 3 |
| bwd.recompute:block1.attn.qkv | 0.032 | 0.033 | 0.1 | 3 |
| bwd.recompute:block1.attn.sdpa | 0.287 | 0.289 | 0.5 | 3 |
| bwd.recompute:block1.attn.proj | 0.031 | 0.031 | 0.1 | 3 |
| bwd.recompute:block1.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block1.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block1.grad | 0.827 | 0.830 | 1.4 | 3 |
| bwd:block0 | 1.802 | 1.808 | 3.0 | 2 |
| bwd.invert:block0 | 0.540 | 0.543 | 0.9 | 3 |
| bwd.invert:block0.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block0.attn.qkv | 0.032 | 0.034 | 0.1 | 3 |
| bwd.invert:block0.attn.sdpa | 0.286 | 0.288 | 0.5 | 3 |
| bwd.invert:block0.attn.proj | 0.030 | 0.030 | 0.0 | 3 |
| bwd.invert:block0.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block0.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd.recompute:block0 | 0.542 | 0.544 | 0.9 | 3 |
| bwd.recompute:block0.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block0.attn.qkv | 0.031 | 0.032 | 0.1 | 3 |
| bwd.recompute:block0.attn.sdpa | 0.287 | 0.289 | 0.5 | 3 |
| bwd.recompute:block0.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block0.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block0.mlp | 0.086 | 0.087 | 0.1 | 3 |
| bwd:block0.grad | 0.826 | 0.829 | 1.4 | 3 |
| bwd:embed | 0.328 | 0.330 | 0.5 | 2 |
| opt | 20.706 | 21.928 | 34.2 | 1 |
| opt:opt.clip | 0.407 | 0.411 | 0.7 | 2 |
| opt:opt.polar_muon_adamw | 20.087 | 21.316 | 33.2 | 2 |
| opt:opt.muon | 15.469 | 16.605 | 25.6 | 2 |
| opt:opt.muon.ns | 19.642 | 20.963 | 32.5 | 3 |
| opt:opt.adamw | 4.534 | 4.661 | 7.5 | 2 |
| opt:opt.moe_bias | 0.014 | 0.016 | 0.0 | 3 |
| opt:opt.zero_grad | 0.156 | 0.224 | 0.3 | 3 |

## Time by part type (sum over layers)

| part type | median ms sum | % of step |
| :--- | ---: | ---: |
| bwd | 23.482 | 38.8 |
| opt | 20.706 | 34.2 |
| opt:opt.polar_muon_adamw | 20.087 | 33.2 |
| opt:opt.muon.ns | 19.642 | 32.5 |
| fwd | 16.306 | 27.0 |
| opt:opt.muon | 15.469 | 25.6 |
| bwd:head+loss | 12.295 | 20.3 |
| bwd:stack | 10.845 | 17.9 |
| bwd:block* | 10.802 | 17.9 |
| fwd:head+loss | 10.430 | 17.3 |
| fwd:stack | 5.179 | 8.6 |
| fwd:block* | 4.961 | 8.2 |
| bwd:block*.grad | 4.950 | 8.2 |
| opt:opt.adamw | 4.534 | 7.5 |
| bwd.recompute:block* | 3.247 | 5.4 |
| bwd.invert:block* | 3.237 | 5.4 |
| fwd:block*.attn.sdpa | 2.297 | 3.8 |
| bwd.recompute:block*.attn.sdpa | 1.720 | 2.8 |
| bwd.invert:block*.attn.sdpa | 1.720 | 2.8 |
| fwd:block*.mlp | 1.047 | 1.7 |
| fwd:block*.attn.qkv | 0.795 | 1.3 |
| fwd:embed | 0.584 | 1.0 |
| fwd:embed.ke | 0.567 | 0.9 |
| fwd:block*.attn.proj | 0.531 | 0.9 |
| bwd.recompute:block*.mlp | 0.515 | 0.9 |
| bwd.invert:block*.mlp | 0.508 | 0.8 |
| opt:opt.clip | 0.407 | 0.7 |
| bwd:embed | 0.328 | 0.5 |
| fwd:block*.ln1 | 0.305 | 0.5 |
| data | 0.296 | 0.5 |
| fwd:block*.ln2 | 0.293 | 0.5 |
| bwd.invert:block*.attn.qkv | 0.189 | 0.3 |
| bwd.recompute:block*.attn.qkv | 0.187 | 0.3 |
| bwd.recompute:block*.attn.proj | 0.181 | 0.3 |
| bwd.invert:block*.attn.proj | 0.180 | 0.3 |
| opt:opt.zero_grad | 0.156 | 0.3 |
| bwd.invert:block*.ln1 | 0.126 | 0.2 |
| bwd.recompute:block*.ln1 | 0.125 | 0.2 |
| bwd.invert:block*.ln2 | 0.121 | 0.2 |
| bwd.recompute:block*.ln2 | 0.120 | 0.2 |
| opt:opt.moe_bias | 0.014 | 0.0 |

## Five slowest leaf parts

1. `opt:opt.muon.ns` — 19.642 ms (32.5% of step)
2. `bwd:block1.grad` — 0.827 ms (1.4% of step)
3. `bwd:block4.grad` — 0.826 ms (1.4% of step)
4. `bwd:block0.grad` — 0.826 ms (1.4% of step)
5. `bwd:block3.grad` — 0.825 ms (1.4% of step)
