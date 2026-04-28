# Python Environment Setup

Set up Python and Conda for the pipeline.

## Install Miniconda

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b
~/miniconda3/bin/conda init bash
source ~/.bashrc
```

## Create Environment

```bash
conda create -n 3dgs python=3.10 -y
conda activate 3dgs
```

## Install PyTorch

```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
```

## Verify

```bash
python -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA: {torch.cuda.is_available()}')"
```

Next: [COLMAP Installation](colmap.md)
