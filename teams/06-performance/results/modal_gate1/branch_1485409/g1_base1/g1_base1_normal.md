# Bench report — g1_base1_normal

**GPU:** NVIDIA A100-SXM4-40GB  |  **dtype:** bf16  |  **B x T:** 16 x 256  |  **torch:** 2.15.0+cu132
**commit:** `14854097c57056f326efd0c7a40cc036a73bbc94`  |  **tag:** g1_base1_normal

## Step (clean)

- median: 65.058 ms
- p10..p90: 63.084 .. 67.089 ms
- tokens/s: 62,959
- MFU: 5.0%  |  HFU: 5.6%

## Diagnostics

### CUDA timing-event allocations

- [OK] clean: events_created_during_steps=0
- [OK] layer: events_created_during_steps=0
- [OK] layer.inner_pass: events_created_during_steps=0

### Benchmark warnings

- [warn] recorder overhead 2.1% > 2.0%: layer numbers are flagged
- [warn] 6 gated part(s) have p10..p90 spread > 10%, so may miss the 5% check: data, fwd:embed, fwd:block0, opt, opt:opt.polar_muon_adamw, opt:opt.muon

## Regions

| part | median ms | p90 | % of step | level |
| :--- | ---: | ---: | ---: | ---: |
| data | 0.620 | 0.711 | 1.0 | 1 |
| fwd | 16.887 | 17.206 | 26.0 | 1 |
| fwd:embed | 0.649 | 0.687 | 1.0 | 2 |
| fwd:embed.ke | 0.644 | 0.687 | 1.0 | 3 |
| fwd:stack | 5.634 | 5.902 | 8.7 | 1 |
| fwd:block0 | 0.950 | 1.099 | 1.5 | 2 |
| fwd:block0.ln1 | 0.067 | 0.078 | 0.1 | 3 |
| fwd:block0.attn.qkv | 0.180 | 0.215 | 0.3 | 3 |
| fwd:block0.attn.sdpa | 0.443 | 0.476 | 0.7 | 3 |
| fwd:block0.attn.proj | 0.128 | 0.155 | 0.2 | 3 |
| fwd:block0.ln2 | 0.051 | 0.059 | 0.1 | 3 |
| fwd:block0.mlp | 0.197 | 0.228 | 0.3 | 3 |
| fwd:block1 | 0.895 | 0.932 | 1.4 | 2 |
| fwd:block1.ln1 | 0.051 | 0.058 | 0.1 | 3 |
| fwd:block1.attn.qkv | 0.144 | 0.168 | 0.2 | 3 |
| fwd:block1.attn.sdpa | 0.397 | 0.422 | 0.6 | 3 |
| fwd:block1.attn.proj | 0.112 | 0.137 | 0.2 | 3 |
| fwd:block1.ln2 | 0.050 | 0.056 | 0.1 | 3 |
| fwd:block1.mlp | 0.184 | 0.214 | 0.3 | 3 |
| fwd:block2 | 0.890 | 0.917 | 1.4 | 2 |
| fwd:block2.ln1 | 0.049 | 0.058 | 0.1 | 3 |
| fwd:block2.attn.qkv | 0.142 | 0.166 | 0.2 | 3 |
| fwd:block2.attn.sdpa | 0.395 | 0.420 | 0.6 | 3 |
| fwd:block2.attn.proj | 0.106 | 0.137 | 0.2 | 3 |
| fwd:block2.ln2 | 0.049 | 0.056 | 0.1 | 3 |
| fwd:block2.mlp | 0.182 | 0.215 | 0.3 | 3 |
| fwd:block3 | 0.886 | 0.914 | 1.4 | 2 |
| fwd:block3.ln1 | 0.049 | 0.058 | 0.1 | 3 |
| fwd:block3.attn.qkv | 0.143 | 0.166 | 0.2 | 3 |
| fwd:block3.attn.sdpa | 0.395 | 0.422 | 0.6 | 3 |
| fwd:block3.attn.proj | 0.103 | 0.130 | 0.2 | 3 |
| fwd:block3.ln2 | 0.049 | 0.057 | 0.1 | 3 |
| fwd:block3.mlp | 0.181 | 0.211 | 0.3 | 3 |
| fwd:block4 | 0.885 | 0.906 | 1.4 | 2 |
| fwd:block4.ln1 | 0.049 | 0.057 | 0.1 | 3 |
| fwd:block4.attn.qkv | 0.144 | 0.172 | 0.2 | 3 |
| fwd:block4.attn.sdpa | 0.395 | 0.417 | 0.6 | 3 |
| fwd:block4.attn.proj | 0.104 | 0.136 | 0.2 | 3 |
| fwd:block4.ln2 | 0.049 | 0.059 | 0.1 | 3 |
| fwd:block4.mlp | 0.184 | 0.216 | 0.3 | 3 |
| fwd:block5 | 0.882 | 0.910 | 1.4 | 2 |
| fwd:block5.ln1 | 0.050 | 0.060 | 0.1 | 3 |
| fwd:block5.attn.qkv | 0.141 | 0.165 | 0.2 | 3 |
| fwd:block5.attn.sdpa | 0.394 | 0.417 | 0.6 | 3 |
| fwd:block5.attn.proj | 0.100 | 0.134 | 0.2 | 3 |
| fwd:block5.ln2 | 0.049 | 0.058 | 0.1 | 3 |
| fwd:block5.mlp | 0.184 | 0.214 | 0.3 | 3 |
| fwd:head+loss | 10.479 | 10.492 | 16.1 | 2 |
| bwd | 23.530 | 23.544 | 36.2 | 1 |
| bwd:head+loss | 12.391 | 12.402 | 19.0 | 2 |
| bwd:stack | 10.811 | 10.821 | 16.6 | 1 |
| bwd:block5 | 1.791 | 1.794 | 2.8 | 2 |
| bwd.invert:block5 | 0.539 | 0.541 | 0.8 | 3 |
| bwd.invert:block5.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block5.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block5.attn.sdpa | 0.286 | 0.289 | 0.4 | 3 |
| bwd.invert:block5.attn.proj | 0.030 | 0.032 | 0.0 | 3 |
| bwd.invert:block5.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block5.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd.recompute:block5 | 0.539 | 0.541 | 0.8 | 3 |
| bwd.recompute:block5.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block5.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block5.attn.sdpa | 0.284 | 0.286 | 0.4 | 3 |
| bwd.recompute:block5.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block5.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block5.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd:block5.grad | 0.822 | 0.825 | 1.3 | 3 |
| bwd:block4 | 1.799 | 1.803 | 2.8 | 2 |
| bwd.invert:block4 | 0.540 | 0.543 | 0.8 | 3 |
| bwd.invert:block4.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block4.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block4.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.invert:block4.attn.proj | 0.031 | 0.031 | 0.0 | 3 |
| bwd.invert:block4.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.invert:block4.mlp | 0.085 | 0.085 | 0.1 | 3 |
| bwd.recompute:block4 | 0.542 | 0.545 | 0.8 | 3 |
| bwd.recompute:block4.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block4.attn.qkv | 0.032 | 0.032 | 0.0 | 3 |
| bwd.recompute:block4.attn.sdpa | 0.287 | 0.288 | 0.4 | 3 |
| bwd.recompute:block4.attn.proj | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block4.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block4.mlp | 0.086 | 0.087 | 0.1 | 3 |
| bwd:block4.grad | 0.823 | 0.826 | 1.3 | 3 |
| bwd:block3 | 1.794 | 1.798 | 2.8 | 2 |
| bwd.invert:block3 | 0.539 | 0.541 | 0.8 | 3 |
| bwd.invert:block3.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block3.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block3.attn.sdpa | 0.286 | 0.287 | 0.4 | 3 |
| bwd.invert:block3.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block3.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block3.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd.recompute:block3 | 0.541 | 0.543 | 0.8 | 3 |
| bwd.recompute:block3.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block3.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block3.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.recompute:block3.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block3.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block3.mlp | 0.085 | 0.085 | 0.1 | 3 |
| bwd:block3.grad | 0.823 | 0.825 | 1.3 | 3 |
| bwd:block2 | 1.790 | 1.794 | 2.8 | 2 |
| bwd.invert:block2 | 0.540 | 0.542 | 0.8 | 3 |
| bwd.invert:block2.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block2.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block2.attn.sdpa | 0.287 | 0.289 | 0.4 | 3 |
| bwd.invert:block2.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block2.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block2.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd.recompute:block2 | 0.543 | 0.545 | 0.8 | 3 |
| bwd.recompute:block2.ln1 | 0.020 | 0.021 | 0.0 | 3 |
| bwd.recompute:block2.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block2.attn.sdpa | 0.287 | 0.289 | 0.4 | 3 |
| bwd.recompute:block2.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block2.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block2.mlp | 0.086 | 0.087 | 0.1 | 3 |
| bwd:block2.grad | 0.819 | 0.823 | 1.3 | 3 |
| bwd:block1 | 1.798 | 1.801 | 2.8 | 2 |
| bwd.invert:block1 | 0.543 | 0.545 | 0.8 | 3 |
| bwd.invert:block1.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block1.attn.qkv | 0.032 | 0.032 | 0.0 | 3 |
| bwd.invert:block1.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.invert:block1.attn.proj | 0.032 | 0.032 | 0.0 | 3 |
| bwd.invert:block1.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block1.mlp | 0.086 | 0.087 | 0.1 | 3 |
| bwd.recompute:block1 | 0.542 | 0.544 | 0.8 | 3 |
| bwd.recompute:block1.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block1.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block1.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.recompute:block1.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block1.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block1.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd:block1.grad | 0.824 | 0.828 | 1.3 | 3 |
| bwd:block0 | 1.795 | 1.799 | 2.8 | 2 |
| bwd.invert:block0 | 0.539 | 0.542 | 0.8 | 3 |
| bwd.invert:block0.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block0.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block0.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.invert:block0.attn.proj | 0.030 | 0.030 | 0.0 | 3 |
| bwd.invert:block0.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block0.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd.recompute:block0 | 0.541 | 0.544 | 0.8 | 3 |
| bwd.recompute:block0.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block0.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block0.attn.sdpa | 0.287 | 0.289 | 0.4 | 3 |
| bwd.recompute:block0.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block0.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block0.mlp | 0.085 | 0.087 | 0.1 | 3 |
| bwd:block0.grad | 0.824 | 0.827 | 1.3 | 3 |
| bwd:embed | 0.318 | 0.319 | 0.5 | 2 |
| opt | 24.457 | 27.399 | 37.6 | 1 |
| opt:opt.clip | 0.410 | 0.414 | 0.6 | 2 |
| opt:opt.polar_muon_adamw | 23.856 | 26.722 | 36.7 | 2 |
| opt:opt.muon | 18.911 | 21.449 | 29.1 | 2 |
| opt:opt.muon.ns | 24.831 | 28.124 | 38.2 | 3 |
| opt:opt.adamw | 4.845 | 5.129 | 7.4 | 2 |
| opt:opt.moe_bias | 0.014 | 0.017 | 0.0 | 3 |
| opt:opt.zero_grad | 0.214 | 0.263 | 0.3 | 3 |

