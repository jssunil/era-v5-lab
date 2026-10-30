# Bench report — pr29_a100real4_normal

**GPU:** NVIDIA A100-SXM4-40GB  |  **dtype:** bf16  |  **B x T:** 16 x 256  |  **torch:** 2.15.0+cu132
**commit:** `dc0b1703d7d0c51b152bd37d81f6fc2b3ddcf64d`  |  **tag:** pr29_a100real4_normal

## Step (clean)

- median: 65.307 ms
- p10..p90: 63.265 .. 70.784 ms
- tokens/s: 62,719
- MFU: 5.0%  |  HFU: 5.5%

## Diagnostics

### CUDA timing-event allocations

- [OK] clean: events_created_during_steps=0
- [OK] layer: events_created_during_steps=0
- [OK] layer.inner_pass: events_created_during_steps=0

### Benchmark warnings

- [warn] recorder overhead 2.2% > 2.0%: layer numbers are flagged
- [warn] 5 gated part(s) have p10..p90 spread > 10%, so may miss the 5% check: data, fwd:block0, opt, opt:opt.polar_muon_adamw, opt:opt.muon

## Regions

| part | median ms | p90 | % of step | level |
| :--- | ---: | ---: | ---: | ---: |
| data | 0.734 | 0.795 | 1.1 | 1 |
| fwd | 17.026 | 17.294 | 26.1 | 1 |
| fwd:embed | 0.671 | 0.697 | 1.0 | 2 |
| fwd:embed.ke | 0.640 | 0.664 | 1.0 | 3 |
| fwd:stack | 5.787 | 6.000 | 8.9 | 1 |
| fwd:block0 | 1.071 | 1.157 | 1.6 | 2 |
| fwd:block0.ln1 | 0.063 | 0.076 | 0.1 | 3 |
| fwd:block0.attn.qkv | 0.181 | 0.204 | 0.3 | 3 |
| fwd:block0.attn.sdpa | 0.445 | 0.477 | 0.7 | 3 |
| fwd:block0.attn.proj | 0.123 | 0.142 | 0.2 | 3 |
| fwd:block0.ln2 | 0.052 | 0.055 | 0.1 | 3 |
| fwd:block0.mlp | 0.190 | 0.214 | 0.3 | 3 |
| fwd:block1 | 0.902 | 0.935 | 1.4 | 2 |
| fwd:block1.ln1 | 0.051 | 0.054 | 0.1 | 3 |
| fwd:block1.attn.qkv | 0.143 | 0.164 | 0.2 | 3 |
| fwd:block1.attn.sdpa | 0.399 | 0.422 | 0.6 | 3 |
| fwd:block1.attn.proj | 0.102 | 0.120 | 0.2 | 3 |
| fwd:block1.ln2 | 0.050 | 0.053 | 0.1 | 3 |
| fwd:block1.mlp | 0.182 | 0.207 | 0.3 | 3 |
| fwd:block2 | 0.892 | 0.920 | 1.4 | 2 |
| fwd:block2.ln1 | 0.050 | 0.053 | 0.1 | 3 |
| fwd:block2.attn.qkv | 0.141 | 0.164 | 0.2 | 3 |
| fwd:block2.attn.sdpa | 0.397 | 0.416 | 0.6 | 3 |
| fwd:block2.attn.proj | 0.098 | 0.122 | 0.2 | 3 |
| fwd:block2.ln2 | 0.050 | 0.052 | 0.1 | 3 |
| fwd:block2.mlp | 0.182 | 0.204 | 0.3 | 3 |
| fwd:block3 | 0.882 | 0.910 | 1.4 | 2 |
| fwd:block3.ln1 | 0.049 | 0.052 | 0.1 | 3 |
| fwd:block3.attn.qkv | 0.141 | 0.154 | 0.2 | 3 |
| fwd:block3.attn.sdpa | 0.396 | 0.418 | 0.6 | 3 |
| fwd:block3.attn.proj | 0.101 | 0.123 | 0.2 | 3 |
| fwd:block3.ln2 | 0.049 | 0.060 | 0.1 | 3 |
| fwd:block3.mlp | 0.180 | 0.206 | 0.3 | 3 |
| fwd:block4 | 0.882 | 0.905 | 1.4 | 2 |
| fwd:block4.ln1 | 0.049 | 0.052 | 0.1 | 3 |
| fwd:block4.attn.qkv | 0.141 | 0.164 | 0.2 | 3 |
| fwd:block4.attn.sdpa | 0.397 | 0.418 | 0.6 | 3 |
| fwd:block4.attn.proj | 0.098 | 0.122 | 0.2 | 3 |
| fwd:block4.ln2 | 0.050 | 0.052 | 0.1 | 3 |
| fwd:block4.mlp | 0.181 | 0.196 | 0.3 | 3 |
| fwd:block5 | 0.881 | 0.902 | 1.3 | 2 |
| fwd:block5.ln1 | 0.049 | 0.052 | 0.1 | 3 |
| fwd:block5.attn.qkv | 0.139 | 0.162 | 0.2 | 3 |
| fwd:block5.attn.sdpa | 0.396 | 0.415 | 0.6 | 3 |
| fwd:block5.attn.proj | 0.099 | 0.120 | 0.2 | 3 |
| fwd:block5.ln2 | 0.050 | 0.052 | 0.1 | 3 |
| fwd:block5.mlp | 0.179 | 0.203 | 0.3 | 3 |
| fwd:head+loss | 10.435 | 10.450 | 16.0 | 2 |
| bwd | 23.441 | 23.457 | 35.9 | 1 |
| bwd:head+loss | 12.282 | 12.292 | 18.8 | 2 |
| bwd:stack | 10.819 | 10.829 | 16.6 | 1 |
| bwd:block5 | 1.795 | 1.798 | 2.7 | 2 |
| bwd.invert:block5 | 0.537 | 0.539 | 0.8 | 3 |
| bwd.invert:block5.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block5.attn.qkv | 0.032 | 0.032 | 0.0 | 3 |
| bwd.invert:block5.attn.sdpa | 0.288 | 0.290 | 0.4 | 3 |
| bwd.invert:block5.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block5.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block5.mlp | 0.083 | 0.085 | 0.1 | 3 |
| bwd.recompute:block5 | 0.537 | 0.539 | 0.8 | 3 |
| bwd.recompute:block5.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block5.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block5.attn.sdpa | 0.286 | 0.287 | 0.4 | 3 |
| bwd.recompute:block5.attn.proj | 0.030 | 0.030 | 0.0 | 3 |
| bwd.recompute:block5.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block5.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd:block5.grad | 0.823 | 0.826 | 1.3 | 3 |
| bwd:block4 | 1.798 | 1.802 | 2.8 | 2 |
| bwd.invert:block4 | 0.537 | 0.540 | 0.8 | 3 |
| bwd.invert:block4.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block4.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block4.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.invert:block4.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block4.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.invert:block4.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd.recompute:block4 | 0.540 | 0.542 | 0.8 | 3 |
| bwd.recompute:block4.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block4.attn.qkv | 0.031 | 0.031 | 0.0 | 3 |
| bwd.recompute:block4.attn.sdpa | 0.287 | 0.289 | 0.4 | 3 |
| bwd.recompute:block4.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block4.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block4.mlp | 0.086 | 0.087 | 0.1 | 3 |
| bwd:block4.grad | 0.823 | 0.826 | 1.3 | 3 |
| bwd:block3 | 1.792 | 1.795 | 2.7 | 2 |
| bwd.invert:block3 | 0.535 | 0.537 | 0.8 | 3 |
| bwd.invert:block3.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block3.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block3.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.invert:block3.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block3.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block3.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd.recompute:block3 | 0.537 | 0.540 | 0.8 | 3 |
| bwd.recompute:block3.ln1 | 0.022 | 0.022 | 0.0 | 3 |
| bwd.recompute:block3.attn.qkv | 0.031 | 0.033 | 0.0 | 3 |
| bwd.recompute:block3.attn.sdpa | 0.285 | 0.286 | 0.4 | 3 |
| bwd.recompute:block3.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block3.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block3.mlp | 0.085 | 0.085 | 0.1 | 3 |
| bwd:block3.grad | 0.822 | 0.825 | 1.3 | 3 |
| bwd:block2 | 1.796 | 1.800 | 2.8 | 2 |
| bwd.invert:block2 | 0.536 | 0.539 | 0.8 | 3 |
| bwd.invert:block2.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block2.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block2.attn.sdpa | 0.286 | 0.289 | 0.4 | 3 |
| bwd.invert:block2.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block2.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.invert:block2.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd.recompute:block2 | 0.540 | 0.542 | 0.8 | 3 |
| bwd.recompute:block2.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block2.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block2.attn.sdpa | 0.288 | 0.289 | 0.4 | 3 |
| bwd.recompute:block2.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block2.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block2.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block2.grad | 0.823 | 0.826 | 1.3 | 3 |
| bwd:block1 | 1.801 | 1.804 | 2.8 | 2 |
| bwd.invert:block1 | 0.540 | 0.542 | 0.8 | 3 |
| bwd.invert:block1.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block1.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block1.attn.sdpa | 0.287 | 0.289 | 0.4 | 3 |
| bwd.invert:block1.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block1.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block1.mlp | 0.086 | 0.087 | 0.1 | 3 |
| bwd.recompute:block1 | 0.540 | 0.543 | 0.8 | 3 |
| bwd.recompute:block1.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block1.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block1.attn.sdpa | 0.287 | 0.289 | 0.4 | 3 |
| bwd.recompute:block1.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block1.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.recompute:block1.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd:block1.grad | 0.827 | 0.828 | 1.3 | 3 |
| bwd:block0 | 1.797 | 1.802 | 2.8 | 2 |
| bwd.invert:block0 | 0.538 | 0.540 | 0.8 | 3 |
| bwd.invert:block0.ln1 | 0.021 | 0.023 | 0.0 | 3 |
| bwd.invert:block0.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block0.attn.sdpa | 0.287 | 0.288 | 0.4 | 3 |
| bwd.invert:block0.attn.proj | 0.030 | 0.030 | 0.0 | 3 |
| bwd.invert:block0.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.invert:block0.mlp | 0.084 | 0.084 | 0.1 | 3 |
| bwd.recompute:block0 | 0.538 | 0.540 | 0.8 | 3 |
| bwd.recompute:block0.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block0.attn.qkv | 0.031 | 0.031 | 0.0 | 3 |
| bwd.recompute:block0.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.recompute:block0.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block0.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block0.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block0.grad | 0.824 | 0.827 | 1.3 | 3 |
| bwd:embed | 0.333 | 0.336 | 0.5 | 2 |
| opt | 23.962 | 25.383 | 36.7 | 1 |
| opt:opt.clip | 0.408 | 0.412 | 0.6 | 2 |
| opt:opt.polar_muon_adamw | 23.271 | 24.658 | 35.6 | 2 |
| opt:opt.muon | 18.493 | 19.787 | 28.3 | 2 |
| opt:opt.muon.ns | 23.977 | 25.653 | 36.7 | 3 |
| opt:opt.adamw | 4.616 | 4.749 | 7.1 | 2 |
| opt:opt.moe_bias | 0.014 | 0.015 | 0.0 | 3 |
| opt:opt.zero_grad | 0.226 | 0.272 | 0.3 | 3 |

