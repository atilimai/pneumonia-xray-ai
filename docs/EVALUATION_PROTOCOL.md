# Evaluation Protocol

This document defines the evaluation procedure for the Pneumonia Detection project.

## Goal

The goal of evaluation is to measure how well the trained binary classifier distinguishes:

- `PNEUMONIA` (positive class)
- `NORMAL` (negative class)

The evaluation must report both threshold-independent and threshold-dependent metrics.

---

## Evaluation Split

Final evaluation is performed on the **held-out test split**.

The validation split may be used during development for model selection and optional threshold exploration, but the final reported test results must be computed only once using the locked evaluation procedure.

---

## Positive and Negative Class Definition

- **Positive class:** `PNEUMONIA`
- **Negative class:** `NORMAL`

This convention is used throughout confusion matrix reporting and metric definitions.

Accepted label encoding:

- `0` = `NORMAL`
- `1` = `PNEUMONIA`

---

## Required Metrics

The following metrics must be reported:

### Threshold-independent

- **ROC AUC**
  - Computed from predicted probabilities for the positive class.
  - Used as the main threshold-independent summary of discrimination performance.

### Threshold-dependent

- **Confusion Matrix**
  - True Positive (TP)
  - True Negative (TN)
  - False Positive (FP)
  - False Negative (FN)

- **Sensitivity (Recall / True Positive Rate)**
  - Formula: `TP / (TP + FN)`

- **Specificity (True Negative Rate)**
  - Formula: `TN / (TN + FP)`

- **Precision**
  - Formula: `TP / (TP + FP)`

- **Accuracy**
  - Formula: `(TP + TN) / (TP + TN + FP + FN)`

- **Per-class error breakdown**
  - Count and percentage of false positives
  - Count and percentage of false negatives

---

## Threshold Selection Policy

### Default Policy

The default classification threshold is:

- **threshold = 0.5**

A sample is classified as:

- `PNEUMONIA` if predicted probability >= 0.5
- `NORMAL` if predicted probability < 0.5

### Rationale

A threshold of 0.5 is the standard baseline for binary probabilistic classifiers. It provides a simple, reproducible starting point and avoids overfitting threshold choice to the test set.

### Important Rule

**The test set must not be used to optimize the threshold.**

Any deviation from the default threshold of 0.5 must include a documented justification, the validation procedure used to select the new threshold, and the metric trade-off that motivated the change.

If threshold adjustment is explored, it must be done using:

- the validation split, or
- a separately defined development procedure

and the chosen threshold must then be fixed before final test evaluation.

### Clinical Note

Because false negatives are especially important in pneumonia detection, future threshold adjustments may prioritize **higher sensitivity** over specificity. However, unless such a policy is selected using validation data and documented explicitly, the final reported threshold remains **0.5**.

---

## Input to Evaluation

The evaluation script expects a table of predictions containing at least:

- `y_true` — ground-truth binary label
- `y_prob` — predicted probability for the positive class

Optional columns such as image path or sample ID may also be included.

---

## Configuration Reference

The evaluation procedure should be consistent with the configuration defined in:

`configs/evaluation/base.yaml`

The evaluation config is expected to define:

- evaluation split
- positive and negative class names
- positive and negative class labels
- decision threshold
- threshold policy
- required prediction columns
- metrics to compute
- output artifact paths
- plot settings

If the evaluation protocol and the evaluation config disagree, the protocol should be updated first and the config should be kept consistent with the documented protocol.

---

## Evaluation Workflow

The final evaluation workflow is:

1. Load the saved model checkpoint selected during validation.
2. Run inference on the held-out test split.
3. Save predicted probabilities for the positive class (`PNEUMONIA`).
4. Store predictions in `artifacts/predictions/test_predictions.csv`.
5. Apply the fixed decision threshold.
6. Compute threshold-dependent metrics.
7. Compute ROC AUC from predicted probabilities.
8. Save figures and metric reports to the configured artifact paths.
9. Report results with the dataset split, threshold, positive class definition, and metric definitions.

---

## Required Outputs

The evaluation process must produce:

### Figures

- ROC curve plot
- Confusion matrix plot

### Reported Values

- ROC AUC
- Confusion matrix counts
- Sensitivity
- Specificity
- Precision
- Accuracy
- False positive count
- False negative count

### Saved Artifacts

Suggested output paths:

- `artifacts/figures/roc_curve.png`
- `artifacts/figures/confusion_matrix.png`
- `artifacts/reports/evaluation_metrics.json`

---

## Reporting Convention

All final reported numbers must clearly state:

- dataset split used
- chosen threshold
- positive class definition
- whether probabilities or hard predictions were used

---

## Summary

The evaluation protocol for this project is:

- Evaluate on the held-out **test split**
- Treat `PNEUMONIA` as the **positive class**
- Compute ROC AUC from predicted probabilities
- Use **threshold = 0.5** unless a validation-based threshold is explicitly documented
- Report confusion matrix, sensitivity, specificity, precision, accuracy, and per-class error breakdown
- Keep the evaluation protocol consistent with `configs/evaluation/base.yaml`
