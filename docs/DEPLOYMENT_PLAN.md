# Deployment Plan

This document outlines the planned approach for publishing and sharing the Pneumonia Detection project at the end of Week 5.

---

## 1. GitHub Repository Release

The primary delivery is the GitHub repository itself.

**Planned contents of the final GitHub release:**
- Clean, documented source code in `src/`
- Reproducible training notebook in `notebooks/`
- Final configuration files in `configs/`
- Evaluation report in `artifacts/reports/`
- Sample Grad-CAM figures in `artifacts/figures/`
- Complete `docs/` documentation

**Release tag:** A versioned GitHub Release (e.g., `v1.0.0`) will be created to mark the project milestone.

---

## 2. Model Artifacts

Model checkpoint files (`.pt` or `.pth`) are too large to commit directly to GitHub.

**Planned options:**
- Upload the best checkpoint to **Hugging Face Hub** as a model repository
- Alternatively, attach the checkpoint to a GitHub Release as a binary asset
- Document the checkpoint provenance (training config, dataset version, final metrics) in a model card

---

## 3. Optional: Hugging Face Model Page

A Hugging Face model repository may be created to host:
- The trained model checkpoint
- A `README.md` model card with:
  - Model description and training details
  - Evaluation metrics
  - Intended use and limitations
  - Medical disclaimer

---

## 4. Demo Model Loading Strategy

The lightweight demo will load the trained pneumonia classification model when the Gradio application starts.

### Primary Strategy: Hugging Face Hub

The preferred strategy is to upload the final trained checkpoint to the **Hugging Face Hub** and load it from there during demo startup.

This approach is preferred because:

- large model checkpoint files should not be committed directly to GitHub;
- Hugging Face Spaces integrates naturally with Hugging Face Hub;
- the demo repository can remain lightweight;
- the model checkpoint can be versioned and documented with a model card;
- checkpoint provenance, including training configuration and evaluation metrics, can be recorded clearly.

The demo should load the following items:

- trained model checkpoint;
- model architecture/configuration;
- preprocessing settings such as image size and normalization values;
- class label mapping.

Expected loading flow:

1. Initialize the selected model architecture.
2. Download or access the trained checkpoint from Hugging Face Hub.
3. Load the checkpoint weights into the model.
4. Set the model to evaluation mode.
5. Apply the same preprocessing pipeline used during training.
6. Run inference on the uploaded image.

### Fallback Strategy: Bundled Checkpoint

If Hugging Face Hub loading is not available during development, the demo may temporarily use a bundled local checkpoint.

Suggested fallback path:

```text
app/checkpoints/best_model.pt

---
## 5. Optional: Demo Application

A lightweight interactive demo may be deployed on **Hugging Face Spaces** using **Gradio**.

**Planned demo features:**
- Upload a chest X-ray image
- Receive a predicted label (Pneumonia / Normal) with confidence score
- See a Grad-CAM heatmap overlay
- Prominent disclaimer: educational use only, not a medical tool

---

## Constraints

- No deployment to production medical systems
- Any public demo must include a clear medical disclaimer
- Model weights shared publicly must reference the dataset license and usage terms
- The demo is optional and depends on project completion by Week 5

See [`docs/issues/10_demo_deployment_plan.md`](issues/10_demo_deployment_plan.md) for the deployment issue draft.
