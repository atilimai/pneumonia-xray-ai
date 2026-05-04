# Evaluation Protocol

## Purpose

This document defines the evaluation protocol for the Pneumonia Detection model before model training and final testing.

The goal is to make evaluation decisions in advance so that the results are not influenced by observed model performance.

This protocol covers:

- The dataset split used for evaluation
- The decision threshold policy
- The primary evaluation metric
- The full list of reported metrics
- The required reporting format
- The saved figures that should be included in the evaluation report

Implementation of evaluation code is out of scope for this document.

---

## Evaluation Split

The test split will be reserved strictly for final evaluation.

The validation split may be used during training for monitoring model behavior, but it should not be used as the final source of reported model performance.

Because the validation split is small, with only 8 images per class, validation metrics may be unstable and should be interpreted carefully.

Training loss may be used as the primary stopping signal during training when validation metrics are too unreliable.

The test split must not be used for:

- Model selection
- Hyperparameter tuning
- Threshold optimization
- Early stopping decisions
- Repeated trial-and-error evaluation

The test set should only be used once the model, threshold policy, and evaluation procedure have already been finalized.

---

## Classification Setting

The task is binary classification.

The model predicts the probability that a chest X-ray belongs to the pneumonia class.

The two classes are:

| Class Label | Meaning |
|---|---|
| 0 | Normal |
| 1 | Pneumonia |

Predicted probabilities are converted into class labels using a decision threshold.

---

## Decision Threshold Policy

The default decision threshold will be:

```text
0.5
