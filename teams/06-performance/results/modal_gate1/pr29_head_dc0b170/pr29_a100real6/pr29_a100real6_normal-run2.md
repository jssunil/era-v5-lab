# Bench report — pr29_a100real6_normal-run2

**GPU:** NVIDIA A100-SXM4-40GB  |  **dtype:** bf16  |  **B x T:** 16 x 256  |  **torch:** 2.15.0+cu132
**commit:** `dc0b1703d7d0c51b152bd37d81f6fc2b3ddcf64d`  |  **tag:** pr29_a100real6_normal-run2

## Step (clean)

- median: 66.260 ms
- p10..p90: 60.871 .. 74.447 ms
- tokens/s: 61,817
- MFU: 4.9%  |  HFU: 5.5%

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
| data | 0.516 | 0.754 | 0.8 | 1 |
| fwd | 16.594 | 17.356 | 25.0 | 1 |
| fwd:embed | 0.622 | 0.687 | 0.9 | 2 |
| fwd:embed.ke | 0.641 | 0.722 | 1.0 | 3 |
| fwd:stack | 5.413 | 6.045 | 8.2 | 1 |
| fwd:block0 | 0.858 | 1.138 | 1.3 | 2 |
| fwd:block0.ln1 | 0.063 | 0.081 | 0.1 | 3 |
| fwd:block0.attn.qkv | 0.178 | 0.256 | 0.3 | 3 |
| fwd:block0.attn.sdpa | 0.443 | 0.531 | 0.7 | 3 |
| fwd:block0.attn.proj | 0.128 | 0.173 | 0.2 | 3 |
| fwd:block0.ln2 | 0.051 | 0.067 | 0.1 | 3 |
| fwd:block0.mlp | 0.191 | 0.237 | 0.3 | 3 |
| fwd:block1 | 0.876 | 0.956 | 1.3 | 2 |
| fwd:block1.ln1 | 0.050 | 0.061 | 0.1 | 3 |
| fwd:block1.attn.qkv | 0.146 | 0.171 | 0.2 | 3 |
| fwd:block1.attn.sdpa | 0.402 | 0.452 | 0.6 | 3 |
| fwd:block1.attn.proj | 0.115 | 0.160 | 0.2 | 3 |
| fwd:block1.ln2 | 0.049 | 0.057 | 0.1 | 3 |
| fwd:block1.mlp | 0.184 | 0.220 | 0.3 | 3 |
| fwd:block2 | 0.869 | 0.940 | 1.3 | 2 |
| fwd:block2.ln1 | 0.049 | 0.056 | 0.1 | 3 |
| fwd:block2.attn.qkv | 0.141 | 0.170 | 0.2 | 3 |
| fwd:block2.attn.sdpa | 0.398 | 0.445 | 0.6 | 3 |
| fwd:block2.attn.proj | 0.111 | 0.160 | 0.2 | 3 |
| fwd:block2.ln2 | 0.049 | 0.056 | 0.1 | 3 |
| fwd:block2.mlp | 0.186 | 0.214 | 0.3 | 3 |
| fwd:block3 | 0.866 | 0.926 | 1.3 | 2 |
| fwd:block3.ln1 | 0.049 | 0.056 | 0.1 | 3 |
| fwd:block3.attn.qkv | 0.143 | 0.174 | 0.2 | 3 |
| fwd:block3.attn.sdpa | 0.398 | 0.441 | 0.6 | 3 |
| fwd:block3.attn.proj | 0.106 | 0.158 | 0.2 | 3 |
| fwd:block3.ln2 | 0.048 | 0.057 | 0.1 | 3 |
| fwd:block3.mlp | 0.184 | 0.218 | 0.3 | 3 |
| fwd:block4 | 0.865 | 0.932 | 1.3 | 2 |
| fwd:block4.ln1 | 0.049 | 0.056 | 0.1 | 3 |
| fwd:block4.attn.qkv | 0.143 | 0.173 | 0.2 | 3 |
| fwd:block4.attn.sdpa | 0.397 | 0.443 | 0.6 | 3 |
| fwd:block4.attn.proj | 0.109 | 0.150 | 0.2 | 3 |
| fwd:block4.ln2 | 0.049 | 0.057 | 0.1 | 3 |
| fwd:block4.mlp | 0.184 | 0.222 | 0.3 | 3 |
| fwd:block5 | 0.866 | 0.935 | 1.3 | 2 |
| fwd:block5.ln1 | 0.049 | 0.056 | 0.1 | 3 |
| fwd:block5.attn.qkv | 0.143 | 0.175 | 0.2 | 3 |
| fwd:block5.attn.sdpa | 0.393 | 0.434 | 0.6 | 3 |
| fwd:block5.attn.proj | 0.108 | 0.153 | 0.2 | 3 |
| fwd:block5.ln2 | 0.049 | 0.055 | 0.1 | 3 |
| fwd:block5.mlp | 0.185 | 0.217 | 0.3 | 3 |
| fwd:head+loss | 10.469 | 10.480 | 15.8 | 2 |
| bwd | 23.451 | 23.464 | 35.4 | 1 |
| bwd:head+loss | 12.382 | 12.394 | 18.7 | 2 |
| bwd:stack | 10.744 | 10.753 | 16.2 | 1 |
| bwd:block5 | 1.781 | 1.785 | 2.7 | 2 |
| bwd.invert:block5 | 0.534 | 0.536 | 0.8 | 3 |
| bwd.invert:block5.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block5.attn.qkv | 0.031 | 0.031 | 0.0 | 3 |
| bwd.invert:block5.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.invert:block5.attn.proj | 0.030 | 0.032 | 0.0 | 3 |
| bwd.invert:block5.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block5.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd.recompute:block5 | 0.535 | 0.537 | 0.8 | 3 |
| bwd.recompute:block5.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block5.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block5.attn.sdpa | 0.283 | 0.285 | 0.4 | 3 |
| bwd.recompute:block5.attn.proj | 0.030 | 0.030 | 0.0 | 3 |
| bwd.recompute:block5.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.recompute:block5.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd:block5.grad | 0.818 | 0.821 | 1.2 | 3 |
| bwd:block4 | 1.788 | 1.792 | 2.7 | 2 |
| bwd.invert:block4 | 0.536 | 0.538 | 0.8 | 3 |
| bwd.invert:block4.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block4.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block4.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.invert:block4.attn.proj | 0.030 | 0.030 | 0.0 | 3 |
| bwd.invert:block4.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.invert:block4.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd.recompute:block4 | 0.538 | 0.540 | 0.8 | 3 |
| bwd.recompute:block4.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block4.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block4.attn.sdpa | 0.286 | 0.287 | 0.4 | 3 |
| bwd.recompute:block4.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block4.ln2 | 0.020 | 0.021 | 0.0 | 3 |
| bwd.recompute:block4.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block4.grad | 0.818 | 0.822 | 1.2 | 3 |
| bwd:block3 | 1.781 | 1.785 | 2.7 | 2 |
| bwd.invert:block3 | 0.534 | 0.537 | 0.8 | 3 |
| bwd.invert:block3.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block3.attn.qkv | 0.031 | 0.031 | 0.0 | 3 |
| bwd.invert:block3.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.invert:block3.attn.proj | 0.030 | 0.032 | 0.0 | 3 |
| bwd.invert:block3.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block3.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd.recompute:block3 | 0.537 | 0.539 | 0.8 | 3 |
| bwd.recompute:block3.ln1 | 0.021 | 0.023 | 0.0 | 3 |
| bwd.recompute:block3.attn.qkv | 0.031 | 0.033 | 0.0 | 3 |
| bwd.recompute:block3.attn.sdpa | 0.284 | 0.286 | 0.4 | 3 |
| bwd.recompute:block3.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block3.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block3.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd:block3.grad | 0.818 | 0.820 | 1.2 | 3 |
| bwd:block2 | 1.781 | 1.785 | 2.7 | 2 |
| bwd.invert:block2 | 0.535 | 0.538 | 0.8 | 3 |
| bwd.invert:block2.ln1 | 0.022 | 0.022 | 0.0 | 3 |
| bwd.invert:block2.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block2.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.invert:block2.attn.proj | 0.030 | 0.030 | 0.0 | 3 |
| bwd.invert:block2.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.invert:block2.mlp | 0.082 | 0.083 | 0.1 | 3 |
| bwd.recompute:block2 | 0.538 | 0.541 | 0.8 | 3 |
| bwd.recompute:block2.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block2.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block2.attn.sdpa | 0.286 | 0.289 | 0.4 | 3 |
| bwd.recompute:block2.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block2.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block2.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block2.grad | 0.816 | 0.819 | 1.2 | 3 |
| bwd:block1 | 1.788 | 1.792 | 2.7 | 2 |
| bwd.invert:block1 | 0.538 | 0.540 | 0.8 | 3 |
| bwd.invert:block1.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block1.attn.qkv | 0.032 | 0.032 | 0.0 | 3 |
| bwd.invert:block1.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.invert:block1.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block1.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block1.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd.recompute:block1 | 0.538 | 0.541 | 0.8 | 3 |
| bwd.recompute:block1.ln1 | 0.022 | 0.022 | 0.0 | 3 |
| bwd.recompute:block1.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block1.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.recompute:block1.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block1.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block1.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd:block1.grad | 0.820 | 0.822 | 1.2 | 3 |
| bwd:block0 | 1.784 | 1.789 | 2.7 | 2 |
| bwd.invert:block0 | 0.535 | 0.537 | 0.8 | 3 |
| bwd.invert:block0.ln1 | 0.022 | 0.022 | 0.0 | 3 |
| bwd.invert:block0.attn.qkv | 0.031 | 0.033 | 0.0 | 3 |
| bwd.invert:block0.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.invert:block0.attn.proj | 0.029 | 0.030 | 0.0 | 3 |
| bwd.invert:block0.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.invert:block0.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd.recompute:block0 | 0.537 | 0.539 | 0.8 | 3 |
| bwd.recompute:block0.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block0.attn.qkv | 0.031 | 0.031 | 0.0 | 3 |
| bwd.recompute:block0.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.recompute:block0.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block0.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block0.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block0.grad | 0.819 | 0.822 | 1.2 | 3 |
| bwd:embed | 0.315 | 0.317 | 0.5 | 2 |
| opt | 22.025 | 27.308 | 33.2 | 1 |
| opt:opt.clip | 0.410 | 0.414 | 0.6 | 2 |
| opt:opt.polar_muon_adamw | 21.428 | 26.635 | 32.3 | 2 |
| opt:opt.muon | 16.826 | 21.707 | 25.4 | 2 |
| opt:opt.muon.ns | 23.844 | 33.214 | 36.0 | 3 |
| opt:opt.adamw | 4.548 | 5.098 | 6.9 | 2 |
| opt:opt.moe_bias | 0.015 | 0.018 | 0.0 | 3 |
| opt:opt.zero_grad | 0.203 | 0.304 | 0.3 | 3 |

