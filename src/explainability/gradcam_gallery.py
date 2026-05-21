from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch
from PIL import Image
from torch import nn

try:
    import timm
except ImportError:  # pragma: no cover - only needed for the CLI checkpoint path
    timm = None


IMAGENET_MEAN = (0.485, 0.456, 0.406)
IMAGENET_STD = (0.229, 0.224, 0.225)
CLASS_NAMES = {0: "NORMAL", 1: "PNEUMONIA"}


@dataclass(frozen=True)
class GradCAMSample:
    image_path: Path
    y_true: int
    y_prob: float
    y_pred: int
    outcome: str


class GradCAM:
    """Minimal Grad-CAM implementation for CNN image classifiers."""

    def __init__(self, model: nn.Module, target_layer: nn.Module) -> None:
        self.model = model
        self.target_layer = target_layer
        self.activations: torch.Tensor | None = None
        self.gradients: torch.Tensor | None = None
        self._handles = [
            target_layer.register_forward_hook(self._save_activations),
            target_layer.register_full_backward_hook(self._save_gradients),
        ]

    def _save_activations(self, _module: nn.Module, _inputs: tuple[torch.Tensor, ...], output: torch.Tensor) -> None:
        self.activations = output.detach()

    def _save_gradients(
        self,
        _module: nn.Module,
        _grad_input: tuple[torch.Tensor, ...],
        grad_output: tuple[torch.Tensor, ...],
    ) -> None:
        self.gradients = grad_output[0].detach()

    def close(self) -> None:
        for handle in self._handles:
            handle.remove()

    def __enter__(self) -> "GradCAM":
        return self

    def __exit__(self, _exc_type, _exc_value, _traceback) -> None:
        self.close()

    def generate(self, image_tensor: torch.Tensor, target_class: int) -> np.ndarray:
        self.model.zero_grad(set_to_none=True)
        logits = self.model(image_tensor)
        score = _class_score(logits, target_class)
        score.backward()

        if self.activations is None or self.gradients is None:
            raise RuntimeError("Grad-CAM hooks did not capture activations and gradients.")

        activations = self.activations[0]
        gradients = self.gradients[0]
        weights = gradients.mean(dim=(1, 2), keepdim=True)
        heatmap = torch.relu((weights * activations).sum(dim=0))
        heatmap = heatmap.cpu().numpy()

        heatmap_min = float(heatmap.min())
        heatmap_max = float(heatmap.max())
        if heatmap_max <= heatmap_min:
            return np.zeros_like(heatmap, dtype=np.float32)

        return ((heatmap - heatmap_min) / (heatmap_max - heatmap_min)).astype(np.float32)


def _class_score(logits: torch.Tensor, target_class: int) -> torch.Tensor:
    if logits.ndim == 1:
        logits = logits.unsqueeze(0)

    if logits.shape[1] == 1:
        # Binary single-logit models represent P(PNEUMONIA). Negating the logit
        # gives a useful target score for NORMAL examples.
        return logits[:, 0].sum() if target_class == 1 else (-logits[:, 0]).sum()

    return logits[:, target_class].sum()


def find_last_conv_layer(model: nn.Module) -> tuple[str, nn.Module]:
    candidates = [(name, module) for name, module in model.named_modules() if isinstance(module, nn.Conv2d)]
    if not candidates:
        raise ValueError("No Conv2d layer found. Pass --target-layer for a compatible model layer.")
    return candidates[-1]


def get_module_by_name(model: nn.Module, name: str) -> nn.Module:
    modules = dict(model.named_modules())
    if name not in modules:
        raise ValueError(f"Target layer '{name}' not found in model.")
    return modules[name]


def load_image_array(path: Path, image_size: int | Sequence[int]) -> np.ndarray:
    size = _normalize_image_size(image_size)
    image = Image.open(path).convert("RGB").resize(size, Image.LANCZOS)
    return np.asarray(image, dtype=np.float32) / 255.0


