# 3D Gaussian Splatting Installation

Install the 3DGS framework.

## Clone Repository

```bash
git clone https://github.com/graphdeco-inria/gaussian-splatting.git
cd gaussian-splatting
```

## Activate Environment

```bash
conda activate 3dgs
```

## Install Dependencies

```bash
pip install -r requirements.txt --no-build-isolation
```

## Build Submodules

```bash
# Fix cstdint error first
find submodules -name "*.h" -o -name "*.cu" | xargs grep -l "uint32_t\|int32_t" | \
    xargs sed -i '1i#include <cstdint>'

# Build
pip install submodules/diff-gaussian-rasterization --no-build-isolation
pip install submodules/simple-knn --no-build-isolation
```

## Verify

```bash
python train.py --help
```

Next: [Verification](verify.md)
