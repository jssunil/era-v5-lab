# Bench report — pr29_a100real4_normal-run2

**GPU:** NVIDIA A100-SXM4-40GB  |  **dtype:** bf16  |  **B x T:** 16 x 256  |  **torch:** 2.15.0+cu132
**commit:** `dc0b1703d7d0c51b152bd37d81f6fc2b3ddcf64d`  |  **tag:** pr29_a100real4_normal-run2

## Step (clean)

- median: 64.808 ms
- p10..p90: 63.566 .. 67.742 ms
- tokens/s: 63,202
- MFU: 5.0%  |  HFU: 5.6%

## Diagnostics

### CUDA timing-event allocations

- [OK] clean: events_created_during_steps=0
- [OK] layer: events_created_during_steps=0
- [OK] layer.inner_pass: events_created_during_steps=0

### Benchmark warnings

- [warn] recorder overhead 2.0% > 2.0%: layer numbers are flagged
- [warn] 7 gated part(s) have p10..p90 spread > 10%, so may miss the 5% check: data, fwd:embed, fwd:stack, fwd:block0, opt, opt:opt.polar_muon_adamw (+1 more)

## Regions

| part | median ms | p90 | % of step | level |
| :--- | ---: | ---: | ---: | ---: |
| data | 0.696 | 0.790 | 1.1 | 1 |
| fwd | 17.104 | 17.467 | 26.4 | 1 |
| fwd:embed | 0.677 | 0.721 | 1.0 | 2 |
| fwd:embed.ke | 0.632 | 0.672 | 1.0 | 3 |
| fwd:stack | 5.851 | 6.194 | 9.0 | 1 |
| fwd:block0 | 1.073 | 1.196 | 1.7 | 2 |
| fwd:block0.ln1 | 0.064 | 0.076 | 0.1 | 3 |
| fwd:block0.attn.qkv | 0.173 | 0.201 | 0.3 | 3 |
| fwd:block0.attn.sdpa | 0.435 | 0.478 | 0.7 | 3 |
| fwd:block0.attn.proj | 0.121 | 0.146 | 0.2 | 3 |
| fwd:block0.ln2 | 0.051 | 0.057 | 0.1 | 3 |
| fwd:block0.mlp | 0.191 | 0.214 | 0.3 | 3 |
| fwd:block1 | 0.910 | 0.956 | 1.4 | 2 |
| fwd:block1.ln1 | 0.052 | 0.057 | 0.1 | 3 |
| fwd:block1.attn.qkv | 0.144 | 0.163 | 0.2 | 3 |
| fwd:block1.attn.sdpa | 0.398 | 0.417 | 0.6 | 3 |
| fwd:block1.attn.proj | 0.102 | 0.128 | 0.2 | 3 |
| fwd:block1.ln2 | 0.049 | 0.052 | 0.1 | 3 |
| fwd:block1.mlp | 0.182 | 0.209 | 0.3 | 3 |
| fwd:block2 | 0.902 | 0.952 | 1.4 | 2 |
| fwd:block2.ln1 | 0.050 | 0.056 | 0.1 | 3 |
| fwd:block2.attn.qkv | 0.141 | 0.160 | 0.2 | 3 |
| fwd:block2.attn.sdpa | 0.397 | 0.420 | 0.6 | 3 |
| fwd:block2.attn.proj | 0.099 | 0.123 | 0.2 | 3 |
| fwd:block2.ln2 | 0.049 | 0.058 | 0.1 | 3 |
| fwd:block2.mlp | 0.183 | 0.206 | 0.3 | 3 |
| fwd:block3 | 0.897 | 0.932 | 1.4 | 2 |
| fwd:block3.ln1 | 0.049 | 0.053 | 0.1 | 3 |
| fwd:block3.attn.qkv | 0.142 | 0.165 | 0.2 | 3 |
| fwd:block3.attn.sdpa | 0.397 | 0.417 | 0.6 | 3 |
| fwd:block3.attn.proj | 0.103 | 0.126 | 0.2 | 3 |
| fwd:block3.ln2 | 0.049 | 0.051 | 0.1 | 3 |
| fwd:block3.mlp | 0.178 | 0.200 | 0.3 | 3 |
| fwd:block4 | 0.899 | 0.928 | 1.4 | 2 |
| fwd:block4.ln1 | 0.049 | 0.053 | 0.1 | 3 |
| fwd:block4.attn.qkv | 0.141 | 0.164 | 0.2 | 3 |
| fwd:block4.attn.sdpa | 0.397 | 0.419 | 0.6 | 3 |
| fwd:block4.attn.proj | 0.104 | 0.126 | 0.2 | 3 |
| fwd:block4.ln2 | 0.049 | 0.052 | 0.1 | 3 |
| fwd:block4.mlp | 0.181 | 0.208 | 0.3 | 3 |
| fwd:block5 | 0.895 | 0.935 | 1.4 | 2 |
| fwd:block5.ln1 | 0.049 | 0.052 | 0.1 | 3 |
| fwd:block5.attn.qkv | 0.140 | 0.162 | 0.2 | 3 |
| fwd:block5.attn.sdpa | 0.397 | 0.417 | 0.6 | 3 |
| fwd:block5.attn.proj | 0.102 | 0.126 | 0.2 | 3 |
| fwd:block5.ln2 | 0.049 | 0.052 | 0.1 | 3 |
| fwd:block5.mlp | 0.179 | 0.203 | 0.3 | 3 |
| fwd:head+loss | 10.433 | 10.450 | 16.1 | 2 |
| bwd | 23.441 | 23.458 | 36.2 | 1 |
| bwd:head+loss | 12.281 | 12.294 | 18.9 | 2 |
| bwd:stack | 10.815 | 10.827 | 16.7 | 1 |
| bwd:block5 | 1.793 | 1.796 | 2.8 | 2 |
| bwd.invert:block5 | 0.537 | 0.539 | 0.8 | 3 |
| bwd.invert:block5.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block5.attn.qkv | 0.032 | 0.032 | 0.0 | 3 |
| bwd.invert:block5.attn.sdpa | 0.288 | 0.290 | 0.4 | 3 |
| bwd.invert:block5.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block5.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block5.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd.recompute:block5 | 0.537 | 0.539 | 0.8 | 3 |
| bwd.recompute:block5.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block5.attn.qkv | 0.031 | 0.033 | 0.0 | 3 |
| bwd.recompute:block5.attn.sdpa | 0.286 | 0.287 | 0.4 | 3 |
| bwd.recompute:block5.attn.proj | 0.030 | 0.030 | 0.0 | 3 |
| bwd.recompute:block5.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.recompute:block5.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd:block5.grad | 0.823 | 0.825 | 1.3 | 3 |
| bwd:block4 | 1.797 | 1.802 | 2.8 | 2 |
| bwd.invert:block4 | 0.537 | 0.540 | 0.8 | 3 |
| bwd.invert:block4.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block4.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block4.attn.sdpa | 0.287 | 0.288 | 0.4 | 3 |
| bwd.invert:block4.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block4.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block4.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd.recompute:block4 | 0.539 | 0.542 | 0.8 | 3 |
| bwd.recompute:block4.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block4.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block4.attn.sdpa | 0.288 | 0.289 | 0.4 | 3 |
| bwd.recompute:block4.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block4.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block4.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block4.grad | 0.821 | 0.824 | 1.3 | 3 |
| bwd:block3 | 1.791 | 1.794 | 2.8 | 2 |
| bwd.invert:block3 | 0.535 | 0.537 | 0.8 | 3 |
| bwd.invert:block3.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block3.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block3.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.invert:block3.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block3.ln2 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block3.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd.recompute:block3 | 0.537 | 0.539 | 0.8 | 3 |
| bwd.recompute:block3.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block3.attn.qkv | 0.031 | 0.033 | 0.0 | 3 |
| bwd.recompute:block3.attn.sdpa | 0.284 | 0.286 | 0.4 | 3 |
| bwd.recompute:block3.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block3.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.recompute:block3.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block3.grad | 0.821 | 0.824 | 1.3 | 3 |
| bwd:block2 | 1.795 | 1.801 | 2.8 | 2 |
| bwd.invert:block2 | 0.536 | 0.539 | 0.8 | 3 |
| bwd.invert:block2.ln1 | 0.022 | 0.022 | 0.0 | 3 |
| bwd.invert:block2.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block2.attn.sdpa | 0.287 | 0.289 | 0.4 | 3 |
| bwd.invert:block2.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block2.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.invert:block2.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd.recompute:block2 | 0.540 | 0.543 | 0.8 | 3 |
| bwd.recompute:block2.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block2.attn.qkv | 0.031 | 0.031 | 0.0 | 3 |
| bwd.recompute:block2.attn.sdpa | 0.288 | 0.290 | 0.4 | 3 |
| bwd.recompute:block2.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block2.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block2.mlp | 0.086 | 0.087 | 0.1 | 3 |
| bwd:block2.grad | 0.822 | 0.826 | 1.3 | 3 |
| bwd:block1 | 1.801 | 1.804 | 2.8 | 2 |
| bwd.invert:block1 | 0.539 | 0.541 | 0.8 | 3 |
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
| bwd.recompute:block1.mlp | 0.085 | 0.085 | 0.1 | 3 |
| bwd:block1.grad | 0.826 | 0.828 | 1.3 | 3 |
| bwd:block0 | 1.798 | 1.803 | 2.8 | 2 |
| bwd.invert:block0 | 0.537 | 0.539 | 0.8 | 3 |
| bwd.invert:block0.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block0.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block0.attn.sdpa | 0.286 | 0.287 | 0.4 | 3 |
| bwd.invert:block0.attn.proj | 0.029 | 0.030 | 0.0 | 3 |
| bwd.invert:block0.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.invert:block0.mlp | 0.084 | 0.084 | 0.1 | 3 |
| bwd.recompute:block0 | 0.538 | 0.541 | 0.8 | 3 |
| bwd.recompute:block0.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block0.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block0.attn.sdpa | 0.286 | 0.289 | 0.4 | 3 |
| bwd.recompute:block0.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block0.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block0.mlp | 0.086 | 0.087 | 0.1 | 3 |
| bwd:block0.grad | 0.825 | 0.828 | 1.3 | 3 |
| bwd:embed | 0.333 | 0.336 | 0.5 | 2 |
| opt | 25.970 | 27.759 | 40.1 | 1 |
| opt:opt.clip | 0.409 | 0.413 | 0.6 | 2 |
| opt:opt.polar_muon_adamw | 25.266 | 27.099 | 39.0 | 2 |
| opt:opt.muon | 20.263 | 21.827 | 31.3 | 2 |
| opt:opt.muon.ns | 24.321 | 26.148 | 37.5 | 3 |
| opt:opt.adamw | 4.881 | 5.133 | 7.5 | 2 |
| opt:opt.moe_bias | 0.014 | 0.015 | 0.0 | 3 |
| opt:opt.zero_grad | 0.203 | 0.265 | 0.3 | 3 |