## Time by part type (sum over layers)

| part type | median ms sum | % of step |
| :--- | ---: | ---: |
| opt:opt.muon.ns | 23.844 | 36.0 |
| bwd | 23.451 | 35.4 |
| opt | 22.025 | 33.2 |
| opt:opt.polar_muon_adamw | 21.428 | 32.3 |
| opt:opt.muon | 16.826 | 25.4 |
| fwd | 16.594 | 25.0 |
| bwd:head+loss | 12.382 | 18.7 |
| bwd:stack | 10.744 | 16.2 |
| bwd:block* | 10.702 | 16.2 |
| fwd:head+loss | 10.469 | 15.8 |
| fwd:stack | 5.413 | 8.2 |
| fwd:block* | 5.199 | 7.8 |
| bwd:block*.grad | 4.910 | 7.4 |
| opt:opt.adamw | 4.548 | 6.9 |
| bwd.recompute:block* | 3.220 | 4.9 |
| bwd.invert:block* | 3.210 | 4.8 |
| fwd:block*.attn.sdpa | 2.431 | 3.7 |
| bwd.invert:block*.attn.sdpa | 1.709 | 2.6 |
| bwd.recompute:block*.attn.sdpa | 1.709 | 2.6 |
| fwd:block*.mlp | 1.115 | 1.7 |
| fwd:block*.attn.qkv | 0.895 | 1.4 |
| fwd:block*.attn.proj | 0.676 | 1.0 |
| fwd:embed.ke | 0.641 | 1.0 |
| fwd:embed | 0.622 | 0.9 |
| data | 0.516 | 0.8 |
| bwd.recompute:block*.mlp | 0.507 | 0.8 |
| bwd.invert:block*.mlp | 0.501 | 0.8 |
| opt:opt.clip | 0.410 | 0.6 |
| bwd:embed | 0.315 | 0.5 |
| fwd:block*.ln1 | 0.310 | 0.5 |
| fwd:block*.ln2 | 0.295 | 0.4 |
| opt:opt.zero_grad | 0.203 | 0.3 |
| bwd.invert:block*.attn.qkv | 0.187 | 0.3 |
| bwd.recompute:block*.attn.qkv | 0.186 | 0.3 |
| bwd.recompute:block*.attn.proj | 0.180 | 0.3 |
| bwd.invert:block*.attn.proj | 0.178 | 0.3 |
| bwd.invert:block*.ln1 | 0.125 | 0.2 |
| bwd.recompute:block*.ln1 | 0.124 | 0.2 |
| bwd.invert:block*.ln2 | 0.120 | 0.2 |
| bwd.recompute:block*.ln2 | 0.120 | 0.2 |
| opt:opt.moe_bias | 0.015 | 0.0 |

## Five slowest leaf parts

1. `opt:opt.muon.ns` — 23.844 ms (36.0% of step)
2. `bwd:block1.grad` — 0.820 ms (1.2% of step)
3. `bwd:block0.grad` — 0.819 ms (1.2% of step)
4. `bwd:block5.grad` — 0.818 ms (1.2% of step)
5. `bwd:block4.grad` — 0.818 ms (1.2% of step)
