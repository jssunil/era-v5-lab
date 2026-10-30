# Bench report — g1_lab2_normal

**GPU:** NVIDIA A100-SXM4-40GB  |  **dtype:** bf16  |  **B x T:** 32 x 512  |  **torch:** 2.15.0+cu132
**commit:** `14854097c57056f326efd0c7a40cc036a73bbc94`  |  **tag:** g1_lab2_normal

## Step (clean)

- median: 547.698 ms
- p10..p90: 532.985 .. 579.164 ms
- tokens/s: 29,914
- MFU: 3.1%  |  HFU: 3.9%

## Diagnostics

### CUDA timing-event allocations

- [OK] clean: events_created_during_steps=0
- [OK] layer: events_created_during_steps=0
- [OK] layer.inner_pass: events_created_during_steps=0

### Benchmark warnings

- [warn] 27 gated part(s) have p10..p90 spread > 10%, so may miss the 5% check: data, fwd:stack, fwd:block0, fwd:block1, fwd:block2, fwd:block3 (+21 more)

## Regions

| part | median ms | p90 | % of step | level |
| :--- | ---: | ---: | ---: | ---: |
| data | 1.125 | 1.273 | 0.2 | 1 |
| fwd | 109.529 | 115.032 | 20.0 | 1 |
| fwd:embed | 4.482 | 4.534 | 0.8 | 2 |
| fwd:embed.ke | 4.433 | 4.484 | 0.8 | 3 |
| fwd:stack | 63.879 | 69.306 | 11.7 | 1 |
| fwd:block0 | 6.738 | 7.203 | 1.2 | 2 |
| fwd:block0.ln1 | 0.052 | 0.053 | 0.0 | 3 |
| fwd:block0.attn.qkv | 0.050 | 0.051 | 0.0 | 3 |
| fwd:block0.attn.sdpa | 0.082 | 0.084 | 0.0 | 3 |
| fwd:block0.attn.proj | 0.038 | 0.039 | 0.0 | 3 |
| fwd:block0.ln2 | 0.053 | 0.054 | 0.0 | 3 |
| fwd:block0.moe.router | 0.141 | 0.143 | 0.0 | 3 |
| fwd:block0.moe.dispatch | 6.663 | 7.115 | 1.2 | 3 |
| fwd:block0.moe.dispatch.expert0 | 0.857 | 0.933 | 0.2 | 3 |
| fwd:block0.moe.dispatch.expert1 | 0.821 | 0.899 | 0.1 | 3 |
| fwd:block0.moe.dispatch.expert2 | 0.799 | 0.880 | 0.1 | 3 |
| fwd:block0.moe.dispatch.expert3 | 0.785 | 0.877 | 0.1 | 3 |
| fwd:block0.moe.dispatch.expert4 | 0.816 | 0.881 | 0.1 | 3 |
| fwd:block0.moe.dispatch.expert5 | 0.786 | 0.868 | 0.1 | 3 |
| fwd:block0.moe.dispatch.expert6 | 0.747 | 0.859 | 0.1 | 3 |
| fwd:block0.moe.dispatch.expert7 | 0.753 | 0.851 | 0.1 | 3 |
| fwd:block0.moe.shared | 0.369 | 0.411 | 0.1 | 3 |
| fwd:block1 | 7.133 | 7.945 | 1.3 | 2 |
| fwd:block1.ln1 | 0.108 | 0.130 | 0.0 | 3 |
| fwd:block1.attn.qkv | 0.239 | 0.265 | 0.0 | 3 |
| fwd:block1.attn.sdpa | 0.158 | 0.180 | 0.0 | 3 |
| fwd:block1.attn.proj | 0.131 | 0.163 | 0.0 | 3 |
| fwd:block1.ln2 | 0.080 | 0.094 | 0.0 | 3 |
| fwd:block1.moe.router | 0.414 | 0.503 | 0.1 | 3 |
| fwd:block1.moe.dispatch | 6.545 | 7.099 | 1.2 | 3 |
| fwd:block1.moe.dispatch.expert0 | 0.723 | 0.817 | 0.1 | 3 |
| fwd:block1.moe.dispatch.expert1 | 0.793 | 0.878 | 0.1 | 3 |
| fwd:block1.moe.dispatch.expert2 | 0.788 | 0.874 | 0.1 | 3 |
| fwd:block1.moe.dispatch.expert3 | 0.766 | 0.861 | 0.1 | 3 |
| fwd:block1.moe.dispatch.expert4 | 0.771 | 0.861 | 0.1 | 3 |
| fwd:block1.moe.dispatch.expert5 | 0.766 | 0.866 | 0.1 | 3 |
| fwd:block1.moe.dispatch.expert6 | 0.760 | 0.862 | 0.1 | 3 |
| fwd:block1.moe.dispatch.expert7 | 0.745 | 0.852 | 0.1 | 3 |
| fwd:block1.moe.shared | 0.364 | 0.400 | 0.1 | 3 |
| fwd:block2 | 7.025 | 7.746 | 1.3 | 2 |
| fwd:block2.ln1 | 0.104 | 0.125 | 0.0 | 3 |
| fwd:block2.attn.qkv | 0.233 | 0.264 | 0.0 | 3 |
| fwd:block2.attn.sdpa | 0.150 | 0.170 | 0.0 | 3 |
| fwd:block2.attn.proj | 0.130 | 0.154 | 0.0 | 3 |
| fwd:block2.ln2 | 0.080 | 0.093 | 0.0 | 3 |
| fwd:block2.moe.router | 0.400 | 0.484 | 0.1 | 3 |
| fwd:block2.moe.dispatch | 6.583 | 7.002 | 1.2 | 3 |
| fwd:block2.moe.dispatch.expert0 | 0.732 | 0.823 | 0.1 | 3 |
| fwd:block2.moe.dispatch.expert1 | 0.766 | 0.862 | 0.1 | 3 |
| fwd:block2.moe.dispatch.expert2 | 0.774 | 0.859 | 0.1 | 3 |
| fwd:block2.moe.dispatch.expert3 | 0.825 | 0.886 | 0.2 | 3 |
| fwd:block2.moe.dispatch.expert4 | 0.764 | 0.857 | 0.1 | 3 |
| fwd:block2.moe.dispatch.expert5 | 0.749 | 0.828 | 0.1 | 3 |
| fwd:block2.moe.dispatch.expert6 | 0.743 | 0.842 | 0.1 | 3 |
| fwd:block2.moe.dispatch.expert7 | 0.763 | 0.857 | 0.1 | 3 |
| fwd:block2.moe.shared | 0.371 | 0.403 | 0.1 | 3 |
| fwd:block3 | 7.035 | 7.648 | 1.3 | 2 |
| fwd:block3.ln1 | 0.104 | 0.122 | 0.0 | 3 |
| fwd:block3.attn.qkv | 0.228 | 0.258 | 0.0 | 3 |
| fwd:block3.attn.sdpa | 0.148 | 0.172 | 0.0 | 3 |
| fwd:block3.attn.proj | 0.125 | 0.156 | 0.0 | 3 |
| fwd:block3.ln2 | 0.079 | 0.093 | 0.0 | 3 |
| fwd:block3.moe.router | 0.392 | 0.484 | 0.1 | 3 |
| fwd:block3.moe.dispatch | 6.500 | 6.913 | 1.2 | 3 |
| fwd:block3.moe.dispatch.expert0 | 0.718 | 0.804 | 0.1 | 3 |
| fwd:block3.moe.dispatch.expert1 | 0.772 | 0.859 | 0.1 | 3 |
| fwd:block3.moe.dispatch.expert2 | 0.765 | 0.854 | 0.1 | 3 |
| fwd:block3.moe.dispatch.expert3 | 0.746 | 0.849 | 0.1 | 3 |
| fwd:block3.moe.dispatch.expert4 | 0.767 | 0.858 | 0.1 | 3 |
| fwd:block3.moe.dispatch.expert5 | 0.784 | 0.866 | 0.1 | 3 |
| fwd:block3.moe.dispatch.expert6 | 0.761 | 0.855 | 0.1 | 3 |
| fwd:block3.moe.dispatch.expert7 | 0.744 | 0.851 | 0.1 | 3 |
| fwd:block3.moe.shared | 0.364 | 0.392 | 0.1 | 3 |
| fwd:block4 | 7.075 | 7.692 | 1.3 | 2 |
| fwd:block4.ln1 | 0.104 | 0.122 | 0.0 | 3 |
| fwd:block4.attn.qkv | 0.225 | 0.262 | 0.0 | 3 |
| fwd:block4.attn.sdpa | 0.145 | 0.171 | 0.0 | 3 |
| fwd:block4.attn.proj | 0.129 | 0.154 | 0.0 | 3 |
| fwd:block4.ln2 | 0.079 | 0.094 | 0.0 | 3 |
| fwd:block4.moe.router | 0.389 | 0.479 | 0.1 | 3 |
| fwd:block4.moe.dispatch | 6.527 | 6.913 | 1.2 | 3 |
| fwd:block4.moe.dispatch.expert0 | 0.728 | 0.798 | 0.1 | 3 |
| fwd:block4.moe.dispatch.expert1 | 0.779 | 0.857 | 0.1 | 3 |
| fwd:block4.moe.dispatch.expert2 | 0.778 | 0.859 | 0.1 | 3 |
| fwd:block4.moe.dispatch.expert3 | 0.766 | 0.864 | 0.1 | 3 |
| fwd:block4.moe.dispatch.expert4 | 0.743 | 0.833 | 0.1 | 3 |
| fwd:block4.moe.dispatch.expert5 | 0.739 | 0.833 | 0.1 | 3 |
| fwd:block4.moe.dispatch.expert6 | 0.767 | 0.863 | 0.1 | 3 |
| fwd:block4.moe.dispatch.expert7 | 0.761 | 0.850 | 0.1 | 3 |
| fwd:block4.moe.shared | 0.356 | 0.385 | 0.1 | 3 |
| fwd:block5 | 6.942 | 7.629 | 1.3 | 2 |
| fwd:block5.ln1 | 0.103 | 0.128 | 0.0 | 3 |
| fwd:block5.attn.qkv | 0.224 | 0.252 | 0.0 | 3 |
| fwd:block5.attn.sdpa | 0.142 | 0.165 | 0.0 | 3 |
| fwd:block5.attn.proj | 0.123 | 0.148 | 0.0 | 3 |
| fwd:block5.ln2 | 0.080 | 0.095 | 0.0 | 3 |
| fwd:block5.moe.router | 0.382 | 0.475 | 0.1 | 3 |
| fwd:block5.moe.dispatch | 6.356 | 6.934 | 1.2 | 3 |
| fwd:block5.moe.dispatch.expert0 | 0.704 | 0.792 | 0.1 | 3 |
| fwd:block5.moe.dispatch.expert1 | 0.753 | 0.843 | 0.1 | 3 |
| fwd:block5.moe.dispatch.expert2 | 0.748 | 0.836 | 0.1 | 3 |
| fwd:block5.moe.dispatch.expert3 | 0.742 | 0.840 | 0.1 | 3 |
| fwd:block5.moe.dispatch.expert4 | 0.754 | 0.852 | 0.1 | 3 |
| fwd:block5.moe.dispatch.expert5 | 0.749 | 0.849 | 0.1 | 3 |
| fwd:block5.moe.dispatch.expert6 | 0.743 | 0.846 | 0.1 | 3 |
| fwd:block5.moe.dispatch.expert7 | 0.765 | 0.858 | 0.1 | 3 |
| fwd:block5.moe.shared | 0.368 | 0.399 | 0.1 | 3 |
| fwd:block6 | 6.947 | 7.554 | 1.3 | 2 |
| fwd:block6.ln1 | 0.105 | 0.122 | 0.0 | 3 |
| fwd:block6.attn.qkv | 0.224 | 0.256 | 0.0 | 3 |
| fwd:block6.attn.sdpa | 0.144 | 0.162 | 0.0 | 3 |
| fwd:block6.attn.proj | 0.125 | 0.158 | 0.0 | 3 |
| fwd:block6.ln2 | 0.078 | 0.094 | 0.0 | 3 |
| fwd:block6.moe.router | 0.390 | 0.479 | 0.1 | 3 |
| fwd:block6.moe.dispatch | 6.477 | 6.891 | 1.2 | 3 |
| fwd:block6.moe.dispatch.expert0 | 0.740 | 0.801 | 0.1 | 3 |
| fwd:block6.moe.dispatch.expert1 | 0.781 | 0.857 | 0.1 | 3 |
| fwd:block6.moe.dispatch.expert2 | 0.743 | 0.839 | 0.1 | 3 |
| fwd:block6.moe.dispatch.expert3 | 0.743 | 0.821 | 0.1 | 3 |
| fwd:block6.moe.dispatch.expert4 | 0.744 | 0.843 | 0.1 | 3 |
| fwd:block6.moe.dispatch.expert5 | 0.768 | 0.852 | 0.1 | 3 |
| fwd:block6.moe.dispatch.expert6 | 0.755 | 0.848 | 0.1 | 3 |
| fwd:block6.moe.dispatch.expert7 | 0.756 | 0.854 | 0.1 | 3 |
| fwd:block6.moe.shared | 0.368 | 0.399 | 0.1 | 3 |
| fwd:block7 | 6.946 | 7.528 | 1.3 | 2 |
| fwd:block7.ln1 | 0.104 | 0.127 | 0.0 | 3 |
| fwd:block7.attn.qkv | 0.219 | 0.252 | 0.0 | 3 |
| fwd:block7.attn.sdpa | 0.142 | 0.164 | 0.0 | 3 |
| fwd:block7.attn.proj | 0.127 | 0.154 | 0.0 | 3 |
| fwd:block7.ln2 | 0.077 | 0.093 | 0.0 | 3 |
| fwd:block7.moe.router | 0.384 | 0.468 | 0.1 | 3 |
| fwd:block7.moe.dispatch | 6.389 | 6.853 | 1.2 | 3 |
| fwd:block7.moe.dispatch.expert0 | 0.737 | 0.789 | 0.1 | 3 |
| fwd:block7.moe.dispatch.expert1 | 0.749 | 0.859 | 0.1 | 3 |
| fwd:block7.moe.dispatch.expert2 | 0.727 | 0.820 | 0.1 | 3 |
| fwd:block7.moe.dispatch.expert3 | 0.746 | 0.830 | 0.1 | 3 |
| fwd:block7.moe.dispatch.expert4 | 0.753 | 0.844 | 0.1 | 3 |
| fwd:block7.moe.dispatch.expert5 | 0.760 | 0.839 | 0.1 | 3 |
| fwd:block7.moe.dispatch.expert6 | 0.754 | 0.844 | 0.1 | 3 |
| fwd:block7.moe.dispatch.expert7 | 0.735 | 0.832 | 0.1 | 3 |
| fwd:block7.moe.shared | 0.364 | 0.398 | 0.1 | 3 |
| fwd:block8 | 6.969 | 7.582 | 1.3 | 2 |
| fwd:block8.ln1 | 0.104 | 0.122 | 0.0 | 3 |
| fwd:block8.attn.qkv | 0.221 | 0.254 | 0.0 | 3 |
| fwd:block8.attn.sdpa | 0.141 | 0.160 | 0.0 | 3 |
| fwd:block8.attn.proj | 0.126 | 0.153 | 0.0 | 3 |
| fwd:block8.ln2 | 0.079 | 0.092 | 0.0 | 3 |
| fwd:block8.moe.router | 0.382 | 0.472 | 0.1 | 3 |
| fwd:block8.moe.dispatch | 6.448 | 6.873 | 1.2 | 3 |
| fwd:block8.moe.dispatch.expert0 | 0.740 | 0.793 | 0.1 | 3 |
| fwd:block8.moe.dispatch.expert1 | 0.769 | 0.855 | 0.1 | 3 |
| fwd:block8.moe.dispatch.expert2 | 0.756 | 0.840 | 0.1 | 3 |
| fwd:block8.moe.dispatch.expert3 | 0.754 | 0.840 | 0.1 | 3 |
| fwd:block8.moe.dispatch.expert4 | 0.749 | 0.844 | 0.1 | 3 |
| fwd:block8.moe.dispatch.expert5 | 0.752 | 0.851 | 0.1 | 3 |
| fwd:block8.moe.dispatch.expert6 | 0.741 | 0.842 | 0.1 | 3 |
| fwd:block8.moe.dispatch.expert7 | 0.750 | 0.847 | 0.1 | 3 |
| fwd:block8.moe.shared | 0.361 | 0.384 | 0.1 | 3 |
| fwd:head+loss | 40.963 | 41.005 | 7.5 | 2 |
| bwd | 269.158 | 293.250 | 49.1 | 1 |
| bwd:head+loss | 48.176 | 48.195 | 8.8 | 2 |
| bwd:stack | 220.420 | 244.538 | 40.2 | 1 |
| bwd:block8 | 25.437 | 27.526 | 4.6 | 2 |
| bwd.invert:block8 | 7.710 | 8.223 | 1.4 | 3 |
| bwd.invert:block8.ln1 | 0.054 | 0.054 | 0.0 | 3 |
| bwd.invert:block8.attn.qkv | 0.050 | 0.052 | 0.0 | 3 |
| bwd.invert:block8.attn.sdpa | 0.082 | 0.083 | 0.0 | 3 |
| bwd.invert:block8.attn.proj | 0.038 | 0.039 | 0.0 | 3 |
| bwd.invert:block8.ln2 | 0.053 | 0.055 | 0.0 | 3 |
| bwd.invert:block8.moe.router | 0.067 | 0.068 | 0.0 | 3 |
| bwd.invert:block8.moe.dispatch | 6.537 | 7.030 | 1.2 | 3 |
| bwd.invert:block8.moe.dispatch.expert0 | 1.326 | 1.510 | 0.2 | 3 |
| bwd.invert:block8.moe.dispatch.expert1 | 0.796 | 0.882 | 0.1 | 3 |
| bwd.invert:block8.moe.dispatch.expert2 | 0.697 | 0.750 | 0.1 | 3 |
| bwd.invert:block8.moe.dispatch.expert3 | 0.686 | 0.736 | 0.1 | 3 |
| bwd.invert:block8.moe.dispatch.expert4 | 0.677 | 0.713 | 0.1 | 3 |
| bwd.invert:block8.moe.dispatch.expert5 | 0.677 | 0.715 | 0.1 | 3 |
| bwd.invert:block8.moe.dispatch.expert6 | 0.671 | 0.707 | 0.1 | 3 |
| bwd.invert:block8.moe.dispatch.expert7 | 0.671 | 0.721 | 0.1 | 3 |
| bwd.invert:block8.moe.shared | 0.359 | 0.387 | 0.1 | 3 |
| bwd.recompute:block8 | 8.422 | 8.815 | 1.5 | 3 |
| bwd.recompute:block8.ln1 | 0.152 | 0.169 | 0.0 | 3 |
| bwd.recompute:block8.attn.qkv | 0.281 | 0.307 | 0.1 | 3 |
| bwd.recompute:block8.attn.sdpa | 0.217 | 0.243 | 0.0 | 3 |
| bwd.recompute:block8.attn.proj | 0.171 | 0.198 | 0.0 | 3 |
| bwd.recompute:block8.ln2 | 0.096 | 0.117 | 0.0 | 3 |
| bwd.recompute:block8.moe.router | 0.374 | 0.409 | 0.1 | 3 |
| bwd.recompute:block8.moe.dispatch | 6.251 | 6.503 | 1.1 | 3 |
| bwd.recompute:block8.moe.dispatch.expert0 | 0.735 | 0.786 | 0.1 | 3 |
| bwd.recompute:block8.moe.dispatch.expert1 | 0.737 | 0.821 | 0.1 | 3 |
| bwd.recompute:block8.moe.dispatch.expert2 | 0.726 | 0.760 | 0.1 | 3 |
| bwd.recompute:block8.moe.dispatch.expert3 | 0.721 | 0.766 | 0.1 | 3 |
| bwd.recompute:block8.moe.dispatch.expert4 | 0.720 | 0.767 | 0.1 | 3 |
| bwd.recompute:block8.moe.dispatch.expert5 | 0.720 | 0.761 | 0.1 | 3 |
| bwd.recompute:block8.moe.dispatch.expert6 | 0.712 | 0.749 | 0.1 | 3 |
| bwd.recompute:block8.moe.dispatch.expert7 | 0.716 | 0.751 | 0.1 | 3 |
| bwd.recompute:block8.moe.shared | 0.366 | 0.385 | 0.1 | 3 |
| bwd:block8.grad | 11.976 | 12.660 | 2.2 | 3 |
| bwd:block7 | 24.394 | 27.095 | 4.5 | 2 |
| bwd.invert:block7 | 7.849 | 8.515 | 1.4 | 3 |
| bwd.invert:block7.ln1 | 0.124 | 0.156 | 0.0 | 3 |
| bwd.invert:block7.attn.qkv | 0.272 | 0.326 | 0.0 | 3 |
| bwd.invert:block7.attn.sdpa | 0.157 | 0.171 | 0.0 | 3 |
| bwd.invert:block7.attn.proj | 0.134 | 0.165 | 0.0 | 3 |
| bwd.invert:block7.ln2 | 0.083 | 0.093 | 0.0 | 3 |
| bwd.invert:block7.moe.router | 0.316 | 0.374 | 0.1 | 3 |
| bwd.invert:block7.moe.dispatch | 5.804 | 6.158 | 1.1 | 3 |
| bwd.invert:block7.moe.dispatch.expert0 | 0.720 | 0.866 | 0.1 | 3 |
| bwd.invert:block7.moe.dispatch.expert1 | 0.672 | 0.721 | 0.1 | 3 |
| bwd.invert:block7.moe.dispatch.expert2 | 0.667 | 0.707 | 0.1 | 3 |
| bwd.invert:block7.moe.dispatch.expert3 | 0.666 | 0.705 | 0.1 | 3 |
| bwd.invert:block7.moe.dispatch.expert4 | 0.664 | 0.699 | 0.1 | 3 |
| bwd.invert:block7.moe.dispatch.expert5 | 0.664 | 0.698 | 0.1 | 3 |
| bwd.invert:block7.moe.dispatch.expert6 | 0.654 | 0.687 | 0.1 | 3 |
| bwd.invert:block7.moe.dispatch.expert7 | 0.660 | 0.701 | 0.1 | 3 |
| bwd.invert:block7.moe.shared | 0.351 | 0.373 | 0.1 | 3 |
| bwd.recompute:block7 | 8.160 | 8.809 | 1.5 | 3 |
| bwd.recompute:block7.ln1 | 0.120 | 0.142 | 0.0 | 3 |
| bwd.recompute:block7.attn.qkv | 0.268 | 0.304 | 0.0 | 3 |
| bwd.recompute:block7.attn.sdpa | 0.175 | 0.203 | 0.0 | 3 |
| bwd.recompute:block7.attn.proj | 0.154 | 0.178 | 0.0 | 3 |
| bwd.recompute:block7.ln2 | 0.092 | 0.109 | 0.0 | 3 |
| bwd.recompute:block7.moe.router | 0.322 | 0.382 | 0.1 | 3 |
| bwd.recompute:block7.moe.dispatch | 6.017 | 6.398 | 1.1 | 3 |
| bwd.recompute:block7.moe.dispatch.expert0 | 0.703 | 0.770 | 0.1 | 3 |
| bwd.recompute:block7.moe.dispatch.expert1 | 0.708 | 0.763 | 0.1 | 3 |
| bwd.recompute:block7.moe.dispatch.expert2 | 0.703 | 0.741 | 0.1 | 3 |
| bwd.recompute:block7.moe.dispatch.expert3 | 0.698 | 0.743 | 0.1 | 3 |
| bwd.recompute:block7.moe.dispatch.expert4 | 0.695 | 0.739 | 0.1 | 3 |
| bwd.recompute:block7.moe.dispatch.expert5 | 0.700 | 0.743 | 0.1 | 3 |
| bwd.recompute:block7.moe.dispatch.expert6 | 0.703 | 0.754 | 0.1 | 3 |
| bwd.recompute:block7.moe.dispatch.expert7 | 0.703 | 0.746 | 0.1 | 3 |
| bwd.recompute:block7.moe.shared | 0.358 | 0.377 | 0.1 | 3 |
| bwd:block7.grad | 11.570 | 12.388 | 2.1 | 3 |
| bwd:block6 | 24.258 | 27.595 | 4.4 | 2 |
| bwd.invert:block6 | 7.712 | 8.460 | 1.4 | 3 |
| bwd.invert:block6.ln1 | 0.130 | 0.154 | 0.0 | 3 |
| bwd.invert:block6.attn.qkv | 0.258 | 0.308 | 0.0 | 3 |
| bwd.invert:block6.attn.sdpa | 0.156 | 0.177 | 0.0 | 3 |
| bwd.invert:block6.attn.proj | 0.141 | 0.173 | 0.0 | 3 |
| bwd.invert:block6.ln2 | 0.082 | 0.097 | 0.0 | 3 |
| bwd.invert:block6.moe.router | 0.299 | 0.365 | 0.1 | 3 |
| bwd.invert:block6.moe.dispatch | 5.722 | 6.149 | 1.0 | 3 |
| bwd.invert:block6.moe.dispatch.expert0 | 0.736 | 0.895 | 0.1 | 3 |
| bwd.invert:block6.moe.dispatch.expert1 | 0.670 | 0.734 | 0.1 | 3 |
| bwd.invert:block6.moe.dispatch.expert2 | 0.658 | 0.700 | 0.1 | 3 |
| bwd.invert:block6.moe.dispatch.expert3 | 0.655 | 0.698 | 0.1 | 3 |
| bwd.invert:block6.moe.dispatch.expert4 | 0.648 | 0.692 | 0.1 | 3 |
| bwd.invert:block6.moe.dispatch.expert5 | 0.652 | 0.695 | 0.1 | 3 |
| bwd.invert:block6.moe.dispatch.expert6 | 0.646 | 0.690 | 0.1 | 3 |
| bwd.invert:block6.moe.dispatch.expert7 | 0.650 | 0.689 | 0.1 | 3 |
| bwd.invert:block6.moe.shared | 0.348 | 0.369 | 0.1 | 3 |
| bwd.recompute:block6 | 8.078 | 8.762 | 1.5 | 3 |
| bwd.recompute:block6.ln1 | 0.120 | 0.149 | 0.0 | 3 |
| bwd.recompute:block6.attn.qkv | 0.253 | 0.292 | 0.0 | 3 |
| bwd.recompute:block6.attn.sdpa | 0.182 | 0.221 | 0.0 | 3 |
| bwd.recompute:block6.attn.proj | 0.158 | 0.183 | 0.0 | 3 |
| bwd.recompute:block6.ln2 | 0.090 | 0.109 | 0.0 | 3 |
| bwd.recompute:block6.moe.router | 0.313 | 0.383 | 0.1 | 3 |
| bwd.recompute:block6.moe.dispatch | 5.990 | 6.385 | 1.1 | 3 |
| bwd.recompute:block6.moe.dispatch.expert0 | 0.712 | 0.780 | 0.1 | 3 |
| bwd.recompute:block6.moe.dispatch.expert1 | 0.702 | 0.757 | 0.1 | 3 |
| bwd.recompute:block6.moe.dispatch.expert2 | 0.685 | 0.739 | 0.1 | 3 |
| bwd.recompute:block6.moe.dispatch.expert3 | 0.687 | 0.733 | 0.1 | 3 |
| bwd.recompute:block6.moe.dispatch.expert4 | 0.699 | 0.737 | 0.1 | 3 |
| bwd.recompute:block6.moe.dispatch.expert5 | 0.698 | 0.748 | 0.1 | 3 |
| bwd.recompute:block6.moe.dispatch.expert6 | 0.692 | 0.737 | 0.1 | 3 |
| bwd.recompute:block6.moe.dispatch.expert7 | 0.700 | 0.751 | 0.1 | 3 |
| bwd.recompute:block6.moe.shared | 0.355 | 0.380 | 0.1 | 3 |
| bwd:block6.grad | 11.557 | 12.501 | 2.1 | 3 |
| bwd:block5 | 24.015 | 27.670 | 4.4 | 2 |
| bwd.invert:block5 | 7.736 | 8.421 | 1.4 | 3 |
| bwd.invert:block5.ln1 | 0.129 | 0.153 | 0.0 | 3 |
| bwd.invert:block5.attn.qkv | 0.259 | 0.310 | 0.0 | 3 |
| bwd.invert:block5.attn.sdpa | 0.155 | 0.176 | 0.0 | 3 |
| bwd.invert:block5.attn.proj | 0.139 | 0.165 | 0.0 | 3 |
| bwd.invert:block5.ln2 | 0.083 | 0.098 | 0.0 | 3 |
| bwd.invert:block5.moe.router | 0.302 | 0.354 | 0.1 | 3 |
| bwd.invert:block5.moe.dispatch | 5.713 | 6.123 | 1.0 | 3 |
| bwd.invert:block5.moe.dispatch.expert0 | 0.740 | 0.853 | 0.1 | 3 |
| bwd.invert:block5.moe.dispatch.expert1 | 0.669 | 0.716 | 0.1 | 3 |
| bwd.invert:block5.moe.dispatch.expert2 | 0.658 | 0.703 | 0.1 | 3 |
| bwd.invert:block5.moe.dispatch.expert3 | 0.653 | 0.696 | 0.1 | 3 |
| bwd.invert:block5.moe.dispatch.expert4 | 0.648 | 0.687 | 0.1 | 3 |
| bwd.invert:block5.moe.dispatch.expert5 | 0.649 | 0.691 | 0.1 | 3 |
| bwd.invert:block5.moe.dispatch.expert6 | 0.644 | 0.695 | 0.1 | 3 |
| bwd.invert:block5.moe.dispatch.expert7 | 0.654 | 0.695 | 0.1 | 3 |
| bwd.invert:block5.moe.shared | 0.350 | 0.373 | 0.1 | 3 |
| bwd.recompute:block5 | 8.086 | 8.622 | 1.5 | 3 |
| bwd.recompute:block5.ln1 | 0.120 | 0.146 | 0.0 | 3 |
| bwd.recompute:block5.attn.qkv | 0.261 | 0.292 | 0.0 | 3 |
| bwd.recompute:block5.attn.sdpa | 0.172 | 0.203 | 0.0 | 3 |
| bwd.recompute:block5.attn.proj | 0.151 | 0.179 | 0.0 | 3 |
| bwd.recompute:block5.ln2 | 0.089 | 0.105 | 0.0 | 3 |
| bwd.recompute:block5.moe.router | 0.311 | 0.367 | 0.1 | 3 |
| bwd.recompute:block5.moe.dispatch | 5.999 | 6.356 | 1.1 | 3 |
| bwd.recompute:block5.moe.dispatch.expert0 | 0.698 | 0.754 | 0.1 | 3 |
| bwd.recompute:block5.moe.dispatch.expert1 | 0.696 | 0.743 | 0.1 | 3 |
| bwd.recompute:block5.moe.dispatch.expert2 | 0.690 | 0.735 | 0.1 | 3 |
| bwd.recompute:block5.moe.dispatch.expert3 | 0.694 | 0.735 | 0.1 | 3 |
| bwd.recompute:block5.moe.dispatch.expert4 | 0.700 | 0.736 | 0.1 | 3 |
| bwd.recompute:block5.moe.dispatch.expert5 | 0.701 | 0.740 | 0.1 | 3 |
| bwd.recompute:block5.moe.dispatch.expert6 | 0.703 | 0.749 | 0.1 | 3 |
| bwd.recompute:block5.moe.dispatch.expert7 | 0.693 | 0.738 | 0.1 | 3 |
| bwd.recompute:block5.moe.shared | 0.354 | 0.377 | 0.1 | 3 |
| bwd:block5.grad | 11.391 | 12.492 | 2.1 | 3 |
| bwd:block4 | 24.236 | 27.267 | 4.4 | 2 |
| bwd.invert:block4 | 7.718 | 8.365 | 1.4 | 3 |
| bwd.invert:block4.ln1 | 0.124 | 0.153 | 0.0 | 3 |
| bwd.invert:block4.attn.qkv | 0.252 | 0.307 | 0.0 | 3 |
| bwd.invert:block4.attn.sdpa | 0.154 | 0.166 | 0.0 | 3 |
| bwd.invert:block4.attn.proj | 0.130 | 0.159 | 0.0 | 3 |
| bwd.invert:block4.ln2 | 0.082 | 0.094 | 0.0 | 3 |
| bwd.invert:block4.moe.router | 0.296 | 0.363 | 0.1 | 3 |
| bwd.invert:block4.moe.dispatch | 5.741 | 6.095 | 1.0 | 3 |
| bwd.invert:block4.moe.dispatch.expert0 | 0.730 | 0.876 | 0.1 | 3 |
| bwd.invert:block4.moe.dispatch.expert1 | 0.670 | 0.712 | 0.1 | 3 |
| bwd.invert:block4.moe.dispatch.expert2 | 0.657 | 0.698 | 0.1 | 3 |
| bwd.invert:block4.moe.dispatch.expert3 | 0.649 | 0.694 | 0.1 | 3 |
| bwd.invert:block4.moe.dispatch.expert4 | 0.656 | 0.690 | 0.1 | 3 |
| bwd.invert:block4.moe.dispatch.expert5 | 0.648 | 0.690 | 0.1 | 3 |
| bwd.invert:block4.moe.dispatch.expert6 | 0.653 | 0.686 | 0.1 | 3 |
| bwd.invert:block4.moe.dispatch.expert7 | 0.652 | 0.687 | 0.1 | 3 |
| bwd.invert:block4.moe.shared | 0.347 | 0.366 | 0.1 | 3 |
| bwd.recompute:block4 | 8.148 | 8.629 | 1.5 | 3 |
| bwd.recompute:block4.ln1 | 0.119 | 0.147 | 0.0 | 3 |
| bwd.recompute:block4.attn.qkv | 0.256 | 0.289 | 0.0 | 3 |
| bwd.recompute:block4.attn.sdpa | 0.181 | 0.215 | 0.0 | 3 |
| bwd.recompute:block4.attn.proj | 0.154 | 0.183 | 0.0 | 3 |
| bwd.recompute:block4.ln2 | 0.091 | 0.106 | 0.0 | 3 |
| bwd.recompute:block4.moe.router | 0.308 | 0.373 | 0.1 | 3 |
| bwd.recompute:block4.moe.dispatch | 6.026 | 6.338 | 1.1 | 3 |
| bwd.recompute:block4.moe.dispatch.expert0 | 0.703 | 0.741 | 0.1 | 3 |
| bwd.recompute:block4.moe.dispatch.expert1 | 0.700 | 0.747 | 0.1 | 3 |
| bwd.recompute:block4.moe.dispatch.expert2 | 0.700 | 0.746 | 0.1 | 3 |
| bwd.recompute:block4.moe.dispatch.expert3 | 0.700 | 0.739 | 0.1 | 3 |
| bwd.recompute:block4.moe.dispatch.expert4 | 0.705 | 0.740 | 0.1 | 3 |
| bwd.recompute:block4.moe.dispatch.expert5 | 0.699 | 0.743 | 0.1 | 3 |
| bwd.recompute:block4.moe.dispatch.expert6 | 0.697 | 0.740 | 0.1 | 3 |
| bwd.recompute:block4.moe.dispatch.expert7 | 0.695 | 0.731 | 0.1 | 3 |
| bwd.recompute:block4.moe.shared | 0.358 | 0.379 | 0.1 | 3 |
| bwd:block4.grad | 11.487 | 12.407 | 2.1 | 3 |
| bwd:block3 | 24.026 | 26.720 | 4.4 | 2 |
| bwd.invert:block3 | 7.666 | 8.364 | 1.4 | 3 |
| bwd.invert:block3.ln1 | 0.125 | 0.156 | 0.0 | 3 |
| bwd.invert:block3.attn.qkv | 0.254 | 0.300 | 0.0 | 3 |
| bwd.invert:block3.attn.sdpa | 0.153 | 0.176 | 0.0 | 3 |
| bwd.invert:block3.attn.proj | 0.135 | 0.173 | 0.0 | 3 |
| bwd.invert:block3.ln2 | 0.081 | 0.100 | 0.0 | 3 |
| bwd.invert:block3.moe.router | 0.302 | 0.357 | 0.1 | 3 |
| bwd.invert:block3.moe.dispatch | 5.729 | 6.155 | 1.0 | 3 |
| bwd.invert:block3.moe.dispatch.expert0 | 0.714 | 0.853 | 0.1 | 3 |
| bwd.invert:block3.moe.dispatch.expert1 | 0.668 | 0.718 | 0.1 | 3 |
| bwd.invert:block3.moe.dispatch.expert2 | 0.657 | 0.696 | 0.1 | 3 |
| bwd.invert:block3.moe.dispatch.expert3 | 0.654 | 0.691 | 0.1 | 3 |
| bwd.invert:block3.moe.dispatch.expert4 | 0.650 | 0.693 | 0.1 | 3 |
| bwd.invert:block3.moe.dispatch.expert5 | 0.657 | 0.696 | 0.1 | 3 |
| bwd.invert:block3.moe.dispatch.expert6 | 0.650 | 0.684 | 0.1 | 3 |
| bwd.invert:block3.moe.dispatch.expert7 | 0.652 | 0.686 | 0.1 | 3 |
| bwd.invert:block3.moe.shared | 0.354 | 0.373 | 0.1 | 3 |
| bwd.recompute:block3 | 8.079 | 8.653 | 1.5 | 3 |
| bwd.recompute:block3.ln1 | 0.119 | 0.148 | 0.0 | 3 |
| bwd.recompute:block3.attn.qkv | 0.255 | 0.292 | 0.0 | 3 |
| bwd.recompute:block3.attn.sdpa | 0.186 | 0.229 | 0.0 | 3 |
| bwd.recompute:block3.attn.proj | 0.152 | 0.178 | 0.0 | 3 |
| bwd.recompute:block3.ln2 | 0.091 | 0.105 | 0.0 | 3 |
| bwd.recompute:block3.moe.router | 0.310 | 0.367 | 0.1 | 3 |
| bwd.recompute:block3.moe.dispatch | 6.036 | 6.301 | 1.1 | 3 |
| bwd.recompute:block3.moe.dispatch.expert0 | 0.697 | 0.752 | 0.1 | 3 |
| bwd.recompute:block3.moe.dispatch.expert1 | 0.709 | 0.740 | 0.1 | 3 |
| bwd.recompute:block3.moe.dispatch.expert2 | 0.705 | 0.746 | 0.1 | 3 |
| bwd.recompute:block3.moe.dispatch.expert3 | 0.707 | 0.770 | 0.1 | 3 |
| bwd.recompute:block3.moe.dispatch.expert4 | 0.698 | 0.736 | 0.1 | 3 |
| bwd.recompute:block3.moe.dispatch.expert5 | 0.702 | 0.749 | 0.1 | 3 |
| bwd.recompute:block3.moe.dispatch.expert6 | 0.694 | 0.739 | 0.1 | 3 |
| bwd.recompute:block3.moe.dispatch.expert7 | 0.699 | 0.740 | 0.1 | 3 |
| bwd.recompute:block3.moe.shared | 0.356 | 0.382 | 0.1 | 3 |
| bwd:block3.grad | 11.403 | 12.333 | 2.1 | 3 |
| bwd:block2 | 23.973 | 26.510 | 4.4 | 2 |
| bwd.invert:block2 | 7.682 | 8.349 | 1.4 | 3 |
| bwd.invert:block2.ln1 | 0.127 | 0.153 | 0.0 | 3 |
| bwd.invert:block2.attn.qkv | 0.259 | 0.311 | 0.0 | 3 |
| bwd.invert:block2.attn.sdpa | 0.154 | 0.176 | 0.0 | 3 |
| bwd.invert:block2.attn.proj | 0.137 | 0.165 | 0.0 | 3 |
| bwd.invert:block2.ln2 | 0.080 | 0.097 | 0.0 | 3 |
| bwd.invert:block2.moe.router | 0.300 | 0.355 | 0.1 | 3 |
| bwd.invert:block2.moe.dispatch | 5.740 | 6.124 | 1.0 | 3 |
| bwd.invert:block2.moe.dispatch.expert0 | 0.729 | 0.859 | 0.1 | 3 |
| bwd.invert:block2.moe.dispatch.expert1 | 0.663 | 0.720 | 0.1 | 3 |
| bwd.invert:block2.moe.dispatch.expert2 | 0.661 | 0.708 | 0.1 | 3 |
| bwd.invert:block2.moe.dispatch.expert3 | 0.656 | 0.699 | 0.1 | 3 |
| bwd.invert:block2.moe.dispatch.expert4 | 0.655 | 0.697 | 0.1 | 3 |
| bwd.invert:block2.moe.dispatch.expert5 | 0.658 | 0.699 | 0.1 | 3 |
| bwd.invert:block2.moe.dispatch.expert6 | 0.661 | 0.693 | 0.1 | 3 |
| bwd.invert:block2.moe.dispatch.expert7 | 0.656 | 0.694 | 0.1 | 3 |
| bwd.invert:block2.moe.shared | 0.349 | 0.374 | 0.1 | 3 |
| bwd.recompute:block2 | 8.056 | 8.722 | 1.5 | 3 |
| bwd.recompute:block2.ln1 | 0.120 | 0.149 | 0.0 | 3 |
| bwd.recompute:block2.attn.qkv | 0.250 | 0.280 | 0.0 | 3 |
| bwd.recompute:block2.attn.sdpa | 0.193 | 0.228 | 0.0 | 3 |
| bwd.recompute:block2.attn.proj | 0.152 | 0.175 | 0.0 | 3 |
| bwd.recompute:block2.ln2 | 0.089 | 0.103 | 0.0 | 3 |
| bwd.recompute:block2.moe.router | 0.313 | 0.362 | 0.1 | 3 |
| bwd.recompute:block2.moe.dispatch | 6.030 | 6.382 | 1.1 | 3 |
| bwd.recompute:block2.moe.dispatch.expert0 | 0.701 | 0.747 | 0.1 | 3 |
| bwd.recompute:block2.moe.dispatch.expert1 | 0.706 | 0.741 | 0.1 | 3 |
| bwd.recompute:block2.moe.dispatch.expert2 | 0.708 | 0.752 | 0.1 | 3 |
| bwd.recompute:block2.moe.dispatch.expert3 | 0.712 | 0.756 | 0.1 | 3 |
| bwd.recompute:block2.moe.dispatch.expert4 | 0.697 | 0.746 | 0.1 | 3 |
| bwd.recompute:block2.moe.dispatch.expert5 | 0.695 | 0.735 | 0.1 | 3 |
| bwd.recompute:block2.moe.dispatch.expert6 | 0.693 | 0.752 | 0.1 | 3 |
| bwd.recompute:block2.moe.dispatch.expert7 | 0.685 | 0.733 | 0.1 | 3 |
| bwd.recompute:block2.moe.shared | 0.355 | 0.379 | 0.1 | 3 |
| bwd:block2.grad | 11.460 | 12.285 | 2.1 | 3 |
| bwd:block1 | 23.879 | 26.564 | 4.4 | 2 |
| bwd.invert:block1 | 7.718 | 8.267 | 1.4 | 3 |
| bwd.invert:block1.ln1 | 0.129 | 0.147 | 0.0 | 3 |
| bwd.invert:block1.attn.qkv | 0.254 | 0.303 | 0.0 | 3 |
| bwd.invert:block1.attn.sdpa | 0.153 | 0.171 | 0.0 | 3 |
| bwd.invert:block1.attn.proj | 0.133 | 0.160 | 0.0 | 3 |
| bwd.invert:block1.ln2 | 0.082 | 0.097 | 0.0 | 3 |
| bwd.invert:block1.moe.router | 0.303 | 0.354 | 0.1 | 3 |
| bwd.invert:block1.moe.dispatch | 5.751 | 6.076 | 1.0 | 3 |
| bwd.invert:block1.moe.dispatch.expert0 | 0.735 | 0.841 | 0.1 | 3 |
| bwd.invert:block1.moe.dispatch.expert1 | 0.674 | 0.714 | 0.1 | 3 |
| bwd.invert:block1.moe.dispatch.expert2 | 0.660 | 0.696 | 0.1 | 3 |
| bwd.invert:block1.moe.dispatch.expert3 | 0.655 | 0.698 | 0.1 | 3 |
| bwd.invert:block1.moe.dispatch.expert4 | 0.659 | 0.698 | 0.1 | 3 |
| bwd.invert:block1.moe.dispatch.expert5 | 0.653 | 0.699 | 0.1 | 3 |
| bwd.invert:block1.moe.dispatch.expert6 | 0.650 | 0.698 | 0.1 | 3 |
| bwd.invert:block1.moe.dispatch.expert7 | 0.653 | 0.700 | 0.1 | 3 |
| bwd.invert:block1.moe.shared | 0.351 | 0.372 | 0.1 | 3 |
| bwd.recompute:block1 | 8.130 | 8.670 | 1.5 | 3 |
| bwd.recompute:block1.ln1 | 0.122 | 0.144 | 0.0 | 3 |
| bwd.recompute:block1.attn.qkv | 0.255 | 0.283 | 0.0 | 3 |
| bwd.recompute:block1.attn.sdpa | 0.195 | 0.229 | 0.0 | 3 |
| bwd.recompute:block1.attn.proj | 0.152 | 0.181 | 0.0 | 3 |
| bwd.recompute:block1.ln2 | 0.090 | 0.104 | 0.0 | 3 |
| bwd.recompute:block1.moe.router | 0.310 | 0.371 | 0.1 | 3 |
| bwd.recompute:block1.moe.dispatch | 6.038 | 6.399 | 1.1 | 3 |
| bwd.recompute:block1.moe.dispatch.expert0 | 0.700 | 0.749 | 0.1 | 3 |
| bwd.recompute:block1.moe.dispatch.expert1 | 0.712 | 0.752 | 0.1 | 3 |
| bwd.recompute:block1.moe.dispatch.expert2 | 0.706 | 0.751 | 0.1 | 3 |
| bwd.recompute:block1.moe.dispatch.expert3 | 0.712 | 0.767 | 0.1 | 3 |
| bwd.recompute:block1.moe.dispatch.expert4 | 0.701 | 0.736 | 0.1 | 3 |
| bwd.recompute:block1.moe.dispatch.expert5 | 0.705 | 0.750 | 0.1 | 3 |
| bwd.recompute:block1.moe.dispatch.expert6 | 0.693 | 0.727 | 0.1 | 3 |
| bwd.recompute:block1.moe.dispatch.expert7 | 0.688 | 0.745 | 0.1 | 3 |
| bwd.recompute:block1.moe.shared | 0.354 | 0.374 | 0.1 | 3 |
| bwd:block1.grad | 11.454 | 12.211 | 2.1 | 3 |
| bwd:block0 | 23.657 | 27.270 | 4.3 | 2 |
| bwd.invert:block0 | 7.757 | 8.359 | 1.4 | 3 |
| bwd.invert:block0.ln1 | 0.131 | 0.149 | 0.0 | 3 |
| bwd.invert:block0.attn.qkv | 0.260 | 0.303 | 0.0 | 3 |
| bwd.invert:block0.attn.sdpa | 0.154 | 0.171 | 0.0 | 3 |
| bwd.invert:block0.attn.proj | 0.133 | 0.160 | 0.0 | 3 |
| bwd.invert:block0.ln2 | 0.082 | 0.100 | 0.0 | 3 |
| bwd.invert:block0.moe.router | 0.304 | 0.351 | 0.1 | 3 |
| bwd.invert:block0.moe.dispatch | 5.808 | 6.130 | 1.1 | 3 |
| bwd.invert:block0.moe.dispatch.expert0 | 0.734 | 0.842 | 0.1 | 3 |
| bwd.invert:block0.moe.dispatch.expert1 | 0.677 | 0.711 | 0.1 | 3 |
| bwd.invert:block0.moe.dispatch.expert2 | 0.662 | 0.702 | 0.1 | 3 |
| bwd.invert:block0.moe.dispatch.expert3 | 0.654 | 0.695 | 0.1 | 3 |
| bwd.invert:block0.moe.dispatch.expert4 | 0.668 | 0.711 | 0.1 | 3 |
| bwd.invert:block0.moe.dispatch.expert5 | 0.666 | 0.694 | 0.1 | 3 |
| bwd.invert:block0.moe.dispatch.expert6 | 0.652 | 0.696 | 0.1 | 3 |
| bwd.invert:block0.moe.dispatch.expert7 | 0.653 | 0.692 | 0.1 | 3 |
| bwd.invert:block0.moe.shared | 0.351 | 0.376 | 0.1 | 3 |
| bwd.recompute:block0 | 8.070 | 8.663 | 1.5 | 3 |
| bwd.recompute:block0.ln1 | 0.122 | 0.141 | 0.0 | 3 |
| bwd.recompute:block0.attn.qkv | 0.252 | 0.283 | 0.0 | 3 |
| bwd.recompute:block0.attn.sdpa | 0.199 | 0.235 | 0.0 | 3 |
| bwd.recompute:block0.attn.proj | 0.156 | 0.185 | 0.0 | 3 |
| bwd.recompute:block0.ln2 | 0.090 | 0.104 | 0.0 | 3 |
| bwd.recompute:block0.moe.router | 0.308 | 0.363 | 0.1 | 3 |
| bwd.recompute:block0.moe.dispatch | 5.972 | 6.361 | 1.1 | 3 |
| bwd.recompute:block0.moe.dispatch.expert0 | 0.694 | 0.751 | 0.1 | 3 |
| bwd.recompute:block0.moe.dispatch.expert1 | 0.706 | 0.753 | 0.1 | 3 |
| bwd.recompute:block0.moe.dispatch.expert2 | 0.705 | 0.740 | 0.1 | 3 |
| bwd.recompute:block0.moe.dispatch.expert3 | 0.700 | 0.748 | 0.1 | 3 |
| bwd.recompute:block0.moe.dispatch.expert4 | 0.702 | 0.760 | 0.1 | 3 |
| bwd.recompute:block0.moe.dispatch.expert5 | 0.689 | 0.736 | 0.1 | 3 |
| bwd.recompute:block0.moe.dispatch.expert6 | 0.688 | 0.736 | 0.1 | 3 |
| bwd.recompute:block0.moe.dispatch.expert7 | 0.680 | 0.724 | 0.1 | 3 |
| bwd.recompute:block0.moe.shared | 0.355 | 0.377 | 0.1 | 3 |
| bwd:block0.grad | 11.386 | 12.115 | 2.1 | 3 |
| bwd:embed | 0.520 | 0.554 | 0.1 | 2 |
| opt | 183.781 | 195.604 | 33.6 | 1 |
| opt:opt.clip | 5.514 | 6.160 | 1.0 | 2 |
| opt:opt.muon | 172.963 | 184.252 | 31.6 | 2 |
| opt:opt.muon.ns | 164.863 | 172.691 | 30.1 | 3 |
| opt:opt.adamw | 2.626 | 2.817 | 0.5 | 2 |
| opt:opt.moe_bias | 1.060 | 1.109 | 0.2 | 3 |
| opt:opt.zero_grad | 1.598 | 1.702 | 0.3 | 3 |

