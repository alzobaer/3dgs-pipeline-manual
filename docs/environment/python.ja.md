# Python環境の構築

パイプライン用のPythonおよびConda環境をセットアップします。

---

## Minicondaのインストール

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b
~/miniconda3/bin/conda init bash
source ~/.bashrc
```

---

## conda環境の作成

```bash
conda create -n 3dgs python=3.10 -y
conda activate 3dgs
```

---

## PyTorchのインストール

```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
```

---

## 動作確認

```bash
python -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA: {torch.cuda.is_available()}')"
```

次：[COLMAPのインストール](colmap.md)
