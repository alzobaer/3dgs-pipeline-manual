# GPU・メモリの問題

GPUとメモリの管理方法。

---

## GPU使用量の監視

```bash
watch -n 1 nvidia-smi
```

---

## メモリ不足の解決策

### データサイズの削減

| 方法 | コマンド | 節約VRAM |
|-----|--------|-------|
| FPSを下げる | `fps=3`（5fpsの代わりに） | 約30% |
| 解像度を下げる | `scale=1920:1080` | 約75% |
| フレーム数を減らす | 最良の200フレームを選択 | 状況による |

### メモリの最適化

```bash
# PyTorchメモリ設定
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

# キャッシュのクリア
python -c "import torch; torch.cuda.empty_cache()"
```

---

## 解像度・FPS別VRAM要件

| 解像度 | FPS | フレーム数 | 必要VRAM |
|-----|---|------|------|
| 4K | 5 | 約329枚 | 48 GB |
| 4K | 3 | 約197枚 | 24 GB |
| 2K | 5 | 約329枚 | 12 GB |
| 1080p | 5 | 約329枚 | 8 GB |
