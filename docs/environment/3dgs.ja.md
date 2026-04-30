# 3D Gaussian Splattingのインストール

3DGSフレームワークをインストールします。

---

## リポジトリのクローン

```bash
git clone https://github.com/graphdeco-inria/gaussian-splatting.git
cd gaussian-splatting
```

---

## conda環境の有効化

```bash
conda activate 3dgs
```

---

## 依存パッケージのインストール

```bash
pip install -r requirements.txt --no-build-isolation
```

---

## サブモジュールのビルド

```bash
# cstdintエラーの修正
find submodules -name "*.h" -o -name "*.cu" | xargs grep -l "uint32_t\|int32_t" | \
    xargs sed -i '1i#include <cstdint>'

# ビルド
pip install submodules/diff-gaussian-rasterization --no-build-isolation
pip install submodules/simple-knn --no-build-isolation
```

---

## 動作確認

```bash
python train.py --help
```

次：[動作確認](verify.md)
