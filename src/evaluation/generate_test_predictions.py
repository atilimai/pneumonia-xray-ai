from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
import timm
import torch
from PIL import Image
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms


CLASS_TO_LABEL = {
    "NORMAL": 0,
    "PNEUMONIA": 1,
}


class ChestXrayTestDataset(Dataset):
    def __init__(self, data_dir: Path, image_size: int):
        self.samples = []

        self.transform = transforms.Compose(
            [
                transforms.Resize((image_size, image_size)),
                transforms.ToTensor(),
                transforms.Normalize(
                    mean=[0.485, 0.456, 0.406],
                    std=[0.229, 0.224, 0.225],
                ),
            ]
        )

        for class_name, label in CLASS_TO_LABEL.items():
            class_dir = data_dir / class_name

            if not class_dir.exists():
                raise FileNotFoundError(f"Missing class directory: {class_dir}")

            for image_path in sorted(class_dir.glob("*")):
                if image_path.suffix.lower() in {".jpg", ".jpeg", ".png"}:
                    self.samples.append((image_path, label))

        if not self.samples:
            raise RuntimeError(f"No test images found under: {data_dir}")

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, index):
        image_path, label = self.samples[index]
        image = Image.open(image_path).convert("RGB")
        image = self.transform(image)

        return image, label, str(image_path)


def load_checkpoint_model(checkpoint_path: Path, device: torch.device):
    checkpoint = torch.load(checkpoint_path, map_location=device)

    model_name = checkpoint.get("model_name", "tf_efficientnetv2_s")
    image_size = checkpoint.get("image_size", 224)

    model = timm.create_model(
        model_name,
        pretrained=False,
        num_classes=1,
    )

    model.load_state_dict(checkpoint["model_state_dict"])
    model.to(device)
    model.eval()

    return model, model_name, image_size


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate test predictions CSV.")

    parser.add_argument(
        "--data-dir",
        type=str,
        default="data/raw/chest_xray/test",
        help="Path to test split folder.",
    )
    parser.add_argument(
        "--checkpoint",
        type=str,
        default="artifacts/checkpoints/best_model.pt",
        help="Path to trained model checkpoint.",
    )
    parser.add_argument(
        "--output-csv",
        type=str,
        default="artifacts/predictions/test_predictions.csv",
        help="Path to output predictions CSV.",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=32,
        help="Batch size for inference.",
    )

    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    checkpoint_path = Path(args.checkpoint)
    output_csv = Path(args.output_csv)

    if not checkpoint_path.exists():
        raise FileNotFoundError(f"Checkpoint not found: {checkpoint_path}")

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    model, model_name, image_size = load_checkpoint_model(checkpoint_path, device)

    print(f"Loaded model: {model_name}")
    print(f"Image size: {image_size}")

    dataset = ChestXrayTestDataset(data_dir=data_dir, image_size=image_size)

    loader = DataLoader(
        dataset,
        batch_size=args.batch_size,
        shuffle=False,
        num_workers=0,
    )

    rows = []

    with torch.no_grad():
        for images, labels, image_paths in loader:
            images = images.to(device)

            logits = model(images).squeeze(1)
            probs = torch.sigmoid(logits).cpu().numpy()

            for image_path, y_true, y_prob in zip(image_paths, labels.numpy(), probs):
                rows.append(
                    {
                        "image_path": image_path,
                        "y_true": int(y_true),
                        "y_prob": float(y_prob),
                    }
                )

    output_csv.parent.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame(rows)
    df.to_csv(output_csv, index=False)

    print(f"Saved predictions to: {output_csv}")
    print(f"Rows: {len(df)}")
    print(df.head())


if __name__ == "__main__":
    main()