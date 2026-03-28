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

**Risk:** Grad-CAM heatmaps may highlight spurious or non-clinical features (e.g., image labels, borders, scanning artifacts) rather than lung pathology. This can create a false sense of model interpretability.

**Mitigation:** Critically inspect heatmaps. Include examples of both plausible and implausible activations in the report. Do not claim clinical reliability for any heatmap output.

---

## 4. Weak Generalization

**Risk:** The dataset was collected from a single clinical setting (Guangzhou Women and Children's Medical Center). The model may not generalize to X-rays from other populations, equipment types, or imaging protocols.

**Mitigation:** Document this limitation clearly in the model card and project README. Do not claim broad clinical applicability.

---

## 5. Class Imbalance

**Risk:** The training set contains approximately three times as many pneumonia cases as normal cases. A naive classifier could achieve high accuracy by predicting pneumonia for all inputs.

**Mitigation:** Use a weighted loss function or oversampling. Evaluate using sensitivity and specificity separately, not just accuracy.

---

## 6. Medical Misuse

**Risk:** A publicly available demo or model could be misused by individuals attempting to self-diagnose or diagnose others without clinical expertise.

**Mitigation:** Include a prominent disclaimer on all public-facing outputs. Label the project clearly as a research and educational tool. Do not design the demo to resemble a clinical application.

---

## 7. Google Colab Instability

**Risk:** Colab sessions disconnect after periods of inactivity or when resource limits are reached. Long training runs may be interrupted without saving the latest checkpoint.

**Mitigation:** Save checkpoints frequently during training. Use Colab Pro or alternative persistent storage (e.g., Google Drive) to avoid losing progress.
