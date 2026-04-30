# COLMAPのインストール

Structure-from-Motion用のCOLMAPをインストールします。

---

## クイックインストール（Ubuntu）

```bash
sudo apt-get install -y colmap
```

---

## ソースからビルド（最新版）

```bash
# 依存パッケージのインストール
sudo apt-get install -y \
    git cmake build-essential \
    libboost-all-dev libeigen3-dev \
    libsuitesparse-dev libfreeimage-dev \
    libgoogle-glog-dev libgflags-dev \
    libglew-dev qtbase5-dev

# クローン
git clone https://github.com/colmap/colmap.git
cd colmap
mkdir build && cd build

# ビルド
cmake .. -DCMAKE_CUDA_ARCHITECTURES=native
make -j$(nproc)
sudo make install
```

---

## 動作確認

```bash
colmap -h
```

次：[3DGSのインストール](3dgs.md)
