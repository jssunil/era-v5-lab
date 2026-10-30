# Bench report — g1_lab2_normal-run2

**GPU:** NVIDIA A100-SXM4-40GB  |  **dtype:** bf16  |  **B x T:** 32 x 512  |  **torch:** 2.15.0+cu132
**commit:** `14854097c57056f326efd0c7a40cc036a73bbc94`  |  **tag:** g1_lab2_normal-run2

## Step (clean)

- median: 560.968 ms
- p10..p90: 538.620 .. 613.473 ms
- tokens/s: 29,207
- MFU: 3.0%  |  HFU: 3.8%

## Diagnostics

### CUDA timing-event allocations

- [OK] clean: events_created_during_steps=0
- [OK] layer: events_created_during_steps=0
- [OK] layer.inner_pass: events_created_during_steps=0

### Benchmark warnings

- [warn] 25 gated part(s) have p10..p90 spread > 10%, so may miss the 5% check: data, fwd:stack, fwd:block0, fwd:block1, fwd:block2, fwd:block3 (+19 more)

## Regions

| part | median ms | p90 | % of step | level |
| :--- | ---: | ---: | ---: | ---: |
| data | 1.118 | 1.223 | 0.2 | 1 |
| fwd | 108.887 | 113.694 | 19.4 | 1 |
| fwd:embed | 4.481 | 4.530 | 0.8 | 2 |
| fwd:embed.ke | 4.439 | 4.487 | 0.8 | 3 |
| fwd:stack | 63.266 | 67.970 | 11.3 | 1 |
| fwd:block0 | 6.598 | 7.107 | 1.2 | 2 |
| fwd:block0.ln1 | 0.052 | 0.053 | 0.0 | 3 |
| fwd:block0.attn.qkv | 0.050 | 0.050 | 0.0 | 3 |
| fwd:block0.attn.sdpa | 0.082 | 0.084 | 0.0 | 3 |
| fwd:block0.attn.proj | 0.038 | 0.039 | 0.0 | 3 |
| fwd:block0.ln2 | 0.053 | 0.054 | 0.0 | 3 |
| fwd:block0.moe.router | 0.146 | 0.152 | 0.0 | 3 |
| fwd:block0.moe.dispatch | 6.514 | 7.026 | 1.2 | 3 |
| fwd:block0.moe.dispatch.expert0 | 0.805 | 0.912 | 0.1 | 3 |
| fwd:block0.moe.dispatch.expert1 | 0.770 | 0.888 | 0.1 | 3 |
| fwd:block0.moe.dispatch.expert2 | 0.813 | 0.877 | 0.1 | 3 |
| fwd:block0.moe.dispatch.expert3 | 0.766 | 0.875 | 0.1 | 3 |
| fwd:block0.moe.dispatch.expert4 | 0.790 | 0.875 | 0.1 | 3 |
| fwd:block0.moe.dispatch.expert5 | 0.792 | 0.892 | 0.1 | 3 |
| fwd:block0.moe.dispatch.expert6 | 0.762 | 0.853 | 0.1 | 3 |
| fwd:block0.moe.dispatch.expert7 | 0.734 | 0.849 | 0.1 | 3 |
| fwd:block0.moe.shared | 0.357 | 0.399 | 0.1 | 3 |
| fwd:block1 | 7.153 | 7.638 | 1.3 | 2 |
| fwd:block1.ln1 | 0.108 | 0.126 | 0.0 | 3 |
| fwd:block1.attn.qkv | 0.233 | 0.263 | 0.0 | 3 |
| fwd:block1.attn.sdpa | 0.155 | 0.172 | 0.0 | 3 |
| fwd:block1.attn.proj | 0.129 | 0.152 | 0.0 | 3 |
| fwd:block1.ln2 | 0.076 | 0.089 | 0.0 | 3 |
| fwd:block1.moe.router | 0.414 | 0.481 | 0.1 | 3 |
| fwd:block1.moe.dispatch | 6.498 | 6.942 | 1.2 | 3 |
| fwd:block1.moe.dispatch.expert0 | 0.701 | 0.805 | 0.1 | 3 |
| fwd:block1.moe.dispatch.expert1 | 0.800 | 0.905 | 0.1 | 3 |
| fwd:block1.moe.dispatch.expert2 | 0.782 | 0.871 | 0.1 | 3 |
| fwd:block1.moe.dispatch.expert3 | 0.755 | 0.857 | 0.1 | 3 |
| fwd:block1.moe.dispatch.expert4 | 0.802 | 0.881 | 0.1 | 3 |
| fwd:block1.moe.dispatch.expert5 | 0.758 | 0.853 | 0.1 | 3 |
| fwd:block1.moe.dispatch.expert6 | 0.722 | 0.830 | 0.1 | 3 |
| fwd:block1.moe.dispatch.expert7 | 0.740 | 0.809 | 0.1 | 3 |
| fwd:block1.moe.shared | 0.365 | 0.396 | 0.1 | 3 |
| fwd:block2 | 6.947 | 7.509 | 1.2 | 2 |
| fwd:block2.ln1 | 0.101 | 0.122 | 0.0 | 3 |
| fwd:block2.attn.qkv | 0.227 | 0.256 | 0.0 | 3 |
| fwd:block2.attn.sdpa | 0.148 | 0.169 | 0.0 | 3 |
| fwd:block2.attn.proj | 0.127 | 0.152 | 0.0 | 3 |
| fwd:block2.ln2 | 0.078 | 0.093 | 0.0 | 3 |
| fwd:block2.moe.router | 0.406 | 0.481 | 0.1 | 3 |
| fwd:block2.moe.dispatch | 6.423 | 6.905 | 1.1 | 3 |
| fwd:block2.moe.dispatch.expert0 | 0.741 | 0.805 | 0.1 | 3 |
| fwd:block2.moe.dispatch.expert1 | 0.755 | 0.859 | 0.1 | 3 |
| fwd:block2.moe.dispatch.expert2 | 0.765 | 0.863 | 0.1 | 3 |
| fwd:block2.moe.dispatch.expert3 | 0.795 | 0.877 | 0.1 | 3 |
| fwd:block2.moe.dispatch.expert4 | 0.758 | 0.851 | 0.1 | 3 |
| fwd:block2.moe.dispatch.expert5 | 0.726 | 0.826 | 0.1 | 3 |
| fwd:block2.moe.dispatch.expert6 | 0.736 | 0.829 | 0.1 | 3 |
| fwd:block2.moe.dispatch.expert7 | 0.738 | 0.835 | 0.1 | 3 |
| fwd:block2.moe.shared | 0.353 | 0.387 | 0.1 | 3 |
| fwd:block3 | 6.967 | 7.533 | 1.2 | 2 |
| fwd:block3.ln1 | 0.102 | 0.124 | 0.0 | 3 |
| fwd:block3.attn.qkv | 0.224 | 0.253 | 0.0 | 3 |
| fwd:block3.attn.sdpa | 0.146 | 0.166 | 0.0 | 3 |
| fwd:block3.attn.proj | 0.123 | 0.154 | 0.0 | 3 |
| fwd:block3.ln2 | 0.076 | 0.091 | 0.0 | 3 |
| fwd:block3.moe.router | 0.398 | 0.477 | 0.1 | 3 |
| fwd:block3.moe.dispatch | 6.430 | 6.843 | 1.1 | 3 |
| fwd:block3.moe.dispatch.expert0 | 0.708 | 0.787 | 0.1 | 3 |
| fwd:block3.moe.dispatch.expert1 | 0.761 | 0.862 | 0.1 | 3 |
| fwd:block3.moe.dispatch.expert2 | 0.767 | 0.855 | 0.1 | 3 |
| fwd:block3.moe.dispatch.expert3 | 0.750 | 0.841 | 0.1 | 3 |
| fwd:block3.moe.dispatch.expert4 | 0.778 | 0.856 | 0.1 | 3 |
| fwd:block3.moe.dispatch.expert5 | 0.778 | 0.863 | 0.1 | 3 |
| fwd:block3.moe.dispatch.expert6 | 0.749 | 0.839 | 0.1 | 3 |
| fwd:block3.moe.dispatch.expert7 | 0.733 | 0.796 | 0.1 | 3 |
| fwd:block3.moe.shared | 0.360 | 0.389 | 0.1 | 3 |
| fwd:block4 | 6.994 | 7.662 | 1.2 | 2 |
| fwd:block4.ln1 | 0.101 | 0.120 | 0.0 | 3 |
| fwd:block4.attn.qkv | 0.219 | 0.250 | 0.0 | 3 |
| fwd:block4.attn.sdpa | 0.142 | 0.163 | 0.0 | 3 |
| fwd:block4.attn.proj | 0.123 | 0.151 | 0.0 | 3 |
| fwd:block4.ln2 | 0.076 | 0.092 | 0.0 | 3 |
| fwd:block4.moe.router | 0.387 | 0.471 | 0.1 | 3 |
| fwd:block4.moe.dispatch | 6.524 | 6.895 | 1.2 | 3 |
| fwd:block4.moe.dispatch.expert0 | 0.735 | 0.795 | 0.1 | 3 |
| fwd:block4.moe.dispatch.expert1 | 0.771 | 0.864 | 0.1 | 3 |
| fwd:block4.moe.dispatch.expert2 | 0.765 | 0.862 | 0.1 | 3 |
| fwd:block4.moe.dispatch.expert3 | 0.760 | 0.855 | 0.1 | 3 |
| fwd:block4.moe.dispatch.expert4 | 0.770 | 0.841 | 0.1 | 3 |
| fwd:block4.moe.dispatch.expert5 | 0.752 | 0.841 | 0.1 | 3 |
| fwd:block4.moe.dispatch.expert6 | 0.762 | 0.830 | 0.1 | 3 |
| fwd:block4.moe.dispatch.expert7 | 0.745 | 0.842 | 0.1 | 3 |
| fwd:block4.moe.shared | 0.356 | 0.386 | 0.1 | 3 |
| fwd:block5 | 6.879 | 7.540 | 1.2 | 2 |
| fwd:block5.ln1 | 0.101 | 0.123 | 0.0 | 3 |
| fwd:block5.attn.qkv | 0.221 | 0.250 | 0.0 | 3 |
| fwd:block5.attn.sdpa | 0.144 | 0.162 | 0.0 | 3 |
| fwd:block5.attn.proj | 0.122 | 0.151 | 0.0 | 3 |
| fwd:block5.ln2 | 0.077 | 0.092 | 0.0 | 3 |
| fwd:block5.moe.router | 0.385 | 0.467 | 0.1 | 3 |
| fwd:block5.moe.dispatch | 6.356 | 6.804 | 1.1 | 3 |
| fwd:block5.moe.dispatch.expert0 | 0.738 | 0.791 | 0.1 | 3 |
| fwd:block5.moe.dispatch.expert1 | 0.775 | 0.854 | 0.1 | 3 |
| fwd:block5.moe.dispatch.expert2 | 0.746 | 0.830 | 0.1 | 3 |
| fwd:block5.moe.dispatch.expert3 | 0.734 | 0.839 | 0.1 | 3 |
| fwd:block5.moe.dispatch.expert4 | 0.754 | 0.838 | 0.1 | 3 |
| fwd:block5.moe.dispatch.expert5 | 0.744 | 0.837 | 0.1 | 3 |
| fwd:block5.moe.dispatch.expert6 | 0.739 | 0.819 | 0.1 | 3 |
| fwd:block5.moe.dispatch.expert7 | 0.746 | 0.835 | 0.1 | 3 |
| fwd:block5.moe.shared | 0.364 | 0.399 | 0.1 | 3 |
| fwd:block6 | 6.983 | 7.634 | 1.2 | 2 |
| fwd:block6.ln1 | 0.101 | 0.125 | 0.0 | 3 |
| fwd:block6.attn.qkv | 0.220 | 0.258 | 0.0 | 3 |
| fwd:block6.attn.sdpa | 0.144 | 0.166 | 0.0 | 3 |
| fwd:block6.attn.proj | 0.125 | 0.153 | 0.0 | 3 |
| fwd:block6.ln2 | 0.075 | 0.092 | 0.0 | 3 |
| fwd:block6.moe.router | 0.380 | 0.489 | 0.1 | 3 |
| fwd:block6.moe.dispatch | 6.491 | 6.954 | 1.2 | 3 |
| fwd:block6.moe.dispatch.expert0 | 0.734 | 0.806 | 0.1 | 3 |
| fwd:block6.moe.dispatch.expert1 | 0.788 | 0.856 | 0.1 | 3 |
| fwd:block6.moe.dispatch.expert2 | 0.770 | 0.854 | 0.1 | 3 |
| fwd:block6.moe.dispatch.expert3 | 0.745 | 0.851 | 0.1 | 3 |
| fwd:block6.moe.dispatch.expert4 | 0.742 | 0.833 | 0.1 | 3 |
| fwd:block6.moe.dispatch.expert5 | 0.768 | 0.844 | 0.1 | 3 |
| fwd:block6.moe.dispatch.expert6 | 0.764 | 0.845 | 0.1 | 3 |
| fwd:block6.moe.dispatch.expert7 | 0.761 | 0.847 | 0.1 | 3 |
| fwd:block6.moe.shared | 0.364 | 0.398 | 0.1 | 3 |
| fwd:block7 | 6.911 | 7.430 | 1.2 | 2 |
| fwd:block7.ln1 | 0.101 | 0.123 | 0.0 | 3 |
| fwd:block7.attn.qkv | 0.219 | 0.249 | 0.0 | 3 |
| fwd:block7.attn.sdpa | 0.141 | 0.165 | 0.0 | 3 |
| fwd:block7.attn.proj | 0.119 | 0.148 | 0.0 | 3 |
| fwd:block7.ln2 | 0.075 | 0.090 | 0.0 | 3 |
| fwd:block7.moe.router | 0.389 | 0.473 | 0.1 | 3 |
| fwd:block7.moe.dispatch | 6.398 | 6.777 | 1.1 | 3 |
| fwd:block7.moe.dispatch.expert0 | 0.697 | 0.777 | 0.1 | 3 |
| fwd:block7.moe.dispatch.expert1 | 0.776 | 0.855 | 0.1 | 3 |
| fwd:block7.moe.dispatch.expert2 | 0.745 | 0.846 | 0.1 | 3 |
| fwd:block7.moe.dispatch.expert3 | 0.755 | 0.846 | 0.1 | 3 |
| fwd:block7.moe.dispatch.expert4 | 0.758 | 0.849 | 0.1 | 3 |
| fwd:block7.moe.dispatch.expert5 | 0.743 | 0.823 | 0.1 | 3 |
| fwd:block7.moe.dispatch.expert6 | 0.724 | 0.820 | 0.1 | 3 |
| fwd:block7.moe.dispatch.expert7 | 0.742 | 0.827 | 0.1 | 3 |
| fwd:block7.moe.shared | 0.363 | 0.394 | 0.1 | 3 |
| fwd:block8 | 6.864 | 7.490 | 1.2 | 2 |
| fwd:block8.ln1 | 0.101 | 0.121 | 0.0 | 3 |
| fwd:block8.attn.qkv | 0.217 | 0.248 | 0.0 | 3 |
| fwd:block8.attn.sdpa | 0.143 | 0.162 | 0.0 | 3 |
| fwd:block8.attn.proj | 0.120 | 0.150 | 0.0 | 3 |
| fwd:block8.ln2 | 0.075 | 0.090 | 0.0 | 3 |
| fwd:block8.moe.router | 0.383 | 0.479 | 0.1 | 3 |
| fwd:block8.moe.dispatch | 6.410 | 6.778 | 1.1 | 3 |
| fwd:block8.moe.dispatch.expert0 | 0.739 | 0.782 | 0.1 | 3 |
| fwd:block8.moe.dispatch.expert1 | 0.763 | 0.851 | 0.1 | 3 |
| fwd:block8.moe.dispatch.expert2 | 0.759 | 0.840 | 0.1 | 3 |
| fwd:block8.moe.dispatch.expert3 | 0.734 | 0.839 | 0.1 | 3 |
| fwd:block8.moe.dispatch.expert4 | 0.727 | 0.815 | 0.1 | 3 |
| fwd:block8.moe.dispatch.expert5 | 0.739 | 0.836 | 0.1 | 3 |
| fwd:block8.moe.dispatch.expert6 | 0.749 | 0.857 | 0.1 | 3 |
| fwd:block8.moe.dispatch.expert7 | 0.754 | 0.854 | 0.1 | 3 |
| fwd:block8.moe.shared | 0.363 | 0.398 | 0.1 | 3 |
| fwd:head+loss | 40.966 | 41.006 | 7.3 | 2 |
| bwd | 269.007 | 287.451 | 48.0 | 1 |
| bwd:head+loss | 48.172 | 48.192 | 8.6 | 2 |
| bwd:stack | 220.305 | 238.751 | 39.3 | 1 |
| bwd:block8 | 25.267 | 28.189 | 4.5 | 2 |
| bwd.invert:block8 | 7.636 | 8.064 | 1.4 | 3 |
| bwd.invert:block8.ln1 | 0.054 | 0.054 | 0.0 | 3 |
| bwd.invert:block8.attn.qkv | 0.050 | 0.051 | 0.0 | 3 |
| bwd.invert:block8.attn.sdpa | 0.082 | 0.084 | 0.0 | 3 |
| bwd.invert:block8.attn.proj | 0.038 | 0.038 | 0.0 | 3 |
| bwd.invert:block8.ln2 | 0.053 | 0.055 | 0.0 | 3 |
| bwd.invert:block8.moe.router | 0.066 | 0.067 | 0.0 | 3 |
| bwd.invert:block8.moe.dispatch | 6.463 | 6.842 | 1.2 | 3 |
| bwd.invert:block8.moe.dispatch.expert0 | 1.308 | 1.496 | 0.2 | 3 |
| bwd.invert:block8.moe.dispatch.expert1 | 0.792 | 0.848 | 0.1 | 3 |
| bwd.invert:block8.moe.dispatch.expert2 | 0.695 | 0.734 | 0.1 | 3 |
| bwd.invert:block8.moe.dispatch.expert3 | 0.682 | 0.718 | 0.1 | 3 |
| bwd.invert:block8.moe.dispatch.expert4 | 0.677 | 0.724 | 0.1 | 3 |
| bwd.invert:block8.moe.dispatch.expert5 | 0.674 | 0.714 | 0.1 | 3 |
| bwd.invert:block8.moe.dispatch.expert6 | 0.672 | 0.709 | 0.1 | 3 |
| bwd.invert:block8.moe.dispatch.expert7 | 0.679 | 0.720 | 0.1 | 3 |
| bwd.invert:block8.moe.shared | 0.360 | 0.383 | 0.1 | 3 |
| bwd.recompute:block8 | 8.340 | 8.787 | 1.5 | 3 |
| bwd.recompute:block8.ln1 | 0.147 | 0.160 | 0.0 | 3 |
| bwd.recompute:block8.attn.qkv | 0.276 | 0.310 | 0.0 | 3 |
| bwd.recompute:block8.attn.sdpa | 0.232 | 0.295 | 0.0 | 3 |
| bwd.recompute:block8.attn.proj | 0.168 | 0.195 | 0.0 | 3 |
| bwd.recompute:block8.ln2 | 0.092 | 0.103 | 0.0 | 3 |
| bwd.recompute:block8.moe.router | 0.375 | 0.421 | 0.1 | 3 |
| bwd.recompute:block8.moe.dispatch | 6.181 | 6.478 | 1.1 | 3 |
| bwd.recompute:block8.moe.dispatch.expert0 | 0.729 | 0.786 | 0.1 | 3 |
| bwd.recompute:block8.moe.dispatch.expert1 | 0.724 | 0.758 | 0.1 | 3 |
| bwd.recompute:block8.moe.dispatch.expert2 | 0.720 | 0.760 | 0.1 | 3 |
| bwd.recompute:block8.moe.dispatch.expert3 | 0.720 | 0.757 | 0.1 | 3 |
| bwd.recompute:block8.moe.dispatch.expert4 | 0.716 | 0.759 | 0.1 | 3 |
| bwd.recompute:block8.moe.dispatch.expert5 | 0.715 | 0.749 | 0.1 | 3 |
| bwd.recompute:block8.moe.dispatch.expert6 | 0.711 | 0.757 | 0.1 | 3 |
| bwd.recompute:block8.moe.dispatch.expert7 | 0.714 | 0.747 | 0.1 | 3 |
| bwd.recompute:block8.moe.shared | 0.361 | 0.388 | 0.1 | 3 |
| bwd:block8.grad | 11.845 | 12.714 | 2.1 | 3 |
| bwd:block7 | 24.711 | 26.800 | 4.4 | 2 |
| bwd.invert:block7 | 7.831 | 8.349 | 1.4 | 3 |
| bwd.invert:block7.ln1 | 0.127 | 0.146 | 0.0 | 3 |
| bwd.invert:block7.attn.qkv | 0.302 | 0.361 | 0.1 | 3 |
| bwd.invert:block7.attn.sdpa | 0.158 | 0.176 | 0.0 | 3 |
| bwd.invert:block7.attn.proj | 0.135 | 0.160 | 0.0 | 3 |
| bwd.invert:block7.ln2 | 0.080 | 0.090 | 0.0 | 3 |
| bwd.invert:block7.moe.router | 0.314 | 0.355 | 0.1 | 3 |
| bwd.invert:block7.moe.dispatch | 5.779 | 6.055 | 1.0 | 3 |
| bwd.invert:block7.moe.dispatch.expert0 | 0.734 | 0.837 | 0.1 | 3 |
| bwd.invert:block7.moe.dispatch.expert1 | 0.683 | 0.720 | 0.1 | 3 |
| bwd.invert:block7.moe.dispatch.expert2 | 0.663 | 0.706 | 0.1 | 3 |
| bwd.invert:block7.moe.dispatch.expert3 | 0.659 | 0.693 | 0.1 | 3 |
| bwd.invert:block7.moe.dispatch.expert4 | 0.657 | 0.696 | 0.1 | 3 |
| bwd.invert:block7.moe.dispatch.expert5 | 0.662 | 0.692 | 0.1 | 3 |
| bwd.invert:block7.moe.dispatch.expert6 | 0.654 | 0.702 | 0.1 | 3 |
| bwd.invert:block7.moe.dispatch.expert7 | 0.654 | 0.687 | 0.1 | 3 |
| bwd.invert:block7.moe.shared | 0.351 | 0.371 | 0.1 | 3 |
| bwd.recompute:block7 | 8.090 | 8.605 | 1.4 | 3 |
| bwd.recompute:block7.ln1 | 0.117 | 0.143 | 0.0 | 3 |
| bwd.recompute:block7.attn.qkv | 0.262 | 0.292 | 0.0 | 3 |
| bwd.recompute:block7.attn.sdpa | 0.174 | 0.199 | 0.0 | 3 |
| bwd.recompute:block7.attn.proj | 0.149 | 0.169 | 0.0 | 3 |
| bwd.recompute:block7.ln2 | 0.088 | 0.104 | 0.0 | 3 |
| bwd.recompute:block7.moe.router | 0.326 | 0.380 | 0.1 | 3 |
| bwd.recompute:block7.moe.dispatch | 6.008 | 6.305 | 1.1 | 3 |
| bwd.recompute:block7.moe.dispatch.expert0 | 0.711 | 0.752 | 0.1 | 3 |
| bwd.recompute:block7.moe.dispatch.expert1 | 0.707 | 0.746 | 0.1 | 3 |
| bwd.recompute:block7.moe.dispatch.expert2 | 0.700 | 0.746 | 0.1 | 3 |
| bwd.recompute:block7.moe.dispatch.expert3 | 0.700 | 0.742 | 0.1 | 3 |
| bwd.recompute:block7.moe.dispatch.expert4 | 0.699 | 0.736 | 0.1 | 3 |
| bwd.recompute:block7.moe.dispatch.expert5 | 0.694 | 0.744 | 0.1 | 3 |
| bwd.recompute:block7.moe.dispatch.expert6 | 0.696 | 0.739 | 0.1 | 3 |
| bwd.recompute:block7.moe.dispatch.expert7 | 0.696 | 0.732 | 0.1 | 3 |
| bwd.recompute:block7.moe.shared | 0.358 | 0.382 | 0.1 | 3 |
| bwd:block7.grad | 11.571 | 12.216 | 2.1 | 3 |
| bwd:block6 | 24.595 | 26.689 | 4.4 | 2 |
| bwd.invert:block6 | 7.770 | 8.364 | 1.4 | 3 |
| bwd.invert:block6.ln1 | 0.124 | 0.143 | 0.0 | 3 |
| bwd.invert:block6.attn.qkv | 0.254 | 0.297 | 0.0 | 3 |
| bwd.invert:block6.attn.sdpa | 0.156 | 0.173 | 0.0 | 3 |
| bwd.invert:block6.attn.proj | 0.134 | 0.160 | 0.0 | 3 |
| bwd.invert:block6.ln2 | 0.078 | 0.093 | 0.0 | 3 |
| bwd.invert:block6.moe.router | 0.311 | 0.352 | 0.1 | 3 |
| bwd.invert:block6.moe.dispatch | 5.765 | 6.069 | 1.0 | 3 |
| bwd.invert:block6.moe.dispatch.expert0 | 0.754 | 0.870 | 0.1 | 3 |
| bwd.invert:block6.moe.dispatch.expert1 | 0.672 | 0.717 | 0.1 | 3 |
| bwd.invert:block6.moe.dispatch.expert2 | 0.658 | 0.701 | 0.1 | 3 |
| bwd.invert:block6.moe.dispatch.expert3 | 0.651 | 0.692 | 0.1 | 3 |
| bwd.invert:block6.moe.dispatch.expert4 | 0.653 | 0.686 | 0.1 | 3 |
| bwd.invert:block6.moe.dispatch.expert5 | 0.653 | 0.695 | 0.1 | 3 |
| bwd.invert:block6.moe.dispatch.expert6 | 0.649 | 0.693 | 0.1 | 3 |
| bwd.invert:block6.moe.dispatch.expert7 | 0.657 | 0.701 | 0.1 | 3 |
| bwd.invert:block6.moe.shared | 0.346 | 0.367 | 0.1 | 3 |
| bwd.recompute:block6 | 8.033 | 8.449 | 1.4 | 3 |
| bwd.recompute:block6.ln1 | 0.118 | 0.135 | 0.0 | 3 |
| bwd.recompute:block6.attn.qkv | 0.252 | 0.283 | 0.0 | 3 |
| bwd.recompute:block6.attn.sdpa | 0.187 | 0.215 | 0.0 | 3 |
| bwd.recompute:block6.attn.proj | 0.152 | 0.181 | 0.0 | 3 |
| bwd.recompute:block6.ln2 | 0.088 | 0.102 | 0.0 | 3 |
| bwd.recompute:block6.moe.router | 0.321 | 0.374 | 0.1 | 3 |
| bwd.recompute:block6.moe.dispatch | 5.973 | 6.222 | 1.1 | 3 |
| bwd.recompute:block6.moe.dispatch.expert0 | 0.702 | 0.746 | 0.1 | 3 |
| bwd.recompute:block6.moe.dispatch.expert1 | 0.700 | 0.743 | 0.1 | 3 |
| bwd.recompute:block6.moe.dispatch.expert2 | 0.690 | 0.726 | 0.1 | 3 |
| bwd.recompute:block6.moe.dispatch.expert3 | 0.698 | 0.733 | 0.1 | 3 |
| bwd.recompute:block6.moe.dispatch.expert4 | 0.690 | 0.728 | 0.1 | 3 |
| bwd.recompute:block6.moe.dispatch.expert5 | 0.691 | 0.727 | 0.1 | 3 |
| bwd.recompute:block6.moe.dispatch.expert6 | 0.690 | 0.726 | 0.1 | 3 |
| bwd.recompute:block6.moe.dispatch.expert7 | 0.698 | 0.735 | 0.1 | 3 |
| bwd.recompute:block6.moe.shared | 0.353 | 0.377 | 0.1 | 3 |
| bwd:block6.grad | 11.650 | 12.423 | 2.1 | 3 |
| bwd:block5 | 24.309 | 26.385 | 4.3 | 2 |
| bwd.invert:block5 | 7.729 | 8.204 | 1.4 | 3 |
| bwd.invert:block5.ln1 | 0.127 | 0.146 | 0.0 | 3 |
| bwd.invert:block5.attn.qkv | 0.252 | 0.308 | 0.0 | 3 |
| bwd.invert:block5.attn.sdpa | 0.157 | 0.173 | 0.0 | 3 |
| bwd.invert:block5.attn.proj | 0.131 | 0.160 | 0.0 | 3 |
| bwd.invert:block5.ln2 | 0.080 | 0.096 | 0.0 | 3 |
| bwd.invert:block5.moe.router | 0.307 | 0.367 | 0.1 | 3 |
| bwd.invert:block5.moe.dispatch | 5.752 | 6.008 | 1.0 | 3 |
| bwd.invert:block5.moe.dispatch.expert0 | 0.743 | 0.854 | 0.1 | 3 |
| bwd.invert:block5.moe.dispatch.expert1 | 0.664 | 0.704 | 0.1 | 3 |
| bwd.invert:block5.moe.dispatch.expert2 | 0.655 | 0.688 | 0.1 | 3 |
| bwd.invert:block5.moe.dispatch.expert3 | 0.651 | 0.694 | 0.1 | 3 |
| bwd.invert:block5.moe.dispatch.expert4 | 0.652 | 0.687 | 0.1 | 3 |
| bwd.invert:block5.moe.dispatch.expert5 | 0.652 | 0.689 | 0.1 | 3 |
| bwd.invert:block5.moe.dispatch.expert6 | 0.647 | 0.692 | 0.1 | 3 |
| bwd.invert:block5.moe.dispatch.expert7 | 0.647 | 0.686 | 0.1 | 3 |
| bwd.invert:block5.moe.shared | 0.349 | 0.370 | 0.1 | 3 |
| bwd.recompute:block5 | 7.988 | 8.489 | 1.4 | 3 |
| bwd.recompute:block5.ln1 | 0.117 | 0.138 | 0.0 | 3 |
| bwd.recompute:block5.attn.qkv | 0.257 | 0.293 | 0.0 | 3 |
| bwd.recompute:block5.attn.sdpa | 0.169 | 0.188 | 0.0 | 3 |
| bwd.recompute:block5.attn.proj | 0.146 | 0.175 | 0.0 | 3 |
| bwd.recompute:block5.ln2 | 0.088 | 0.103 | 0.0 | 3 |
| bwd.recompute:block5.moe.router | 0.315 | 0.368 | 0.1 | 3 |
| bwd.recompute:block5.moe.dispatch | 5.955 | 6.245 | 1.1 | 3 |
| bwd.recompute:block5.moe.dispatch.expert0 | 0.697 | 0.737 | 0.1 | 3 |
| bwd.recompute:block5.moe.dispatch.expert1 | 0.699 | 0.735 | 0.1 | 3 |
| bwd.recompute:block5.moe.dispatch.expert2 | 0.692 | 0.745 | 0.1 | 3 |
| bwd.recompute:block5.moe.dispatch.expert3 | 0.690 | 0.736 | 0.1 | 3 |
| bwd.recompute:block5.moe.dispatch.expert4 | 0.699 | 0.736 | 0.1 | 3 |
| bwd.recompute:block5.moe.dispatch.expert5 | 0.702 | 0.739 | 0.1 | 3 |
| bwd.recompute:block5.moe.dispatch.expert6 | 0.698 | 0.750 | 0.1 | 3 |
| bwd.recompute:block5.moe.dispatch.expert7 | 0.692 | 0.733 | 0.1 | 3 |
| bwd.recompute:block5.moe.shared | 0.355 | 0.382 | 0.1 | 3 |
| bwd:block5.grad | 11.370 | 12.323 | 2.0 | 3 |
| bwd:block4 | 24.193 | 26.437 | 4.3 | 2 |
| bwd.invert:block4 | 7.648 | 8.240 | 1.4 | 3 |
| bwd.invert:block4.ln1 | 0.124 | 0.148 | 0.0 | 3 |
| bwd.invert:block4.attn.qkv | 0.250 | 0.302 | 0.0 | 3 |
| bwd.invert:block4.attn.sdpa | 0.153 | 0.170 | 0.0 | 3 |
| bwd.invert:block4.attn.proj | 0.129 | 0.155 | 0.0 | 3 |
| bwd.invert:block4.ln2 | 0.078 | 0.091 | 0.0 | 3 |
| bwd.invert:block4.moe.router | 0.312 | 0.374 | 0.1 | 3 |
| bwd.invert:block4.moe.dispatch | 5.728 | 6.078 | 1.0 | 3 |
| bwd.invert:block4.moe.dispatch.expert0 | 0.731 | 0.869 | 0.1 | 3 |
| bwd.invert:block4.moe.dispatch.expert1 | 0.668 | 0.714 | 0.1 | 3 |
| bwd.invert:block4.moe.dispatch.expert2 | 0.659 | 0.703 | 0.1 | 3 |
| bwd.invert:block4.moe.dispatch.expert3 | 0.651 | 0.692 | 0.1 | 3 |
| bwd.invert:block4.moe.dispatch.expert4 | 0.653 | 0.691 | 0.1 | 3 |
| bwd.invert:block4.moe.dispatch.expert5 | 0.648 | 0.684 | 0.1 | 3 |
| bwd.invert:block4.moe.dispatch.expert6 | 0.649 | 0.685 | 0.1 | 3 |
| bwd.invert:block4.moe.dispatch.expert7 | 0.648 | 0.689 | 0.1 | 3 |
| bwd.invert:block4.moe.shared | 0.346 | 0.368 | 0.1 | 3 |
| bwd.recompute:block4 | 7.985 | 8.431 | 1.4 | 3 |
| bwd.recompute:block4.ln1 | 0.117 | 0.137 | 0.0 | 3 |
| bwd.recompute:block4.attn.qkv | 0.247 | 0.282 | 0.0 | 3 |
| bwd.recompute:block4.attn.sdpa | 0.176 | 0.205 | 0.0 | 3 |
| bwd.recompute:block4.attn.proj | 0.147 | 0.176 | 0.0 | 3 |
| bwd.recompute:block4.ln2 | 0.087 | 0.101 | 0.0 | 3 |
| bwd.recompute:block4.moe.router | 0.309 | 0.371 | 0.1 | 3 |
| bwd.recompute:block4.moe.dispatch | 5.953 | 6.210 | 1.1 | 3 |
| bwd.recompute:block4.moe.dispatch.expert0 | 0.692 | 0.730 | 0.1 | 3 |
| bwd.recompute:block4.moe.dispatch.expert1 | 0.700 | 0.737 | 0.1 | 3 |
| bwd.recompute:block4.moe.dispatch.expert2 | 0.697 | 0.739 | 0.1 | 3 |
| bwd.recompute:block4.moe.dispatch.expert3 | 0.693 | 0.737 | 0.1 | 3 |
| bwd.recompute:block4.moe.dispatch.expert4 | 0.701 | 0.735 | 0.1 | 3 |
| bwd.recompute:block4.moe.dispatch.expert5 | 0.697 | 0.733 | 0.1 | 3 |
| bwd.recompute:block4.moe.dispatch.expert6 | 0.694 | 0.729 | 0.1 | 3 |
| bwd.recompute:block4.moe.dispatch.expert7 | 0.688 | 0.724 | 0.1 | 3 |
| bwd.recompute:block4.moe.shared | 0.356 | 0.374 | 0.1 | 3 |
| bwd:block4.grad | 11.387 | 12.191 | 2.0 | 3 |
| bwd:block3 | 24.103 | 26.154 | 4.3 | 2 |
| bwd.invert:block3 | 7.652 | 8.171 | 1.4 | 3 |
| bwd.invert:block3.ln1 | 0.125 | 0.146 | 0.0 | 3 |
| bwd.invert:block3.attn.qkv | 0.246 | 0.302 | 0.0 | 3 |
| bwd.invert:block3.attn.sdpa | 0.153 | 0.187 | 0.0 | 3 |
| bwd.invert:block3.attn.proj | 0.136 | 0.179 | 0.0 | 3 |
| bwd.invert:block3.ln2 | 0.079 | 0.102 | 0.0 | 3 |
| bwd.invert:block3.moe.router | 0.305 | 0.357 | 0.1 | 3 |
| bwd.invert:block3.moe.dispatch | 5.711 | 5.989 | 1.0 | 3 |
| bwd.invert:block3.moe.dispatch.expert0 | 0.716 | 0.819 | 0.1 | 3 |
| bwd.invert:block3.moe.dispatch.expert1 | 0.658 | 0.701 | 0.1 | 3 |
| bwd.invert:block3.moe.dispatch.expert2 | 0.656 | 0.700 | 0.1 | 3 |
| bwd.invert:block3.moe.dispatch.expert3 | 0.651 | 0.689 | 0.1 | 3 |
| bwd.invert:block3.moe.dispatch.expert4 | 0.653 | 0.689 | 0.1 | 3 |
| bwd.invert:block3.moe.dispatch.expert5 | 0.652 | 0.688 | 0.1 | 3 |
| bwd.invert:block3.moe.dispatch.expert6 | 0.653 | 0.688 | 0.1 | 3 |
| bwd.invert:block3.moe.dispatch.expert7 | 0.649 | 0.685 | 0.1 | 3 |
| bwd.invert:block3.moe.shared | 0.353 | 0.377 | 0.1 | 3 |
| bwd.recompute:block3 | 8.004 | 8.452 | 1.4 | 3 |
| bwd.recompute:block3.ln1 | 0.115 | 0.133 | 0.0 | 3 |
| bwd.recompute:block3.attn.qkv | 0.251 | 0.285 | 0.0 | 3 |
| bwd.recompute:block3.attn.sdpa | 0.187 | 0.214 | 0.0 | 3 |
| bwd.recompute:block3.attn.proj | 0.143 | 0.170 | 0.0 | 3 |
| bwd.recompute:block3.ln2 | 0.085 | 0.101 | 0.0 | 3 |
| bwd.recompute:block3.moe.router | 0.309 | 0.373 | 0.1 | 3 |
| bwd.recompute:block3.moe.dispatch | 5.976 | 6.290 | 1.1 | 3 |
| bwd.recompute:block3.moe.dispatch.expert0 | 0.690 | 0.743 | 0.1 | 3 |
| bwd.recompute:block3.moe.dispatch.expert1 | 0.705 | 0.748 | 0.1 | 3 |
| bwd.recompute:block3.moe.dispatch.expert2 | 0.693 | 0.736 | 0.1 | 3 |
| bwd.recompute:block3.moe.dispatch.expert3 | 0.702 | 0.739 | 0.1 | 3 |
| bwd.recompute:block3.moe.dispatch.expert4 | 0.699 | 0.754 | 0.1 | 3 |
| bwd.recompute:block3.moe.dispatch.expert5 | 0.695 | 0.739 | 0.1 | 3 |
| bwd.recompute:block3.moe.dispatch.expert6 | 0.698 | 0.744 | 0.1 | 3 |
| bwd.recompute:block3.moe.dispatch.expert7 | 0.694 | 0.735 | 0.1 | 3 |
| bwd.recompute:block3.moe.shared | 0.356 | 0.373 | 0.1 | 3 |
| bwd:block3.grad | 11.306 | 12.052 | 2.0 | 3 |
| bwd:block2 | 24.091 | 26.304 | 4.3 | 2 |
| bwd.invert:block2 | 7.630 | 8.163 | 1.4 | 3 |
| bwd.invert:block2.ln1 | 0.124 | 0.144 | 0.0 | 3 |
| bwd.invert:block2.attn.qkv | 0.252 | 0.300 | 0.0 | 3 |
| bwd.invert:block2.attn.sdpa | 0.151 | 0.176 | 0.0 | 3 |
| bwd.invert:block2.attn.proj | 0.129 | 0.163 | 0.0 | 3 |
| bwd.invert:block2.ln2 | 0.076 | 0.092 | 0.0 | 3 |
| bwd.invert:block2.moe.router | 0.298 | 0.349 | 0.1 | 3 |
| bwd.invert:block2.moe.dispatch | 5.714 | 5.998 | 1.0 | 3 |
| bwd.invert:block2.moe.dispatch.expert0 | 0.716 | 0.829 | 0.1 | 3 |
| bwd.invert:block2.moe.dispatch.expert1 | 0.666 | 0.711 | 0.1 | 3 |
| bwd.invert:block2.moe.dispatch.expert2 | 0.657 | 0.694 | 0.1 | 3 |
| bwd.invert:block2.moe.dispatch.expert3 | 0.658 | 0.694 | 0.1 | 3 |
| bwd.invert:block2.moe.dispatch.expert4 | 0.655 | 0.685 | 0.1 | 3 |
| bwd.invert:block2.moe.dispatch.expert5 | 0.655 | 0.701 | 0.1 | 3 |
| bwd.invert:block2.moe.dispatch.expert6 | 0.655 | 0.693 | 0.1 | 3 |
| bwd.invert:block2.moe.dispatch.expert7 | 0.660 | 0.690 | 0.1 | 3 |
| bwd.invert:block2.moe.shared | 0.349 | 0.372 | 0.1 | 3 |
| bwd.recompute:block2 | 8.041 | 8.615 | 1.4 | 3 |
| bwd.recompute:block2.ln1 | 0.116 | 0.139 | 0.0 | 3 |
| bwd.recompute:block2.attn.qkv | 0.246 | 0.276 | 0.0 | 3 |
| bwd.recompute:block2.attn.sdpa | 0.193 | 0.218 | 0.0 | 3 |
| bwd.recompute:block2.attn.proj | 0.150 | 0.175 | 0.0 | 3 |
| bwd.recompute:block2.ln2 | 0.085 | 0.100 | 0.0 | 3 |
| bwd.recompute:block2.moe.router | 0.310 | 0.369 | 0.1 | 3 |
| bwd.recompute:block2.moe.dispatch | 6.005 | 6.320 | 1.1 | 3 |
| bwd.recompute:block2.moe.dispatch.expert0 | 0.698 | 0.746 | 0.1 | 3 |
| bwd.recompute:block2.moe.dispatch.expert1 | 0.702 | 0.738 | 0.1 | 3 |
| bwd.recompute:block2.moe.dispatch.expert2 | 0.697 | 0.757 | 0.1 | 3 |
| bwd.recompute:block2.moe.dispatch.expert3 | 0.705 | 0.754 | 0.1 | 3 |
| bwd.recompute:block2.moe.dispatch.expert4 | 0.695 | 0.739 | 0.1 | 3 |
| bwd.recompute:block2.moe.dispatch.expert5 | 0.693 | 0.740 | 0.1 | 3 |
| bwd.recompute:block2.moe.dispatch.expert6 | 0.692 | 0.722 | 0.1 | 3 |
| bwd.recompute:block2.moe.dispatch.expert7 | 0.689 | 0.731 | 0.1 | 3 |
| bwd.recompute:block2.moe.shared | 0.355 | 0.374 | 0.1 | 3 |
| bwd:block2.grad | 11.206 | 12.028 | 2.0 | 3 |
| bwd:block1 | 23.984 | 26.287 | 4.3 | 2 |
| bwd.invert:block1 | 7.596 | 8.226 | 1.4 | 3 |
| bwd.invert:block1.ln1 | 0.123 | 0.142 | 0.0 | 3 |
| bwd.invert:block1.attn.qkv | 0.253 | 0.302 | 0.0 | 3 |
| bwd.invert:block1.attn.sdpa | 0.152 | 0.167 | 0.0 | 3 |
| bwd.invert:block1.attn.proj | 0.124 | 0.152 | 0.0 | 3 |
| bwd.invert:block1.ln2 | 0.079 | 0.092 | 0.0 | 3 |
| bwd.invert:block1.moe.router | 0.302 | 0.337 | 0.1 | 3 |
| bwd.invert:block1.moe.dispatch | 5.716 | 6.035 | 1.0 | 3 |
| bwd.invert:block1.moe.dispatch.expert0 | 0.709 | 0.819 | 0.1 | 3 |
| bwd.invert:block1.moe.dispatch.expert1 | 0.675 | 0.738 | 0.1 | 3 |
| bwd.invert:block1.moe.dispatch.expert2 | 0.656 | 0.690 | 0.1 | 3 |
| bwd.invert:block1.moe.dispatch.expert3 | 0.652 | 0.688 | 0.1 | 3 |
| bwd.invert:block1.moe.dispatch.expert4 | 0.664 | 0.722 | 0.1 | 3 |
| bwd.invert:block1.moe.dispatch.expert5 | 0.655 | 0.693 | 0.1 | 3 |
| bwd.invert:block1.moe.dispatch.expert6 | 0.649 | 0.692 | 0.1 | 3 |
| bwd.invert:block1.moe.dispatch.expert7 | 0.653 | 0.694 | 0.1 | 3 |
| bwd.invert:block1.moe.shared | 0.348 | 0.367 | 0.1 | 3 |
| bwd.recompute:block1 | 8.014 | 8.655 | 1.4 | 3 |
| bwd.recompute:block1.ln1 | 0.118 | 0.139 | 0.0 | 3 |
| bwd.recompute:block1.attn.qkv | 0.245 | 0.278 | 0.0 | 3 |
| bwd.recompute:block1.attn.sdpa | 0.197 | 0.224 | 0.0 | 3 |
| bwd.recompute:block1.attn.proj | 0.152 | 0.177 | 0.0 | 3 |
| bwd.recompute:block1.ln2 | 0.086 | 0.102 | 0.0 | 3 |
| bwd.recompute:block1.moe.router | 0.311 | 0.372 | 0.1 | 3 |
| bwd.recompute:block1.moe.dispatch | 5.990 | 6.329 | 1.1 | 3 |
| bwd.recompute:block1.moe.dispatch.expert0 | 0.698 | 0.740 | 0.1 | 3 |
| bwd.recompute:block1.moe.dispatch.expert1 | 0.713 | 0.760 | 0.1 | 3 |
| bwd.recompute:block1.moe.dispatch.expert2 | 0.698 | 0.742 | 0.1 | 3 |
| bwd.recompute:block1.moe.dispatch.expert3 | 0.707 | 0.751 | 0.1 | 3 |
| bwd.recompute:block1.moe.dispatch.expert4 | 0.699 | 0.749 | 0.1 | 3 |
| bwd.recompute:block1.moe.dispatch.expert5 | 0.693 | 0.745 | 0.1 | 3 |
| bwd.recompute:block1.moe.dispatch.expert6 | 0.681 | 0.731 | 0.1 | 3 |
| bwd.recompute:block1.moe.dispatch.expert7 | 0.689 | 0.734 | 0.1 | 3 |
| bwd.recompute:block1.moe.shared | 0.351 | 0.373 | 0.1 | 3 |
| bwd:block1.grad | 11.269 | 12.128 | 2.0 | 3 |
| bwd:block0 | 23.852 | 26.414 | 4.3 | 2 |
| bwd.invert:block0 | 7.601 | 8.134 | 1.4 | 3 |
| bwd.invert:block0.ln1 | 0.125 | 0.144 | 0.0 | 3 |
| bwd.invert:block0.attn.qkv | 0.252 | 0.293 | 0.0 | 3 |
| bwd.invert:block0.attn.sdpa | 0.152 | 0.162 | 0.0 | 3 |
| bwd.invert:block0.attn.proj | 0.126 | 0.158 | 0.0 | 3 |
| bwd.invert:block0.ln2 | 0.078 | 0.092 | 0.0 | 3 |
| bwd.invert:block0.moe.router | 0.303 | 0.344 | 0.1 | 3 |
| bwd.invert:block0.moe.dispatch | 5.724 | 6.014 | 1.0 | 3 |
| bwd.invert:block0.moe.dispatch.expert0 | 0.717 | 0.831 | 0.1 | 3 |
| bwd.invert:block0.moe.dispatch.expert1 | 0.662 | 0.701 | 0.1 | 3 |
| bwd.invert:block0.moe.dispatch.expert2 | 0.662 | 0.705 | 0.1 | 3 |
| bwd.invert:block0.moe.dispatch.expert3 | 0.658 | 0.696 | 0.1 | 3 |
| bwd.invert:block0.moe.dispatch.expert4 | 0.658 | 0.701 | 0.1 | 3 |
| bwd.invert:block0.moe.dispatch.expert5 | 0.655 | 0.699 | 0.1 | 3 |
| bwd.invert:block0.moe.dispatch.expert6 | 0.648 | 0.686 | 0.1 | 3 |
| bwd.invert:block0.moe.dispatch.expert7 | 0.651 | 0.682 | 0.1 | 3 |
| bwd.invert:block0.moe.shared | 0.350 | 0.368 | 0.1 | 3 |
| bwd.recompute:block0 | 7.990 | 8.512 | 1.4 | 3 |
| bwd.recompute:block0.ln1 | 0.115 | 0.137 | 0.0 | 3 |
| bwd.recompute:block0.attn.qkv | 0.246 | 0.277 | 0.0 | 3 |
| bwd.recompute:block0.attn.sdpa | 0.202 | 0.234 | 0.0 | 3 |
| bwd.recompute:block0.attn.proj | 0.151 | 0.179 | 0.0 | 3 |
| bwd.recompute:block0.ln2 | 0.086 | 0.104 | 0.0 | 3 |
| bwd.recompute:block0.moe.router | 0.310 | 0.365 | 0.1 | 3 |
| bwd.recompute:block0.moe.dispatch | 5.963 | 6.244 | 1.1 | 3 |
| bwd.recompute:block0.moe.dispatch.expert0 | 0.697 | 0.747 | 0.1 | 3 |
| bwd.recompute:block0.moe.dispatch.expert1 | 0.697 | 0.739 | 0.1 | 3 |
| bwd.recompute:block0.moe.dispatch.expert2 | 0.707 | 0.760 | 0.1 | 3 |
| bwd.recompute:block0.moe.dispatch.expert3 | 0.698 | 0.732 | 0.1 | 3 |
| bwd.recompute:block0.moe.dispatch.expert4 | 0.705 | 0.749 | 0.1 | 3 |
| bwd.recompute:block0.moe.dispatch.expert5 | 0.691 | 0.733 | 0.1 | 3 |
| bwd.recompute:block0.moe.dispatch.expert6 | 0.688 | 0.735 | 0.1 | 3 |
| bwd.recompute:block0.moe.dispatch.expert7 | 0.681 | 0.719 | 0.1 | 3 |
| bwd.recompute:block0.moe.shared | 0.356 | 0.380 | 0.1 | 3 |
| bwd:block0.grad | 11.109 | 11.937 | 2.0 | 3 |
| bwd:embed | 0.519 | 0.567 | 0.1 | 2 |
| opt | 182.534 | 194.267 | 32.5 | 1 |
| opt:opt.clip | 5.435 | 6.186 | 1.0 | 2 |
| opt:opt.muon | 172.147 | 182.444 | 30.7 | 2 |
| opt:opt.muon.ns | 165.699 | 173.764 | 29.5 | 3 |
| opt:opt.adamw | 2.512 | 2.916 | 0.4 | 2 |
| opt:opt.moe_bias | 1.054 | 1.118 | 0.2 | 3 |
| opt:opt.zero_grad | 1.608 | 1.796 | 0.3 | 3 |