## Time by part type (sum over layers)

| part type | median ms sum | % of step |
| :--- | ---: | ---: |
| opt:opt.muon.ns | 24.831 | 38.2 |
| opt | 24.457 | 37.6 |
| opt:opt.polar_muon_adamw | 23.856 | 36.7 |
| bwd | 23.530 | 36.2 |
| opt:opt.muon | 18.911 | 29.1 |
| fwd | 16.887 | 26.0 |
| bwd:head+loss | 12.391 | 19.0 |
| bwd:stack | 10.811 | 16.6 |
| bwd:block* | 10.767 | 16.6 |
| fwd:head+loss | 10.479 | 16.1 |
| fwd:stack | 5.634 | 8.7 |
| fwd:block* | 5.388 | 8.3 |
| bwd:block*.grad | 4.937 | 7.6 |
| opt:opt.adamw | 4.845 | 7.4 |
| bwd.recompute:block* | 3.247 | 5.0 |
| bwd.invert:block* | 3.238 | 5.0 |
| fwd:block*.attn.sdpa | 2.420 | 3.7 |
| bwd.invert:block*.attn.sdpa | 1.715 | 2.6 |
| bwd.recompute:block*.attn.sdpa | 1.714 | 2.6 |
| fwd:block*.mlp | 1.113 | 1.7 |
| fwd:block*.attn.qkv | 0.895 | 1.4 |
| fwd:block*.attn.proj | 0.654 | 1.0 |
| fwd:embed | 0.649 | 1.0 |
| fwd:embed.ke | 0.644 | 1.0 |
| data | 0.620 | 1.0 |
| bwd.recompute:block*.mlp | 0.510 | 0.8 |
| bwd.invert:block*.mlp | 0.505 | 0.8 |
| opt:opt.clip | 0.410 | 0.6 |
| bwd:embed | 0.318 | 0.5 |
| fwd:block*.ln1 | 0.315 | 0.5 |
| fwd:block*.ln2 | 0.298 | 0.5 |
| opt:opt.zero_grad | 0.214 | 0.3 |
| bwd.invert:block*.attn.qkv | 0.189 | 0.3 |
| bwd.recompute:block*.attn.qkv | 0.188 | 0.3 |
| bwd.invert:block*.attn.proj | 0.183 | 0.3 |
| bwd.recompute:block*.attn.proj | 0.182 | 0.3 |
| bwd.invert:block*.ln1 | 0.126 | 0.2 |
| bwd.recompute:block*.ln1 | 0.126 | 0.2 |
| bwd.invert:block*.ln2 | 0.120 | 0.2 |
| bwd.recompute:block*.ln2 | 0.120 | 0.2 |
| opt:opt.moe_bias | 0.014 | 0.0 |

## Five slowest leaf parts

1. `opt:opt.muon.ns` — 24.831 ms (38.2% of step)
2. `bwd:block1.grad` — 0.824 ms (1.3% of step)
3. `bwd:block0.grad` — 0.824 ms (1.3% of step)
4. `bwd:block4.grad` — 0.823 ms (1.3% of step)
5. `bwd:block3.grad` — 0.823 ms (1.3% of step)
