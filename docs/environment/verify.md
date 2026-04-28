# Environment Verification

Verify all components are installed correctly.

## Checklist

Run each command and verify output:

### CUDA
```bash
nvcc --version
# ✅ Should show: release 12.4
```

### GPU
```bash
nvidia-smi
# ✅ Should show your GPU and CUDA 12.4
```

### Python
```bash
python --version
# ✅ Should show: Python 3.10.x
```

### PyTorch
```bash
python -c "import torch; print(torch.__version__, torch.cuda.is_available())"
# ✅ Should show: 2.x.x+cu124 True
```

### COLMAP
```bash
colmap -h
# ✅ Should show help message
```

### 3DGS
```bash
cd ~/gaussian-splatting
python train.py --help
# ✅ Should show training options
```

## All Green?

→ Ready for [Data Preparation](../data-prep/video-requirements.md)

## Issues?

→ Check [Troubleshooting](../troubleshooting/common-issues.md)
