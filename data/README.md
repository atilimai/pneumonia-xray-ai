# Data Directory

This directory holds all dataset files for the Pneumonia Detection project. **No dataset files are committed to this repository.**

---

## Expected Dataset Source

Download the dataset from Kaggle:
**[Chest X-Ray Images (Pneumonia) — Kermany et al.](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)**

After downloading and extracting, place the contents under `data/raw/`.

---

## Expected Folder Structure After Download

```
data/
├── raw/
│   └── chest_xray/
│       ├── train/
│       │   ├── NORMAL/
│       │   └── PNEUMONIA/
│       ├── val/
│       │   ├── NORMAL/
│       │   └── PNEUMONIA/
│       └── test/
│           ├── NORMAL/
│           └── PNEUMONIA/
├── interim/        # Intermediate data (e.g., resized images, split manifests)
├── processed/      # Final preprocessed tensors or datasets ready for training
└── external/       # Any additional reference data (e.g., external validation sets)
```

---

## Folder Meanings

| Folder | Purpose |
|---|---|
| `raw/` | Original, unmodified files exactly as downloaded |
| `interim/` | Partially processed data — transformations applied but not finalized |
| `processed/` | Final dataset ready for model input (resized, normalized, split-confirmed) |
| `external/` | Any supplementary datasets used for comparison or additional validation |

---

## Why Dataset Files Stay Out of Git

- The dataset is several gigabytes in size and would bloat the repository
- Kaggle data is subject to its own terms of use and should not be redistributed
- Git is not designed for large binary files; use Git LFS or Hugging Face Datasets Hub for model-ready data if needed
- The `.gitignore` at the project root excludes all files under `data/raw/`, `data/interim/`, `data/processed/`, and `data/external/` while preserving `.gitkeep` placeholders
