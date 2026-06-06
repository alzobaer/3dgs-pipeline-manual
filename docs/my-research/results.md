# Results & Validation

Research results and validation. All values match the submitted manuscript (Computers and Electronics in Agriculture).

## Reconstruction Quality Metrics (Condition 1, 5 fps, Jan 19)

| Metric | Value | Interpretation |
|--------|-------|----------------|
| **PSNR** | 23.71 dB | Good (>20 dB acceptable) |
| **SSIM** | 0.773 | Good (1.0 = perfect) |
| **LPIPS** | 0.222 | Good (0.0 = perfect) |
| **PSNR temporal CV** | 3.5% | Excellent consistency across 22 sessions |
| **Mean PSNR (22 sessions)** | 23.84 dB | All sessions exceed 22.5 dB |

## Plant Trait Measurement Results

| Metric | Proposed (render-space) | Baseline (direct PLY) | Improvement |
|--------|------------------------|----------------------|-------------|
| **h_norm CV** | **9.8%** | 28.0% | **2.86× more stable** |
| **a_norm CV** | 16.7% | 22.6% (PLY spread) | More stable |
| Scale-calibrated PLY CV | — | 35.1% | Worse than direct PLY |

## Plant Growth Time-Lapse

<video controls width="100%" style="border-radius:8px; margin-bottom:1rem;">
  <source src="../../assets/videos/results/timelapse-growth.mp4" type="video/mp4">
</video>
*3DGS-rendered plant growth across all 22 acquisition dates (Jan 19 – Mar 9, 2026). Each frame shows the height measured from the rendered canonical image.*

---

## Validation Results

- **Dates:** 22 capture dates
- **Duration:** 49 days (Jan 19 – Mar 9, 2026)
- **Success Rate:** 100% (22/22)
- **Computing:** DNN19, RTX 6000 Ada

## Key Finding

Fixed viewpoint (Condition 1, 5 fps) outperforms all other acquisition conditions:

| Condition | PSNR |
|-----------|------|
| **Cond. 1 — Fixed end-a, lower viewpoint** | **23.71 dB** |
| Cond. 5 — One-way a→d, tier 1 | 21.42 dB |
| Cond. 2 — Fixed end-b, lower viewpoint | 20.11 dB |
| Cond. 3 — Round-trip, tier 1 | 19.37 dB |
| Merged (all 6 combined) | 18.60 dB |

**Lesson:** Acquisition consistency > method sophistication
