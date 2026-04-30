# COLMAPパラメータ

最適なCOLMAP設定。

---

## 重要なパラメータ

```bash
--ImageReader.single_camera 1          # 単一カメラモデル
--ImageReader.camera_model PINHOLE     # カメラの種類
--Mapper.ba_global_max_num_iterations 20  # クラッシュ防止
--Mapper.max_num_models 1              # 単一再構成
```

---

## なぜこれらの設定か？

- **single_camera=1：** 全フレームが同一カメラから撮影
- **BA iterations=20：** SIGSEGVエラーを防止
- **exhaustive_matcher：** 固定視点に最適
