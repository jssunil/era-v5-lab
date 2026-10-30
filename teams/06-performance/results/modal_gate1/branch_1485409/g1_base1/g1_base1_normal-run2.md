# Bench report — g1_base1_normal-run2

**GPU:** NVIDIA A100-SXM4-40GB  |  **dtype:** bf16  |  **B x T:** 16 x 256  |  **torch:** 2.15.0+cu132
**commit:** `14854097c57056f326efd0c7a40cc036a73bbc94`  |  **tag:** g1_base1_normal-run2

## Step (clean)

- median: 66.159 ms
- p10..p90: 62.743 .. 68.340 ms
- tokens/s: 61,912
- MFU: 4.9%  |  HFU: 5.5%

## Diagnostics

### CUDA timing-event allocations

- [OK] clean: events_created_during_steps=0
- [OK] layer: events_created_during_steps=0
- [OK] layer.inner_pass: events_created_during_steps=0

### Benchmark warnings

- [warn] recorder overhead 2.3% > 2.0%: layer numbers are flagged
- [warn] 13 gated part(s) have p10..p90 spread > 10%, so may miss the 5% check: data, fwd:embed, fwd:stack, fwd:block0, fwd:block1, fwd:block2 (+7 more)

## Regions

| part | median ms | p90 | % of step | level |
| :--- | ---: | ---: | ---: | ---: |
| data | 0.664 | 0.783 | 1.0 | 1 |
| fwd | 17.108 | 17.853 | 25.9 | 1 |
| fwd:embed | 0.663 | 0.699 | 1.0 | 2 |
| fwd:embed.ke | 0.632 | 0.664 | 1.0 | 3 |
| fwd:stack | 5.844 | 6.522 | 8.8 | 1 |
| fwd:block0 | 1.066 | 1.197 | 1.6 | 2 |
| fwd:block0.ln1 | 0.060 | 0.074 | 0.1 | 3 |
| fwd:block0.attn.qkv | 0.170 | 0.202 | 0.3 | 3 |
| fwd:block0.attn.sdpa | 0.421 | 0.469 | 0.6 | 3 |
| fwd:block0.attn.proj | 0.124 | 0.143 | 0.2 | 3 |
| fwd:block0.ln2 | 0.051 | 0.055 | 0.1 | 3 |
| fwd:block0.mlp | 0.193 | 0.221 | 0.3 | 3 |
| fwd:block1 | 0.913 | 0.993 | 1.4 | 2 |
| fwd:block1.ln1 | 0.050 | 0.055 | 0.1 | 3 |
| fwd:block1.attn.qkv | 0.142 | 0.165 | 0.2 | 3 |
| fwd:block1.attn.sdpa | 0.394 | 0.416 | 0.6 | 3 |
| fwd:block1.attn.proj | 0.105 | 0.128 | 0.2 | 3 |
| fwd:block1.ln2 | 0.050 | 0.053 | 0.1 | 3 |
| fwd:block1.mlp | 0.183 | 0.206 | 0.3 | 3 |
| fwd:block2 | 0.900 | 0.972 | 1.4 | 2 |
| fwd:block2.ln1 | 0.049 | 0.053 | 0.1 | 3 |
| fwd:block2.attn.qkv | 0.141 | 0.165 | 0.2 | 3 |
| fwd:block2.attn.sdpa | 0.392 | 0.415 | 0.6 | 3 |
| fwd:block2.attn.proj | 0.109 | 0.129 | 0.2 | 3 |
| fwd:block2.ln2 | 0.049 | 0.052 | 0.1 | 3 |
| fwd:block2.mlp | 0.182 | 0.208 | 0.3 | 3 |
| fwd:block3 | 0.898 | 1.004 | 1.4 | 2 |
| fwd:block3.ln1 | 0.048 | 0.056 | 0.1 | 3 |
| fwd:block3.attn.qkv | 0.141 | 0.162 | 0.2 | 3 |
| fwd:block3.attn.sdpa | 0.392 | 0.417 | 0.6 | 3 |
| fwd:block3.attn.proj | 0.106 | 0.129 | 0.2 | 3 |
| fwd:block3.ln2 | 0.049 | 0.051 | 0.1 | 3 |
| fwd:block3.mlp | 0.183 | 0.207 | 0.3 | 3 |
| fwd:block4 | 0.898 | 1.021 | 1.4 | 2 |
| fwd:block4.ln1 | 0.048 | 0.053 | 0.1 | 3 |
| fwd:block4.attn.qkv | 0.142 | 0.163 | 0.2 | 3 |
| fwd:block4.attn.sdpa | 0.392 | 0.413 | 0.6 | 3 |
| fwd:block4.attn.proj | 0.103 | 0.126 | 0.2 | 3 |
| fwd:block4.ln2 | 0.049 | 0.052 | 0.1 | 3 |
| fwd:block4.mlp | 0.182 | 0.204 | 0.3 | 3 |
| fwd:block5 | 0.892 | 0.993 | 1.3 | 2 |
| fwd:block5.ln1 | 0.049 | 0.053 | 0.1 | 3 |
| fwd:block5.attn.qkv | 0.140 | 0.161 | 0.2 | 3 |
| fwd:block5.attn.sdpa | 0.392 | 0.412 | 0.6 | 3 |
| fwd:block5.attn.proj | 0.102 | 0.125 | 0.2 | 3 |
| fwd:block5.ln2 | 0.049 | 0.051 | 0.1 | 3 |
| fwd:block5.mlp | 0.181 | 0.208 | 0.3 | 3 |
| fwd:head+loss | 10.470 | 10.484 | 15.8 | 2 |
| bwd | 23.452 | 23.469 | 35.4 | 1 |
| bwd:head+loss | 12.377 | 12.389 | 18.7 | 2 |
| bwd:stack | 10.749 | 10.761 | 16.2 | 1 |
| bwd:block5 | 1.781 | 1.785 | 2.7 | 2 |
| bwd.invert:block5 | 0.535 | 0.537 | 0.8 | 3 |
| bwd.invert:block5.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block5.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block5.attn.sdpa | 0.286 | 0.287 | 0.4 | 3 |
| bwd.invert:block5.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block5.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block5.mlp | 0.083 | 0.084 | 0.1 | 3 |
| bwd.recompute:block5 | 0.536 | 0.538 | 0.8 | 3 |
| bwd.recompute:block5.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block5.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block5.attn.sdpa | 0.283 | 0.285 | 0.4 | 3 |
| bwd.recompute:block5.attn.proj | 0.030 | 0.030 | 0.0 | 3 |
| bwd.recompute:block5.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block5.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd:block5.grad | 0.817 | 0.820 | 1.2 | 3 |
| bwd:block4 | 1.787 | 1.791 | 2.7 | 2 |
| bwd.invert:block4 | 0.538 | 0.540 | 0.8 | 3 |
| bwd.invert:block4.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block4.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block4.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.invert:block4.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block4.ln2 | 0.019 | 0.019 | 0.0 | 3 |
| bwd.invert:block4.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd.recompute:block4 | 0.540 | 0.542 | 0.8 | 3 |
| bwd.recompute:block4.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block4.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block4.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.recompute:block4.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block4.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block4.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block4.grad | 0.818 | 0.821 | 1.2 | 3 |
| bwd:block3 | 1.783 | 1.786 | 2.7 | 2 |
| bwd.invert:block3 | 0.536 | 0.539 | 0.8 | 3 |
| bwd.invert:block3.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block3.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block3.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.invert:block3.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block3.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block3.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd.recompute:block3 | 0.538 | 0.540 | 0.8 | 3 |
| bwd.recompute:block3.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block3.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block3.attn.sdpa | 0.284 | 0.286 | 0.4 | 3 |
| bwd.recompute:block3.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block3.ln2 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block3.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd:block3.grad | 0.819 | 0.822 | 1.2 | 3 |
| bwd:block2 | 1.781 | 1.786 | 2.7 | 2 |
| bwd.invert:block2 | 0.537 | 0.539 | 0.8 | 3 |
| bwd.invert:block2.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block2.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block2.attn.sdpa | 0.286 | 0.287 | 0.4 | 3 |
| bwd.invert:block2.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.invert:block2.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block2.mlp | 0.082 | 0.083 | 0.1 | 3 |
| bwd.recompute:block2 | 0.541 | 0.545 | 0.8 | 3 |
| bwd.recompute:block2.ln1 | 0.020 | 0.021 | 0.0 | 3 |
| bwd.recompute:block2.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block2.attn.sdpa | 0.287 | 0.289 | 0.4 | 3 |
| bwd.recompute:block2.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block2.ln2 | 0.020 | 0.023 | 0.0 | 3 |
| bwd.recompute:block2.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block2.grad | 0.816 | 0.820 | 1.2 | 3 |
| bwd:block1 | 1.789 | 1.794 | 2.7 | 2 |
| bwd.invert:block1 | 0.540 | 0.543 | 0.8 | 3 |
| bwd.invert:block1.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.invert:block1.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block1.attn.sdpa | 0.286 | 0.288 | 0.4 | 3 |
| bwd.invert:block1.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.invert:block1.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block1.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd.recompute:block1 | 0.540 | 0.543 | 0.8 | 3 |
| bwd.recompute:block1.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.recompute:block1.attn.qkv | 0.033 | 0.033 | 0.0 | 3 |
| bwd.recompute:block1.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.recompute:block1.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block1.ln2 | 0.019 | 0.022 | 0.0 | 3 |
| bwd.recompute:block1.mlp | 0.084 | 0.085 | 0.1 | 3 |
| bwd:block1.grad | 0.820 | 0.822 | 1.2 | 3 |
| bwd:block0 | 1.786 | 1.790 | 2.7 | 2 |
| bwd.invert:block0 | 0.537 | 0.540 | 0.8 | 3 |
| bwd.invert:block0.ln1 | 0.022 | 0.023 | 0.0 | 3 |
| bwd.invert:block0.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.invert:block0.attn.sdpa | 0.285 | 0.287 | 0.4 | 3 |
| bwd.invert:block0.attn.proj | 0.029 | 0.030 | 0.0 | 3 |
| bwd.invert:block0.ln2 | 0.019 | 0.022 | 0.0 | 3 |
| bwd.invert:block0.mlp | 0.083 | 0.083 | 0.1 | 3 |
| bwd.recompute:block0 | 0.539 | 0.541 | 0.8 | 3 |
| bwd.recompute:block0.ln1 | 0.020 | 0.020 | 0.0 | 3 |
| bwd.recompute:block0.attn.qkv | 0.031 | 0.031 | 0.0 | 3 |
| bwd.recompute:block0.attn.sdpa | 0.286 | 0.289 | 0.4 | 3 |
| bwd.recompute:block0.attn.proj | 0.030 | 0.031 | 0.0 | 3 |
| bwd.recompute:block0.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block0.mlp | 0.085 | 0.086 | 0.1 | 3 |
| bwd:block0.grad | 0.819 | 0.822 | 1.2 | 3 |
| bwd:embed | 0.316 | 0.318 | 0.5 | 2 |
| opt | 25.695 | 37.431 | 38.8 | 1 |
| opt:opt.clip | 0.411 | 0.415 | 0.6 | 2 |
| opt:opt.polar_muon_adamw | 25.006 | 36.752 | 37.8 | 2 |
| opt:opt.muon | 19.887 | 29.525 | 30.1 | 2 |
| opt:opt.muon.ns | 24.123 | 25.545 | 36.5 | 3 |
| opt:opt.adamw | 4.890 | 7.021 | 7.4 | 2 |
| opt:opt.moe_bias | 0.016 | 0.019 | 0.0 | 3 |
| opt:opt.zero_grad | 0.209 | 0.262 | 0.3 | 3 |

