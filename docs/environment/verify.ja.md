# 環境の動作確認

全コンポーネントが正しくインストールされているか確認します。

---

## チェックリスト

各コマンドを実行し、出力を確認してください：

### CUDA
```bash
nvcc --version
# ✅ 表示されるべき内容：release 12.4
```

### GPU
```bash
nvidia-smi
# ✅ 表示されるべき内容：GPUの情報とCUDA 12.4
```

### Python
```bash
python --version
# ✅ 表示されるべき内容：Python 3.10.x
```

### PyTorch
```bash
python -c "import torch; print(torch.__version__, torch.cuda.is_available())"
# ✅ 表示されるべき内容：2.x.x+cu124 True
```

### COLMAP
```bash
colmap -h
# ✅ 表示されるべき内容：ヘルプメッセージ
```

### 3DGS
```bash
cd ~/gaussian-splatting
python train.py --help
# ✅ 表示されるべき内容：学習オプション
```

---

## 全て確認できたら？

→ [データ準備](../data-prep/video-requirements.md)へ進む

## 問題が発生した場合

→ [トラブルシューティング](../troubleshooting/common-issues.md)を確認する
