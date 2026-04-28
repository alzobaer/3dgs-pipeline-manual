# CUDA Installation

Install CUDA 12.4 for GPU acceleration.

## Why CUDA 12.4?

- Required for 3DGS
- Best compatibility with PyTorch
- Tested configuration

## Installation

```bash
# Add CUDA repository
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
sudo apt-get update

# Install CUDA 12.4
sudo apt-get -y install cuda-toolkit-12-4

# Add to PATH
echo 'export PATH=/usr/local/cuda-12.4/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-12.4/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc
```

## Verification

```bash
nvcc --version
# Should show: release 12.4

nvidia-smi
# Should show your GPU
```

Next: [Python Environment](python.md)
