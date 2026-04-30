# よくある問題

頻繁に発生する問題と解決策。

---

## CUDAの問題

### 問題：バージョンの不一致
```bash
# 解決策
pip uninstall torch torchvision
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124
```

---

## COLMAPの問題

### 問題：SIGSEGV セグメンテーションフォルト
```bash
# 解決策：BAイテレーションを制限
--Mapper.ba_global_max_num_iterations 20
```

### 問題：sparse/0 が見つからない
```bash
# 解決策
mkdir -p sparse/0
cp sparse/*.bin sparse/0/
```

---

## 3DGSの問題

### 問題：メモリ不足（OOM）
```bash
# 解決策1：フレームレートを下げる
ffmpeg -i video.mp4 -vf "fps=3" ...

# 解決策2：解像度を下げる
ffmpeg -i video.mp4 -vf "fps=5,scale=1920:1080" ...
```

### 問題：モジュールが見つからない
```bash
# 解決策：--no-build-isolation を使用
pip install submodules/diff-gaussian-rasterization --no-build-isolation
```

詳細は各専用ページを参照してください。
