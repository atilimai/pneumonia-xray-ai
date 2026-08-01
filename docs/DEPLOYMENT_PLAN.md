# Deployment Plan

This document outlines the approach for publishing and sharing the Pneumonia Detection project. The GitHub repository is the main deliverable and is ready; the Hugging Face model page and the Gradio demo are optional next steps that are not live yet (see the status notes below and `docs/RELEASE_CHECKLIST.md`).

---

## 1. GitHub Repository Release
The primary delivery is the GitHub repository itself, acting as the central codebase.

**Final contents of the GitHub release:**
- Clean, documented source code in `src/`
- Reproducible training notebook in `notebooks/`
- Final configuration files in `configs/`
- Evaluation report in `artifacts/reports/`
- Sample Grad-CAM figures in `artifacts/figures/`
- Complete `docs/` documentation

---

## 2. Model Artifacts & Hosting
The trained model checkpoint (`.pt` file) is too large to commit directly to GitHub. The plan is to host the final best model weights on the **Hugging Face Hub** as a dedicated model repository, accompanied by a model card (see `MODEL_CARD.md`).

**Current status:** not yet uploaded. A shareable checkpoint is not in the repo yet. As an alternative to a separate Hugging Face repo, the weights can also be attached as a binary asset on the GitHub Release. See `docs/RELEASE_CHECKLIST.md` for the upload steps.

---

## 3. Demo Application (Hugging Face Spaces)
The planned demo is a lightweight **Gradio** interface on **Hugging Face Spaces**.

**Planned features:**
- **Inference:** upload a chest X-ray image (JPEG/PNG) and get a prediction (Normal vs. Pneumonia) with a confidence score.
- **Explainability:** a Grad-CAM heatmap overlaid on the X-ray to show where the model focused.
- **Medical Disclaimer:** a visible disclaimer stating the app is for educational purposes only.

**Planned model loading:** the Gradio app would load the trained weights from the Hugging Face Hub repository (or the GitHub Release) at startup, so the Space itself stays small.

**Current status:** not built or deployed yet. `app/` contains only the structure and a README; there is no `app.py`. Deployment is optional for this release and depends on having a trained checkpoint first.

---

## Constraints & Compliance
- Strictly restricted from production medical or clinical usage.
- Explicit medical disclaimer is permanently displayed on the user interface.
- Public model weights comply with the original dataset license and usage terms.
