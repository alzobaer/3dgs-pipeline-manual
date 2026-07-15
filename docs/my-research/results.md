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

## Plant Trait Monitoring Results (cross-session consistency)

!!! note "Why CV is the right metric"
    This is a **monitoring** system: the goal is to track relative change over time, not to report absolute, calibrated trait values. The coefficient of variation (CV, lower = more consistent) is therefore the primary and appropriate evaluation metric.

| Metric | Proposed (render-space) | Baseline (direct PLY) | Improvement |
|--------|------------------------|----------------------|-------------|
| **h_norm CV** | **9.8%** | 28.0% | **2.86× more stable** |
| **a_norm CV** | 16.7% | 22.6% (PLY spread) | More stable |
| Scale-calibrated PLY CV | — | 35.1% | Worse than direct PLY |

## Biological Validation — Pruning-Event Detection

The render-space signal detects real crop-management events, which is the key evidence that it tracks biology rather than noise.

| Aspect | Result |
|--------|--------|
| Documented pruning events detected | **3 / 3** |
| Mean drop at pruning | ≈ 0.20 normalized height (15–27 pp) |
| Significance (pruning vs. non-pruning dates) | **p = 0.0008** |
| Background variation | 9.8% (CV) — drops are well above it |

## Physical-Reference Validation — 45 cm Pipe

Render-space height is corroborated against an in-scene 45 cm bench pipe used as a ruler, `h_gt = (plant_px / pipe_px) × 45 cm`, annotated across all 22 sessions.

| Aspect | Result |
|--------|--------|
| Correlation (render-space vs. pipe reference) | **r = 0.74**, p < 0.001 |
| R² | 0.55 |
| Reference mean height | 159.9 cm |
| Spread | h_gt CV 8.9% vs. h_norm CV 9.6% |

!!! note "Corroboration, not accuracy"
    r = 0.74 shows the signal is **grounded in real-world scale** — it is not a claim of absolute-height accuracy. The ~45% unexplained variance is noise in the pipe reference itself (SfM scale ambiguity across sessions), not pipeline error.

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

---

## Limitations and Future Ground Truth

!!! warning "Honest limitations"
    - **No calibrated ground truth (RMSE):** these 22 sessions have no tape-measured physical heights, so the system is validated for **consistency (CV)** and **change detection**, not absolute accuracy. The 45 cm-pipe result is corroboration, not calibration.
    - **Reference-instrument noise:** the pipe reference carries its own SfM scale ambiguity (pipe spans 263–420 px for a fixed 45 cm), which accounts for most of the unexplained variance in the r = 0.74 agreement.
    - **Operator not blinded** to the pruning schedule; events were confirmed from work logs post-hoc.

!!! tip "Planned ground-truth protocol (future work)"
    A three-tier protocol would upgrade the evaluation from consistency to absolute accuracy:

    1. **Tape measurements** on 5–10 tagged plants per session (direct RMSE).
    2. **Rigid calibration bar** of known length in-scene — removes the dominant variance source of a movable pipe.
    3. **ArUco markers** for a full per-session similarity transform → absolute metric units.