## Time by part type (sum over layers)

| part type | median ms sum | % of step |
| :--- | ---: | ---: |
| bwd | 269.158 | 49.1 |
| bwd:stack | 220.420 | 40.2 |
| bwd:block* | 217.875 | 39.8 |
| opt | 183.781 | 33.6 |
| opt:opt.muon | 172.963 | 31.6 |
| opt:opt.muon.ns | 164.863 | 30.1 |
| fwd | 109.529 | 20.0 |
| bwd:block*.grad | 103.684 | 18.9 |
| bwd.recompute:block* | 73.228 | 13.4 |
| bwd.invert:block* | 69.549 | 12.7 |
| fwd:stack | 63.879 | 11.7 |
| fwd:block* | 62.811 | 11.5 |
| fwd:block*.moe.dispatch | 58.488 | 10.7 |
| bwd.recompute:block*.moe.dispatch | 54.359 | 9.9 |
| bwd.invert:block*.moe.dispatch | 52.543 | 9.6 |
| bwd:head+loss | 48.176 | 8.8 |
| fwd:head+loss | 40.963 | 7.5 |
| bwd.invert:block*.moe.dispatch.expert0 | 7.164 | 1.3 |
| fwd:block*.moe.dispatch.expert1 | 6.983 | 1.3 |
| fwd:block*.moe.dispatch.expert2 | 6.878 | 1.3 |
| fwd:block*.moe.dispatch.expert3 | 6.874 | 1.3 |
| fwd:block*.moe.dispatch.expert4 | 6.860 | 1.3 |
| fwd:block*.moe.dispatch.expert5 | 6.853 | 1.3 |
| fwd:block*.moe.dispatch.expert7 | 6.772 | 1.2 |
| fwd:block*.moe.dispatch.expert6 | 6.772 | 1.2 |
| fwd:block*.moe.dispatch.expert0 | 6.679 | 1.2 |
| bwd.recompute:block*.moe.dispatch.expert1 | 6.376 | 1.2 |
| bwd.recompute:block*.moe.dispatch.expert0 | 6.343 | 1.2 |
| bwd.recompute:block*.moe.dispatch.expert3 | 6.331 | 1.2 |
| bwd.recompute:block*.moe.dispatch.expert2 | 6.328 | 1.2 |
| bwd.recompute:block*.moe.dispatch.expert4 | 6.318 | 1.2 |
| bwd.recompute:block*.moe.dispatch.expert5 | 6.308 | 1.2 |
| bwd.recompute:block*.moe.dispatch.expert6 | 6.276 | 1.1 |
| bwd.recompute:block*.moe.dispatch.expert7 | 6.259 | 1.1 |
| bwd.invert:block*.moe.dispatch.expert1 | 6.159 | 1.1 |
| bwd.invert:block*.moe.dispatch.expert2 | 5.977 | 1.1 |
| bwd.invert:block*.moe.dispatch.expert3 | 5.929 | 1.1 |
| bwd.invert:block*.moe.dispatch.expert4 | 5.926 | 1.1 |
| bwd.invert:block*.moe.dispatch.expert5 | 5.923 | 1.1 |
| bwd.invert:block*.moe.dispatch.expert7 | 5.902 | 1.1 |
| bwd.invert:block*.moe.dispatch.expert6 | 5.881 | 1.1 |
| opt:opt.clip | 5.514 | 1.0 |
| fwd:embed | 4.482 | 0.8 |
| fwd:embed.ke | 4.433 | 0.8 |
| fwd:block*.moe.shared | 3.282 | 0.6 |
| fwd:block*.moe.router | 3.274 | 0.6 |
| bwd.recompute:block*.moe.shared | 3.213 | 0.6 |
| bwd.invert:block*.moe.shared | 3.162 | 0.6 |
| bwd.recompute:block*.moe.router | 2.869 | 0.5 |
| opt:opt.adamw | 2.626 | 0.5 |
| bwd.invert:block*.moe.router | 2.489 | 0.5 |
| bwd.recompute:block*.attn.qkv | 2.330 | 0.4 |
| bwd.invert:block*.attn.qkv | 2.118 | 0.4 |
| fwd:block*.attn.qkv | 1.864 | 0.3 |
| bwd.recompute:block*.attn.sdpa | 1.699 | 0.3 |
| opt:opt.zero_grad | 1.598 | 0.3 |
| bwd.recompute:block*.attn.proj | 1.398 | 0.3 |
| bwd.invert:block*.attn.sdpa | 1.316 | 0.2 |
| fwd:block*.attn.sdpa | 1.251 | 0.2 |
| data | 1.125 | 0.2 |
| bwd.invert:block*.attn.proj | 1.120 | 0.2 |
| bwd.recompute:block*.ln1 | 1.113 | 0.2 |
| bwd.invert:block*.ln1 | 1.073 | 0.2 |
| opt:opt.moe_bias | 1.060 | 0.2 |
| fwd:block*.attn.proj | 1.054 | 0.2 |
| fwd:block*.ln1 | 0.891 | 0.2 |
| bwd.recompute:block*.ln2 | 0.819 | 0.1 |
| bwd.invert:block*.ln2 | 0.708 | 0.1 |
| fwd:block*.ln2 | 0.686 | 0.1 |
| bwd:embed | 0.520 | 0.1 |

## Five slowest leaf parts

1. `opt:opt.muon.ns` — 164.863 ms (30.1% of step)
2. `bwd:block8.grad` — 11.976 ms (2.2% of step)
3. `bwd:block7.grad` — 11.570 ms (2.1% of step)
4. `bwd:block6.grad` — 11.557 ms (2.1% of step)
5. `bwd:block4.grad` — 11.487 ms (2.1% of step)
