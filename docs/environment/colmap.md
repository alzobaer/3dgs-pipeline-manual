# COLMAP Installation

Install COLMAP for Structure-from-Motion.

## Quick Install (Ubuntu)

```bash
sudo apt-get install -y colmap
```

## Build from Source (Latest)

```bash
# Install dependencies
sudo apt-get install -y \
    git cmake build-essential \
    libboost-all-dev libeigen3-dev \
    libsuitesparse-dev libfreeimage-dev \
    libgoogle-glog-dev libgflags-dev \
    libglew-dev qtbase5-dev

# Clone
git clone https://github.com/colmap/colmap.git
cd colmap
mkdir build && cd build

# Build
cmake .. -DCMAKE_CUDA_ARCHITECTURES=native
make -j$(nproc)
sudo make install
```

## Verify

```bash
colmap -h
```

Next: [3DGS Installation](3dgs.md)
