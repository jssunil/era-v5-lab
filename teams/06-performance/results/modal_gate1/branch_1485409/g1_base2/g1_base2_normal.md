# Bench report — g1_base2_normal

**GPU:** NVIDIA A100-SXM4-40GB  |  **dtype:** bf16  |  **B x T:** 16 x 256  |  **torch:** 2.15.0+cu132
**commit:** `14854097c57056f326efd0c7a40cc036a73bbc94`  |  **tag:** g1_base2_normal

## Step (clean)

- median: 84.591 ms
- p10..p90: 77.425 .. 89.435 ms
- tokens/s: 48,421
- MFU: 3.8%  |  HFU: 4.3%

## Diagnostics

### CUDA timing-event allocations

- [OK] clean: events_created_during_steps=0
- [OK] layer: events_created_during_steps=0
- [OK] layer.inner_pass: events_created_during_steps=0

### Benchmark warnings

- [warn] recorder overhead 2.2% > 2.0%: layer numbers are flagged
- [warn] 13 gated part(s) have p10..p90 spread > 10%, so may miss the 5% check: data, fwd:embed, fwd:stack, fwd:block0, fwd:block1, fwd:block2 (+7 more)

## Regions

| part | median ms | p90 | % of step | level |
| :--- | ---: | ---: | ---: | ---: |
| data | 0.904 | 1.018 | 1.1 | 1 |
| fwd | 18.992 | 19.576 | 22.5 | 1 |
| fwd:embed | 0.785 | 0.836 | 0.9 | 2 |
| fwd:embed.ke | 0.785 | 0.827 | 0.9 | 3 |
| fwd:stack | 7.591 | 8.131 | 9.0 | 1 |
| fwd:block0 | 1.427 | 1.601 | 1.7 | 2 |
| fwd:block0.ln1 | 0.098 | 0.118 | 0.1 | 3 |
| fwd:block0.attn.qkv | 0.278 | 0.313 | 0.3 | 3 |
| fwd:block0.attn.sdpa | 0.634 | 0.695 | 0.7 | 3 |
| fwd:block0.attn.proj | 0.205 | 0.224 | 0.2 | 3 |
| fwd:block0.ln2 | 0.071 | 0.089 | 0.1 | 3 |
| fwd:block0.mlp | 0.267 | 0.301 | 0.3 | 3 |
| fwd:block1 | 1.178 | 1.275 | 1.4 | 2 |
| fwd:block1.ln1 | 0.071 | 0.089 | 0.1 | 3 |
| fwd:block1.attn.qkv | 0.200 | 0.226 | 0.2 | 3 |
| fwd:block1.attn.sdpa | 0.501 | 0.545 | 0.6 | 3 |
| fwd:block1.attn.proj | 0.185 | 0.210 | 0.2 | 3 |
| fwd:block1.ln2 | 0.066 | 0.077 | 0.1 | 3 |
| fwd:block1.mlp | 0.250 | 0.283 | 0.3 | 3 |
| fwd:block2 | 1.156 | 1.250 | 1.4 | 2 |
| fwd:block2.ln1 | 0.068 | 0.082 | 0.1 | 3 |
| fwd:block2.attn.qkv | 0.197 | 0.222 | 0.2 | 3 |
| fwd:block2.attn.sdpa | 0.491 | 0.537 | 0.6 | 3 |
| fwd:block2.attn.proj | 0.182 | 0.208 | 0.2 | 3 |
| fwd:block2.ln2 | 0.065 | 0.078 | 0.1 | 3 |
| fwd:block2.mlp | 0.246 | 0.271 | 0.3 | 3 |
| fwd:block3 | 1.144 | 1.261 | 1.4 | 2 |
| fwd:block3.ln1 | 0.066 | 0.081 | 0.1 | 3 |
| fwd:block3.attn.qkv | 0.197 | 0.223 | 0.2 | 3 |
| fwd:block3.attn.sdpa | 0.480 | 0.516 | 0.6 | 3 |
| fwd:block3.attn.proj | 0.186 | 0.211 | 0.2 | 3 |
| fwd:block3.ln2 | 0.063 | 0.076 | 0.1 | 3 |
| fwd:block3.mlp | 0.244 | 0.271 | 0.3 | 3 |
| fwd:block4 | 1.136 | 1.236 | 1.3 | 2 |
| fwd:block4.ln1 | 0.066 | 0.073 | 0.1 | 3 |
| fwd:block4.attn.qkv | 0.195 | 0.220 | 0.2 | 3 |
| fwd:block4.attn.sdpa | 0.476 | 0.516 | 0.6 | 3 |
| fwd:block4.attn.proj | 0.182 | 0.197 | 0.2 | 3 |
| fwd:block4.ln2 | 0.062 | 0.076 | 0.1 | 3 |
| fwd:block4.mlp | 0.242 | 0.278 | 0.3 | 3 |
| fwd:block5 | 1.111 | 1.232 | 1.3 | 2 |
| fwd:block5.ln1 | 0.066 | 0.076 | 0.1 | 3 |
| fwd:block5.attn.qkv | 0.190 | 0.214 | 0.2 | 3 |
| fwd:block5.attn.sdpa | 0.479 | 0.513 | 0.6 | 3 |
| fwd:block5.attn.proj | 0.180 | 0.205 | 0.2 | 3 |
| fwd:block5.ln2 | 0.063 | 0.078 | 0.1 | 3 |
| fwd:block5.mlp | 0.244 | 0.267 | 0.3 | 3 |
| fwd:head+loss | 10.459 | 10.477 | 12.4 | 2 |
| bwd | 23.423 | 23.567 | 27.7 | 1 |
| bwd:head+loss | 12.283 | 12.296 | 14.5 | 2 |
| bwd:stack | 10.813 | 10.951 | 12.8 | 1 |
| bwd:block5 | 1.794 | 1.811 | 2.1 | 2 |
| bwd.invert:block5 | 0.535 | 0.559 | 0.6 | 3 |
| bwd.invert:block5.ln1 | 0.020 | 0.023 | 0.0 | 3 |
| bwd.invert:block5.attn.qkv | 0.031 | 0.033 | 0.0 | 3 |
| bwd.invert:block5.attn.sdpa | 0.286 | 0.289 | 0.3 | 3 |
| bwd.invert:block5.attn.proj | 0.031 | 0.034 | 0.0 | 3 |
| bwd.invert:block5.ln2 | 0.020 | 0.023 | 0.0 | 3 |
| bwd.invert:block5.mlp | 0.084 | 0.088 | 0.1 | 3 |
| bwd.recompute:block5 | 0.536 | 0.557 | 0.6 | 3 |
| bwd.recompute:block5.ln1 | 0.020 | 0.024 | 0.0 | 3 |
| bwd.recompute:block5.attn.qkv | 0.032 | 0.037 | 0.0 | 3 |
| bwd.recompute:block5.attn.sdpa | 0.284 | 0.288 | 0.3 | 3 |
| bwd.recompute:block5.attn.proj | 0.030 | 0.034 | 0.0 | 3 |
| bwd.recompute:block5.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.recompute:block5.mlp | 0.084 | 0.088 | 0.1 | 3 |
| bwd:block5.grad | 0.823 | 0.836 | 1.0 | 3 |
| bwd:block4 | 1.798 | 1.820 | 2.1 | 2 |
| bwd.invert:block4 | 0.539 | 0.559 | 0.6 | 3 |
| bwd.invert:block4.ln1 | 0.022 | 0.024 | 0.0 | 3 |
| bwd.invert:block4.attn.qkv | 0.032 | 0.038 | 0.0 | 3 |
| bwd.invert:block4.attn.sdpa | 0.287 | 0.290 | 0.3 | 3 |
| bwd.invert:block4.attn.proj | 0.030 | 0.032 | 0.0 | 3 |
| bwd.invert:block4.ln2 | 0.019 | 0.020 | 0.0 | 3 |
| bwd.invert:block4.mlp | 0.085 | 0.088 | 0.1 | 3 |
| bwd.recompute:block4 | 0.539 | 0.558 | 0.6 | 3 |
| bwd.recompute:block4.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block4.attn.qkv | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block4.attn.sdpa | 0.287 | 0.290 | 0.3 | 3 |
| bwd.recompute:block4.attn.proj | 0.031 | 0.034 | 0.0 | 3 |
| bwd.recompute:block4.ln2 | 0.019 | 0.024 | 0.0 | 3 |
| bwd.recompute:block4.mlp | 0.086 | 0.089 | 0.1 | 3 |
| bwd:block4.grad | 0.823 | 0.836 | 1.0 | 3 |
| bwd:block3 | 1.794 | 1.815 | 2.1 | 2 |
| bwd.invert:block3 | 0.536 | 0.557 | 0.6 | 3 |
| bwd.invert:block3.ln1 | 0.020 | 0.023 | 0.0 | 3 |
| bwd.invert:block3.attn.qkv | 0.031 | 0.034 | 0.0 | 3 |
| bwd.invert:block3.attn.sdpa | 0.286 | 0.290 | 0.3 | 3 |
| bwd.invert:block3.attn.proj | 0.031 | 0.035 | 0.0 | 3 |
| bwd.invert:block3.ln2 | 0.020 | 0.025 | 0.0 | 3 |
| bwd.invert:block3.mlp | 0.085 | 0.087 | 0.1 | 3 |
| bwd.recompute:block3 | 0.537 | 0.560 | 0.6 | 3 |
| bwd.recompute:block3.ln1 | 0.022 | 0.025 | 0.0 | 3 |
| bwd.recompute:block3.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block3.attn.sdpa | 0.285 | 0.289 | 0.3 | 3 |
| bwd.recompute:block3.attn.proj | 0.030 | 0.035 | 0.0 | 3 |
| bwd.recompute:block3.ln2 | 0.019 | 0.021 | 0.0 | 3 |
| bwd.recompute:block3.mlp | 0.085 | 0.088 | 0.1 | 3 |
| bwd:block3.grad | 0.824 | 0.838 | 1.0 | 3 |
| bwd:block2 | 1.794 | 1.814 | 2.1 | 2 |
| bwd.invert:block2 | 0.537 | 0.558 | 0.6 | 3 |
| bwd.invert:block2.ln1 | 0.021 | 0.023 | 0.0 | 3 |
| bwd.invert:block2.attn.qkv | 0.032 | 0.034 | 0.0 | 3 |
| bwd.invert:block2.attn.sdpa | 0.288 | 0.291 | 0.3 | 3 |
| bwd.invert:block2.attn.proj | 0.030 | 0.032 | 0.0 | 3 |
| bwd.invert:block2.ln2 | 0.019 | 0.022 | 0.0 | 3 |
| bwd.invert:block2.mlp | 0.083 | 0.086 | 0.1 | 3 |
| bwd.recompute:block2 | 0.539 | 0.563 | 0.6 | 3 |
| bwd.recompute:block2.ln1 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.recompute:block2.attn.qkv | 0.031 | 0.033 | 0.0 | 3 |
| bwd.recompute:block2.attn.sdpa | 0.288 | 0.292 | 0.3 | 3 |
| bwd.recompute:block2.attn.proj | 0.031 | 0.033 | 0.0 | 3 |
| bwd.recompute:block2.ln2 | 0.020 | 0.024 | 0.0 | 3 |
| bwd.recompute:block2.mlp | 0.086 | 0.088 | 0.1 | 3 |
| bwd:block2.grad | 0.821 | 0.833 | 1.0 | 3 |
| bwd:block1 | 1.798 | 1.821 | 2.1 | 2 |
| bwd.invert:block1 | 0.538 | 0.561 | 0.6 | 3 |
| bwd.invert:block1.ln1 | 0.020 | 0.024 | 0.0 | 3 |
| bwd.invert:block1.attn.qkv | 0.031 | 0.034 | 0.0 | 3 |
| bwd.invert:block1.attn.sdpa | 0.286 | 0.290 | 0.3 | 3 |
| bwd.invert:block1.attn.proj | 0.031 | 0.035 | 0.0 | 3 |
| bwd.invert:block1.ln2 | 0.020 | 0.022 | 0.0 | 3 |
| bwd.invert:block1.mlp | 0.086 | 0.089 | 0.1 | 3 |
| bwd.recompute:block1 | 0.538 | 0.556 | 0.6 | 3 |
| bwd.recompute:block1.ln1 | 0.020 | 0.023 | 0.0 | 3 |
| bwd.recompute:block1.attn.qkv | 0.032 | 0.033 | 0.0 | 3 |
| bwd.recompute:block1.attn.sdpa | 0.286 | 0.289 | 0.3 | 3 |
| bwd.recompute:block1.attn.proj | 0.031 | 0.032 | 0.0 | 3 |
| bwd.recompute:block1.ln2 | 0.019 | 0.022 | 0.0 | 3 |
| bwd.recompute:block1.mlp | 0.085 | 0.088 | 0.1 | 3 |
| bwd:block1.grad | 0.825 | 0.839 | 1.0 | 3 |
| bwd:block0 | 1.798 | 1.818 | 2.1 | 2 |
| bwd.invert:block0 | 0.537 | 0.743 | 0.6 | 3 |
| bwd.invert:block0.ln1 | 0.022 | 0.025 | 0.0 | 3 |
| bwd.invert:block0.attn.qkv | 0.032 | 0.037 | 0.0 | 3 |
| bwd.invert:block0.attn.sdpa | 0.286 | 0.290 | 0.3 | 3 |
| bwd.invert:block0.attn.proj | 0.030 | 0.033 | 0.0 | 3 |
| bwd.invert:block0.ln2 | 0.019 | 0.027 | 0.0 | 3 |
| bwd.invert:block0.mlp | 0.084 | 0.168 | 0.1 | 3 |
| bwd.recompute:block0 | 0.541 | 1.798 | 0.6 | 3 |
| bwd.recompute:block0.ln1 | 0.020 | 0.080 | 0.0 | 3 |
| bwd.recompute:block0.attn.qkv | 0.031 | 0.218 | 0.0 | 3 |
| bwd.recompute:block0.attn.sdpa | 0.288 | 0.552 | 0.3 | 3 |
| bwd.recompute:block0.attn.proj | 0.030 | 0.206 | 0.0 | 3 |
| bwd.recompute:block0.ln2 | 0.020 | 0.074 | 0.0 | 3 |
| bwd.recompute:block0.mlp | 0.085 | 0.273 | 0.1 | 3 |
| bwd:block0.grad | 1.355 | 2.124 | 1.6 | 3 |
| bwd:embed | 0.318 | 0.327 | 0.4 | 2 |
| opt | 37.894 | 41.614 | 44.8 | 1 |
| opt:opt.clip | 0.411 | 0.419 | 0.5 | 2 |
| opt:opt.polar_muon_adamw | 37.145 | 40.807 | 43.9 | 2 |
| opt:opt.muon | 31.389 | 34.977 | 37.1 | 2 |
| opt:opt.muon.ns | 37.631 | 39.681 | 44.5 | 3 |
| opt:opt.adamw | 5.553 | 5.885 | 6.6 | 2 |
| opt:opt.moe_bias | 0.018 | 0.023 | 0.0 | 3 |
| opt:opt.zero_grad | 0.334 | 0.379 | 0.4 | 3 |

