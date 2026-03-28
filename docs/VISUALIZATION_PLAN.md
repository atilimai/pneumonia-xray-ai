# Visualization Plan

This document lists all visual outputs the project should produce by the end of Week 4. All figures should be saved to `artifacts/figures/`.

---

## 1. Class Distribution Chart

**Purpose:** Show the class balance (Pneumonia vs Normal) across the train, val, and test splits.
**Type:** Bar chart
**When:** During EDA (Week 2)

---

## 2. Sample Image Grids

**Purpose:** Display a representative grid of raw images for each class so that visual differences are apparent.
**Type:** Image grid (e.g., 4×4 or 5×5 per class)
**When:** During EDA (Week 2)

---

## 3. Training Curves

**Purpose:** Show model learning progress over epochs. Essential for diagnosing overfitting or underfitting.
**Type:** Line plots — training loss, validation loss, training accuracy, validation accuracy
**When:** During and after training (Week 3)

---

## 4. Confusion Matrix

**Purpose:** Show the full breakdown of True Positives, True Negatives, False Positives, and False Negatives on the test set.
**Type:** Heatmap-style 2×2 matrix with counts and normalized percentages
**When:** After evaluation (Week 3)

---

## 5. ROC Curve

**Purpose:** Visualize classifier performance across all decision thresholds and report ROC AUC.
**Type:** Line plot with AUC annotated, diagonal baseline shown
**When:** After evaluation (Week 3)

---

## 6. Grad-CAM Gallery

**Purpose:** Show heatmap overlays on test images for qualitative model interpretability inspection.
**Type:** Side-by-side original X-ray and Grad-CAM overlay image grid
**Subset:** Include correct predictions (both classes), false positives, and false negatives
**When:** After Grad-CAM integration (Week 4)

---

## 7. False Positive Gallery

**Purpose:** Inspect images the model incorrectly labelled as Pneumonia when the ground truth is Normal.
**Type:** Image grid with predicted confidence scores
**When:** After evaluation and Grad-CAM integration (Week 4)

---

## 8. False Negative Gallery

**Purpose:** Inspect images the model missed — actual Pneumonia cases labelled as Normal.
**Type:** Image grid with predicted confidence scores
**When:** After evaluation and Grad-CAM integration (Week 4)

---

## Output Location

All figures should be saved to `artifacts/figures/` using descriptive filenames (e.g., `confusion_matrix_test.png`, `roc_curve.png`, `gradcam_gallery_tp.png`).
