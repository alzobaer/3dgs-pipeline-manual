# Quick Start

Get your 3DGS pipeline running in 30 minutes.

---

## Prerequisites

Before starting, ensure you have:

- **Operating System:** Ubuntu 22.04 LTS or later
- **GPU:** NVIDIA GPU with CUDA support (RTX 6000 Ada or equivalent recommended)
- **Storage:** At least 100 GB free space
- **Memory:** 32 GB RAM minimum (64 GB+ recommended)
- **Internet:** For downloading dependencies

---

## Step 1: Install CUDA (5 minutes)

CUDA 12.4 is required for this pipeline.

```bash
# Download and install CUDA 12.4
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
sudo apt-get update
sudo apt-get -y install cuda-toolkit-12-4

# Verify installation
nvcc --version
nvidia-smi
```

**Expected output:** CUDA version 12.4 and your GPU information

---

## Step 2: Install COLMAP (5 minutes)

COLMAP is used for Structure-from-Motion reconstruction.

```bash
# Install dependencies
sudo apt-get update
sudo apt-get install -y \
    git \
    cmake \
    build-essential \
    libboost-all-dev \
    libeigen3-dev \
    libsuitesparse-dev \
    libfreeimage-dev \
    libgoogle-glog-dev \
    libgflags-dev \
    libglew-dev \
    qtbase5-dev \
    libqt5opengl5-dev

# Clone and build COLMAP
git clone https://github.com/colmap/colmap.git
cd colmap
mkdir build
cd build
cmake .. -DCMAKE_CUDA_ARCHITECTURES=native
make -j$(nproc)
sudo make install

# Verify installation
colmap -h
```

**Expected output:** COLMAP help message

---

## Step 3: Install 3D Gaussian Splatting (10 minutes)

Clone and set up the 3DGS repository.

```bash
# Clone repository
git clone https://github.com/graphdeco-inria/gaussian-splatting.git
cd gaussian-splatting

# Create conda environment
conda create -n 3dgs python=3.10 -y
conda activate 3dgs

# Install PyTorch with CUDA 12.4 support
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124

# Install dependencies (with fix for cstdint error)
pip install -r requirements.txt --no-build-isolation

# Build submodules
pip install submodules/diff-gaussian-rasterization --no-build-isolation
pip install submodules/simple-knn --no-build-isolation

# Verify installation
python -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA available: {torch.cuda.is_available()}')"
```

**Expected output:** 
```
PyTorch: 2.x.x+cu124
CUDA available: True
```

---

## Step 4: Install FFmpeg (2 minutes)

FFmpeg is needed for video frame extraction.

```bash
sudo apt-get install -y ffmpeg

# Verify installation
ffmpeg -version
```

---

## Step 5: Test with Sample Data (5 minutes)

Run a quick test to verify everything works.

### Download Test Video

```bash
# Create test directory
mkdir -p ~/3dgs-test
cd ~/3dgs-test

# If you have a test video, place it here
# Otherwise, we'll create test data in the next step
```

### Extract Frames

```bash
# Extract frames at 5fps
ffmpeg -i your_video.mp4 -vf "fps=5" -qscale:v 2 frames/frame_%04d.jpg

# Verify frames extracted
ls frames/ | wc -l
# Should show ~329 frames for 60-second video
```

### Run COLMAP

```bash
# Create output directory
mkdir -p colmap_output

# Run COLMAP feature extraction
colmap feature_extractor \
    --database_path colmap_output/database.db \
    --image_path frames/ \
    --ImageReader.single_camera 1 \
    --ImageReader.camera_model PINHOLE \
    --SiftExtraction.use_gpu 1

# Run COLMAP exhaustive matcher
colmap exhaustive_matcher \
    --database_path colmap_output/database.db \
    --SiftMatching.use_gpu 1

# Run COLMAP mapper
mkdir -p colmap_output/sparse
colmap mapper \
    --database_path colmap_output/database.db \
    --image_path frames/ \
    --output_path colmap_output/sparse \
    --Mapper.ba_global_max_num_iterations 20 \
    --Mapper.max_num_models 1
```

### Run 3DGS Training

```bash
# Activate conda environment
conda activate 3dgs

# Set memory configuration
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

# Run training
cd ~/gaussian-splatting
python train.py \
    -s ~/3dgs-test \
    -m ~/3dgs-test/output \
    --iterations 30000

# Training will take ~18-30 minutes
```

### Check Results

```bash
# View output
ls ~/3dgs-test/output/point_cloud/iteration_30000/

# Should see: point_cloud.ply
```

---

## Expected Results

After completing these steps, you should have:

✅ CUDA 12.4 installed and working  
✅ COLMAP installed and functional  
✅ 3DGS environment set up  
✅ FFmpeg ready for frame extraction  
✅ Test reconstruction completed  

**Quality Metrics (for our dataset):**
- PSNR: ~23.80 dB (good)
- Training time: ~18-30 minutes
- File size: ~200 MB (point cloud)

---

## Common Issues

### Issue 1: CUDA Version Mismatch

**Problem:** PyTorch shows different CUDA version

**Solution:**
```bash
pip uninstall torch torchvision
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
```

### Issue 2: COLMAP Segmentation Fault

**Problem:** COLMAP crashes during mapper

**Solution:**
```bash
# Limit bundle adjustment iterations
--Mapper.ba_global_max_num_iterations 20
--Mapper.max_num_models 1
```

### Issue 3: Out of Memory (OOM)

**Problem:** GPU runs out of memory

**Solution:**
```bash
# Reduce frame rate (fewer frames)
ffmpeg -i video.mp4 -vf "fps=3" ...  # Use 3fps instead of 5fps

# Or downscale resolution
ffmpeg -i video.mp4 -vf "fps=5,scale=1920:1080" ...  # Use 1080p instead of 4K
```

### Issue 4: Module Not Found Error

**Problem:** Python can't find submodules

**Solution:**
```bash
# Use --no-build-isolation flag
pip install submodules/diff-gaussian-rasterization --no-build-isolation
pip install submodules/simple-knn --no-build-isolation
```

---

## Next Steps

Now that your environment is set up:

1. **[Process Your Own Data](../data-prep/video-requirements.md)** - Capture and prepare videos
2. **[Run Complete Pipeline](../pipeline/overview.md)** - Execute full workflow
3. **[View My Research](../my-research/contributions.md)** - See results and methods
4. **[Troubleshooting](../troubleshooting/common-issues.md)** - Fix common problems

---

## Verification Checklist

Before proceeding to full pipeline:

- [ ] CUDA 12.4 installed (`nvcc --version`)
- [ ] GPU detected (`nvidia-smi`)
- [ ] COLMAP working (`colmap -h`)
- [ ] Conda environment created (`conda activate 3dgs`)
- [ ] PyTorch with CUDA (`python -c "import torch; print(torch.cuda.is_available())"`)
- [ ] FFmpeg installed (`ffmpeg -version`)
- [ ] Test reconstruction completed
- [ ] Point cloud generated

---

**Estimated Time:** 30 minutes total  
**Difficulty:** Intermediate  
**Prerequisites:** Basic Linux command line knowledge

---

*Need help? Check the [Troubleshooting Guide](../troubleshooting/common-issues.md) or contact the lab.*
