"""
compute_heights_rendered.py — generate heights_rendered.csv from 3DGS models
=============================================================================
Renders each session from the canonical pose — the 25th held-out test frame
(the test split keeps every 8th COLMAP frame) = cameras.json[200] = frame_00201,
≈40 s into the walk at 5 fps — and extracts two scale-invariant traits:

  h_norm        = (r95 − r5) / H_R
  green_coverage = mask_pixel_count / (H_R × W_R)

where r5, r95 are the 5th/95th-percentile rows of the HSV-segmented plant
mask, and H_R × W_R is the native render resolution from cameras.json.

HSV thresholds (OpenCV convention, 8-bit):
  Hue   : [25, 95]   (degrees/2)
  Sat   : ≥ 20
  Val   : ≥ 30

Requirements: CUDA GPU, gaussian-splatting repo at ~/gaussian-splatting
Usage:
  conda activate gaussian_splatting
  python analysis/compute_heights_rendered.py [--output analysis/heights_rendered.csv]
"""

import sys, json, argparse, csv
import numpy as np
import cv2
import torch
from pathlib import Path
from argparse import Namespace

sys.path.insert(0, str(Path.home() / 'gaussian-splatting'))
from gaussian_renderer import render, GaussianModel
from utils.graphics_utils import getWorld2View2, getProjectionMatrix

# ── constants ──────────────────────────────────────────────────────────────────
OUTPUT_ROOT = Path('/media/HDD-24TB/Zobaer_Research_Lab/3DGS_TimeSeries/output')
ITERATION   = 30000
CAM_IDX     = 200  # canonical pose = 25th held-out test frame = cameras.json[200] = frame_00201 (~40 s)

H_LOW, H_HIGH = 25, 95   # hue bounds (OpenCV 0-179)
S_LOW, V_LOW  =  20, 30  # saturation / value minimums

pipe = Namespace(convert_SHs_python=False, compute_cov3D_python=False,
                 debug=False, antialiasing=False)
bg   = torch.zeros(3, device='cuda')


def get_model_dir(date: str) -> str:
    return 'gs_model_v2' if date == '20260119' else 'gs_model'


def compute_traits_cv2(img_rgb: np.ndarray) -> dict:
    """Return h_norm, green_coverage, and pixel-level stats."""
    H, W = img_rgb.shape[:2]
    img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
    hsv     = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    mask    = cv2.inRange(hsv, (H_LOW, S_LOW, V_LOW), (H_HIGH, 255, 255))

    rows = np.where(mask.any(axis=1))[0]
    if len(rows) == 0:
        return dict(height_px=0.0, height_norm=0.0, green_coverage=0.0,
                    top_row_px=0.0, bottom_row_px=0.0, image_H=H, image_W=W,
                    status='empty_mask')

    r5  = float(np.percentile(rows, 5))
    r95 = float(np.percentile(rows, 95))
    h_norm       = round((r95 - r5) / H, 4)
    green_coverage = round(float(mask.sum()) / 255.0 / (H * W), 4)

    return dict(height_px=round(r95 - r5, 1),
                height_norm=h_norm,
                green_coverage=green_coverage,
                top_row_px=round(r5, 1),
                bottom_row_px=round(r95, 1),
                image_H=H, image_W=W,
                status='ok')


