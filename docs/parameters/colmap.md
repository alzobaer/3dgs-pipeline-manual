# COLMAP Parameters

Optimal COLMAP settings.

## Critical Parameters

```bash
--ImageReader.single_camera 1  # One camera model
--ImageReader.camera_model PINHOLE  # Camera type
--Mapper.ba_global_max_num_iterations 20  # Prevent crash
--Mapper.max_num_models 1  # Single reconstruction
```

## Why These Settings?

- **single_camera=1**: All frames from same camera
- **BA iterations=20**: Prevents SIGSEGV error
- **exhaustive_matcher**: Best for fixed viewpoint
