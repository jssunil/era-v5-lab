# Bench report — g1_base2_normal-run2

**GPU:** NVIDIA A100-SXM4-40GB  |  **dtype:** bf16  |  **B x T:** 16 x 256  |  **torch:** 2.15.0+cu132
**commit:** `14854097c57056f326efd0c7a40cc036a73bbc94`  |  **tag:** g1_base2_normal-run2

## Step (clean)

- median: 81.208 ms
- p10..p90: 77.463 .. 84.095 ms
- tokens/s: 50,439
- MFU: 4.0%  |  HFU: 4.5%

## Diagnostics

### CUDA timing-event allocations

- [OK] clean: events_created_during_steps=0
- [OK] layer: events_created_during_steps=0
- [OK] layer.inner_pass: events_created_during_steps=0

### Benchmark warnings

- [warn] recorder overhead 2.2% > 2.0%: layer numbers are flagged
- [warn] 11 gated part(s) have p10..p90 spread > 10%, so may miss the 5% check: data, fwd:embed, fwd:stack, fwd:block0, fwd:block1, fwd:block2 (+5 more)

## Regions

| part | median ms | p90 | % of step | level |
| :--- | ---: | ---: | ---: | ---: |
| data | 0.917 | 1.002 | 1.1 | 1 |
| fwd | 19.111 | 19.591 | 23.5 | 1 |
| fwd:embed | 0.778 | 0.816 | 1.0 | 2 |
| fwd:embed.ke | 0.766 | 0.813 | 0.9 | 3 |
| fwd:stack | 7.712 | 8.096 | 9.5 | 1 |
| fwd:block0 | 1.430 | 1.579 | 1.8 | 2 |
| fwd:block0.ln1 | 0.095 | 0.112 | 0.1 | 3 |
| fwd:block0.attn.qkv | 0.259 | 0.310 | 0.3 | 3 |
| fwd:block0.attn.sdpa | 0.603 | 0.687 | 0.7 | 3 |
| fwd:block0.attn.proj | 0.193 | 0.215 | 0.2 | 3 |
| fwd:block0.ln2 | 0.068 | 0.083 | 0.1 | 3 |
| fwd:block0.mlp | 0.259 | 0.293 | 0.3 | 3 |
| fwd:block1 | 1.182 | 1.274 | 1.5 | 2 |
| fwd:block1.ln1 | 0.070 | 0.089 | 0.1 | 3 |
| fwd:block1.attn.qkv | 0.189 | 0.215 | 0.2 | 3 |
| fwd:block1.attn.sdpa | 0.486 | 0.524 | 0.6 | 3 |
| fwd:block1.attn.proj | 0.183 | 0.212 | 0.2 | 3 |
| fwd:block1.ln2 | 0.065 | 0.082 | 0.1 | 3 |
| fwd:block1.mlp | 0.243 | 0.274 | 0.3 | 3 |
| fwd:block2 | 1.177 | 1.262 | 1.4 | 2 |
| fwd:block2.ln1 | 0.067 | 0.079 | 0.1 | 3 |
| fwd:block2.attn.qkv | 0.190 | 0.214 | 0.2 | 3 |
| fwd:block2.attn.sdpa | 0.479 | 0.511 | 0.6 | 3 |
| fwd:block2.attn.proj | 0.184 | 0.209 | 0.2 | 3 |
| fwd:block2.ln2 | 0.063 | 0.078 | 0.1 | 3 |
| fwd:block2.mlp | 0.243 | 0.275 | 0.3 | 3 |
| fwd:block3 | 1.175 | 1.272 | 1.4 | 2 |
| fwd:block3.ln1 | 0.065 | 0.075 | 0.1 | 3 |
| fwd:block3.attn.qkv | 0.188 | 0.216 | 0.2 | 3 |
| fwd:block3.attn.sdpa | 0.473 | 0.511 | 0.6 | 3 |
| fwd:block3.attn.proj | 0.178 | 0.206 | 0.2 | 3 |
| fwd:block3.ln2 | 0.062 | 0.071 | 0.1 | 3 |
| fwd:block3.mlp | 0.234 | 0.268 | 0.3 | 3 |
| fwd:block4 | 1.178 | 1.240 | 1.5 | 2 |
| fwd:block4.ln1 | 0.063 | 0.072 | 0.1 | 3 |
| fwd:block4.attn.qkv | 0.187 | 0.216 | 0.2 | 3 |
| fwd:block4.attn.sdpa | 0.467 | 0.511 | 0.6 | 3 |
| fwd:block4.attn.proj | 0.178 | 0.207 | 0.2 | 3 |
| fwd:block4.ln2 | 0.061 | 0.079 | 0.1 | 3 |
| fwd:block4.mlp | 0.237 | 0.272 | 0.3 | 3 |
| fwd:block5 | 1.136 | 1.234 | 1.4 | 2 |
| fwd:block5.ln1 | 0.065 | 0.078 | 0.1 | 3 |
| fwd:block5.attn.qkv | 0.187 | 0.211 | 0.2 | 3 |
| fwd:block5.attn.sdpa | 0.474 | 0.508 | 0.6 | 3 |
| fwd:block5.attn.proj | 0.178 | 0.204 | 0.2 | 3 |
| fwd:block5.ln2 | 0.061 | 0.079 | 0.1 | 3 |
| fwd:block5.mlp | 0.242 | 0.272 | 0.3 | 3 |
| fwd:head+loss | 10.460 | 10.479 | 12.9 | 2 |
| bwd | 23.431 | 23.448 | 28.9 | 1 |
| bwd:head+loss | 12.281 | 12.292 | 15.1 | 2 |
| bwd:stack | 10.822 | 10.836 | 13.3 | 1 |
| bwd:block5 | 1.792 | 1.797 | 2.2 | 2 |
| bwd.invert:block5 | 0.535 | 0.537 | 0.7 | 3 |
| bwd.invert:block5.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block5.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block5.attn.sdpa | 0.287 | 0.289 | 0.4 | 3 |
| bwd.invert:block5.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block5.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block5.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd.recompute:block5 | 0.535 | 0.537 | 0.7 | 3 |
| bwd.recompute:block5.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block5.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block5.attn.sdpa | 0.285 | 0.286 | 0.4 | 3 |
| bwd.recompute:block5.attn.proj | 0.030 | 0.030 | 0.0 | 3 |
| bwd.recompute:block5.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.recompute:block5.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd:block5.grad | 0.821 | 0.824 | 1.0 | 3 |
| bwd:block4 | 1.801 | 1.806 | 2.2 | 2 |
| bwd.invert:block4 | 0.537 | 0.540 | 0.7 | 3 |
| bwd.invert:block4.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block4.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block4.attn.sdpa | 0.287 | 0.289 | 0.4 | 3 |
| bwd.invert:block4.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block4.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block4.mlp | 0.085 | 0.085 | 0.1 | 3 |
| bwd.recompute:block4 | 0.540 | 0.542 | 0.7 | 3 |
| bwd.recompute:block4.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block4.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block4.attn.sdpa | 0.287 | 0.289 | 0.4 | 3 |
| bwd.recompute:block4.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block4.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block4.mlp | 0.086 | 0.087 | 0.1 | 3 |
| bwd:block4.grad | 0.822 | 0.826 | 1.0 | 3 |
| bwd:block3 | 1.793 | 1.798 | 2.2 | 2 |
| bwd.invert:block3 | 0.534 | 0.538 | 0.7 | 3 |
| bwd.invert:block3.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block3.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block3.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.invert:block3.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block3.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block3.mlp | 0.084 | 0.086 | 0.1 | 3 |
| bwd.recompute:block3 | 0.537 | 0.539 | 0.7 | 3 |
| bwd.recompute:block3.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block3.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block3.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.recompute:block3.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block3.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.recompute:block3.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block3.grad | 0.821 | 0.825 | 1.0 | 3 |
| bwd:block2 | 1.794 | 1.799 | 2.2 | 2 |
| bwd.invert:block2 | 0.535 | 0.537 | 0.7 | 3 |
| bwd.invert:block2.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block2.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block2.attn.sdpa | 0.287 | 0.289 | 0.4 | 3 |
| bwd.invert:block2.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block2.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.invert:block2.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd.recompute:block2 | 0.538 | 0.542 | 0.7 | 3 |
| bwd.recompute:block2.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block2.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block2.attn.sdpa | 0.288 | 0.290 | 0.4 | 3 |
| bwd.recompute:block2.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block2.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block2.mlp | 0.086 | 0.087 | 0.1 | 3 |
| bwd:block2.grad | 0.820 | 0.824 | 1.0 | 3 |
| bwd:block1 | 1.800 | 1.805 | 2.2 | 2 |
| bwd.invert:block1 | 0.537 | 0.540 | 0.7 | 3 |
| bwd.invert:block1.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block1.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block1.attn.sdpa | 0.287 | 0.288 | 0.4 | 3 |
| bwd.invert:block1.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block1.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block1.mlp | 0.086 | 0.087 | 0.1 | 3 |
| bwd.recompute:block1 | 0.538 | 0.541 | 0.7 | 3 |
| bwd.recompute:block1.ln1 | 0.022 | 0.022 | 0.0 | 3 |
| bwd.recompute:block1.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block1.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.recompute:block1.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block1.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.recompute:block1.mlp | 0.085 | 0.085 | 0.1 | 3 |
| bwd:block1.grad | 0.824 | 0.826 | 1.0 | 3 |
| bwd:block0 | 1.800 | 1.806 | 2.2 | 2 |
| bwd.invert:block0 | 0.537 | 0.539 | 0.7 | 3 |
| bwd.invert:block0.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block0.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block0.attn.sdpa | 0.287 | 0.289 | 0.4 | 3 |
| bwd.invert:block0.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block0.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.invert:block0.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd.recompute:block0 | 0.537 | 0.852 | 0.7 | 3 |
| bwd.recompute:block0.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block0.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block0.attn.sdpa | 0.288 | 0.295 | 0.4 | 3 |
| bwd.recompute:block0.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block0.ln2 | 0.019 | 0.025 | 0.0 | 3 |
| bwd.recompute:block0.mlp | 0.085 | 0.230 | 0.1 | 3 |
| bwd:block0.grad | 0.834 | 1.986 | 1.0 | 3 |
| bwd:embed | 0.318 | 0.319 | 0.4 | 2 |
| opt | 40.504 | 42.244 | 49.9 | 1 |
| opt:opt.clip | 0.410 | 0.414 | 0.5 | 2 |
| opt:opt.polar_muon_adamw | 39.766 | 41.454 | 49.0 | 2 |
| opt:opt.muon | 33.715 | 35.244 | 41.5 | 2 |
| opt:opt.muon.ns | 38.409 | 39.275 | 47.3 | 3 |
| opt:opt.adamw | 5.844 | 6.186 | 7.2 | 2 |
| opt:opt.moe_bias | 0.018 | 0.022 | 0.0 | 3 |
| opt:opt.zero_grad | 0.332 | 0.374 | 0.4 | 3 |

