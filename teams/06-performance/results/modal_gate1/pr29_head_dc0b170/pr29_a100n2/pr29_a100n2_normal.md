# Bench report — pr29_a100n2_normal

**GPU:** NVIDIA A100-SXM4-40GB  |  **dtype:** bf16  |  **B x T:** 16 x 256  |  **torch:** 2.15.0+cu132
**commit:** `dc0b1703d7d0c51b152bd37d81f6fc2b3ddcf64d`  |  **tag:** pr29_a100n2_normal

## Step (clean)

- median: 65.361 ms
- p10..p90: 63.718 .. 67.656 ms
- tokens/s: 62,667
- MFU: 5.0%  |  HFU: 5.5%

## Diagnostics

### CUDA timing-event allocations

- [OK] clean: events_created_during_steps=0
- [OK] layer: events_created_during_steps=0
- [OK] layer.inner_pass: events_created_during_steps=0

### Benchmark warnings

- [warn] recorder overhead 2.0% > 2.0%: layer numbers are flagged
- [warn] 4 gated part(s) have p10..p90 spread > 10%, so may miss the 5% check: data, fwd:embed, fwd:block0, opt:opt.muon

## Regions

| part | median ms | p90 | % of step | level |
| :--- | ---: | ---: | ---: | ---: |
| data | 0.401 | 0.463 | 0.6 | 1 |
| fwd | 17.012 | 17.300 | 26.0 | 1 |
| fwd:embed | 0.648 | 0.692 | 1.0 | 2 |
| fwd:embed.ke | 0.643 | 0.683 | 1.0 | 3 |
| fwd:stack | 5.769 | 6.011 | 8.8 | 1 |
| fwd:block0 | 0.999 | 1.148 | 1.5 | 2 |
| fwd:block0.ln1 | 0.070 | 0.076 | 0.1 | 3 |
| fwd:block0.attn.qkv | 0.189 | 0.233 | 0.3 | 3 |
| fwd:block0.attn.sdpa | 0.460 | 0.491 | 0.7 | 3 |
| fwd:block0.attn.proj | 0.136 | 0.152 | 0.2 | 3 |
| fwd:block0.ln2 | 0.052 | 0.069 | 0.1 | 3 |
| fwd:block0.mlp | 0.195 | 0.223 | 0.3 | 3 |
| fwd:block1 | 0.908 | 0.937 | 1.4 | 2 |
| fwd:block1.ln1 | 0.051 | 0.057 | 0.1 | 3 |
| fwd:block1.attn.qkv | 0.144 | 0.165 | 0.2 | 3 |
| fwd:block1.attn.sdpa | 0.397 | 0.423 | 0.6 | 3 |
| fwd:block1.attn.proj | 0.113 | 0.137 | 0.2 | 3 |
| fwd:block1.ln2 | 0.050 | 0.052 | 0.1 | 3 |
| fwd:block1.mlp | 0.182 | 0.209 | 0.3 | 3 |
| fwd:block2 | 0.901 | 0.928 | 1.4 | 2 |
| fwd:block2.ln1 | 0.050 | 0.052 | 0.1 | 3 |
| fwd:block2.attn.qkv | 0.142 | 0.163 | 0.2 | 3 |
| fwd:block2.attn.sdpa | 0.396 | 0.417 | 0.6 | 3 |
| fwd:block2.attn.proj | 0.104 | 0.128 | 0.2 | 3 |
| fwd:block2.ln2 | 0.049 | 0.051 | 0.1 | 3 |
| fwd:block2.mlp | 0.181 | 0.202 | 0.3 | 3 |
| fwd:block3 | 0.899 | 0.920 | 1.4 | 2 |
| fwd:block3.ln1 | 0.049 | 0.051 | 0.1 | 3 |
| fwd:block3.attn.qkv | 0.143 | 0.167 | 0.2 | 3 |
| fwd:block3.attn.sdpa | 0.394 | 0.418 | 0.6 | 3 |
| fwd:block3.attn.proj | 0.100 | 0.129 | 0.2 | 3 |
| fwd:block3.ln2 | 0.049 | 0.050 | 0.1 | 3 |
| fwd:block3.mlp | 0.179 | 0.205 | 0.3 | 3 |
| fwd:block4 | 0.896 | 0.915 | 1.4 | 2 |
| fwd:block4.ln1 | 0.049 | 0.070 | 0.1 | 3 |
| fwd:block4.attn.qkv | 0.143 | 0.163 | 0.2 | 3 |
| fwd:block4.attn.sdpa | 0.393 | 0.416 | 0.6 | 3 |
| fwd:block4.attn.proj | 0.102 | 0.128 | 0.2 | 3 |
| fwd:block4.ln2 | 0.049 | 0.051 | 0.1 | 3 |
| fwd:block4.mlp | 0.182 | 0.209 | 0.3 | 3 |
| fwd:block5 | 0.894 | 0.909 | 1.4 | 2 |
| fwd:block5.ln1 | 0.049 | 0.051 | 0.1 | 3 |
| fwd:block5.attn.qkv | 0.141 | 0.165 | 0.2 | 3 |
| fwd:block5.attn.sdpa | 0.392 | 0.407 | 0.6 | 3 |
| fwd:block5.attn.proj | 0.099 | 0.128 | 0.2 | 3 |
| fwd:block5.ln2 | 0.049 | 0.051 | 0.1 | 3 |
| fwd:block5.mlp | 0.181 | 0.204 | 0.3 | 3 |
| fwd:head+loss | 10.473 | 10.483 | 16.0 | 2 |
| bwd | 23.482 | 23.500 | 35.9 | 1 |
| bwd:head+loss | 12.363 | 12.376 | 18.9 | 2 |
| bwd:stack | 10.775 | 10.786 | 16.5 | 1 |
| bwd:block5 | 1.786 | 1.789 | 2.7 | 2 |
| bwd.invert:block5 | 0.537 | 0.539 | 0.8 | 3 |
| bwd.invert:block5.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block5.attn.qkv | 0.032 | 0.032 | 0.0 | 3 |
| bwd.invert:block5.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.invert:block5.attn.proj | 0.030 | 0.032 | 0.0 | 3 |
| bwd.invert:block5.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block5.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd.recompute:block5 | 0.538 | 0.540 | 0.8 | 3 |
| bwd.recompute:block5.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block5.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block5.attn.sdpa | 0.284 | 0.287 | 0.4 | 3 |
| bwd.recompute:block5.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block5.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block5.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd:block5.grad | 0.820 | 0.822 | 1.3 | 3 |
| bwd:block4 | 1.790 | 1.794 | 2.7 | 2 |
| bwd.invert:block4 | 0.537 | 0.539 | 0.8 | 3 |
| bwd.invert:block4.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block4.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block4.attn.sdpa | 0.285 | 0.286 | 0.4 | 3 |
| bwd.invert:block4.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block4.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block4.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd.recompute:block4 | 0.539 | 0.541 | 0.8 | 3 |
| bwd.recompute:block4.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block4.attn.qkv | 0.031 | 0.031 | 0.0 | 3 |
| bwd.recompute:block4.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.recompute:block4.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block4.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block4.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block4.grad | 0.820 | 0.823 | 1.3 | 3 |
| bwd:block3 | 1.784 | 1.789 | 2.7 | 2 |
| bwd.invert:block3 | 0.535 | 0.538 | 0.8 | 3 |
| bwd.invert:block3.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block3.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block3.attn.sdpa | 0.284 | 0.285 | 0.4 | 3 |
| bwd.invert:block3.attn.proj | 0.031 | 0.033 | 0.0 | 3 |
| bwd.invert:block3.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block3.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd.recompute:block3 | 0.539 | 0.541 | 0.8 | 3 |
| bwd.recompute:block3.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block3.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block3.attn.sdpa | 0.283 | 0.285 | 0.4 | 3 |
| bwd.recompute:block3.attn.proj | 0.031 | 0.031 | 0.0 | 3 |
| bwd.recompute:block3.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block3.mlp | 0.085 | 0.085 | 0.1 | 3 |
| bwd:block3.grad | 0.820 | 0.823 | 1.3 | 3 |
| bwd:block2 | 1.789 | 1.794 | 2.7 | 2 |
| bwd.invert:block2 | 0.536 | 0.538 | 0.8 | 3 |
| bwd.invert:block2.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block2.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block2.attn.sdpa | 0.284 | 0.285 | 0.4 | 3 |
| bwd.invert:block2.attn.proj | 0.031 | 0.031 | 0.0 | 3 |
| bwd.invert:block2.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.invert:block2.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd.recompute:block2 | 0.540 | 0.543 | 0.8 | 3 |
| bwd.recompute:block2.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block2.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block2.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.recompute:block2.attn.proj | 0.031 | 0.033 | 0.0 | 3 |
| bwd.recompute:block2.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block2.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block2.grad | 0.822 | 0.825 | 1.3 | 3 |
| bwd:block1 | 1.793 | 1.797 | 2.7 | 2 |
| bwd.invert:block1 | 0.540 | 0.543 | 0.8 | 3 |
| bwd.invert:block1.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block1.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block1.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.invert:block1.attn.proj | 0.031 | 0.033 | 0.0 | 3 |
| bwd.invert:block1.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block1.mlp | 0.086 | 0.087 | 0.1 | 3 |
| bwd.recompute:block1 | 0.541 | 0.543 | 0.8 | 3 |
| bwd.recompute:block1.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block1.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block1.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.recompute:block1.attn.proj | 0.031 | 0.031 | 0.0 | 3 |
| bwd.recompute:block1.ln2 | 0.019 | 0.022 | 0.0 | 3 |
| bwd.recompute:block1.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd:block1.grad | 0.824 | 0.826 | 1.3 | 3 |
| bwd:block0 | 1.789 | 1.795 | 2.7 | 2 |
| bwd.invert:block0 | 0.537 | 0.540 | 0.8 | 3 |
| bwd.invert:block0.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block0.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block0.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.invert:block0.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block0.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block0.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd.recompute:block0 | 0.539 | 0.542 | 0.8 | 3 |
| bwd.recompute:block0.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block0.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block0.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.recompute:block0.attn.proj | 0.030 | 0.032 | 0.0 | 3 |
| bwd.recompute:block0.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block0.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block0.grad | 0.824 | 0.827 | 1.3 | 3 |
| bwd:embed | 0.336 | 0.337 | 0.5 | 2 |
| opt | 25.212 | 26.399 | 38.6 | 1 |
| opt:opt.clip | 0.411 | 0.413 | 0.6 | 2 |
| opt:opt.polar_muon_adamw | 24.556 | 25.714 | 37.6 | 2 |
| opt:opt.muon | 19.555 | 20.659 | 29.9 | 2 |
| opt:opt.muon.ns | 24.054 | 25.207 | 36.8 | 3 |
| opt:opt.adamw | 4.866 | 5.028 | 7.4 | 2 |
| opt:opt.moe_bias | 0.015 | 0.016 | 0.0 | 3 |
| opt:opt.zero_grad | 0.245 | 0.271 | 0.4 | 3 |

