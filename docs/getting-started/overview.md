# Getting Started

Welcome to the 3D Gaussian Splatting pipeline for time-series plant phenotyping!

---

## What You'll Learn

This manual will guide you through:

✅ **Complete environment setup** - CUDA, COLMAP, 3DGS  
✅ **Video capture and processing** - Best practices for data collection  
✅ **Pipeline execution** - Step-by-step reconstruction workflow  
✅ **Quality evaluation** - Metrics and validation  
✅ **Trait extraction** - Automated plant measurement  

---

## Who This Manual Is For

### Beginners
New to 3D reconstruction? Start here:
1. [System Requirements](requirements.md) - Check if your hardware is compatible
2. [Quick Start](quick-start.md) - Get running in 30 minutes
3. [Video Requirements](../data-prep/video-requirements.md) - Learn data capture

### Active Users
Already familiar with the basics?
1. [Pipeline Overview](../pipeline/overview.md) - Understand the workflow
2. [Dataset Details](../data-prep/dataset.md) - See our validated configuration
3. [Troubleshooting](../troubleshooting/common-issues.md) - Fix common issues

### Researchers
Looking for technical details?
1. [My Research](../my-research/contributions.md) - Original contributions
2. [Parameters](../parameters/recommended.md) - Optimal settings
3. [Results & Validation](../my-research/results.md) - Quality metrics

---

## Prerequisites

Before starting, you should have:

- **Basic Linux knowledge** - Command line familiarity
- **Python experience** - Basic understanding preferred
- **NVIDIA GPU** - Required for CUDA acceleration
- **Time commitment** - 2-3 hours for initial setup

---

## Learning Path

### Path 1: Quick Setup (30 minutes)
Perfect for getting started quickly:
```
Quick Start → Test Run → Verify Results
```

### Path 2: Complete Setup (2-3 hours)
Comprehensive installation and testing:
```
System Requirements → Environment Setup → 
Data Preparation → Pipeline Execution
```

### Path 3: Research Focus (1 week)
Deep dive into methods and optimization:
```
Complete Setup → My Research → 
Parameters → Advanced Topics
```

---

## Pipeline at a Glance

<video controls width="100%" style="border-radius:8px; margin-bottom:1rem;">
  <source src="../assets/videos/tutorials/pipeline-overview.mp4" type="video/mp4">
</video>
*Animated walkthrough of all 6 pipeline stages with real data thumbnails*

---

## What Makes This Different?

This pipeline is **validated on real greenhouse data**:

- ✅ **22 capture dates** over 50 days
- ✅ **PSNR: 23.80 dB** - High quality reconstruction
- ✅ **100% success rate** - Robust pipeline
- ✅ **Scale-invariant measurement** - 44.7pp improvement over traditional methods

---

## Quick Links

| Task | Link |
|------|------|
| Install everything | [Quick Start](quick-start.md) |
| Check requirements | [System Requirements](requirements.md) |
| Capture videos | [Video Requirements](../data-prep/video-requirements.md) |
| Run pipeline | [Pipeline Overview](../pipeline/overview.md) |
| Fix problems | [Troubleshooting](../troubleshooting/common-issues.md) |
| See results | [My Research](../my-research/contributions.md) |

---

## Support

Need help?

- **Common Issues:** Check [Troubleshooting Guide](../troubleshooting/common-issues.md)
- **Lab Support:** Contact Mineno Laboratory
- **Documentation:** Browse this manual
- **Feedback:** Submit via GitHub issues

---

## Next Steps

Ready to begin?

1. **[Check System Requirements](requirements.md)** - Verify hardware compatibility
2. **[Quick Start Guide](quick-start.md)** - Install and test (30 min)
3. **[Capture Your Data](../data-prep/video-requirements.md)** - Learn best practices

---

*Last updated: April 14, 2026*
