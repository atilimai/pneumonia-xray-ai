# Risks and Limitations

This document records known risks and limitations of the Pneumonia Detection project. These should be considered throughout development and disclosed in any public-facing outputs.

---

## 1. Data Leakage

**Risk:** The Kermany et al. dataset has a known history of near-duplicate images appearing across train, validation, and test splits. If this is not addressed, evaluation metrics may be inflated.

**Mitigation:** Respect the original split boundaries without shuffling across sets. Consider auditing for duplicates if evaluation results appear suspiciously high.

---

## 2. Overfitting

**Risk:** The training set is small relative to the model capacity of large pretrained networks. The model may memorize training examples rather than learn generalizable features.

**Mitigation:** Use data augmentation, dropout regularization, early stopping, and monitor validation loss throughout training.

---

## 3. Misleading Visual Explanations (Grad-CAM)

**Risk:** Grad-CAM heatmaps may highlight spurious or non-clinical features, such as image labels, borders, or scanning artifacts, rather than lung pathology. This can create a false sense of model interpretability.

**Mitigation:** Critically inspect heatmaps. Include examples of both plausible and implausible activations in the report. Do not claim clinical reliability for any heatmap output.

---

## 4. Weak Generalization

**Risk:** The dataset was collected from a single clinical setting, Guangzhou Women and Children's Medical Center. The model may not generalize to X-rays from other populations, equipment types, or imaging protocols.

**Mitigation:** Document this limitation clearly in the model card and project README. Do not claim broad clinical applicability.

---

## 5. Class Imbalance

**Risk:** The training set contains approximately three times as many pneumonia cases as normal cases. A naive classifier could achieve high accuracy by predicting pneumonia for most inputs.

**Mitigation:** Use a weighted loss function, class weighting, or oversampling when appropriate. Evaluate using sensitivity, specificity, precision, recall, and ROC AUC instead of relying only on accuracy.

---

## 6. Medical Misuse

**Risk:** A publicly available demo or model could be misused by individuals attempting to self-diagnose or diagnose others without clinical expertise.

**Mitigation:** Include a prominent disclaimer on all public-facing outputs. Label the project clearly as a research and educational tool. Do not design the demo to resemble a clinical application.

---

## 7. Google Colab Instability

**Risk:** Colab sessions may disconnect after periods of inactivity or when resource limits are reached. Long training runs may be interrupted without saving the latest checkpoint.

**Mitigation:** Save checkpoints frequently during training. Use persistent storage such as Google Drive or Hugging Face Hub for important outputs. Keep the best checkpoint separately from periodic checkpoints.

---

## 8. Small Validation Split

**Risk:** The Kaggle dataset contains a very small validation split, with only a few images per class. This makes validation metrics unstable and highly sensitive to individual samples.

**Mitigation:** Avoid overinterpreting validation metrics. Use the validation split mainly for development monitoring and reserve the held-out test split for final evaluation. Clearly state which split is used when reporting metrics.

---

## 9. FAST_DEV_RUN Results Are Not Final Performance

**Risk:** The Colab training notebook includes `FAST_DEV_RUN = True` for quick end-to-end verification. This mode uses a small subset of the dataset and only one epoch, so the generated metrics are not representative of final model performance.

**Mitigation:** Use `FAST_DEV_RUN = True` only to confirm that the notebook runs successfully. For real training, set `FAST_DEV_RUN = False` so the full dataset and configured number of epochs are used. Do not report FAST_DEV_RUN metrics as final results.

---

## 10. Kaggle API Token Security

**Risk:** The Colab notebook requires a Kaggle API token to download the dataset. If the token is written directly into notebook cells, outputs, or committed files, it could be exposed publicly.

**Mitigation:** Enter the token only when prompted during runtime. Never commit `kaggle.json`, raw API tokens, or token-containing notebook outputs to GitHub. Revoke and regenerate any token that may have been exposed.

---

## 11. Notebook and Runtime Reproducibility Limits

**Risk:** A notebook may run successfully in one Colab session but fail later due to dependency changes, GPU availability, runtime resets, or changes in external services such as Kaggle downloads.

**Mitigation:** Keep dependencies documented and pinned when possible. Use configuration files for hyperparameters. Record runtime assumptions, dataset source, and generated artifacts. Accept that exact bit-level reproducibility may not be possible across different GPU hardware or CUDA versions.

---

## 12. Dataset Access Dependency

**Risk:** The project depends on downloading the chest X-ray dataset from Kaggle. If the dataset page changes, the Kaggle API token is unavailable, or Kaggle access is restricted, the training notebook may fail to run.

**Mitigation:** Document the dataset source clearly. Keep the expected dataset folder contract in `data/README.md` and `docs/DATASET.md`. If necessary, allow users to manually place the dataset under the expected `data/raw/chest_xray/` structure.

---

## 13. Checkpoint and Artifact Storage Risk

**Risk:** Model checkpoints, logs, and generated figures may be lost if they are saved only inside temporary Colab runtime storage.

**Mitigation:** Save important outputs to persistent locations such as Google Drive, Hugging Face Hub, or committed artifact folders when appropriate. Check that expected outputs exist after each training run.

---

## 14. Demo Model Loading Risk

**Risk:** The planned demo depends on loading a trained checkpoint from Hugging Face Hub or a bundled fallback checkpoint. If the checkpoint, architecture config, or preprocessing settings do not match, demo predictions may be incorrect or fail at runtime.

**Mitigation:** Document the checkpoint source, model architecture, preprocessing settings, and class mapping. Load the model once at application startup and verify that the checkpoint matches the selected architecture before demo release.

---

## 15. Evaluation Threshold Risk

**Risk:** The default decision threshold of `0.5` may not be optimal for pneumonia detection, especially because false negatives may be more harmful than false positives.

**Mitigation:** Use `0.5` as the default threshold unless an alternative threshold is selected using validation data and documented before final test evaluation. Do not tune the decision threshold using the test set.

---

## 16. Educational Scope Limitation

**Risk:** The project may be misunderstood as a deployable clinical pneumonia detection tool.

**Mitigation:** State clearly in the README, demo interface, model card, and reports that the project is for research and educational purposes only. The model is not a medical device, has not been clinically validated, and must not be used for diagnosis, treatment decisions, or any clinical workflow.