## Time by part type (sum over layers)

| part type | median ms sum | % of step |
| :--- | ---: | ---: |
| opt | 25.212 | 38.6 |
| opt:opt.polar_muon_adamw | 24.556 | 37.6 |
| opt:opt.muon.ns | 24.054 | 36.8 |
| bwd | 23.482 | 35.9 |
| opt:opt.muon | 19.555 | 29.9 |
| fwd | 17.012 | 26.0 |
| bwd:head+loss | 12.363 | 18.9 |
| bwd:stack | 10.775 | 16.5 |
| bwd:block* | 10.731 | 16.4 |
| fwd:head+loss | 10.473 | 16.0 |
| fwd:stack | 5.769 | 8.8 |
| fwd:block* | 5.497 | 8.4 |
| bwd:block*.grad | 4.932 | 7.5 |
| opt:opt.adamw | 4.866 | 7.4 |
| bwd.recompute:block* | 3.234 | 4.9 |
| bwd.invert:block* | 3.220 | 4.9 |
| fwd:block*.attn.sdpa | 2.433 | 3.7 |
| bwd.invert:block*.attn.sdpa | 1.707 | 2.6 |
| bwd.recompute:block*.attn.sdpa | 1.706 | 2.6 |
| fwd:block*.mlp | 1.101 | 1.7 |
| fwd:block*.attn.qkv | 0.903 | 1.4 |
| fwd:block*.attn.proj | 0.655 | 1.0 |
| fwd:embed | 0.648 | 1.0 |
| fwd:embed.ke | 0.643 | 1.0 |
| bwd.recompute:block*.mlp | 0.508 | 0.8 |
| bwd.invert:block*.mlp | 0.503 | 0.8 |
| opt:opt.clip | 0.411 | 0.6 |
| data | 0.401 | 0.6 |
| bwd:embed | 0.336 | 0.5 |
| fwd:block*.ln1 | 0.318 | 0.5 |
| fwd:block*.ln2 | 0.299 | 0.5 |
| opt:opt.zero_grad | 0.245 | 0.4 |
| bwd.invert:block*.attn.qkv | 0.187 | 0.3 |
| bwd.recompute:block*.attn.qkv | 0.187 | 0.3 |
| bwd.recompute:block*.attn.proj | 0.182 | 0.3 |
| bwd.invert:block*.attn.proj | 0.181 | 0.3 |
| bwd.invert:block*.ln1 | 0.126 | 0.2 |
| bwd.recompute:block*.ln1 | 0.126 | 0.2 |
| bwd.recompute:block*.ln2 | 0.121 | 0.2 |
| bwd.invert:block*.ln2 | 0.120 | 0.2 |
| opt:opt.moe_bias | 0.015 | 0.0 |

## Five slowest leaf parts

1. `opt:opt.muon.ns` — 24.054 ms (36.8% of step)
2. `bwd:block1.grad` — 0.824 ms (1.3% of step)
3. `bwd:block0.grad` — 0.824 ms (1.3% of step)
4. `bwd:block2.grad` — 0.822 ms (1.3% of step)
5. `bwd:block5.grad` — 0.820 ms (1.3% of step)
