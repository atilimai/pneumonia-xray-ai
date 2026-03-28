# Evaluation Metrics

This document describes the evaluation metrics planned for the Pneumonia Detection project and explains why each is relevant for this task.

---

## Why Standard Accuracy Is Not Enough

Binary classification accuracy alone is misleading for imbalanced medical datasets. A model that always predicts "Pneumonia" would achieve high accuracy without being useful. Medical classification problems require a more nuanced set of metrics, particularly those that reflect clinical risk.

---

## Planned Metrics

### Accuracy
**Definition:** Proportion of all predictions (positive and negative) that are correct.
**Use:** Provides a baseline overview but should not be the primary metric.

---

### Precision
**Definition:** Of all samples predicted as Pneumonia, what fraction actually have pneumonia.
**Use:** Useful for understanding false positive rate — how often the model incorrectly flags a healthy patient.

---

### Recall (Sensitivity)
**Definition:** Of all actual Pneumonia cases, what fraction the model correctly identifies.
**Also known as:** True Positive Rate (TPR), Sensitivity.
**Use:** The most clinically important metric for this task. Missing a true pneumonia case (false negative) is a high-cost error.

---

### Sensitivity
Same as Recall. See above. Highlighted separately because it is the primary clinical success metric for this project.

---

### Specificity
**Definition:** Of all actual Normal cases, what fraction the model correctly identifies as Normal.
**Also known as:** True Negative Rate (TNR).
**Use:** Complements sensitivity. High specificity means the model avoids over-diagnosing pneumonia in healthy patients.

---

### ROC AUC (Area Under the Receiver Operating Characteristic Curve)
**Definition:** Measures the model's ability to discriminate between the two classes across all decision thresholds.
**Range:** 0.5 (random) to 1.0 (perfect).
**Use:** Threshold-independent summary of classifier performance. The primary aggregate metric for comparing models.

---

### Confusion Matrix
**Definition:** A 2×2 table showing True Positives, True Negatives, False Positives, and False Negatives.
**Use:** Provides full visibility into the types of errors the model makes. Required for computing all of the above metrics.

---

## Decision Threshold

The default decision threshold for binary classification is 0.5 (softmax probability). Adjusting this threshold trades off sensitivity against specificity. The evaluation protocol will document the chosen threshold and its justification.

See `docs/issues/06_evaluation_protocol_definition.md` for the full evaluation protocol plan.
