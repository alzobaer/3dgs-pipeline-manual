# GPU & Memory Issues

GPU and memory management.

## Monitor GPU Usage

```bash
watch -n 1 nvidia-smi
```

## Out of Memory Solutions

### Reduce Data Size

| Method | Command | VRAM Saved |
|--------|---------|------------|
| Lower FPS | `fps=3` instead of `fps=5` | ~30% |
| Downscale | `scale=1920:1080` | ~75% |
| Fewer frames | Select best 200 | Variable |

### Optimize Memory

```bash
# PyTorch memory settings
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

# Clear cache
python -c "import torch; torch.cuda.empty_cache()"
```

## VRAM Requirements

| Resolution | FPS | Frames | VRAM Needed |
|------------|-----|--------|-------------|
| 4K | 5 | ~329 | 48 GB |
| 4K | 3 | ~197 | 24 GB |
| 2K | 5 | ~329 | 12 GB |
| 1080p | 5 | ~329 | 8 GB |
