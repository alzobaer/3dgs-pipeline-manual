# My Research Overview

3D Gaussian Splatting for time-series plant **monitoring** in greenhouses.

!!! note "Framing: monitoring, not absolute measurement"
    This work is a **relative growth-monitoring / change-detection** system. It tracks how a plant changes over time and detects biologically meaningful events; it does **not** claim absolute, calibrated trait values. Consistency across sessions (coefficient of variation, CV) is therefore the primary and appropriate evaluation metric.

## Research Focus

Developing a robust 3DGS pipeline for:
- Time-series greenhouse monitoring and change detection
- Scale-invariant, render-space trait extraction
- Detection of real crop-management events (e.g. pruning)

## Key Contributions

1. **Render-space, scale-invariant trait extraction** — height CV 28.0% → 9.8% (2.86× more consistent)
2. **Biological validation via pruning-event detection** — three documented events detected (p = 0.0008)
3. **Physical-reference corroboration** — render-space height vs. an in-scene 45 cm pipe, r = 0.74
4. **Long-term validation** — 49 days, 22 sessions, 100% reconstruction success

See [Original Contributions](contributions.md) for details.

## Publications

Journal paper under review at *Computers and Electronics in Agriculture* (Elsevier).
