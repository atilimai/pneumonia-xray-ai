from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix

from src.evaluation.metrics import compute_all_metrics, apply_threshold


def plot_confusion_matrix(y_true, y_pred, output_path: Path, title: str = "Confusion Matrix") -> None:
    cm = confusion_matrix(y_true, y_pred, labels=[0, 1])
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["NORMAL", "PNEUMONIA"])

    fig, ax = plt.subplots(figsize=(5, 5))
    disp.plot(ax=ax, colorbar=False)
    ax.set_title(title)
    fig.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=160)
    plt.close(fig)


def plot_roc_curve(fpr, tpr, roc_auc: float, output_path: Path, title: str = "ROC Curve") -> None:
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.plot(fpr, tpr, label=f"ROC AUC = {roc_auc:.4f}")
    ax.plot([0, 1], [0, 1], linestyle="--")
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")
    ax.set_title(title)
    ax.legend(loc="lower right")
    fig.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=160)
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate pneumonia classifier predictions.")
    parser.add_argument(
        "--input-csv",
        type=str,
        required=True,
        help="Path to CSV with columns: y_true, y_prob",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.5,
        help="Decision threshold for positive class.",
    )
    parser.add_argument(
        "--metrics-out",
        type=str,
        default="artifacts/reports/evaluation_metrics.json",
        help="Path to output JSON metrics file.",
    )
    parser.add_argument(
        "--confusion-matrix-out",
        type=str,
        default="artifacts/figures/confusion_matrix.png",
        help="Path to confusion matrix figure.",
    )
    parser.add_argument(
        "--roc-curve-out",
        type=str,
        default="artifacts/figures/roc_curve.png",
        help="Path to ROC curve figure.",
    )
    args = parser.parse_args()

    input_csv = Path(args.input_csv)
    if not input_csv.exists():
        raise FileNotFoundError(f"Input CSV not found: {input_csv}")

    df = pd.read_csv(input_csv)

    required_columns = {"y_true", "y_prob"}
    missing = required_columns - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    y_true = df["y_true"].to_numpy(dtype=int)
    y_prob = df["y_prob"].to_numpy(dtype=float)

    metrics = compute_all_metrics(y_true, y_prob, threshold=args.threshold)

    y_pred = apply_threshold(y_prob, threshold=args.threshold)
    plot_confusion_matrix(
        y_true,
        y_pred,
        output_path=Path(args.confusion_matrix_out),
        title="Confusion Matrix",
    )

    roc_data = metrics["roc_curve"]
    plot_roc_curve(
        np.array(roc_data["fpr"]),
        np.array(roc_data["tpr"]),
        metrics["roc_auc"],
        output_path=Path(args.roc_curve_out),
        title="ROC Curve",
    )

    metrics_out = Path(args.metrics_out)
    metrics_out.parent.mkdir(parents=True, exist_ok=True)
    with metrics_out.open("w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    print("Evaluation completed.")
    print(f"Metrics saved to: {metrics_out}")
    print(f"Confusion matrix saved to: {args.confusion_matrix_out}")
    print(f"ROC curve saved to: {args.roc_curve_out}")


if __name__ == "__main__":
    main()