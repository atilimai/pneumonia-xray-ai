---
license: gpl-3.0
tags:
  - image-classification
  - medical-imaging
  - chest-xray
  - pneumonia
  - pytorch
  - timm
library_name: timm
pipeline_tag: image-classification
---

# Model Card - Pneumonia Detection from Chest X-Rays

This file is written so it can be used directly as the `README.md` of the
Hugging Face model repository. Until the weights are uploaded, it lives in the
GitHub repo as `MODEL_CARD.md`.

> **Medical disclaimer:** This model is for educational and research purposes
> only. It is not a medical device, it has not been clinically validated, and it
> must not be used for diagnosis, screening, triage, or any medical decision.
> Always consult a qualified healthcare professional.

## Model description

A binary image classifier that labels a chest X-ray as `NORMAL` or `PNEUMONIA`.
It is a ResNet-50 backbone from the `timm` library, initialized with ImageNet
pretrained weights, with the classification head adapted for two classes and
fine-tuned on the Kermany et al. chest X-ray dataset.

- Architecture: ResNet-50 (`timm`, `resnet50`)
- Pretrained weights: ImageNet
- Input: RGB chest X-ray resized to 224x224
- Output: 2 classes (`NORMAL`, `PNEUMONIA`)
- Decision threshold: 0.5

## Intended use

- Learning and demonstration of transfer learning on medical images.
- Showing an explainability workflow (Grad-CAM) on X-ray data.

Out of scope: any real clinical use, self-diagnosis, or use as a second opinion
in patient care.

## Training data

Chest X-Ray Images (Pneumonia), Kermany et al., Kaggle version v2
(Mendeley DOI `10.17632/rscbjbr9sj.2`).

| Split | NORMAL | PNEUMONIA | Total |
|---|---|---|---|
| Train | 1341 | 3875 | 5216 |
| Val | 8 | 8 | 16 |
| Test | 234 | 390 | 624 |

The training set is imbalanced (about 2.9x more pneumonia than normal). The
original train/val/test split is kept as-is to avoid leakage. More detail in
`docs/DATASET.md` of the GitHub repo.

## Training setup

- Optimizer: AdamW, learning rate 0.001, weight decay 0.0001
- Scheduler: cosine annealing
- Batch size: 32
- Epochs: up to 50 with early stopping
- Augmentation: horizontal flip, small rotation
- Trained on Google Colab (T4 GPU)

Hyperparameters are stored in `configs/` in the GitHub repo, not hardcoded.

## Evaluation

Measured on the held-out test split (624 images) at threshold 0.5.

| Metric | Value |
|---|---|
| Accuracy | 0.8654 |
| Precision | 0.8355 |
| Sensitivity / Recall | 0.9769 |
| Specificity | 0.6795 |
| ROC AUC | 0.9626 |

Confusion matrix: TN 159, FP 75, FN 9, TP 381. The model catches almost all
pneumonia cases but produces a fair number of false positives on normal X-rays.

## Limitations

- Data is from a single hospital, so it does not generalize to other populations
  or scanners.
- The validation split is very small, so validation numbers are unstable.
- Specificity is low (~0.68); many normal cases are flagged as pneumonia.
- Grad-CAM heatmaps can highlight non-clinical areas (borders, labels), so they
  are not proof of what the model "understands".
- See `docs/RISKS_AND_LIMITATIONS.md` for the full list.

## How to use

Once the weights are published, the model can be loaded with `timm` and the
saved `state_dict`:

```python
import timm, torch

model = timm.create_model("resnet50", pretrained=False, num_classes=2)
model.load_state_dict(torch.load("best_model.pt", map_location="cpu"))
model.eval()
```

Preprocess input as RGB, resized to 224x224, with ImageNet normalization, to
match training.

## License

Code: GPL-3.0 (see the repository `LICENSE`). The dataset keeps its original
Creative Commons non-commercial terms from Kaggle / Mendeley; review those
before redistributing any data.
