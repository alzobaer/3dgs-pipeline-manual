# System Requirements

Hardware and software requirements for the 3DGS pipeline.

---

## Minimum Requirements

### Hardware

| Component | Minimum | Recommended | Notes |
|-----------|---------|-------------|-------|
| **CPU** | 4 cores | 8+ cores | Intel/AMD x86_64 |
| **RAM** | 16 GB | 32 GB+ | More for large datasets |
| **GPU** | NVIDIA GTX 1080 (8GB) | RTX 3090/4090/6000 Ada | CUDA required |
| **VRAM** | 8 GB | 24-48 GB | 48GB for 4K @ 5fps |
| **Storage** | 100 GB | 1 TB+ | SSD recommended |
| **Network** | 10 Mbps | 100+ Mbps | For downloads |

### Software

| Software | Version | Purpose |
|----------|---------|---------|
| **OS** | Ubuntu 22.04+ | Linux required |
| **CUDA** | 12.4 | GPU acceleration |
| **Python** | 3.10+ | Programming environment |
| **Git** | 2.0+ | Version control |
| **FFmpeg** | 4.0+ | Video processing |

---

## Tested Configuration

**Our Validated Setup:**

```
Server: DNN19 (Mineno Laboratory)
CPU: Intel Xeon (multiple cores)
RAM: 128 GB
GPU: NVIDIA RTX 6000 Ada (48 GB VRAM)
CUDA: 12.4
OS: Ubuntu 22.04 LTS
Storage: 10 TB HDD
```

**Results:**
- PSNR: 23.71 dB
- Training time: ~18-30 min per date
- Success rate: 100% (22/22 dates)

---

## GPU Requirements

### Why NVIDIA GPU?

CUDA acceleration is **essential** for:
- COLMAP feature extraction (10-100x faster)
- 3DGS training (required)
- Rendering (significantly faster)

### VRAM Requirements by Resolution

| Resolution | Frames (5fps) | VRAM Needed | Example GPU |
|------------|---------------|-------------|-------------|
| 1080p | ~329 | 8 GB | GTX 1080 |
| 2K | ~329 | 12 GB | RTX 3060 |
| 4K | ~329 | 24 GB | RTX 3090 |
| **4K (our setup)** | **~329** | **48 GB** | **RTX 6000 Ada** |

!!! warning "VRAM Limitation"
    If you get OOM (Out of Memory) errors:
    - Reduce frame rate (5fps → 3fps)
    - Downscale resolution (4K → 2K)
    - Use fewer frames

---

## Storage Requirements

### Per Dataset

**For one capture date (Condition 1, 5fps, 4K):**

| Component | Size | Cumulative |
|-----------|------|------------|
| Raw video | ~200 MB | 200 MB |
| Extracted frames | ~1.5 GB | 1.7 GB |
| COLMAP sparse | ~500 MB | 2.2 GB |
| 3DGS model | ~200 MB | 2.4 GB |
| Rendered images | ~2 GB | 4.4 GB |
| **Total** | **~5 GB** | **5 GB** |

**For 22 dates:** ~110 GB

**Recommended:** 500 GB - 1 TB for working space

---

## Network Requirements

### Download Sizes

| Item | Size | Time @ 100 Mbps |
|------|------|-----------------|
| CUDA Toolkit | ~3 GB | ~4 min |
| COLMAP source | ~50 MB | ~5 sec |
| 3DGS repo | ~100 MB | ~10 sec |
| PyTorch + deps | ~2 GB | ~3 min |
| **Total** | **~5 GB** | **~10 min** |

---

## Operating System

### Supported

✅ **Ubuntu 22.04 LTS** (recommended, tested)  
✅ Ubuntu 20.04 LTS (should work)  
✅ Ubuntu 24.04 LTS (should work)  
✅ Other Debian-based (may work)

### Not Supported

❌ Windows (WSL2 may work but untested)  
❌ macOS (no CUDA support)  
❌ Other Linux distros (not tested)