## Time by part type (sum over layers)

| part type | median ms sum | % of step |
| :--- | ---: | ---: |
| opt | 40.504 | 49.9 |
| opt:opt.polar_muon_adamw | 39.766 | 49.0 |
| opt:opt.muon.ns | 38.409 | 47.3 |
| opt:opt.muon | 33.715 | 41.5 |
| bwd | 23.431 | 28.9 |
| fwd | 19.111 | 23.5 |
| bwd:head+loss | 12.281 | 15.1 |
| bwd:stack | 10.822 | 13.3 |
| bwd:block* | 10.781 | 13.3 |
| fwd:head+loss | 10.460 | 12.9 |
| fwd:stack | 7.712 | 9.5 |
| fwd:block* | 7.277 | 9.0 |
| opt:opt.adamw | 5.844 | 7.2 |
| bwd:block*.grad | 4.943 | 6.1 |
| bwd.recompute:block* | 3.223 | 4.0 |
| bwd.invert:block* | 3.213 | 4.0 |
| fwd:block*.attn.sdpa | 2.982 | 3.7 |
| bwd.invert:block*.attn.sdpa | 1.719 | 2.1 |
| bwd.recompute:block*.attn.sdpa | 1.717 | 2.1 |
| fwd:block*.mlp | 1.457 | 1.8 |
| fwd:block*.attn.qkv | 1.201 | 1.5 |
| fwd:block*.attn.proj | 1.094 | 1.3 |
| data | 0.917 | 1.1 |
| fwd:embed | 0.778 | 1.0 |
| fwd:embed.ke | 0.766 | 0.9 |
| bwd.recompute:block*.mlp | 0.510 | 0.6 |
| bwd.invert:block*.mlp | 0.506 | 0.6 |
| fwd:block*.ln1 | 0.424 | 0.5 |
| opt:opt.clip | 0.410 | 0.5 |
| fwd:block*.ln2 | 0.380 | 0.5 |
| opt:opt.zero_grad | 0.332 | 0.4 |
| bwd:embed | 0.318 | 0.4 |
| bwd.invert:block*.attn.qkv | 0.187 | 0.2 |
| bwd.recompute:block*.attn.qkv | 0.187 | 0.2 |
| bwd.recompute:block*.attn.proj | 0.182 | 0.2 |
| bwd.invert:block*.attn.proj | 0.180 | 0.2 |
| bwd.recompute:block*.ln1 | 0.124 | 0.2 |
| bwd.invert:block*.ln1 | 0.123 | 0.2 |
| bwd.invert:block*.ln2 | 0.119 | 0.1 |
| bwd.recompute:block*.ln2 | 0.117 | 0.1 |
| opt:opt.moe_bias | 0.018 | 0.0 |

## Five slowest leaf parts

1. `opt:opt.muon.ns` — 38.409 ms (47.3% of step)
2. `bwd:block0.grad` — 0.834 ms (1.0% of step)
3. `bwd:block1.grad` — 0.824 ms (1.0% of step)
4. `bwd:block4.grad` — 0.822 ms (1.0% of step)
5. `bwd:block5.grad` — 0.821 ms (1.0% of step)