## Time by part type (sum over layers)

| part type | median ms sum | % of step |
| :--- | ---: | ---: |
| opt | 37.894 | 44.8 |
| opt:opt.muon.ns | 37.631 | 44.5 |
| opt:opt.polar_muon_adamw | 37.145 | 43.9 |
| opt:opt.muon | 31.389 | 37.1 |
| bwd | 23.423 | 27.7 |
| fwd | 18.992 | 22.5 |
| bwd:head+loss | 12.283 | 14.5 |
| bwd:stack | 10.813 | 12.8 |
| bwd:block* | 10.776 | 12.7 |
| fwd:head+loss | 10.459 | 12.4 |
| fwd:stack | 7.591 | 9.0 |
| fwd:block* | 7.151 | 8.5 |
| opt:opt.adamw | 5.553 | 6.6 |
| bwd:block*.grad | 5.473 | 6.5 |
| bwd.recompute:block* | 3.228 | 3.8 |
| bwd.invert:block* | 3.219 | 3.8 |
| fwd:block*.attn.sdpa | 3.061 | 3.6 |
| bwd.invert:block*.attn.sdpa | 1.718 | 2.0 |
| bwd.recompute:block*.attn.sdpa | 1.716 | 2.0 |
| fwd:block*.mlp | 1.492 | 1.8 |
| fwd:block*.attn.qkv | 1.256 | 1.5 |
| fwd:block*.attn.proj | 1.121 | 1.3 |
| data | 0.904 | 1.1 |
| fwd:embed | 0.785 | 0.9 |
| fwd:embed.ke | 0.785 | 0.9 |
| bwd.recompute:block*.mlp | 0.511 | 0.6 |
| bwd.invert:block*.mlp | 0.507 | 0.6 |
| fwd:block*.ln1 | 0.433 | 0.5 |
| opt:opt.clip | 0.411 | 0.5 |
| fwd:block*.ln2 | 0.390 | 0.5 |
| opt:opt.zero_grad | 0.334 | 0.4 |
| bwd:embed | 0.318 | 0.4 |
| bwd.invert:block*.attn.qkv | 0.187 | 0.2 |
| bwd.recompute:block*.attn.qkv | 0.187 | 0.2 |
| bwd.recompute:block*.attn.proj | 0.183 | 0.2 |
| bwd.invert:block*.attn.proj | 0.181 | 0.2 |
| bwd.invert:block*.ln1 | 0.125 | 0.1 |
| bwd.recompute:block*.ln1 | 0.124 | 0.1 |
| bwd.invert:block*.ln2 | 0.120 | 0.1 |
| bwd.recompute:block*.ln2 | 0.119 | 0.1 |
| opt:opt.moe_bias | 0.018 | 0.0 |

## Five slowest leaf parts

1. `opt:opt.muon.ns` — 37.631 ms (44.5% of step)
2. `bwd:block0.grad` — 1.355 ms (1.6% of step)
3. `bwd:block1.grad` — 0.825 ms (1.0% of step)
4. `bwd:block3.grad` — 0.824 ms (1.0% of step)
5. `bwd:block5.grad` — 0.823 ms (1.0% of step)
