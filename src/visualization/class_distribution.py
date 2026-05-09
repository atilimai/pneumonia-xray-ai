"""
Generate a class distribution chart (per split: train, val, test).

Output: artifacts/figures/class_distribution.png

Usage:
    python src/visualization/class_distribution.py
    python src/visualization/class_distribution.py --data-dir data/raw/chest_xray --output artifacts/figures/class_distribution.png --dpi 150
"""

import argparse
import os

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import seaborn as sns

SPLITS = ["train", "val", "test"]
CLASSES = ["NORMAL", "PNEUMONIA"]
COLORS = {"NORMAL": "#2ca02c", "PNEUMONIA": "#d62728"}


def count_images(data_dir: str) -> dict:
    counts = {}
    for split in SPLITS:
        counts[split] = {}
        for cls in CLASSES:
            path = os.path.join(data_dir, split, cls)
            if os.path.isdir(path):
                counts[split][cls] = sum(
                    1 for f in os.listdir(path)
                    if f.lower().endswith((".jpg", ".jpeg", ".png"))
                )
            else:
                counts[split][cls] = 0
    return counts


def plot_class_distribution(
    data_dir: str = "data/raw/chest_xray",
    output_path: str = "artifacts/figures/class_distribution.png",
    dpi: int = 150,
) -> None:
    counts = count_images(data_dir)

    total_images = sum(counts[s][c] for s in SPLITS for c in CLASSES)
    if total_images == 0:
        raise FileNotFoundError(
            f"No images found under '{data_dir}'. "
            "Download the Kaggle chest X-ray dataset and place it at that path before running this script."
        )

    sns.set_theme(style="whitegrid", font_scale=1.1)

    fig, axes = plt.subplots(1, 3, figsize=(16, 6))
    fig.suptitle("Class Distribution per Split", fontsize=16, fontweight="bold")

    for ax, split in zip(axes, SPLITS):
        values = [counts[split][cls] for cls in CLASSES]
        split_total = sum(values)

        bars = ax.bar(
            CLASSES,
            values,
            color=[COLORS[c] for c in CLASSES],
            width=0.5,
            edgecolor="white",
            linewidth=1.2,
        )

        y_max = max(values) if max(values) > 0 else 1
        for bar, val in zip(bars, values):
            pct = (val / split_total * 100) if split_total > 0 else 0.0
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + y_max * 0.03,
                f"{val:,}\n({pct:.1f}%)",
                ha="center",
                va="bottom",
                fontsize=10,
                fontweight="bold",
            )

        ratio_str = ""
        if values[0] > 0:
            ratio = values[1] / values[0]
            ratio_str = f"  |  Ratio {ratio:.2f}:1"

        ax.set_title(
            f"{split.capitalize()}  (n={split_total:,}{ratio_str})",
            fontsize=11,
            pad=10,
        )
        ax.set_xlabel("Class", fontsize=11)
        ax.set_ylabel("Number of Images", fontsize=11)
        ax.set_ylim(0, y_max * 1.25)
        ax.tick_params(axis="x", labelsize=10)
        sns.despine(ax=ax, left=False, bottom=False)

    legend_patches = [mpatches.Patch(color=COLORS[c], label=c) for c in CLASSES]
    fig.legend(
        handles=legend_patches,
        loc="upper right",
        bbox_to_anchor=(1.0, 1.0),
        fontsize=11,
        frameon=True,
    )

    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=dpi, bbox_inches="tight")
    plt.close()
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate class distribution chart.")
    parser.add_argument(
        "--data-dir",
        default="data/raw/chest_xray",
        help="Root directory of the chest_xray dataset (default: data/raw/chest_xray)",
    )
    parser.add_argument(
        "--output",
        default="artifacts/figures/class_distribution.png",
        help="Output path for the figure (default: artifacts/figures/class_distribution.png)",
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=150,
        help="Figure resolution in DPI (default: 150)",
    )
    args = parser.parse_args()
    plot_class_distribution(args.data_dir, args.output, args.dpi)
