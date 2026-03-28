# Pneumonia Detection from Chest X-Rays

A machine learning project for binary classification of chest X-ray images as **Pneumonia** or **Normal**, using deep learning with transfer learning.

> ⚠️ **Medical Disclaimer:** This is a research and educational project. It is **not** a medical product, clinical decision support system, or diagnostic tool. Do not use model outputs for any medical purpose.

---

## Problem Statement

Pneumonia is a serious lung infection that can be life-threatening, especially in children and elderly patients. Chest X-ray imaging is one of the primary diagnostic tools used by clinicians. This project explores whether a convolutional neural network trained on a publicly available dataset can reliably distinguish pneumonia from normal lung X-rays.

---

## Dataset

- **Source:** [Kaggle — Chest X-Ray Images (Pneumonia)](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia) by Kermany et al.
- **Labels:** Binary — `PNEUMONIA` / `NORMAL`
- **Format:** JPEG images organized into `train`, `val`, and `test` splits

> 🚫 **Dataset files must not be committed to this repository.** See `data/README.md` for folder structure expectations.

---

## Project Goal

Build a binary image classifier that:
1. Achieves clinically meaningful sensitivity and specificity on the test split
2. Provides visual explanations via Grad-CAM heatmaps
3. Is reproducible, documented, and shareable via GitHub

---

## Planned Approach

| Area | Plan |
|---|---|
| **Model** | Transfer learning with EfficientNet or ResNet (via `timm`) |
| **Training** | Google Colab (GPU runtime) |
| **Evaluation** | Sensitivity, Specificity, ROC AUC, Confusion Matrix |
| **Explainability** | Grad-CAM heatmaps for qualitative interpretation |
| **Publishing** | GitHub repository; optional Hugging Face model page and demo |

---

## Repository Structure

```
.
├── README.md
├── LICENSE
├── .gitignore
├── pyproject.toml
├── requirements.txt
├── PROJECT_OVERVIEW.md
├── ROADMAP.md
├── data/                        # Dataset folders (files NOT committed)
│   ├── raw/                     # Original downloaded data
│   ├── interim/                 # Intermediate transformations
│   ├── processed/               # Final preprocessed data
│   └── external/                # Any external reference data
├── notebooks/                   # Jupyter / Colab notebooks
├── src/                         # Source modules (data, models, training, eval, etc.)
├── configs/                     # Experiment configuration files
├── artifacts/                   # Generated outputs (logs, checkpoints, figures)
├── app/                         # Future lightweight demo application
├── docs/                        # Project documentation and issue drafts
├── tests/                       # Unit and integration tests
└── .github/                     # Issue templates and PR template
```

---

## Metrics (Planned)

- Accuracy
- Precision / Recall
- Sensitivity (True Positive Rate)
- Specificity (True Negative Rate)
- ROC AUC
- Confusion Matrix

See [`docs/METRICS.md`](docs/METRICS.md) for details.

---

## Explainability (Planned)

Grad-CAM will be used to produce heatmap overlays highlighting regions of the X-ray that most influenced the model's prediction. This is intended for qualitative inspection only. See [`docs/EXPLAINABILITY.md`](docs/EXPLAINABILITY.md).

---

## Training Environment (Planned)

Training will be conducted on Google Colab using GPU runtimes. Notebooks in `notebooks/` will contain the full training workflow.

---

## Release Plan (Planned)

- GitHub repository with all code, configs, and documentation
- Model artifacts linked or stored via Git LFS / Hugging Face Hub
- Optional: Hugging Face model page and Gradio demo Space

---

## Getting Started

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Download the dataset from Kaggle and place it under `data/raw/` (see `data/README.md`)
4. Open notebooks in `notebooks/` to follow the workflow

---

## License

See [LICENSE](LICENSE).
