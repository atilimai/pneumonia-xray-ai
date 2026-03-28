# Roadmap — Pneumonia Detection from Chest X-Rays

This roadmap outlines the 5-week plan for bringing the project from initial scaffold to a complete, documented, and publishable state.

---

## Week 1 — Repository Setup and Planning

**Focus:** Establish a clean, well-documented repository foundation.

**Expected Outputs:**
- Repository scaffold merged and reviewed
- All documentation stubs in place
- Issue backlog defined and ready to open in GitHub
- Dataset folder contract agreed and documented

**Exit Criteria:**
- All directories, README files, and docs are committed
- `docs/issues/` contains all 13 issue drafts
- Dataset is NOT committed; `data/README.md` explains the folder contract
- Issue templates are live in `.github/ISSUE_TEMPLATE/`

---

## Week 2 — Data Preparation and Exploratory Analysis

**Focus:** Understand the dataset and define preprocessing decisions.

**Expected Outputs:**
- Dataset downloaded locally and placed under `data/raw/`
- EDA notebook documenting class distribution, image statistics, and sample grids
- Preprocessing decisions documented (resize, normalization, augmentation strategy)
- Interim and processed folders populated with transformed data

**Exit Criteria:**
- EDA notebook is complete, clean, and committed to `notebooks/`
- Class imbalance strategy is documented
- Train/val/test split hygiene is confirmed
- Preprocessing pipeline design is captured in a notebook or config

---

## Week 3 — Model Training and Baseline Evaluation

**Focus:** Train a transfer learning model and evaluate baseline performance.

**Expected Outputs:**
- Baseline model trained on Colab (EfficientNet or ResNet via `timm`)
- Model checkpoint saved to `artifacts/checkpoints/`
- Evaluation metrics computed: accuracy, sensitivity, specificity, ROC AUC
- Confusion matrix and ROC curve figures saved to `artifacts/figures/`

**Exit Criteria:**
- Model achieves reasonable sensitivity and specificity on the test split
- Training curves are logged and visualized
- Evaluation results are recorded in a report under `artifacts/reports/`
- Config used for training is committed to `configs/`

---

## Week 4 — Explainability and Visualization

**Focus:** Add Grad-CAM support and produce a complete visual report.

**Expected Outputs:**
- Grad-CAM heatmaps generated for a representative sample of test images
- Grad-CAM gallery saved to `artifacts/figures/`
- False positive and false negative galleries produced
- All planned visual outputs from `docs/VISUALIZATION_PLAN.md` completed

**Exit Criteria:**
- Grad-CAM workflow is documented in `docs/EXPLAINABILITY.md`
- Heatmap figures are committed or linked in the report
- All visualization outputs from the plan are present

---

## Week 5 — Documentation, Reproducibility, and Release

**Focus:** Finalize documentation, ensure reproducibility, and publish the project.

**Expected Outputs:**
- Full documentation pass completed (all `docs/` files updated)
- Reproducibility checklist verified (seeds, configs, environment pinned)
- GitHub release created with model artifacts and final report
- Optional: Hugging Face model page and Gradio demo deployed
- README updated with final results and demo link

**Exit Criteria:**
- All acceptance criteria in `docs/issues/11_reproducibility_checklist.md` are met
- All acceptance criteria in `docs/issues/13_final_release_checklist.md` are met
- Repository is clean, tagged, and publicly accessible
- Demo (if created) is live and includes a medical disclaimer
