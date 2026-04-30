# COLMAPエラー

COLMAP固有のトラブルシューティング。

---

## セグメンテーションフォルト

**原因：** バンドル調整のオーバーフロー

**解決策：**
```bash
--Mapper.ba_global_max_num_iterations 20
--Mapper.max_num_models 1
```

---

## 1426枚中2枚しか登録されない

**原因：** 動画の種類に対して不適切なマッチャー

**解決策：** 固定視点には exhaustive_matcher を使用：
```bash
colmap exhaustive_matcher --database_path database.db
```

---

## フラグが認識されない

**旧：** `--SiftExtraction.use_gpu`  
**新：** `--FeatureExtraction.use_gpu=1`

COLMAP v3.14以降でフラグ名が変更されました。