def image_to_tensor(image: np.ndarray, device: torch.device | str) -> torch.Tensor:
    tensor = torch.from_numpy(image.transpose(2, 0, 1)).float()
    mean = torch.tensor(IMAGENET_MEAN, dtype=tensor.dtype).view(3, 1, 1)
    std = torch.tensor(IMAGENET_STD, dtype=tensor.dtype).view(3, 1, 1)
    tensor = (tensor - mean) / std
    return tensor.unsqueeze(0).to(device)


def overlay_heatmap(image: np.ndarray, heatmap: np.ndarray, alpha: float = 0.45) -> np.ndarray:
    height, width = image.shape[:2]
    heatmap_image = Image.fromarray((heatmap * 255).astype(np.uint8)).resize((width, height), Image.BILINEAR)
    heatmap_resized = np.asarray(heatmap_image, dtype=np.float32) / 255.0
    heatmap_rgb = plt.get_cmap("jet")(heatmap_resized)[..., :3]
    overlay = (1.0 - alpha) * image + alpha * heatmap_rgb
    return np.clip(overlay, 0.0, 1.0)


def select_true_positive_true_negative_samples(
    predictions: pd.DataFrame,
    threshold: float = 0.5,
    samples_per_class: int = 5,
) -> list[GradCAMSample]:
    required_columns = {"image_path", "y_true", "y_prob"}
    missing = required_columns - set(predictions.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    df = predictions.copy()
    df["y_pred"] = (df["y_prob"].astype(float) >= threshold).astype(int)

    selected: list[GradCAMSample] = []
    for label, outcome in [(1, "TP"), (0, "TN")]:
        subset = df[(df["y_true"].astype(int) == label) & (df["y_pred"] == label)].copy()
        if subset.empty:
            raise ValueError(f"No {outcome} samples found at threshold {threshold}.")

        subset["confidence"] = np.where(label == 1, subset["y_prob"], 1.0 - subset["y_prob"])
        subset = subset.sort_values("confidence", ascending=False).head(samples_per_class)
        for row in subset.itertuples(index=False):
            selected.append(
                GradCAMSample(
                    image_path=Path(row.image_path),
                    y_true=int(row.y_true),
                    y_prob=float(row.y_prob),
                    y_pred=int(row.y_pred),
                    outcome=outcome,
                )
            )

    return selected


def create_gradcam_gallery(
    model: nn.Module,
    samples: Iterable[GradCAMSample],
    output_path: Path,
    target_layer: nn.Module | None = None,
    image_size: int | Sequence[int] = 224,
    device: torch.device | str = "cpu",
    dpi: int = 160,
) -> None:
    samples_by_outcome = {
        "TP": [sample for sample in samples if sample.outcome == "TP"],
        "TN": [sample for sample in samples if sample.outcome == "TN"],
    }
    if not samples_by_outcome["TP"] or not samples_by_outcome["TN"]:
        raise ValueError("Grad-CAM gallery requires at least one TP and one TN sample.")

    model = model.to(device)
    model.eval()
    layer = target_layer if target_layer is not None else find_last_conv_layer(model)[1]

    samples_per_row = max(len(samples_by_outcome["TP"]), len(samples_by_outcome["TN"]))
    columns = samples_per_row * 2
    fig, axes = plt.subplots(2, columns, figsize=(samples_per_row * 4.2, 5.8), squeeze=False)
    for ax in axes.flat:
        ax.axis("off")

    with GradCAM(model, layer) as gradcam:
        for row_index, outcome in enumerate(["TP", "TN"]):
            row_samples = samples_by_outcome[outcome]
            for sample_index in range(samples_per_row):
                original_ax = axes[row_index][sample_index * 2]
                overlay_ax = axes[row_index][sample_index * 2 + 1]
                if sample_index >= len(row_samples):
                    continue

                sample = row_samples[sample_index]
                image = load_image_array(sample.image_path, image_size=image_size)
                image_tensor = image_to_tensor(image, device=device)
                heatmap = gradcam.generate(image_tensor, target_class=sample.y_pred)
                overlay = overlay_heatmap(image, heatmap)

                label = CLASS_NAMES.get(sample.y_pred, str(sample.y_pred))
                confidence = sample.y_prob if sample.y_pred == 1 else 1.0 - sample.y_prob
                original_ax.imshow(image)
                original_ax.set_title(f"{outcome} {label}\nOriginal", fontsize=8)
                overlay_ax.imshow(overlay)
                overlay_ax.set_title(f"Grad-CAM\nconf={confidence:.3f}", fontsize=8)

    fig.suptitle("Grad-CAM Gallery: True Positives and True Negatives", fontsize=14, fontweight="bold", y=0.97)
    fig.tight_layout(rect=(0, 0, 1, 0.91), h_pad=1.8, w_pad=1.0)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=dpi, bbox_inches="tight")
    plt.close(fig)


