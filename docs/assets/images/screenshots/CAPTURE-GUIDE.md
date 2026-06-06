# Screenshot Capture Guide

Save all screenshots to this folder: docs/assets/images/screenshots/

## Filenames to capture (in order)

| Filename | What to capture | Which page uses it |
|---|---|---|
| 01-input-video-frame.png | Single 4K frame from raw plant video | pipeline/video-processing |
| 02-ffmpeg-terminal.png | ffmpeg running frame extraction | pipeline/video-processing, data-prep/frame-extraction |
| 03-frames-folder.png | File browser showing extracted frames | pipeline/video-processing, data-prep/frame-extraction |
| 04-frame-quality-check.png | Good frame vs blurry frame side-by-side | pipeline/video-processing |
| 05-batch-extraction.png | Batch script running for multiple dates | pipeline/video-processing, data-prep/frame-extraction |
| 06-colmap-feature-extraction.png | COLMAP feature extractor terminal | pipeline/colmap-sfm |
| 07-colmap-matching.png | COLMAP exhaustive matching progress | pipeline/colmap-sfm |
| 08-colmap-mapper.png | COLMAP mapper terminal output | pipeline/colmap-sfm |
| 09-colmap-sparse-cloud.png | COLMAP GUI sparse point cloud + cameras | pipeline/colmap-sfm |
| 10-colmap-cloud-closeup.png | Close-up of sparse plant reconstruction | pipeline/colmap-sfm |
| 11-colmap-output-files.png | ls sparse/0/ showing .bin files | pipeline/colmap-sfm |
| 12-nvidia-smi-pretrain.png | nvidia-smi output before training | pipeline/3dgs-training |
| 13-3dgs-training-terminal.png | Training terminal with loss/PSNR metrics | pipeline/3dgs-training |
| 14-sibr-early.png | SIBR viewer at ~1000 iterations | pipeline/3dgs-training |
| 15-sibr-complete.png | SIBR viewer at 30000 iterations | pipeline/3dgs-training |
| 16-pointcloud-output.png | ls -lh showing point_cloud.ply size | pipeline/3dgs-training |
| 17-render-terminal.png | render.py running in terminal | pipeline/rendering |
| 18-render-output-folder.png | Output directory with train/ test/ folders | pipeline/rendering |
| 19-gt-vs-render.png | Ground truth vs rendered image side-by-side | pipeline/rendering |
| 20-metrics-output.png | metrics.py PSNR/SSIM/LPIPS output | pipeline/rendering |
| 21-segmentation-mask.png | Rendered image + binary plant mask | pipeline/trait-extraction |
| 22-height-measurement-overlay.png | Plant image with height ruler overlay | pipeline/trait-extraction |
| 23-trait-extraction-output.png | compute_heights_rendered.py terminal output with CV | pipeline/trait-extraction |
| 24-cv-comparison-chart.png | Bar chart: 9.8% vs 28.0% CV | pipeline/trait-extraction |
| 25-good-vs-bad-frame.png | Good frame vs bad frame comparison | data-prep/video-requirements |
| 26-frame-quality-samples.png | 3 sample frames at 25/50/75% video | data-prep/frame-extraction |
| 27-directory-structure.png | File browser showing complete date folder | data-prep/directory-structure |
| 28-multidate-structure.png | data/ directory with all 22 date folders | data-prep/directory-structure |
| 29-initial-setup.png | ls output after initial directory setup | data-prep/directory-structure |
