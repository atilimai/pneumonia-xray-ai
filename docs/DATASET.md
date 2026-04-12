# Dataset Documentation

## Dataset Name

**Chest X-Ray Images (Pneumonia)**
- **Source:** Kaggle — [https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)
- **Original Authors:** Kermany et al.
- **Format:** JPEG images

---

## Binary Labels

| Label | Meaning |
|---|---|
| `NORMAL` | No pneumonia detected |
| `PNEUMONIA` | Pneumonia present (bacterial or viral, treated as one class) |

This project performs **binary classification** only. Bacterial vs. viral sub-classification is out of scope.

---

## Expected Dataset Structure

After downloading and extracting the Kaggle dataset into `data/raw/`, the expected folder structure is:

```
data/raw/chest_xray/
├── train/
│   ├── NORMAL/        (~1341 images)
│   └── PNEUMONIA/     (~3875 images)
├── val/
│   ├── NORMAL/        (~8 images)
│   └── PNEUMONIA/     (~8 images)
└── test/
    ├── NORMAL/        (~234 images)
    └── PNEUMONIA/     (~390 images)
```

> Image counts are approximate and based on the standard Kaggle distribution.

---

## Key Concerns

### Class Imbalance
The training set has significantly more pneumonia samples than normal samples (~3:1 ratio). This must be addressed to avoid a model that is biased toward predicting pneumonia.

### Split Imbalance Ratios
- **Train:** 3875 / 1341 ≈ **2.89:1**
- **Validation:** 8 / 8 = **1:1**
- **Test:** 390 / 234 ≈ **1.67:1**

This confirms that the strongest class imbalance exists in the training split, where pneumonia samples are nearly 3 times more frequent than normal samples.

Mitigation options include:
- Weighted loss function
- Oversampling / undersampling
- Class-weighted metrics for evaluation

### Medical Imaging Caution
- Images were collected in clinical settings and may contain confounding artifacts
- This dataset is not representative of all global populations or imaging equipment
- Model performance on this dataset does not translate to real-world clinical performance

### Split Hygiene
- The provided train/val/test split should be respected to avoid data leakage
- Images must not be shuffled across splits
- The validation set is small (8 images per class) — this is a known limitation of the dataset and should be noted in evaluation

### Licensing
The dataset is licensed under a Creative Commons license for non-commercial research use. Review the Kaggle page for the current license terms before redistribution.
