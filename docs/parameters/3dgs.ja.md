# 3DGSパラメータ

最適な学習設定。

---

## 主要パラメータ

```bash
--iterations 30000  # 完全な収束まで学習
--resolution -1     # フル解像度（4K）を使用
```

---

## メモリ設定

```bash
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
```

OOMによるメモリ断片化を防止します。