!!! tip "Why Ubuntu?"
    - Best CUDA support
    - Stable package ecosystem
    - Wide community support
    - Used in our lab

---

## Software Dependencies

### Required

```bash
# System packages
build-essential, cmake, git
libboost-all-dev, libeigen3-dev
libsuitesparse-dev, libfreeimage-dev
libgoogle-glog-dev, libgflags-dev
libglew-dev, qtbase5-dev

# Python packages
torch, torchvision (with CUDA)
numpy, pillow, tqdm
plyfile, opencv-python

# Tools
ffmpeg, conda/mamba
```

### Optional

```bash
# For visualization
meshlab, cloudcompare

# For analysis
matplotlib, pandas, scipy

# For development
jupyter, ipython
```

---

## Compatibility Check

### Quick Test

Run these commands to verify:

```bash
# Check Ubuntu version
lsb_release -a
# Should show: Ubuntu 22.04

# Check GPU
nvidia-smi
# Should show: Your GPU model

# Check CUDA capability
nvidia-smi --query-gpu=compute_cap --format=csv
# Should show: ≥7.0 (Volta or newer)

# Check disk space
df -h
# Should show: ≥100 GB free

# Check RAM
free -h
# Should show: ≥16 GB
```

---

## Performance Expectations

### Training Time

| GPU | VRAM | Time (30K iter) | Cost |
|-----|------|-----------------|------|
| RTX 4090 | 24 GB | ~20 min | $1,600 |
| RTX 3090 | 24 GB | ~30 min | $1,000 |
| RTX 6000 Ada | 48 GB | ~18 min | $6,800 |
| A100 | 40 GB | ~15 min | $10,000 |

### COLMAP Time

| Resolution | Frames | Time (feature) | Time (mapper) |
|------------|--------|----------------|---------------|
| 1080p | ~329 | ~5 min | ~10 min |
| 2K | ~329 | ~10 min | ~20 min |
| 4K | ~329 | ~20 min | ~40 min |

---

## Upgrade Recommendations

### If You Have 8 GB VRAM

**Options:**
1. Reduce resolution: 4K → 2K or 1080p
2. Reduce frame rate: 5fps → 3fps
3. Use fewer frames: Select best 200 frames

### If You Have 16 GB RAM

**Should work but:**
- Close other applications
- Monitor memory usage
- Consider 32 GB upgrade

### If You Have Slow Storage

**Impacts:**
- Frame extraction slower
- COLMAP I/O bottleneck
- Consider SSD upgrade

---

## Cloud Alternatives

Don't have the hardware?

### Google Colab
- **GPU:** Tesla T4 (16 GB) or A100 (40 GB)
- **Cost:** Free tier or $10/month Pro
- **Limits:** Session timeouts, storage limits

### AWS EC2
- **Instance:** p3.2xlarge (V100 16GB)
- **Cost:** ~$3/hour
- **Benefits:** Full control, persistent storage

### Paperspace
- **GPU:** Various options
- **Cost:** $0.50-$2/hour
- **Benefits:** Pre-configured ML environments

!!! note "Cloud Considerations"
    - Data upload/download time
    - Session management
    - Cost for long training
    - Storage fees

---

## Verification Checklist

Before proceeding to installation:

- [ ] Ubuntu 22.04 LTS installed
- [ ] NVIDIA GPU with CUDA support (≥8 GB VRAM)
- [ ] At least 16 GB RAM (32 GB+ preferred)
- [ ] At least 100 GB free disk space
- [ ] Internet connection available
- [ ] Sudo/admin access to system

---

## Next Steps

**Hardware ready?**

→ [Quick Start Guide](quick-start.md) - Install everything in 30 minutes

**Need help?**

→ [Troubleshooting](../troubleshooting/common-issues.md) - Common hardware issues

---

*Hardware specifications based on DNN19 server configuration and testing with 22-date greenhouse dataset.*
