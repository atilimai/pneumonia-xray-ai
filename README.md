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

## Project Approach

| Area | Plan |
|---|---|
| **Model** | Transfer learning with ResNet-50 (via `timm`), ImageNet pretrained |
| **Training** | Google Colab (GPU runtime) |
| **Evaluation** | Sensitivity, Specificity, ROC AUC, Confusion Matrix |
| **Explainability** | Grad-CAM heatmaps for qualitative interpretation |
| **Publishing** | GitHub repository; optional Hugging Face model page and demo |

---

## Repository Structure


.
├── README.md
├── LICENSE
├── .gitignore
├── pyproject.toml
├── requirements.txt
├── PROJECT_OVERVIEW.md
├── ROADMAP.md
├── data/ # Dataset folders (files NOT committed)
│ ├── raw/ # Original downloaded data
│ ├── interim/ # Intermediate transformations
│ ├── processed/ # Final preprocessed data
│ └── external/ # Any external reference data
├── notebooks/ # Jupyter / Colab notebooks
├── src/ # Source modules (data, models, training, eval, etc.)
├── configs/ # Experiment configuration files
├── artifacts/ # Generated outputs (logs, checkpoints, figures)
├── app/ # Demo application resources
├── docs/ # Project documentation and issue drafts
├── tests/ # Unit and integration tests
└── .github/ # Issue templates and PR template


---

## Evaluation Metrics

- Accuracy
- Precision / Recall
- Sensitivity (True Positive Rate)
- Specificity (True Negative Rate)
- ROC AUC
- Confusion Matrix

See [`docs/METRICS.md`](docs/METRICS.md) for details.

---

## Results

Final results on the held-out test split (624 images), ResNet-50 at decision
threshold 0.5:

| Metric | Value |
|---|---|
| Accuracy | 0.8654 |
| Precision | 0.8355 |
| Sensitivity / Recall | 0.9769 |
| Specificity | 0.6795 |
| ROC AUC | 0.9626 |

Confusion matrix (TN / FP / FN / TP): 159 / 75 / 9 / 381. The model catches almost
all pneumonia cases (9 false negatives) but flags a number of normal X-rays as
pneumonia (75 false positives). Full write-up in
[`docs/METRICS.md`](docs/METRICS.md) and [`CHANGELOG.md`](CHANGELOG.md).

---

## Explainability

Grad-CAM will be used to produce heatmap overlays highlighting regions of the X-ray that most influenced the model's prediction. This is intended for qualitative inspection only. See [`docs/EXPLAINABILITY.md`](docs/EXPLAINABILITY.md).

---

## Training Environment

Training will be conducted on Google Colab using GPU runtimes. Notebooks in `notebooks/` will contain the full training workflow.

---

## Medical Disclaimer

This project is intended for educational and research purposes only.

The pneumonia detection model, generated predictions, visualizations, metrics, Grad-CAM heatmaps, and any related outputs are not medical devices and must not be used for clinical diagnosis, treatment decisions, patient triage, medical screening, patient care, or replacing professional medical judgment.

Model predictions may be inaccurate, biased, incomplete, or limited by the dataset, preprocessing choices, training procedure, evaluation setup, and model architecture.

Any interpretation of chest X-ray images must be performed by qualified healthcare professionals. This project does not provide medical advice. If there is any concern about pneumonia or any other medical condition, consult a licensed medical professional.

---

## Release

- Release notes: [`CHANGELOG.md`](CHANGELOG.md)
- Release steps and current status: [`docs/RELEASE_CHECKLIST.md`](docs/RELEASE_CHECKLIST.md)
- Model card (ready for Hugging Face): [`MODEL_CARD.md`](MODEL_CARD.md)

The GitHub repository is the main deliverable. Publishing the trained weights on
the Hugging Face Hub and deploying a Gradio demo are optional next steps and are
not live yet.

---

## Demo

A Gradio demo on Hugging Face Spaces is planned but not deployed yet. When it goes
live, the link will be added here and in [`app/README.md`](app/README.md), and the
demo will carry the same medical disclaimer shown above.

---

## Getting Started

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Download the dataset from Kaggle and place it under `data/raw/` (see `data/README.md`)
4. Open notebooks in `notebooks/` to follow the workflow

---

## License

See [LICENSE](LICENSE). Released under GPL-3.0.