def build_timm_model(model_name: str, num_classes: int, checkpoint_path: Path, device: torch.device | str) -> nn.Module:
    if timm is None:
        raise ImportError("timm is required to load a checkpoint from --model-name.")

    model = timm.create_model(model_name, pretrained=False, num_classes=num_classes)
    checkpoint = torch.load(checkpoint_path, map_location=device)
    state_dict = _extract_state_dict(checkpoint)
    model.load_state_dict(state_dict)
    return model


def _extract_state_dict(checkpoint: object) -> dict[str, torch.Tensor]:
    if isinstance(checkpoint, dict):
        for key in ("model_state_dict", "state_dict", "model"):
            value = checkpoint.get(key)
            if isinstance(value, dict):
                checkpoint = value
                break

    if not isinstance(checkpoint, dict):
        raise ValueError("Checkpoint must contain a PyTorch state_dict.")

    state_dict = {}
    for key, value in checkpoint.items():
        clean_key = key.removeprefix("module.")
        state_dict[clean_key] = value
    return state_dict


def _normalize_image_size(image_size: int | Sequence[int]) -> tuple[int, int]:
    if isinstance(image_size, int):
        return (image_size, image_size)
    if len(image_size) != 2:
        raise ValueError("image_size must be an int or a sequence of two ints.")
    return (int(image_size[1]), int(image_size[0]))


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a Grad-CAM TP/TN gallery.")
    parser.add_argument("--predictions-csv", required=True, help="CSV with image_path, y_true, and y_prob columns.")
    parser.add_argument("--checkpoint", required=True, help="Path to a PyTorch model checkpoint.")
    parser.add_argument("--model-name", default="tf_efficientnetv2_s", help="timm model architecture name.")
    parser.add_argument("--num-classes", type=int, default=1, help="Model output classes. Use 1 for BCE logits.")
    parser.add_argument("--target-layer", default=None, help="Optional target layer name. Defaults to last Conv2d.")
    parser.add_argument("--threshold", type=float, default=0.5, help="Decision threshold for y_prob.")
    parser.add_argument("--samples-per-class", type=int, default=5, help="Number of TP and TN examples to include.")
    parser.add_argument("--image-size", type=int, default=224, help="Square image size used during evaluation.")
    parser.add_argument("--output", default="artifacts/figures/gradcam_gallery.png", help="Output PNG path.")
    parser.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu", help="Torch device.")
    args = parser.parse_args()

    device = torch.device(args.device)
    predictions = pd.read_csv(args.predictions_csv)
    samples = select_true_positive_true_negative_samples(
        predictions,
        threshold=args.threshold,
        samples_per_class=args.samples_per_class,
    )
    model = build_timm_model(args.model_name, args.num_classes, Path(args.checkpoint), device=device)
    target_layer = get_module_by_name(model, args.target_layer) if args.target_layer else None

    create_gradcam_gallery(
        model,
        samples,
        output_path=Path(args.output),
        target_layer=target_layer,
        image_size=args.image_size,
        device=device,
    )
    print(f"Grad-CAM gallery saved to: {args.output}")


if __name__ == "__main__":
    main()