## Time by part type (sum over layers)

| part type | median ms sum | % of step |
| :--- | ---: | ---: |
| opt | 25.695 | 38.8 |
| opt:opt.polar_muon_adamw | 25.006 | 37.8 |
| opt:opt.muon.ns | 24.123 | 36.5 |
| bwd | 23.452 | 35.4 |
| opt:opt.muon | 19.887 | 30.1 |
| fwd | 17.108 | 25.9 |
| bwd:head+loss | 12.377 | 18.7 |
| bwd:stack | 10.749 | 16.2 |
| bwd:block* | 10.706 | 16.2 |
| fwd:head+loss | 10.470 | 15.8 |
| fwd:stack | 5.844 | 8.8 |
| fwd:block* | 5.567 | 8.4 |
| bwd:block*.grad | 4.910 | 7.4 |
| opt:opt.adamw | 4.890 | 7.4 |
| bwd.recompute:block* | 3.233 | 4.9 |
| bwd.invert:block* | 3.220 | 4.9 |
| fwd:block*.attn.sdpa | 2.383 | 3.6 |
| bwd.invert:block*.attn.sdpa | 1.711 | 2.6 |
| bwd.recompute:block*.attn.sdpa | 1.709 | 2.6 |
| fwd:block*.mlp | 1.105 | 1.7 |
| fwd:block*.attn.qkv | 0.878 | 1.3 |
| data | 0.664 | 1.0 |
| fwd:embed | 0.663 | 1.0 |
| fwd:block*.attn.proj | 0.649 | 1.0 |
| fwd:embed.ke | 0.632 | 1.0 |
| bwd.recompute:block*.mlp | 0.507 | 0.8 |
| bwd.invert:block*.mlp | 0.501 | 0.8 |
| opt:opt.clip | 0.411 | 0.6 |
| bwd:embed | 0.316 | 0.5 |
| fwd:block*.ln1 | 0.305 | 0.5 |
| fwd:block*.ln2 | 0.298 | 0.5 |
| opt:opt.zero_grad | 0.209 | 0.3 |
| bwd.invert:block*.attn.qkv | 0.188 | 0.3 |
| bwd.recompute:block*.attn.qkv | 0.188 | 0.3 |
| bwd.recompute:block*.attn.proj | 0.180 | 0.3 |
| bwd.invert:block*.attn.proj | 0.179 | 0.3 |
| bwd.invert:block*.ln1 | 0.126 | 0.2 |
| bwd.recompute:block*.ln1 | 0.126 | 0.2 |
| bwd.recompute:block*.ln2 | 0.121 | 0.2 |
| bwd.invert:block*.ln2 | 0.120 | 0.2 |
| opt:opt.moe_bias | 0.016 | 0.0 |

## Five slowest leaf parts

1. `opt:opt.muon.ns` — 24.123 ms (36.5% of step)
2. `bwd:block1.grad` — 0.820 ms (1.2% of step)
3. `bwd:block3.grad` — 0.819 ms (1.2% of step)
4. `bwd:block0.grad` — 0.819 ms (1.2% of step)
5. `bwd:block4.grad` — 0.818 ms (1.2% of step)
