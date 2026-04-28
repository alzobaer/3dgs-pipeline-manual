# COLMAP Errors

COLMAP-specific troubleshooting.

## Segmentation Fault

**Cause:** Bundle adjustment overflow

**Solution:**
```bash
--Mapper.ba_global_max_num_iterations 20
--Mapper.max_num_models 1
```

## Only 2/1426 Images Registered

**Cause:** Wrong matcher for video type

**Solution:** Use exhaustive_matcher for fixed viewpoint:
```bash
colmap exhaustive_matcher --database_path database.db
```

## Feature Extraction Flag Not Recognized

**Old:** `--SiftExtraction.use_gpu`  
**New:** `--FeatureExtraction.use_gpu=1`

COLMAP v3.14+ changed flag names.
