# Recommended Settings

Our validated configuration (PSNR: 23.80 dB).

## Complete Pipeline

| Stage | Parameter | Value |
|-------|-----------|-------|
| Video | Input condition | Condition 1 (fixed) |
| Frames | FPS | 5 fps |
| Frames | Quality | qscale:v 2 |
| COLMAP | Camera model | single_camera=1 |
| COLMAP | Matcher | exhaustive |
| COLMAP | BA iterations | 20 (max) |
| 3DGS | Iterations | 30,000 |
| 3DGS | Resolution | Full 4K |

See [Dataset Details](../data-prep/dataset.md) for full configuration.
