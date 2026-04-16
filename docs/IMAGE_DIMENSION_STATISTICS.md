# Image Dimension Statistics Report

**Dataset:** Chest X-Ray Pneumonia  
**Source:** Kaggle — paultimothymooney/chest-xray-pneumonia  
**Date:** 2026-04-16  
**Total Images Processed:** 11,712

---

## Results

| Metric           | Min (px) | Max (px) | Mean (px) |
|------------------|----------|----------|-----------|
| Width            | 384      | 2916     | 1327.88   |
| Height           | 127      | 2713     | 970.69    |

---

## Observations

- Images vary significantly in size, with width ranging from **384 to 2916 px** and height from **127 to 2713 px**.
- Mean dimensions are approximately **1328 × 971 px**.
- Preprocessing (resizing/normalization) is required before model training due to high variance in dimensions.
