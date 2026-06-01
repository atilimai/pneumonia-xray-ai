# Deployment Plan

This document outlines the final and actual approach taken for publishing and sharing the Pneumonia Detection project.

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
The trained model checkpoint (`.pt` file) is too large to commit directly to GitHub. Therefore, the final best model weights are hosted on the **Hugging Face Hub** as a dedicated model repository, accompanied by a comprehensive model card (`README.md`).

---

## 3. Demo Application (Hugging Face Spaces)
An interactive user interface has been built and deployed on **Hugging Face Spaces** using the **Gradio** framework.

**Key Features of the Demo App:**
- **Inference:** Users can upload a chest X-ray image (JPEG/PNG) and get instant predictions (Normal vs. Pneumonia) with confidence scores.
- **Explainability:** Fully integrated with Grad-CAM to overlay heatmaps on the X-ray, highlighting exactly where the model focused.
- **Medical Disclaimer:** A strict and visible disclaimer indicating the app is for educational purposes only.

**Model Loading Strategy:**
The Gradio application dynamically fetches and loads the trained model weights directly from the Hugging Face Hub repository upon container startup, ensuring the space remains lightweight.

---

## Constraints & Compliance
- Strictly restricted from production medical or clinical usage.
- Explicit medical disclaimer is permanently displayed on the user interface.
- Public model weights comply with the original dataset license and usage terms.
