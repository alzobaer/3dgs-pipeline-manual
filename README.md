# 3DGS Pipeline Manual

**Complete reproducibility manual for 3D Gaussian Splatting time-series plant phenotyping**

[![Deploy MkDocs](https://github.com/alzobaer/3dgs-pipeline-manual/actions/workflows/deploy.yml/badge.svg)](https://github.com/alzobaer/3dgs-pipeline-manual/actions/workflows/deploy.yml)
[![MkDocs Material](https://img.shields.io/badge/docs-MkDocs%20Material-blue)](https://squidfunk.github.io/mkdocs-material/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

📖 **Live site:** https://alzobaer.github.io/3dgs-pipeline-manual/

---

## Overview

This manual documents the full pipeline for reconstructing plant growth in 3D using **3D Gaussian Splatting (3DGS)**, validated over a 50-day time series (22 capture dates, Jan 19 – Mar 9, 2026) at Mineno Laboratory, Shizuoka University.

| Metric | Result |
|--------|--------|
| PSNR | 23.80 dB |
| SSIM | 0.779 |
| LPIPS | 0.216 |
| Temporal CV | 3.5% (excellent) |
| Success rate | 22 / 22 dates (100%) |

---

## Pipeline Stages

```
Video Capture → Frame Extraction → COLMAP SfM → 3DGS Training → Rendering → Trait Extraction
```

1. **Video Acquisition** — fixed-viewpoint video per date
2. **Frame Extraction** — FFmpeg, 2 fps, ~330 frames/date
3. **COLMAP** — Structure-from-Motion sparse reconstruction
4. **3DGS Training** — 30,000 iterations, RTX 6000 Ada, ~20 min/date
5. **Rendering** — novel-view synthesis at consistent viewpoint
6. **Trait Extraction** — height, canopy area, growth curve from rendered images

---

## Local Preview

```bash
# Install dependencies
pip install -r requirements.txt

# Serve locally
mkdocs serve
# → open http://127.0.0.1:8000
```

---

## Deployment

Deployment to GitHub Pages is **automatic** on every push to `main` via GitHub Actions.

To deploy manually:

```bash
mkdocs gh-deploy
```

---

## Repository Structure

```
3dgs-pipeline-manual/
├── docs/
│   ├── index.md                  # Homepage
│   ├── getting-started/          # Overview, hardware, software setup
│   ├── environment/              # Conda, CUDA, dependencies
│   ├── pipeline/                 # Stages 1–6 (detailed)
│   ├── my-research/              # Validation results & figures
│   ├── advanced/                 # Batch processing, parameters
│   ├── troubleshooting/          # GPU memory, COLMAP issues
│   └── assets/
│       ├── images/
│       │   ├── figures/          # Research figures (PSNR, growth curve…)
│       │   ├── screenshots/      # Step-by-step software screenshots
│       │   └── diagrams/         # Pipeline diagrams
│       └── videos/
│           ├── demos/            # Training progress, 360° orbit
│           ├── results/          # GT vs render, time-lapse growth
│           └── tutorials/        # Pipeline overview
├── .github/workflows/deploy.yml  # Auto-deploy to GitHub Pages
├── mkdocs.yml                    # Site configuration
├── requirements.txt              # Python dependencies
└── README.md
```

---

## Citation

If you use this pipeline or manual in your research, please cite:

```bibtex
@misc{zobaer2026_3dgs_plant,
  author    = {Al Zobaer},
  title     = {3D Gaussian Splatting Pipeline for Time-Series Plant Phenotyping},
  year      = {2026},
  publisher = {GitHub},
  url       = {https://alzobaer.github.io/3dgs-pipeline-manual/}
}
```

---

## Author

**Al Zobaer** (M2 Student)  
Mineno Laboratory, Graduate School of Integrated Science and Technology  
Shizuoka University, Japan

---

## License

This documentation is released under the [MIT License](LICENSE).  
The 3DGS training code is subject to the original [gaussian-splatting license](https://github.com/graphdeco-inria/gaussian-splatting/blob/main/LICENSE.md).
