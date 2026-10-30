# Bench report — pr29_a100real1_normal

**GPU:** NVIDIA A100-SXM4-40GB  |  **dtype:** bf16  |  **B x T:** 16 x 256  |  **torch:** 2.15.0+cu132
**commit:** `dc0b1703d7d0c51b152bd37d81f6fc2b3ddcf64d`  |  **tag:** pr29_a100real1_normal

## Step (clean)

- median: 79.620 ms
- p10..p90: 78.170 .. 83.195 ms
- tokens/s: 51,445
- MFU: 4.1%  |  HFU: 4.5%

## Diagnostics

### CUDA timing-event allocations

- [OK] clean: events_created_during_steps=0
- [OK] layer: events_created_during_steps=0
- [OK] layer.inner_pass: events_created_during_steps=0

### Benchmark warnings

- [warn] 8 gated part(s) have p10..p90 spread > 10%, so may miss the 5% check: data, fwd:embed, fwd:block0, fwd:block1, fwd:block2, fwd:block3 (+2 more)

## Regions

| part | median ms | p90 | % of step | level |
| :--- | ---: | ---: | ---: | ---: |
| data | 0.882 | 0.978 | 1.1 | 1 |
| fwd | 19.081 | 19.501 | 24.0 | 1 |
| fwd:embed | 0.775 | 0.827 | 1.0 | 2 |
| fwd:embed.ke | 0.751 | 0.802 | 0.9 | 3 |
| fwd:stack | 7.665 | 8.030 | 9.6 | 1 |
| fwd:block0 | 1.400 | 1.557 | 1.8 | 2 |
| fwd:block0.ln1 | 0.091 | 0.110 | 0.1 | 3 |
| fwd:block0.attn.qkv | 0.241 | 0.272 | 0.3 | 3 |
| fwd:block0.attn.sdpa | 0.587 | 0.643 | 0.7 | 3 |
| fwd:block0.attn.proj | 0.190 | 0.224 | 0.2 | 3 |
| fwd:block0.ln2 | 0.068 | 0.081 | 0.1 | 3 |
| fwd:block0.mlp | 0.260 | 0.298 | 0.3 | 3 |
| fwd:block1 | 1.193 | 1.256 | 1.5 | 2 |
| fwd:block1.ln1 | 0.069 | 0.079 | 0.1 | 3 |
| fwd:block1.attn.qkv | 0.189 | 0.218 | 0.2 | 3 |
| fwd:block1.attn.sdpa | 0.485 | 0.524 | 0.6 | 3 |
| fwd:block1.attn.proj | 0.183 | 0.215 | 0.2 | 3 |
| fwd:block1.ln2 | 0.064 | 0.080 | 0.1 | 3 |
| fwd:block1.mlp | 0.239 | 0.284 | 0.3 | 3 |
| fwd:block2 | 1.158 | 1.242 | 1.5 | 2 |
| fwd:block2.ln1 | 0.066 | 0.075 | 0.1 | 3 |
| fwd:block2.attn.qkv | 0.188 | 0.217 | 0.2 | 3 |
| fwd:block2.attn.sdpa | 0.476 | 0.513 | 0.6 | 3 |
| fwd:block2.attn.proj | 0.179 | 0.213 | 0.2 | 3 |
| fwd:block2.ln2 | 0.063 | 0.082 | 0.1 | 3 |
| fwd:block2.mlp | 0.243 | 0.272 | 0.3 | 3 |
| fwd:block3 | 1.171 | 1.259 | 1.5 | 2 |
| fwd:block3.ln1 | 0.066 | 0.078 | 0.1 | 3 |
| fwd:block3.attn.qkv | 0.185 | 0.209 | 0.2 | 3 |
| fwd:block3.attn.sdpa | 0.477 | 0.513 | 0.6 | 3 |
| fwd:block3.attn.proj | 0.178 | 0.206 | 0.2 | 3 |
| fwd:block3.ln2 | 0.063 | 0.073 | 0.1 | 3 |
| fwd:block3.mlp | 0.239 | 0.278 | 0.3 | 3 |
| fwd:block4 | 1.175 | 1.237 | 1.5 | 2 |
| fwd:block4.ln1 | 0.065 | 0.076 | 0.1 | 3 |
| fwd:block4.attn.qkv | 0.185 | 0.217 | 0.2 | 3 |
| fwd:block4.attn.sdpa | 0.467 | 0.502 | 0.6 | 3 |
| fwd:block4.attn.proj | 0.178 | 0.209 | 0.2 | 3 |
| fwd:block4.ln2 | 0.063 | 0.083 | 0.1 | 3 |
| fwd:block4.mlp | 0.243 | 0.278 | 0.3 | 3 |
| fwd:block5 | 1.154 | 1.226 | 1.4 | 2 |
| fwd:block5.ln1 | 0.065 | 0.075 | 0.1 | 3 |
| fwd:block5.attn.qkv | 0.184 | 0.212 | 0.2 | 3 |
| fwd:block5.attn.sdpa | 0.473 | 0.501 | 0.6 | 3 |
| fwd:block5.attn.proj | 0.178 | 0.212 | 0.2 | 3 |
| fwd:block5.ln2 | 0.062 | 0.079 | 0.1 | 3 |
| fwd:block5.mlp | 0.237 | 0.267 | 0.3 | 3 |
| fwd:head+loss | 10.460 | 10.485 | 13.1 | 2 |
| bwd | 23.388 | 23.407 | 29.4 | 1 |
| bwd:head+loss | 12.291 | 12.304 | 15.4 | 2 |
| bwd:stack | 10.761 | 10.778 | 13.5 | 1 |
| bwd:block5 | 1.784 | 1.791 | 2.2 | 2 |
| bwd.invert:block5 | 0.532 | 0.536 | 0.7 | 3 |
| bwd.invert:block5.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block5.attn.qkv | 0.031 | 0.031 | 0.0 | 3 |
| bwd.invert:block5.attn.sdpa | 0.287 | 0.289 | 0.4 | 3 |
| bwd.invert:block5.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block5.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block5.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd.recompute:block5 | 0.532 | 0.537 | 0.7 | 3 |
| bwd.recompute:block5.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block5.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block5.attn.sdpa | 0.284 | 0.286 | 0.4 | 3 |
| bwd.recompute:block5.attn.proj | 0.030 | 0.030 | 0.0 | 3 |
| bwd.recompute:block5.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.recompute:block5.mlp | 0.084 | 0.084 | 0.1 | 3 |
| bwd:block5.grad | 0.818 | 0.822 | 1.0 | 3 |
| bwd:block4 | 1.789 | 1.794 | 2.2 | 2 |
| bwd.invert:block4 | 0.532 | 0.537 | 0.7 | 3 |
| bwd.invert:block4.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block4.attn.qkv | 0.031 | 0.033 | 0.0 | 3 |
| bwd.invert:block4.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.invert:block4.attn.proj | 0.030 | 0.030 | 0.0 | 3 |
| bwd.invert:block4.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.invert:block4.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd.recompute:block4 | 0.536 | 0.539 | 0.7 | 3 |
| bwd.recompute:block4.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block4.attn.qkv | 0.031 | 0.031 | 0.0 | 3 |
| bwd.recompute:block4.attn.sdpa | 0.286 | 0.289 | 0.4 | 3 |
| bwd.recompute:block4.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block4.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block4.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block4.grad | 0.819 | 0.824 | 1.0 | 3 |
| bwd:block3 | 1.783 | 1.790 | 2.2 | 2 |
| bwd.invert:block3 | 0.530 | 0.534 | 0.7 | 3 |
| bwd.invert:block3.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block3.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block3.attn.sdpa | 0.284 | 0.286 | 0.4 | 3 |
| bwd.invert:block3.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block3.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block3.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd.recompute:block3 | 0.532 | 0.536 | 0.7 | 3 |
| bwd.recompute:block3.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block3.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block3.attn.sdpa | 0.284 | 0.286 | 0.4 | 3 |
| bwd.recompute:block3.attn.proj | 0.030 | 0.030 | 0.0 | 3 |
| bwd.recompute:block3.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.recompute:block3.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd:block3.grad | 0.818 | 0.822 | 1.0 | 3 |
| bwd:block2 | 1.785 | 1.791 | 2.2 | 2 |
| bwd.invert:block2 | 0.531 | 0.537 | 0.7 | 3 |
| bwd.invert:block2.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block2.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block2.attn.sdpa | 0.285 | 0.288 | 0.4 | 3 |
| bwd.invert:block2.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block2.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.invert:block2.mlp | 0.082 | 0.083 | 0.1 | 3 |
| bwd.recompute:block2 | 0.535 | 0.539 | 0.7 | 3 |
| bwd.recompute:block2.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block2.attn.qkv | 0.031 | 0.031 | 0.0 | 3 |
| bwd.recompute:block2.attn.sdpa | 0.286 | 0.289 | 0.4 | 3 |
| bwd.recompute:block2.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block2.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block2.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd:block2.grad | 0.819 | 0.825 | 1.0 | 3 |
| bwd:block1 | 1.791 | 1.798 | 2.2 | 2 |
| bwd.invert:block1 | 0.534 | 0.537 | 0.7 | 3 |
| bwd.invert:block1.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block1.attn.qkv | 0.031 | 0.031 | 0.0 | 3 |
| bwd.invert:block1.attn.sdpa | 0.286 | 0.287 | 0.4 | 3 |
| bwd.invert:block1.attn.proj | 0.030 | 0.032 | 0.0 | 3 |
| bwd.invert:block1.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block1.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd.recompute:block1 | 0.534 | 0.538 | 0.7 | 3 |
| bwd.recompute:block1.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block1.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block1.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.recompute:block1.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block1.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.recompute:block1.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd:block1.grad | 0.821 | 0.824 | 1.0 | 3 |
| bwd:block0 | 1.787 | 1.796 | 2.2 | 2 |
| bwd.invert:block0 | 0.530 | 0.539 | 0.7 | 3 |
| bwd.invert:block0.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block0.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block0.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.invert:block0.attn.proj | 0.029 | 0.030 | 0.0 | 3 |
| bwd.invert:block0.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.invert:block0.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd.recompute:block0 | 0.532 | 0.642 | 0.7 | 3 |
| bwd.recompute:block0.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block0.attn.qkv | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block0.attn.sdpa | 0.285 | 0.289 | 0.4 | 3 |
| bwd.recompute:block0.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block0.ln2 | 0.019 | 0.021 | 0.0 | 3 |
| bwd.recompute:block0.mlp | 0.084 | 0.103 | 0.1 | 3 |
| bwd:block0.grad | 0.823 | 1.974 | 1.0 | 3 |
| bwd:embed | 0.326 | 0.328 | 0.4 | 2 |
| opt | 40.163 | 42.041 | 50.4 | 1 |
| opt:opt.clip | 0.410 | 0.413 | 0.5 | 2 |
| opt:opt.polar_muon_adamw | 39.422 | 41.245 | 49.5 | 2 |
| opt:opt.muon | 33.496 | 35.098 | 42.1 | 2 |
| opt:opt.muon.ns | 38.161 | 39.749 | 47.9 | 3 |
| opt:opt.adamw | 5.794 | 6.056 | 7.3 | 2 |
| opt:opt.moe_bias | 0.018 | 0.022 | 0.0 | 3 |
| opt:opt.zero_grad | 0.310 | 0.380 | 0.4 | 3 |

