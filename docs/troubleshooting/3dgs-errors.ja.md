# 3DGSエラー

3D Gaussian Splatting のトラブルシューティング。

---

## FileNotFoundError：sparse/0/images.bin

**原因：** COLMAP出力が期待される場所にない

**解決策：**
```bash
mkdir -p sparse/0
cp sparse/*.bin sparse/0/
```

---

## CUDA メモリ不足

**解決策：**

1. フレーム数を減らす：
```bash
ffmpeg -i video.mp4 -vf "fps=3" ...
```

2. 解像度を下げる：
```bash
ffmpeg -i video.mp4 -vf "fps=5,scale=1920:1080" ...
```

3. メモリ設定を行う：
```bash
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
```

---

## cstdint コンパイルエラー

**原因：** ラスタライザにヘッダが不足

**解決策：**
```bash
# rasterizer_impl.h の先頭に追加：
#include <cstdint>
```
