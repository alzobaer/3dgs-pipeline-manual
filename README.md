# 3DGS Pipeline Manual

Complete reproducibility manual for 3D Gaussian Splatting pipeline for plant phenotyping.

## Quick Start

```bash
# Install MkDocs
pip install mkdocs mkdocs-material

# Preview locally
mkdocs serve
# Open: http://127.0.0.1:8000

# Build static site
mkdocs build

# Deploy to GitHub Pages
mkdocs gh-deploy
```

## Adding Your Media

### Images

1. Place images in appropriate folders:
   - `docs/assets/images/figures/` - Your research figures
   - `docs/assets/images/photos/` - Greenhouse photos
   - `docs/assets/images/diagrams/` - Pipeline diagrams
   - `docs/assets/images/screenshots/` - Software screenshots

2. Reference in markdown:
```markdown
![Description](assets/images/figures/your-image.png)
*Caption text*
```

### Videos

**Small videos (<50MB):**
```markdown
<video width="100%" controls>
  <source src="assets/videos/demos/your-video.mp4" type="video/mp4">
</video>
```

**Large videos (YouTube):**
```markdown
<iframe width="100%" height="400" 
        src="https://www.youtube.com/embed/VIDEO_ID" 
        frameborder="0" allowfullscreen>
</iframe>
```

### Your Research Figures

Copy your 5 figures to:
- `psnr_over_time_v2.png` → `docs/assets/images/figures/`
- `psnr_by_radiation_v2.png` → `docs/assets/images/figures/`
- `environmental_correlations_v2.png` → `docs/assets/images/figures/`
- `ply_vs_rendered_comparison_v2.png` → `docs/assets/images/figures/`
- `growth_curve_v2.png` → `docs/assets/images/figures/`

## Deployment Options

### Option 1: GitHub Pages (Recommended)

```bash
# 1. Create GitHub repository
# 2. Push your code
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/3dgs-pipeline-manual
git push -u origin main

# 3. Deploy
mkdocs gh-deploy

# Live at: https://YOUR_USERNAME.github.io/3dgs-pipeline-manual/
```

### Option 2: Read the Docs

1. Push to GitHub
2. Go to readthedocs.org
3. Import repository
4. Configure: Use MkDocs
5. Build automatically

### Option 3: Netlify

1. Build site: `mkdocs build`
2. Drag `site/` folder to netlify.com
3. Done!

## Structure

```
3dgs-pipeline-manual/
├── docs/
│   ├── index.md (Homepage)
│   ├── getting-started/
│   ├── environment/
│   ├── pipeline/
│   ├── my-research/ (Your original work)
│   └── assets/
│       ├── images/
│       │   ├── figures/ (Your 5 figures)
│       │   ├── photos/
│       │   ├── diagrams/
│       │   └── screenshots/
│       ├── videos/
│       │   ├── demos/
│       │   └── tutorials/
│       └── pdfs/
├── mkdocs.yml (Configuration)
└── README.md (This file)
```

## Author

**Zobaer Al** (M2)  
Mineno Laboratory  
Shizuoka University

## License

For research and educational purposes.
