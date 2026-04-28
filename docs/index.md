# 3DGS Pipeline Manual

Welcome to the comprehensive manual for **3D Gaussian Splatting (3DGS) for Time-Series Plant Phenotyping**.

![Pipeline Overview](assets/images/diagrams/pipeline-overview.png){ width="100%" }
*Complete pipeline from video capture to trait extraction*

---

## 🎯 Purpose

This manual provides complete step-by-step instructions for reproducing the 3DGS-based time-series plant phenotyping pipeline developed at Mineno Laboratory, Shizuoka University.

!!! success "What You'll Learn"
    - ✅ Complete environment setup (CUDA, COLMAP, 3DGS)
    - ✅ Video processing and frame extraction
    - ✅ Structure-from-Motion reconstruction
    - ✅ 3D Gaussian Splatting training
    - ✅ Quality evaluation and rendering
    - ✅ Plant trait extraction
    - ✅ Time-series growth analysis

---

## 🚀 Quick Start

<div class="grid cards" markdown>

-   :material-rocket-launch:{ .lg .middle } **Quick Start**

    ---

    Get running in 30 minutes

    [:octicons-arrow-right-24: Start now](getting-started/quick-start.md)

-   :material-cog:{ .lg .middle } **Environment Setup**

    ---

    Complete installation guide

    [:octicons-arrow-right-24: Install](environment/intro.md)

-   :material-play-circle:{ .lg .middle } **Run Pipeline**

    ---

    Execute the complete workflow

    [:octicons-arrow-right-24: Execute](pipeline/overview.md)

-   :material-book-open:{ .lg .middle } **My Research**

    ---

    Original contributions & results

    [:octicons-arrow-right-24: View](my-research/overview.md)

</div>

---

## 📊 Pipeline Overview

```mermaid
graph LR
    A[Video Capture<br/>6 cameras, 4K] --> B[Frame Extraction<br/>5fps, ffmpeg]
    B --> C[COLMAP SfM<br/>Feature matching]
    C --> D[3DGS Training<br/>30K iterations]
    D --> E[Novel View<br/>Rendering]
    E --> F[Trait Extraction<br/>Height, canopy]
    F --> G[Growth Analysis<br/>Time-series]
    
    style A fill:#e1f5ff
    style D fill:#ffe1f5
    style G fill:#e1ffe1
```

---

## 🎬 Video Demonstration

### Complete Pipeline Walkthrough

<video controls width="100%" style="border-radius:8px; margin-bottom:1rem;">
  <source src="assets/videos/tutorials/pipeline-overview.mp4" type="video/mp4">
</video>

*Video 1: Complete pipeline execution from video to trait extraction*

---

## 💻 System Requirements

!!! info "Recommended Setup"
    **Operating System:** Ubuntu 22.04 LTS  
    **GPU:** NVIDIA RTX 6000 Ada (48GB VRAM) or equivalent  
    **CUDA:** 12.1 or later  
    **RAM:** 64GB+  
    **Storage:** 2TB+ for full dataset  

See [detailed requirements](getting-started/requirements.md) for minimum specifications.

---

## 🎓 Key Results

This pipeline achieves:

!!! success "Performance Metrics"
    - **PSNR:** 23.84 ± 0.83 dB (reconstruction quality)
    - **Temporal Stability:** CV = 3.5% (excellent consistency)
    - **Height Extraction:** CV = 9.7% (scale-invariant method)
    - **Improvement:** 44.7 percentage points over PLY method

![Results Summary](assets/images/figures/results-summary.png)
*Validated across 22 dates over 50 days*

---

## 📚 Documentation Structure

### For Beginners
- **[Getting Started](getting-started/overview.md)** - Introduction and basic concepts
- **[Environment Setup](environment/intro.md)** - Complete installation guide
- **[Quick Start](getting-started/quick-start.md)** - Get running in 30 minutes

### For Active Users
- **[Pipeline Execution](pipeline/overview.md)** - Complete workflow guide
- **[Parameter Configuration](parameters/recommended.md)** - Optimization tips
- **[Troubleshooting](troubleshooting/common-issues.md)** - Problem solving

### For Researchers
- **[My Research](my-research/overview.md)** - Original contributions
- **[Results & Validation](my-research/results.md)** - Complete experimental results
- **[Publications](my-research/publications.md)** - Papers and presentations

---

## 🔧 Common Use Cases

=== "Single Date Processing"

    ```bash
    # Process one date from start to finish
    ./scripts/run_single_date.sh 20260119
    ```

=== "Multi-Date Analysis"

    ```bash
    # Process multiple dates in batch
    ./scripts/run_batch.sh dates.txt
    ```

=== "Trait Extraction Only"

    ```bash
    # Extract traits from existing models
    python scripts/extract_traits.py --date 20260119
    ```

---

## 📝 Getting Help

!!! question "Need Help?"
    
    **Check these resources:**
    
    1. **[Common Issues](troubleshooting/common-issues.md)** - Known problems and solutions
    2. **[COLMAP Errors](troubleshooting/colmap-errors.md)** - COLMAP-specific issues
    3. **[GPU/Memory](troubleshooting/gpu-memory.md)** - Hardware troubleshooting
    
    **Still stuck?**
    
    Contact: Mineno Laboratory, Shizuoka University  
    Email: zobaer.al.23@shizuoka.ac.jp

---

## 🙏 Acknowledgments

This pipeline was developed as part of greenhouse tomato phenotyping research at Mineno Laboratory, Shizuoka University.

**Author:** Zobaer Al (M2)  
**Supervisor:** Professor Hiroshi Mineno  
**Institution:** Shizuoka University

---

## 📄 Citation

If you use this pipeline in your research, please cite:

```bibtex
@mastersthesis{al2026_3dgs_phenotyping,
  author = {Al, Zobaer},
  title = {3D Gaussian Splatting for Time-Series Greenhouse Tomato Plant Phenotyping},
  school = {Shizuoka University},
  year = {2026},
  type = {Master's Thesis}
}
```

---

**Last updated:** {{ git_revision_date_localized }}
