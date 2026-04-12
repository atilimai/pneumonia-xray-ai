from __future__ import annotations

from typing import Dict, Any

import numpy as np
from sklearn.metrics import confusion_matrix, roc_auc_score, roc_curve


def apply_threshold(y_prob: np.ndarray, threshold: float = 0.5) -> np.ndarray:
    """
    Convert predicted probabilities into binary predictions.

    Args:
        y_prob: Array of predicted probabilities for the positive class.
        threshold: Decision threshold.

    Returns:
        Binary predictions as a NumPy array of 0s and 1s.
    """
    y_prob = np.asarray(y_prob, dtype=float)
    return (y_prob >= threshold).astype(int)


def compute_confusion_counts(y_true: np.ndarray, y_pred: np.ndarray) -> Dict[str, int]:
    """
    Compute confusion matrix counts for binary classification.

    Returns:
        A dict with TN, FP, FN, TP.
    """
    y_true = np.asarray(y_true, dtype=int)
    y_pred = np.asarray(y_pred, dtype=int)

    tn, fp, fn, tp = confusion_matrix(y_true, y_pred, labels=[0, 1]).ravel()
    return {
        "tn": int(tn),
        "fp": int(fp),
        "fn": int(fn),
        "tp": int(tp),
    }


def compute_threshold_metrics(
    y_true: np.ndarray,
    y_prob: np.ndarray,
    threshold: float = 0.5,
) -> Dict[str, Any]:
    """
    Compute binary classification metrics at a chosen threshold.

    Args:
        y_true: Ground-truth labels (0 or 1).
        y_prob: Predicted probabilities for the positive class.
        threshold: Decision threshold.

    Returns:
        Dictionary containing confusion matrix counts and derived metrics.
    """
    y_true = np.asarray(y_true, dtype=int)
    y_prob = np.asarray(y_prob, dtype=float)
    y_pred = apply_threshold(y_prob, threshold=threshold)

    counts = compute_confusion_counts(y_true, y_pred)
    tn = counts["tn"]
    fp = counts["fp"]
    fn = counts["fn"]
    tp = counts["tp"]

    total = tn + fp + fn + tp

    accuracy = (tp + tn) / total if total > 0 else 0.0
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    sensitivity = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    specificity = tn / (tn + fp) if (tn + fp) > 0 else 0.0
    false_positive_rate = fp / (fp + tn) if (fp + tn) > 0 else 0.0
    false_negative_rate = fn / (fn + tp) if (fn + tp) > 0 else 0.0

    return {
        "threshold": float(threshold),
        "counts": counts,
        "accuracy": float(accuracy),
        "precision": float(precision),
        "sensitivity": float(sensitivity),
        "specificity": float(specificity),
        "false_positive_rate": float(false_positive_rate),
        "false_negative_rate": float(false_negative_rate),
        "per_class_error_breakdown": {
            "normal_as_pneumonia_fp_count": int(fp),
            "pneumonia_as_normal_fn_count": int(fn),
        },
    }


def compute_roc_metrics(y_true: np.ndarray, y_prob: np.ndarray) -> Dict[str, Any]:
    """
    Compute ROC AUC and ROC curve points.

    Args:
        y_true: Ground-truth labels (0 or 1).
        y_prob: Predicted probabilities for the positive class.

    Returns:
        Dictionary with ROC AUC and curve arrays.
    """
    y_true = np.asarray(y_true, dtype=int)
    y_prob = np.asarray(y_prob, dtype=float)

    auc = roc_auc_score(y_true, y_prob)
    fpr, tpr, thresholds = roc_curve(y_true, y_prob)

    return {
        "roc_auc": float(auc),
        "roc_curve": {
            "fpr": fpr.tolist(),
            "tpr": tpr.tolist(),
            "thresholds": thresholds.tolist(),
        },
    }


def compute_all_metrics(
    y_true: np.ndarray,
    y_prob: np.ndarray,
    threshold: float = 0.5,
) -> Dict[str, Any]:
    """
    Compute all required evaluation metrics.

    Returns:
        Combined dictionary of threshold-dependent and threshold-independent metrics.
    """
    threshold_metrics = compute_threshold_metrics(y_true, y_prob, threshold=threshold)
    roc_metrics = compute_roc_metrics(y_true, y_prob)

    result = {}
    result.update(threshold_metrics)
    result.update(roc_metrics)
    return result