## Time by part type (sum over layers)

| part type | median ms sum | % of step |
| :--- | ---: | ---: |
| opt | 40.163 | 50.4 |
| opt:opt.polar_muon_adamw | 39.422 | 49.5 |
| opt:opt.muon.ns | 38.161 | 47.9 |
| opt:opt.muon | 33.496 | 42.1 |
| bwd | 23.388 | 29.4 |
| fwd | 19.081 | 24.0 |
| bwd:head+loss | 12.291 | 15.4 |
| bwd:stack | 10.761 | 13.5 |
| bwd:block* | 10.718 | 13.5 |
| fwd:head+loss | 10.460 | 13.1 |
| fwd:stack | 7.665 | 9.6 |
| fwd:block* | 7.252 | 9.1 |
| opt:opt.adamw | 5.794 | 7.3 |
| bwd:block*.grad | 4.919 | 6.2 |
| bwd.recompute:block* | 3.201 | 4.0 |
| bwd.invert:block* | 3.191 | 4.0 |
| fwd:block*.attn.sdpa | 2.965 | 3.7 |
| bwd.invert:block*.attn.sdpa | 1.710 | 2.1 |
| bwd.recompute:block*.attn.sdpa | 1.709 | 2.1 |
| fwd:block*.mlp | 1.461 | 1.8 |
| fwd:block*.attn.qkv | 1.172 | 1.5 |
| fwd:block*.attn.proj | 1.086 | 1.4 |
| data | 0.882 | 1.1 |
| fwd:embed | 0.775 | 1.0 |
| fwd:embed.ke | 0.751 | 0.9 |
| bwd.recompute:block*.mlp | 0.504 | 0.6 |
| bwd.invert:block*.mlp | 0.501 | 0.6 |
| fwd:block*.ln1 | 0.420 | 0.5 |
| opt:opt.clip | 0.410 | 0.5 |
| fwd:block*.ln2 | 0.384 | 0.5 |
| bwd:embed | 0.326 | 0.4 |
| opt:opt.zero_grad | 0.310 | 0.4 |
| bwd.recompute:block*.attn.qkv | 0.184 | 0.2 |
| bwd.invert:block*.attn.qkv | 0.184 | 0.2 |
| bwd.recompute:block*.attn.proj | 0.180 | 0.2 |
| bwd.invert:block*.attn.proj | 0.177 | 0.2 |
| bwd.invert:block*.ln1 | 0.123 | 0.2 |
| bwd.recompute:block*.ln1 | 0.123 | 0.2 |
| bwd.invert:block*.ln2 | 0.117 | 0.1 |
| bwd.recompute:block*.ln2 | 0.117 | 0.1 |
| opt:opt.moe_bias | 0.018 | 0.0 |

## Five slowest leaf parts

1. `opt:opt.muon.ns` — 38.161 ms (47.9% of step)
2. `bwd:block0.grad` — 0.823 ms (1.0% of step)
3. `bwd:block1.grad` — 0.821 ms (1.0% of step)
4. `bwd:block4.grad` — 0.819 ms (1.0% of step)
5. `bwd:block2.grad` — 0.819 ms (1.0% of step)
