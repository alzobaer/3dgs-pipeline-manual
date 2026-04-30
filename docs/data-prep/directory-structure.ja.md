# ディレクトリ構造

3DGSパイプライン用のデータ整理方法を説明します。

---

## 必要な構造

```
data/
└── 20260119/                    ← 日付フォルダ（YYYYMMDD形式）
    ├── video.mp4                ← 入力動画
    ├── frames/                  ← 抽出したJPEGフレーム（Stage 1出力）
    │   ├── frame_0001.jpg
    │   └── ... （約329ファイル）
    ├── database.db              ← COLMAPデータベース（自動生成）
    ├── sparse/                  ← COLMAP出力（Stage 2出力）
    │   └── 0/
    │       ├── cameras.bin
    │       ├── images.bin
    │       └── points3D.bin
    └── output/                  ← 3DGSモデル（Stage 3出力）
        └── point_cloud/
            └── iteration_30000/
                └── point_cloud.ply
```

---

## 複数日付のデータセット全体

```
data/
├── 20260101/
│   ├── video.mp4
│   ├── frames/
│   ├── sparse/
│   └── output/
├── 20260108/
│   └── ...
└── 20260119/
    └── ...

results/
├── traits_20260101.csv
└── all_traits.csv
```

---

## 構造のセットアップ

```bash
DATE="20260119"
mkdir -p data/$DATE/frames
mkdir -p data/$DATE/sparse
cp /path/to/recording.mp4 data/$DATE/video.mp4
ls data/$DATE/
# frames/  video.mp4
```

---

## 各ステージ後のディスク使用量

| ステージ後 | 新規ファイル | 累積サイズ |
|----------|---------|---------|
| 準備 | `video.mp4` | 約2 GB |
| Stage 1（フレーム） | `frames/*.jpg` | 約3.5 GB |
| Stage 2（COLMAP） | `database.db` + `sparse/` | 約3.7 GB |
| Stage 3（3DGS） | `output/point_cloud/` | 約4.0 GB |
| Stage 4（レンダリング） | `output/train/` + `output/test/` | 約6.5 GB |

**1日付あたり約6.5 GB** · **22日分で約143 GB** · **推奨ストレージ：500 GB以上**

---

## 命名規則

| 項目 | 形式 | 例 |
|------|-----|---|
| 日付フォルダ | `YYYYMMDD` | `20260119` |
| 動画ファイル | `video.mp4` | `video.mp4` |
| フレーム | `frame_%04d.jpg` | `frame_0001.jpg` |
| 結果 | `traits_YYYYMMDD.csv` | `traits_20260119.csv` |

!!! warning "パスにスペースや特殊文字を使用しないでください"

---

## 次のステップ

[→ パイプライン開始：動画処理](../pipeline/video-processing.md){ .md-button .md-button--primary }
