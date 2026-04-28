# Common Issues

Frequently encountered problems and solutions.

## CUDA Issues

### Issue: Version Mismatch
```bash
# Solution
pip uninstall torch torchvision
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
```

## COLMAP Issues

### Issue: SIGSEGV Segfault
```bash
# Solution: Limit BA iterations
--Mapper.ba_global_max_num_iterations 20
```

### Issue: sparse/0 Not Found
```bash
# Solution: Create and copy
mkdir -p sparse/0
cp sparse/*.bin sparse/0/
```

## 3DGS Issues

### Issue: Out of Memory
```bash
# Solution 1: Reduce FPS
ffmpeg -i video.mp4 -vf "fps=3" ...

# Solution 2: Downscale
ffmpeg -i video.mp4 -vf "fps=5,scale=1920:1080" ...
```

### Issue: Module Not Found
```bash
# Solution: Use --no-build-isolation
pip install submodules/diff-gaussian-rasterization --no-build-isolation
```

See specialized pages for more details.