## Time by part type (sum over layers)

| part type | median ms sum | % of step |
| :--- | ---: | ---: |
| opt:opt.muon.ns | 23.977 | 36.7 |
| opt | 23.962 | 36.7 |
| bwd | 23.441 | 35.9 |
| opt:opt.polar_muon_adamw | 23.271 | 35.6 |
| opt:opt.muon | 18.493 | 28.3 |
| fwd | 17.026 | 26.1 |
| bwd:head+loss | 12.282 | 18.8 |
| bwd:stack | 10.819 | 16.6 |
| bwd:block* | 10.780 | 16.5 |
| fwd:head+loss | 10.435 | 16.0 |
| fwd:stack | 5.787 | 8.9 |
| fwd:block* | 5.509 | 8.4 |
| bwd:block*.grad | 4.944 | 7.6 |
| opt:opt.adamw | 4.616 | 7.1 |
| bwd.recompute:block* | 3.230 | 4.9 |
| bwd.invert:block* | 3.220 | 4.9 |
| fwd:block*.attn.sdpa | 2.431 | 3.7 |
| bwd.invert:block*.attn.sdpa | 1.717 | 2.6 |
| bwd.recompute:block*.attn.sdpa | 1.717 | 2.6 |
| fwd:block*.mlp | 1.095 | 1.7 |
| fwd:block*.attn.qkv | 0.887 | 1.4 |
| data | 0.734 | 1.1 |
| fwd:embed | 0.671 | 1.0 |
| fwd:embed.ke | 0.640 | 1.0 |
| fwd:block*.attn.proj | 0.622 | 1.0 |
| bwd.recompute:block*.mlp | 0.509 | 0.8 |
| bwd.invert:block*.mlp | 0.505 | 0.8 |
| opt:opt.clip | 0.408 | 0.6 |
| bwd:embed | 0.333 | 0.5 |
| fwd:block*.ln1 | 0.312 | 0.5 |
| fwd:block*.ln2 | 0.302 | 0.5 |
| opt:opt.zero_grad | 0.226 | 0.3 |
| bwd.invert:block*.attn.qkv | 0.188 | 0.3 |
| bwd.recompute:block*.attn.qkv | 0.187 | 0.3 |
| bwd.invert:block*.attn.proj | 0.180 | 0.3 |
| bwd.recompute:block*.attn.proj | 0.180 | 0.3 |
| bwd.invert:block*.ln1 | 0.125 | 0.2 |
| bwd.recompute:block*.ln1 | 0.125 | 0.2 |
| bwd.recompute:block*.ln2 | 0.120 | 0.2 |
| bwd.invert:block*.ln2 | 0.119 | 0.2 |
| opt:opt.moe_bias | 0.014 | 0.0 |

## Five slowest leaf parts

1. `opt:opt.muon.ns` — 23.977 ms (36.7% of step)
2. `bwd:block1.grad` — 0.827 ms (1.3% of step)
3. `bwd:block0.grad` — 0.824 ms (1.3% of step)
4. `bwd:block5.grad` — 0.823 ms (1.3% of step)
5. `bwd:block4.grad` — 0.823 ms (1.3% of step)
