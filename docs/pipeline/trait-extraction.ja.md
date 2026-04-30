# Stage 5：形質抽出

レンダリング画像からスケール不変な植物計測値を抽出します。

---

## このステージの概要

```mermaid
graph LR
    A[📷 レンダリング画像<br/>正規化視点] -->|セグメンテーション| B[🌿 植物マスク]
    B -->|草丈計算| C[📏 画像空間草丈]
    C --> D[📊 植物形質<br/>草丈 · キャノピー]
    style A fill:#e1f5ff
    style D fill:#e1ffe1
```

**推定所要時間：** 1日付あたり約2分

---

## 核心となる革新

従来のPLYベースの手法は三次元座標空間で計測しますが、COLMAPは各日付の再構成に**異なるスケール**を割り当てるため日付間の直接比較ができません。

本手法の解決策：**レンダリング画像空間**（ピクセル）で草丈を計測します。撮影日に関わらず植物が画像内で一定の正規化された位置を占めるため、スケール不変になります。

---

## Step 1：植物セグメンテーション

HSVカラー閾値処理で植物を背景から分離します。

```python
import cv2
import numpy as np

def segment_plant(image_path: str) -> np.ndarray:
    # HSVカラー閾値処理で植物を背景から分離
    # 255=植物ピクセルのバイナリマスクを返す
    img = cv2.imread(image_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 緑色植生の閾値（トマト植物用に調整済み）
    lower_green = np.array([25, 40, 40])
    upper_green = np.array([90, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # マスクのクリーンアップ
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    return mask
```

---

## Step 2：スケール不変草丈の抽出

草丈を画像高さの**比率**として計測します — これがスケール不変性の鍵です。

```python
def extract_height_pixels(mask: np.ndarray) -> dict:
    # 画像空間座標で植物草丈を抽出
    # 草丈を画像高さの割合（0.0〜1.0）として返す
    plant_rows = np.where(mask.any(axis=1))[0]
    if len(plant_rows) == 0:
        return {"height_px": 0, "height_ratio": 0.0, "valid": False}

    top_px    = plant_rows.min()
    bottom_px = plant_rows.max()
    height_px = bottom_px - top_px

    # 画像高さで正規化 → スケール不変
    height_ratio = height_px / mask.shape[0]

    return {
        "height_px": int(height_px),
        "height_ratio": float(height_ratio),
        "valid": True
    }
```

!!! info "なぜ画像高さで割るか？"
    `height_ratio = height_px / image_height` により、COLMAPの任意スケール係数から独立した計測値になります。

---

## Step 3：実行

```bash
conda activate 3dgs

python extract_traits.py \
    --renders_dir output/train/ours_30000/renders \
    --date 20260119 \
    --output results/traits_20260119.csv
```

---

## Step 4：時系列成長解析

```bash
# 全日付で実行
for DATE in 20260101 20260108 20260115; do
    python extract_traits.py \
        --renders_dir data/$DATE/output/train/ours_30000/renders \
        --date $DATE \
        --output results/traits_$DATE.csv
done

# 全日付を統合
python -c "
import pandas as pd, glob
dfs = [pd.read_csv(f) for f in sorted(glob.glob('results/traits_*.csv'))]
pd.concat(dfs).to_csv('results/all_traits.csv', index=False)
"
```

---

## 結果

| 手法 | CV | 解釈 |
|-----|--|---|
| **本手法（画像空間）** | **9.7%** | ✅ 生物学的に意味のある変動 |
| 従来手法（PLY） | 54.4% | ❌ スケールアーティファクトが支配的 |

!!! success "CV 9.7%の意味"
    計測された変動は実際の生物学的変動を反映しており、計測誤差ではありません。複数日の3DGS再構成からのスケール不変形質抽出の**初の検証**です。

---

## 出力CSVフォーマット

```csv
date,image,height_px,height_ratio,top_px,bottom_px,valid
20260119,frame_0001.jpg,1124,0.521,412,1536,True
```

| 列 | 説明 |
|--|---|
| `height_ratio` | **主要指標** — 草丈 / 画像高さ（スケール不変） |
| `valid` | セグメンテーション成功フラグ |

---

## 次のステップ

[→ 研究内容：独自の貢献](../my-research/contributions.md){ .md-button .md-button--primary }
