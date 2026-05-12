from __future__ import annotations

from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd
import torch
from PIL import Image
from torch import nn

matplotlib.use("Agg")

from src.explainability.gradcam_gallery import (
    create_gradcam_gallery,
    select_true_positive_true_negative_samples,
)


class TinyCNN(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 4, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(4, 4, kernel_size=3, padding=1),
            nn.ReLU(),
        )
        self.pool = nn.AdaptiveAvgPool2d(1)
        self.classifier = nn.Linear(4, 1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.features(x)
        x = self.pool(x).flatten(1)
        return self.classifier(x)


def _write_test_image(path: Path, value: int) -> None:
    array = np.full((64, 64, 3), value, dtype=np.uint8)
    array[16:48, 24:40, :] = 255 - value
    Image.fromarray(array).save(path)


def test_gradcam_gallery_is_saved_for_true_positives_and_true_negatives(tmp_path: Path) -> None:
    image_paths = []
    for index, value in enumerate([20, 40, 180, 220]):
        path = tmp_path / f"image_{index}.png"
        _write_test_image(path, value)
        image_paths.append(path)

    predictions = pd.DataFrame(
        {
            "image_path": [str(path) for path in image_paths],
            "y_true": [1, 1, 0, 0],
            "y_prob": [0.95, 0.88, 0.08, 0.12],
        }
    )
    samples = select_true_positive_true_negative_samples(predictions, threshold=0.5, samples_per_class=2)

    output_path = tmp_path / "gradcam_gallery.png"
    create_gradcam_gallery(
        TinyCNN(),
        samples,
        output_path=output_path,
        image_size=64,
        device="cpu",
    )

    assert output_path.exists()
    assert output_path.stat().st_size > 0
