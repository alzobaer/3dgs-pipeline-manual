# 3DGS Errors

3D Gaussian Splatting troubleshooting.

## FileNotFoundError: sparse/0/images.bin

**Cause:** COLMAP output not in expected location

**Solution:**
```bash
mkdir -p sparse/0
cp sparse/*.bin sparse/0/
```

## CUDA Out of Memory

**Solutions:**

1. Reduce frames:
```bash
ffmpeg -i video.mp4 -vf "fps=3" ...
```

2. Downscale:
```bash
ffmpeg -i video.mp4 -vf "fps=5,scale=1920:1080" ...
```

3. Set memory config:
```bash
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
```

## cstdint Compile Error

**Cause:** Missing header in rasterizer

**Solution:**
```bash
# Add to rasterizer_impl.h:
#include <cstdint>
```
