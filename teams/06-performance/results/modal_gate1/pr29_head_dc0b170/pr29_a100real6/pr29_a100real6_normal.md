# Bench report — pr29_a100real6_normal

**GPU:** NVIDIA A100-SXM4-40GB  |  **dtype:** bf16  |  **B x T:** 16 x 256  |  **torch:** 2.15.0+cu132
**commit:** `dc0b1703d7d0c51b152bd37d81f6fc2b3ddcf64d`  |  **tag:** pr29_a100real6_normal

## Step (clean)

- median: 66.063 ms
- p10..p90: 61.595 .. 72.215 ms
- tokens/s: 62,002
- MFU: 4.9%  |  HFU: 5.5%

## Diagnostics

### CUDA timing-event allocations

- [OK] clean: events_created_during_steps=0
- [OK] layer: events_created_during_steps=0
- [OK] layer.inner_pass: events_created_during_steps=0

### Benchmark warnings

- [warn] 9 gated part(s) have p10..p90 spread > 10%, so may miss the 5% check: data, fwd:embed, fwd:stack, fwd:block0, fwd:block1, opt (+3 more)

## Regions

| part | median ms | p90 | % of step | level |
| :--- | ---: | ---: | ---: | ---: |
| data | 0.697 | 0.842 | 1.1 | 1 |
| fwd | 17.091 | 17.714 | 25.9 | 1 |
| fwd:embed | 0.672 | 0.730 | 1.0 | 2 |
| fwd:embed.ke | 0.653 | 0.711 | 1.0 | 3 |
| fwd:stack | 5.805 | 6.307 | 8.8 | 1 |
| fwd:block0 | 1.068 | 1.260 | 1.6 | 2 |
| fwd:block0.ln1 | 0.070 | 0.080 | 0.1 | 3 |
| fwd:block0.attn.qkv | 0.194 | 0.249 | 0.3 | 3 |
| fwd:block0.attn.sdpa | 0.458 | 0.536 | 0.7 | 3 |
| fwd:block0.attn.proj | 0.142 | 0.165 | 0.2 | 3 |
| fwd:block0.ln2 | 0.053 | 0.067 | 0.1 | 3 |
| fwd:block0.mlp | 0.202 | 0.233 | 0.3 | 3 |
| fwd:block1 | 0.912 | 0.989 | 1.4 | 2 |
| fwd:block1.ln1 | 0.052 | 0.058 | 0.1 | 3 |
| fwd:block1.attn.qkv | 0.147 | 0.175 | 0.2 | 3 |
| fwd:block1.attn.sdpa | 0.409 | 0.436 | 0.6 | 3 |
| fwd:block1.attn.proj | 0.114 | 0.159 | 0.2 | 3 |
| fwd:block1.ln2 | 0.050 | 0.057 | 0.1 | 3 |
| fwd:block1.mlp | 0.189 | 0.225 | 0.3 | 3 |
| fwd:block2 | 0.902 | 0.951 | 1.4 | 2 |
| fwd:block2.ln1 | 0.050 | 0.057 | 0.1 | 3 |
| fwd:block2.attn.qkv | 0.148 | 0.170 | 0.2 | 3 |
| fwd:block2.attn.sdpa | 0.399 | 0.448 | 0.6 | 3 |
| fwd:block2.attn.proj | 0.110 | 0.155 | 0.2 | 3 |
| fwd:block2.ln2 | 0.050 | 0.057 | 0.1 | 3 |
| fwd:block2.mlp | 0.187 | 0.218 | 0.3 | 3 |
| fwd:block3 | 0.897 | 0.941 | 1.4 | 2 |
| fwd:block3.ln1 | 0.050 | 0.056 | 0.1 | 3 |
| fwd:block3.attn.qkv | 0.147 | 0.173 | 0.2 | 3 |
| fwd:block3.attn.sdpa | 0.397 | 0.441 | 0.6 | 3 |
| fwd:block3.attn.proj | 0.111 | 0.152 | 0.2 | 3 |
| fwd:block3.ln2 | 0.050 | 0.066 | 0.1 | 3 |
| fwd:block3.mlp | 0.190 | 0.222 | 0.3 | 3 |
| fwd:block4 | 0.892 | 0.945 | 1.4 | 2 |
| fwd:block4.ln1 | 0.050 | 0.057 | 0.1 | 3 |
| fwd:block4.attn.qkv | 0.146 | 0.169 | 0.2 | 3 |
| fwd:block4.attn.sdpa | 0.398 | 0.438 | 0.6 | 3 |
| fwd:block4.attn.proj | 0.111 | 0.155 | 0.2 | 3 |
| fwd:block4.ln2 | 0.051 | 0.058 | 0.1 | 3 |
| fwd:block4.mlp | 0.190 | 0.222 | 0.3 | 3 |
| fwd:block5 | 0.884 | 0.942 | 1.3 | 2 |
| fwd:block5.ln1 | 0.050 | 0.057 | 0.1 | 3 |
| fwd:block5.attn.qkv | 0.145 | 0.175 | 0.2 | 3 |
| fwd:block5.attn.sdpa | 0.396 | 0.435 | 0.6 | 3 |
| fwd:block5.attn.proj | 0.111 | 0.153 | 0.2 | 3 |
| fwd:block5.ln2 | 0.050 | 0.054 | 0.1 | 3 |
| fwd:block5.mlp | 0.187 | 0.224 | 0.3 | 3 |
| fwd:head+loss | 10.468 | 10.482 | 15.8 | 2 |
| bwd | 23.513 | 23.535 | 35.6 | 1 |
| bwd:head+loss | 12.380 | 12.392 | 18.7 | 2 |
| bwd:stack | 10.806 | 10.818 | 16.4 | 1 |
| bwd:block5 | 1.790 | 1.794 | 2.7 | 2 |
| bwd.invert:block5 | 0.537 | 0.539 | 0.8 | 3 |
| bwd.invert:block5.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block5.attn.qkv | 0.032 | 0.032 | 0.0 | 3 |
| bwd.invert:block5.attn.sdpa | 0.285 | 0.288 | 0.4 | 3 |
| bwd.invert:block5.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block5.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block5.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd.recompute:block5 | 0.537 | 0.540 | 0.8 | 3 |
| bwd.recompute:block5.ln1 | 0.021 | 0.022 | 0.0 | 3 |
| bwd.recompute:block5.attn.qkv | 0.033 | 0.034 | 0.0 | 3 |
| bwd.recompute:block5.attn.sdpa | 0.284 | 0.285 | 0.4 | 3 |
| bwd.recompute:block5.attn.proj | 0.030 | 0.030 | 0.0 | 3 |
| bwd.recompute:block5.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block5.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd:block5.grad | 0.823 | 0.825 | 1.2 | 3 |
| bwd:block4 | 1.796 | 1.802 | 2.7 | 2 |
| bwd.invert:block4 | 0.539 | 0.542 | 0.8 | 3 |
| bwd.invert:block4.ln1 | 0.022 | 0.022 | 0.0 | 3 |
| bwd.invert:block4.attn.qkv | 0.032 | 0.034 | 0.0 | 3 |
| bwd.invert:block4.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.invert:block4.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block4.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.invert:block4.mlp | 0.085 | 0.085 | 0.1 | 3 |
| bwd.recompute:block4 | 0.541 | 0.543 | 0.8 | 3 |
| bwd.recompute:block4.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block4.attn.qkv | 0.032 | 0.032 | 0.0 | 3 |
| bwd.recompute:block4.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.recompute:block4.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block4.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block4.mlp | 0.086 | 0.087 | 0.1 | 3 |
| bwd:block4.grad | 0.822 | 0.825 | 1.2 | 3 |
| bwd:block3 | 1.792 | 1.796 | 2.7 | 2 |
| bwd.invert:block3 | 0.537 | 0.539 | 0.8 | 3 |
| bwd.invert:block3.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block3.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block3.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.invert:block3.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block3.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block3.mlp | 0.085 | 0.087 | 0.1 | 3 |
| bwd.recompute:block3 | 0.540 | 0.542 | 0.8 | 3 |
| bwd.recompute:block3.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block3.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block3.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.recompute:block3.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block3.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.recompute:block3.mlp | 0.086 | 0.087 | 0.1 | 3 |
| bwd:block3.grad | 0.822 | 0.824 | 1.2 | 3 |
| bwd:block2 | 1.793 | 1.797 | 2.7 | 2 |
| bwd.invert:block2 | 0.538 | 0.540 | 0.8 | 3 |
| bwd.invert:block2.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block2.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block2.attn.sdpa | 0.287 | 0.288 | 0.4 | 3 |
| bwd.invert:block2.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block2.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block2.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd.recompute:block2 | 0.542 | 0.545 | 0.8 | 3 |
| bwd.recompute:block2.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block2.attn.qkv | 0.032 | 0.032 | 0.0 | 3 |
| bwd.recompute:block2.attn.sdpa | 0.287 | 0.290 | 0.4 | 3 |
| bwd.recompute:block2.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block2.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block2.mlp | 0.086 | 0.087 | 0.1 | 3 |
| bwd:block2.grad | 0.821 | 0.824 | 1.2 | 3 |
| bwd:block1 | 1.800 | 1.803 | 2.7 | 2 |
| bwd.invert:block1 | 0.541 | 0.544 | 0.8 | 3 |
| bwd.invert:block1.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block1.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block1.attn.sdpa | 0.286 | 0.289 | 0.4 | 3 |
| bwd.invert:block1.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block1.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block1.mlp | 0.086 | 0.087 | 0.1 | 3 |
| bwd.recompute:block1 | 0.541 | 0.544 | 0.8 | 3 |
| bwd.recompute:block1.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block1.attn.qkv | 0.032 | 0.034 | 0.0 | 3 |
| bwd.recompute:block1.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.recompute:block1.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block1.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block1.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block1.grad | 0.825 | 0.827 | 1.2 | 3 |
| bwd:block0 | 1.794 | 1.799 | 2.7 | 2 |
| bwd.invert:block0 | 0.539 | 0.541 | 0.8 | 3 |
| bwd.invert:block0.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block0.attn.qkv | 0.033 | 0.034 | 0.0 | 3 |
| bwd.invert:block0.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.invert:block0.attn.proj | 0.030 | 0.030 | 0.0 | 3 |
| bwd.invert:block0.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.invert:block0.mlp | 0.084 | 0.084 | 0.1 | 3 |
| bwd.recompute:block0 | 0.540 | 0.543 | 0.8 | 3 |
| bwd.recompute:block0.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block0.attn.qkv | 0.032 | 0.032 | 0.0 | 3 |
| bwd.recompute:block0.attn.sdpa | 0.287 | 0.289 | 0.4 | 3 |
| bwd.recompute:block0.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block0.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block0.mlp | 0.086 | 0.087 | 0.1 | 3 |
| bwd:block0.grad | 0.822 | 0.825 | 1.2 | 3 |
| bwd:embed | 0.318 | 0.321 | 0.5 | 2 |
| opt | 25.586 | 30.900 | 38.7 | 1 |
| opt:opt.clip | 0.411 | 0.415 | 0.6 | 2 |
| opt:opt.polar_muon_adamw | 24.940 | 30.119 | 37.8 | 2 |
| opt:opt.muon | 19.953 | 24.935 | 30.2 | 2 |
| opt:opt.muon.ns | 25.799 | 34.855 | 39.1 | 3 |
| opt:opt.adamw | 4.721 | 5.192 | 7.1 | 2 |
| opt:opt.moe_bias | 0.015 | 0.016 | 0.0 | 3 |
| opt:opt.zero_grad | 0.245 | 0.321 | 0.4 | 3 |

