from __future__ import annotations

import argparse
import math
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create a gallery of false positive test samples."
    )

    parser.add_argument(
        "--predictions-csv",
        type=str,
        default="artifacts/predictions/test_predictions.csv",
        help="Path to predictions CSV with image_path, y_true, and y_prob columns.",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.5,
        help="Decision threshold for positive class.",
    )
    parser.add_argument(
        "--output-path",
        type=str,
        default="artifacts/figures/false_positives.png",
        help="Path to save false positive gallery.",
    )
    parser.add_argument(
        "--max-images",
        type=int,
        default=12,
        help="Maximum number of false positive samples to show.",
    )

    args = parser.parse_args()

    predictions_path = Path(args.predictions_csv)
    output_path = Path(args.output_path)

    if not predictions_path.exists():
        raise FileNotFoundError(f"Predictions CSV not found: {predictions_path}")

    df = pd.read_csv(predictions_path)

    required_columns = {"image_path", "y_true", "y_prob"}
    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")

    df["y_pred"] = (df["y_prob"].astype(float) >= args.threshold).astype(int)

    false_positives = df[
        (df["y_true"].astype(int) == 0) &
        (df["y_pred"] == 1)
    ].copy()

    false_positives = false_positives.sort_values(
        by="y_prob",
        ascending=False
    ).head(args.max_images)

    if false_positives.empty:
        raise RuntimeError(
            "No false positive samples found at the selected threshold. "
            "Cannot create false positive gallery."
        )

    n_images = len(false_positives)
    cols = min(4, n_images)
    rows = math.ceil(n_images / cols)

    fig, axes = plt.subplots(rows, cols, figsize=(4 * cols, 4 * rows))

    if rows == 1 and cols == 1:
        axes = [axes]
    else:
        axes = axes.flatten()

    for ax, (_, row) in zip(axes, false_positives.iterrows()):
        image_path = Path(row["image_path"])

        if not image_path.exists():
            raise FileNotFoundError(f"Image not found: {image_path}")

        image = Image.open(image_path).convert("RGB")

        ax.imshow(image, cmap="gray")
        ax.axis("off")
        ax.set_title(
            f"True: NORMAL\nPred: PNEUMONIA\np={row['y_prob']:.3f}",
            fontsize=10,
        )

    for ax in axes[n_images:]:
        ax.axis("off")

    fig.suptitle("False Positive Samples - Test Set", fontsize=16)
    plt.tight_layout()
    plt.subplots_adjust(top=0.88)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close(fig)

    print(f"False positives found: {len(false_positives)}")
    print(f"Saved gallery to: {output_path}")


if __name__ == "__main__":
    main()