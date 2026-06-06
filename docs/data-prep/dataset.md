# Dataset Documentation

Complete details of the time-series plant phenotyping dataset used for validation.

---

## Quick Summary

| Property | Value |
|----------|-------|
| **Duration** | 49 days (Jan 19 – Mar 9, 2026) |
| **Capture dates** | 22 |
| **Location** | [Happy Quality greenhouse](https://share.google/alrmfOUOLqGngzcbS), Fukuroi city, Shizuoka |
| **Plant species** | Tomato (*Solanum lycopersicum*) |
| **Camera** | Google Pixel 6a, 4K UHD |
| **Capture method** | Fixed-viewpoint video, ~60s per date |
| **Best PSNR** | 23.71 dB |
| **Temporal CV** | 3.5% |

---

## Capture Dates

| # | Date | Notes |
|---|------|-------|
| 1 | 2026-01-19 | First capture |
| 2 | 2026-01-23 | |
| 3 | 2026-01-26 | |
| 4 | 2026-01-29 | |
| 5 | 2026-02-02 | |
| 6 | 2026-02-05 | |
| 7 | 2026-02-09 | |
| 8 | 2026-02-12 | |
| 9 | 2026-02-16 | |
| 10 | 2026-02-19 | |
| 11 | 2026-02-23 | |
| 12 | 2026-02-26 | |
| 13 | 2026-03-02 | |
| 14 | 2026-03-03 | |
| 15 | 2026-03-04 | |
| 16 | 2026-03-05 | |
| 17 | 2026-03-06 | |
| 18 | 2026-03-07 | |
| 19 | 2026-03-08 | |
| 20 | 2026-03-09 | Final capture |

---

## Location

**Happy Quality Co., Ltd. greenhouse, Fukuroi city, Shizuoka Prefecture, Japan**

The data was collected at a commercial tomato production greenhouse in Fukuroi city. The controlled environment provided consistent temperature and humidity conditions throughout the 49-day monitoring period.

---

## Acquisition Protocol

- Camera mounted at a **fixed position and orientation** for each capture session
- ~60 second walkthrough video at 4K resolution
- Captured during daytime hours under greenhouse lighting
- Same viewpoint maintained across all 22 dates (Condition 1)

---

## Quality Metrics Per Date

| Metric | Mean | Std | Min | Max |
|--------|------|-----|-----|-----|
| PSNR (dB) | 23.71 | ±0.83 | — | — |
| SSIM | 0.773 | — | — | — |
| LPIPS | 0.222 | — | — | — |
| Gaussians | ~630k | — | 188k | 668k |