## Time by part type (sum over layers)

| part type | median ms sum | % of step |
| :--- | ---: | ---: |
| bwd | 269.007 | 48.0 |
| bwd:stack | 220.305 | 39.3 |
| bwd:block* | 219.104 | 39.1 |
| opt | 182.534 | 32.5 |
| opt:opt.muon | 172.147 | 30.7 |
| opt:opt.muon.ns | 165.699 | 29.5 |
| fwd | 108.887 | 19.4 |
| bwd:block*.grad | 102.714 | 18.3 |
| bwd.recompute:block* | 72.484 | 12.9 |
| bwd.invert:block* | 69.091 | 12.3 |
| fwd:stack | 63.266 | 11.3 |
| fwd:block* | 62.297 | 11.1 |
| fwd:block*.moe.dispatch | 58.043 | 10.3 |
| bwd.recompute:block*.moe.dispatch | 54.004 | 9.6 |
| bwd.invert:block*.moe.dispatch | 52.351 | 9.3 |
| bwd:head+loss | 48.172 | 8.6 |
| fwd:head+loss | 40.966 | 7.3 |
| bwd.invert:block*.moe.dispatch.expert0 | 7.127 | 1.3 |
| fwd:block*.moe.dispatch.expert1 | 6.960 | 1.2 |
| fwd:block*.moe.dispatch.expert2 | 6.913 | 1.2 |
| fwd:block*.moe.dispatch.expert4 | 6.879 | 1.2 |
| fwd:block*.moe.dispatch.expert5 | 6.800 | 1.2 |
| fwd:block*.moe.dispatch.expert3 | 6.793 | 1.2 |
| fwd:block*.moe.dispatch.expert6 | 6.708 | 1.2 |
| fwd:block*.moe.dispatch.expert7 | 6.693 | 1.2 |
| fwd:block*.moe.dispatch.expert0 | 6.598 | 1.2 |
| bwd.recompute:block*.moe.dispatch.expert1 | 6.347 | 1.1 |
| bwd.recompute:block*.moe.dispatch.expert0 | 6.316 | 1.1 |
| bwd.recompute:block*.moe.dispatch.expert3 | 6.312 | 1.1 |
| bwd.recompute:block*.moe.dispatch.expert4 | 6.302 | 1.1 |
| bwd.recompute:block*.moe.dispatch.expert2 | 6.294 | 1.1 |
| bwd.recompute:block*.moe.dispatch.expert5 | 6.271 | 1.1 |
| bwd.recompute:block*.moe.dispatch.expert6 | 6.249 | 1.1 |
| bwd.recompute:block*.moe.dispatch.expert7 | 6.242 | 1.1 |
| bwd.invert:block*.moe.dispatch.expert1 | 6.139 | 1.1 |
| bwd.invert:block*.moe.dispatch.expert2 | 5.961 | 1.1 |
| bwd.invert:block*.moe.dispatch.expert4 | 5.923 | 1.1 |
| bwd.invert:block*.moe.dispatch.expert3 | 5.914 | 1.1 |
| bwd.invert:block*.moe.dispatch.expert5 | 5.906 | 1.1 |
| bwd.invert:block*.moe.dispatch.expert7 | 5.899 | 1.1 |
| bwd.invert:block*.moe.dispatch.expert6 | 5.877 | 1.0 |
| opt:opt.clip | 5.435 | 1.0 |
| fwd:embed | 4.481 | 0.8 |
| fwd:embed.ke | 4.439 | 0.8 |
| fwd:block*.moe.router | 3.288 | 0.6 |
| fwd:block*.moe.shared | 3.245 | 0.6 |
| bwd.recompute:block*.moe.shared | 3.204 | 0.6 |
| bwd.invert:block*.moe.shared | 3.153 | 0.6 |
| bwd.recompute:block*.moe.router | 2.886 | 0.5 |
| bwd.invert:block*.moe.router | 2.518 | 0.4 |
| opt:opt.adamw | 2.512 | 0.4 |
| bwd.recompute:block*.attn.qkv | 2.282 | 0.4 |
| bwd.invert:block*.attn.qkv | 2.113 | 0.4 |
| fwd:block*.attn.qkv | 1.831 | 0.3 |
| bwd.recompute:block*.attn.sdpa | 1.718 | 0.3 |
| opt:opt.zero_grad | 1.608 | 0.3 |
| bwd.recompute:block*.attn.proj | 1.357 | 0.2 |
| bwd.invert:block*.attn.sdpa | 1.311 | 0.2 |
| fwd:block*.attn.sdpa | 1.245 | 0.2 |
| data | 1.118 | 0.2 |
| bwd.invert:block*.attn.proj | 1.081 | 0.2 |
| bwd.recompute:block*.ln1 | 1.080 | 0.2 |
| opt:opt.moe_bias | 1.054 | 0.2 |
| bwd.invert:block*.ln1 | 1.053 | 0.2 |
| fwd:block*.attn.proj | 1.026 | 0.2 |
| fwd:block*.ln1 | 0.870 | 0.2 |
| bwd.recompute:block*.ln2 | 0.784 | 0.1 |
| bwd.invert:block*.ln2 | 0.680 | 0.1 |
| fwd:block*.ln2 | 0.660 | 0.1 |
| bwd:embed | 0.519 | 0.1 |

## Five slowest leaf parts

1. `opt:opt.muon.ns` — 165.699 ms (29.5% of step)
2. `bwd:block8.grad` — 11.845 ms (2.1% of step)
3. `bwd:block6.grad` — 11.650 ms (2.1% of step)
4. `bwd:block7.grad` — 11.571 ms (2.1% of step)
5. `bwd:block4.grad` — 11.387 ms (2.0% of step)
