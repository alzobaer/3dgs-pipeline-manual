# Results & Validation

Research results and validation.

## Quality Metrics

| Metric | Value | Interpretation |
|--------|-------|----------------|
| **PSNR** | 23.80 dB | Good (>20 dB acceptable) |
| **SSIM** | 0.779 | Good (1.0 = perfect) |
| **LPIPS** | 0.216 | Good (0.0 = perfect) |
| **CV (temporal)** | 3.5% | Excellent consistency |

## Plant Growth Time-Lapse

<video controls width="100%" style="border-radius:8px; margin-bottom:1rem;">
  <source src="../../assets/videos/results/timelapse-growth.mp4" type="video/mp4">
</video>
*3DGS-rendered plant growth across all 22 acquisition dates (Jan 19 – Mar 9, 2026). Each frame shows the height measured from the point cloud.*

---

## Validation Results

- **Dates:** 22 capture dates
- **Duration:** 50 days (Jan 19 - Mar 9, 2026)
- **Success Rate:** 100% (22/22)
- **Computing:** DNN19, RTX 6000 Ada

## Key Finding

Fixed viewpoint (Condition 1) outperforms:
- Multi-video merged (v1): 17.30 dB
- Motion videos (v3): 19-20 dB
- LongSplat: 15.92 dB

**Lesson:** Acquisition consistency > method sophistication