def render_pose025(base: Path) -> np.ndarray:
    """Load 3DGS model and render from COLMAP camera pose 025 at native resolution."""
    with open(base / 'cameras.json') as f:
        cams = json.load(f)
    cam = cams[CAM_IDX]

    W = cam['width']
    H = cam['height']
    fx, fy = cam['fx'], cam['fy']
    FoVx = 2 * np.arctan(W / (2 * fx))
    FoVy = 2 * np.arctan(H / (2 * fy))

    R  = np.array(cam['rotation'], dtype=np.float64)
    C  = np.array(cam['position'], dtype=np.float64)
    T  = (-R @ C).astype(np.float32)

    class SimpleCamera:
        def __init__(self):
            self.R = R.astype(np.float32); self.T = T
            self.FoVx = FoVx; self.FoVy = FoVy
            self.image_width = W; self.image_height = H
            self.znear = 0.01; self.zfar = 100.0
            self.world_view_transform = torch.tensor(
                getWorld2View2(R, T)).transpose(0, 1).cuda()
            self.projection_matrix = getProjectionMatrix(
                znear=self.znear, zfar=self.zfar,
                fovX=FoVx, fovY=FoVy).transpose(0, 1).cuda()
            self.full_proj_transform = (
                self.world_view_transform.unsqueeze(0).bmm(
                    self.projection_matrix.unsqueeze(0))).squeeze(0)
            self.camera_center = self.world_view_transform.inverse()[3, :3]

    ply_path = base / f'point_cloud/iteration_{ITERATION}/point_cloud.ply'
    gaussians = GaussianModel(3)
    gaussians.load_ply(str(ply_path))

    view = SimpleCamera()
    with torch.no_grad():
        out = render(view, gaussians, pipe, bg)['render']
    img = (out.clamp(0, 1).permute(1, 2, 0).cpu().numpy() * 255).astype('uint8')
    del gaussians
    torch.cuda.empty_cache()
    return img


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', default='analysis/heights_rendered.csv',
                        help='Output CSV path (default: analysis/heights_rendered.csv)')
    parser.add_argument('--dates', nargs='+', default=None,
                        help='Specific dates to process (default: all 2026* sessions)')
    args = parser.parse_args()

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)

    dates = sorted(args.dates) if args.dates else \
            sorted(d.name for d in OUTPUT_ROOT.iterdir() if d.name.startswith('2026'))

    FIELDS = ['date', 'height_px', 'height_norm', 'green_coverage',
              'top_row_px', 'bottom_row_px', 'image_H', 'image_W', 'status']

    rows = []
    print(f"Processing {len(dates)} sessions → {output}")
    print(f"Camera: COLMAP index {CAM_IDX}  |  Iteration: {ITERATION}")
    print(f"HSV thresholds: H∈[{H_LOW},{H_HIGH}], S≥{S_LOW}, V≥{V_LOW}")
    print()

    for date in dates:
        model  = get_model_dir(date)
        base   = OUTPUT_ROOT / date / model
        ply    = base / f'point_cloud/iteration_{ITERATION}/point_cloud.ply'
        cam_js = base / 'cameras.json'

        if not ply.exists():
            print(f'  {date}  SKIP — PLY not found: {ply}')
            rows.append({'date': date, **{k: '' for k in FIELDS[1:]},
                         'status': 'missing_ply'})
            continue

        print(f'  {date}  rendering ...', end='', flush=True)
        img = render_pose025(base)
        traits = compute_traits_cv2(img)
        traits['date'] = date
        rows.append(traits)
        print(f"  h_norm={traits['height_norm']:.4f}  "
              f"green_coverage={traits['green_coverage']:.4f}  [{traits['status']}]")

    with open(output, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, '') for k in FIELDS})

    ok_rows = [r for r in rows if r.get('status') == 'ok']
    if ok_rows:
        vals = [float(r['height_norm']) for r in ok_rows]
        cov  = [float(r['green_coverage']) for r in ok_rows]
        m, s = np.mean(vals), np.std(vals)
        print(f"\nSummary ({len(ok_rows)} sessions):")
        print(f"  h_norm:         mean={m:.4f}  std={s:.4f}  CV={s/m*100:.1f}%")
        mc, sc = np.mean(cov), np.std(cov)
        print(f"  green_coverage: mean={mc:.4f}  std={sc:.4f}  CV={sc/mc*100:.1f}%")
        print(f"\nSaved: {output}")


if __name__ == '__main__':
    main()
