# CUDAのインストール

GPUアクセラレーション用のCUDA 12.4をインストールします。

---

## なぜCUDA 12.4か？

- 3DGSに必要
- PyTorchとの最高の互換性
- 検証済みの構成

---

## インストール手順

```bash
# CUDAリポジトリの追加
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
sudo apt-get update

# CUDA 12.4のインストール
sudo apt-get -y install cuda-toolkit-12-4

# PATHへの追加
echo 'export PATH=/usr/local/cuda-12.4/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-12.4/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc
```

---

## 動作確認

```bash
nvcc --version
# 表示されるべき内容：release 12.4

nvidia-smi
# 表示されるべき内容：GPUの情報
```

次：[Python環境](python.md)