## Time by part type (sum over layers)

| part type | median ms sum | % of step |
| :--- | ---: | ---: |
| opt | 25.970 | 40.1 |
| opt:opt.polar_muon_adamw | 25.266 | 39.0 |
| opt:opt.muon.ns | 24.321 | 37.5 |
| bwd | 23.441 | 36.2 |
| opt:opt.muon | 20.263 | 31.3 |
| fwd | 17.104 | 26.4 |
| bwd:head+loss | 12.281 | 18.9 |
| bwd:stack | 10.815 | 16.7 |
| bwd:block* | 10.775 | 16.6 |
| fwd:head+loss | 10.433 | 16.1 |
| fwd:stack | 5.851 | 9.0 |
| fwd:block* | 5.576 | 8.6 |
| bwd:block*.grad | 4.940 | 7.6 |
| opt:opt.adamw | 4.881 | 7.5 |
| bwd.recompute:block* | 3.229 | 5.0 |
| bwd.invert:block* | 3.218 | 5.0 |
| fwd:block*.attn.sdpa | 2.421 | 3.7 |
| bwd.invert:block*.attn.sdpa | 1.718 | 2.7 |
| bwd.recompute:block*.attn.sdpa | 1.717 | 2.6 |
| fwd:block*.mlp | 1.095 | 1.7 |
| fwd:block*.attn.qkv | 0.883 | 1.4 |
| data | 0.696 | 1.1 |
| fwd:embed | 0.677 | 1.0 |
| fwd:block*.attn.proj | 0.632 | 1.0 |
| fwd:embed.ke | 0.632 | 1.0 |
| bwd.recompute:block*.mlp | 0.511 | 0.8 |
| bwd.invert:block*.mlp | 0.505 | 0.8 |
| opt:opt.clip | 0.409 | 0.6 |
| bwd:embed | 0.333 | 0.5 |
| fwd:block*.ln1 | 0.314 | 0.5 |
| fwd:block*.ln2 | 0.297 | 0.5 |
| opt:opt.zero_grad | 0.203 | 0.3 |
| bwd.invert:block*.attn.qkv | 0.188 | 0.3 |
| bwd.recompute:block*.attn.qkv | 0.186 | 0.3 |
| bwd.recompute:block*.attn.proj | 0.180 | 0.3 |
| bwd.invert:block*.attn.proj | 0.180 | 0.3 |
| bwd.invert:block*.ln1 | 0.125 | 0.2 |
| bwd.recompute:block*.ln1 | 0.124 | 0.2 |
| bwd.invert:block*.ln2 | 0.119 | 0.2 |
| bwd.recompute:block*.ln2 | 0.118 | 0.2 |
| opt:opt.moe_bias | 0.014 | 0.0 |

## Five slowest leaf parts

1. `opt:opt.muon.ns` — 24.321 ms (37.5% of step)
2. `bwd:block1.grad` — 0.826 ms (1.3% of step)
3. `bwd:block0.grad` — 0.825 ms (1.3% of step)
4. `bwd:block5.grad` — 0.823 ms (1.3% of step)
5. `bwd:block2.grad` — 0.822 ms (1.3% of step)
