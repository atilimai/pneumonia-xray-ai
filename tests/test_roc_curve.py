from __future__ import annotations

from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")

from src.evaluation.evaluate import plot_roc_curve
from src.evaluation.metrics import compute_roc_metrics


def test_roc_curve_is_saved_with_auc_annotation(tmp_path: Path) -> None:
    y_true = np.array([0, 0, 1, 1])
    y_prob = np.array([0.05, 0.35, 0.72, 0.96])
    metrics = compute_roc_metrics(y_true, y_prob)

    output_path = tmp_path / "roc_curve.png"
    plot_roc_curve(
        np.array(metrics["roc_curve"]["fpr"]),
        np.array(metrics["roc_curve"]["tpr"]),
        metrics["roc_auc"],
        output_path=output_path,
    )

    assert output_path.exists()
    assert output_path.stat().st_size > 0
    assert metrics["roc_auc"] == 1.0
