# Changelog

This file lists the notable releases of the project.

## v1.0.0 - First public release

First complete version of the pneumonia detection project. It covers the whole
pipeline: data preparation, training on Google Colab, evaluation on the test
split, and Grad-CAM explainability, together with the documentation around it.

> This project is for educational and research use only. It is not a medical
> device and must not be used for diagnosis or any clinical decision. See the
> disclaimer in `README.md`.

### What is included

- A transfer-learning classifier (ResNet-50 from `timm`, pretrained on ImageNet)
  that separates chest X-rays into Normal and Pneumonia.
- A Colab training notebook (`notebooks/colab_training.ipynb`) that runs end to
  end on a fresh session.
- Evaluation code under `src/evaluation/` and the metrics reported on the
  held-out test split.
- Grad-CAM figures and error galleries under `artifacts/figures/`.
- Hyperparameters kept in config files under `configs/` instead of hardcoded in
  the notebook.
- Full documentation under `docs/` (dataset, metrics, risks, reproducibility,
  deployment plan, explainability, and more).

### Final test-set metrics

Model: ResNet-50, image size 224x224, decision threshold 0.5, evaluated on the
test split (624 images). Full details in `docs/METRICS.md`.

| Metric | Value |
|---|---|
| Accuracy | 0.8654 |
| Precision | 0.8355 |
| Sensitivity / Recall | 0.9769 |
| Specificity | 0.6795 |
| ROC AUC | 0.9626 |

Confusion matrix (TN / FP / FN / TP): 159 / 75 / 9 / 381. The model misses very
few pneumonia cases (9 false negatives) but flags a fair number of normal cases
as pneumonia (75 false positives). For this task that is the safer direction to
err in, but the low specificity is still a real limitation.

### Dataset

Chest X-Ray Images (Pneumonia) by Kermany et al., Kaggle version v2
(Mendeley DOI 10.17632/rscbjbr9sj.2). 5,856 images in total
(train 5,216 / val 16 / test 624). The dataset is not stored in this repo; see
`docs/DATASET.md` and `data/README.md` for how to get it and where to put it.

### Known limitations

- The data comes from a single hospital (Guangzhou), so results will not
  transfer directly to other populations or imaging equipment.
- The validation split is tiny (8 images per class), so validation metrics are
  noisy and should not be over-interpreted.
- Specificity is around 0.68, meaning a lot of false positives.
- No shareable trained checkpoint is published yet (see below).
- The full list is in `docs/RISKS_AND_LIMITATIONS.md`.

### Not shipped yet

- The trained model weights are not committed (too large for git) and are not
  yet uploaded to the Hugging Face Hub.
- The Gradio demo and the Hugging Face model page are planned but not live.

`docs/RELEASE_CHECKLIST.md` has the exact steps to tag this release and, if
wanted, to publish the weights and the demo later.
