"""
Generate sample image grids for each class (NORMAL and PNEUMONIA).

Outputs:
    artifacts/figures/sample_grid_normal.png
    artifacts/figures/sample_grid_pneumonia.png

Usage:
    python src/visualization/sample_grid.py
    python src/visualization/sample_grid.py --data-dir data/raw/chest_xray --split train --grid 4 --dpi 150
"""

import argparse
import os
import random

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

CLASSES = ["NORMAL", "PNEUMONIA"]
OUTPUT_NAMES = {
    "NORMAL": "sample_grid_normal.png",
    "PNEUMONIA": "sample_grid_pneumonia.png",
}
TITLES = {
    "NORMAL": "Normal — Sample Chest X-Ray Images",
    "PNEUMONIA": "Pneumonia — Sample Chest X-Ray Images",
}


def load_image(path: str) -> np.ndarray:
    img = Image.open(path).convert("L")
    img = img.resize((224, 224), Image.LANCZOS)
    return np.array(img)


def get_image_paths(class_dir: str) -> list:
    if not os.path.isdir(class_dir):
        return []
    return [
        os.path.join(class_dir, f)
        for f in os.listdir(class_dir)
        if f.lower().endswith((".jpg", ".jpeg", ".png"))
    ]


def plot_sample_grid(
    data_dir: str = "data/raw/chest_xray",
    split: str = "train",
    grid_size: int = 4,
    output_dir: str = "artifacts/figures",
    dpi: int = 150,
    seed: int = 42,
) -> None:
    random.seed(seed)
    n_samples = grid_size * grid_size
    os.makedirs(output_dir, exist_ok=True)

    for cls in CLASSES:
        class_dir = os.path.join(data_dir, split, cls)
        paths = get_image_paths(class_dir)

        if not paths:
            raise FileNotFoundError(
                f"No images found at '{class_dir}'. "
                "Download the Kaggle chest X-ray dataset and place it at the expected path."
            )

        sample_paths = random.sample(paths, min(n_samples, len(paths)))

        fig, axes = plt.subplots(grid_size, grid_size, figsize=(grid_size * 2.5, grid_size * 2.5 + 1))
        fig.suptitle(TITLES[cls], fontsize=14, fontweight="bold", y=1.01)

        for ax, img_path in zip(axes.flat, sample_paths):
            img = load_image(img_path)
            ax.imshow(img, cmap="gray", vmin=0, vmax=255)
            ax.axis("off")

        # Hide any unused axes if fewer images than grid cells
        for ax in list(axes.flat)[len(sample_paths):]:
            ax.axis("off")

        plt.tight_layout()
        output_path = os.path.join(output_dir, OUTPUT_NAMES[cls])
        plt.savefig(output_path, dpi=dpi, bbox_inches="tight")
        plt.close()
        print(f"Saved: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate sample image grids per class.")
    parser.add_argument(
        "--data-dir",
        default="data/raw/chest_xray",
        help="Root directory of the chest_xray dataset (default: data/raw/chest_xray)",
    )
    parser.add_argument(
        "--split",
        default="train",
        choices=["train", "val", "test"],
        help="Dataset split to sample images from (default: train)",
    )
    parser.add_argument(
        "--grid",
        type=int,
        default=4,
        help="Grid size NxN — total N² images per class (default: 4)",
    )
    parser.add_argument(
        "--output-dir",
        default="artifacts/figures",
        help="Directory to save output figures (default: artifacts/figures)",
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=150,
        help="Figure resolution in DPI (default: 150)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for reproducibility (default: 42)",
    )
    args = parser.parse_args()

    plot_sample_grid(
        data_dir=args.data_dir,
        split=args.split,
        grid_size=args.grid,
        output_dir=args.output_dir,
        dpi=args.dpi,
        seed=args.seed,
    )