## Time by part type (sum over layers)

| part type | median ms sum | % of step |
| :--- | ---: | ---: |
| opt:opt.muon.ns | 25.799 | 39.1 |
| opt | 25.586 | 38.7 |
| opt:opt.polar_muon_adamw | 24.940 | 37.8 |
| bwd | 23.513 | 35.6 |
| opt:opt.muon | 19.953 | 30.2 |
| fwd | 17.091 | 25.9 |
| bwd:head+loss | 12.380 | 18.7 |
| bwd:stack | 10.806 | 16.4 |
| bwd:block* | 10.765 | 16.3 |
| fwd:head+loss | 10.468 | 15.8 |
| fwd:stack | 5.805 | 8.8 |
| fwd:block* | 5.555 | 8.4 |
| bwd:block*.grad | 4.936 | 7.5 |
| opt:opt.adamw | 4.721 | 7.1 |
| bwd.recompute:block* | 3.239 | 4.9 |
| bwd.invert:block* | 3.229 | 4.9 |
| fwd:block*.attn.sdpa | 2.458 | 3.7 |
| bwd.invert:block*.attn.sdpa | 1.714 | 2.6 |
| bwd.recompute:block*.attn.sdpa | 1.713 | 2.6 |
| fwd:block*.mlp | 1.146 | 1.7 |
| fwd:block*.attn.qkv | 0.928 | 1.4 |
| fwd:block*.attn.proj | 0.699 | 1.1 |
| data | 0.697 | 1.1 |
| fwd:embed | 0.672 | 1.0 |
| fwd:embed.ke | 0.653 | 1.0 |
| bwd.recompute:block*.mlp | 0.513 | 0.8 |
| bwd.invert:block*.mlp | 0.507 | 0.8 |
| opt:opt.clip | 0.411 | 0.6 |
| fwd:block*.ln1 | 0.323 | 0.5 |
| bwd:embed | 0.318 | 0.5 |
| fwd:block*.ln2 | 0.304 | 0.5 |
| opt:opt.zero_grad | 0.245 | 0.4 |
| bwd.recompute:block*.attn.qkv | 0.191 | 0.3 |
| bwd.invert:block*.attn.qkv | 0.190 | 0.3 |
| bwd.invert:block*.attn.proj | 0.181 | 0.3 |
| bwd.recompute:block*.attn.proj | 0.180 | 0.3 |
| bwd.invert:block*.ln1 | 0.126 | 0.2 |
| bwd.recompute:block*.ln1 | 0.125 | 0.2 |
| bwd.invert:block*.ln2 | 0.120 | 0.2 |
| bwd.recompute:block*.ln2 | 0.120 | 0.2 |
| opt:opt.moe_bias | 0.015 | 0.0 |

## Five slowest leaf parts

1. `opt:opt.muon.ns` — 25.799 ms (39.1% of step)
2. `bwd:block1.grad` — 0.825 ms (1.2% of step)
3. `bwd:block5.grad` — 0.823 ms (1.2% of step)
4. `bwd:block4.grad` — 0.822 ms (1.2% of step)
5. `bwd:block3.grad` — 0.822 ms (1.2% of step)
