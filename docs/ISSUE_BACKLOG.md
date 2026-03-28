# Issue Backlog

This page provides an overview of all issue drafts for the Pneumonia Detection project. These drafts are stored in `docs/issues/` and are ready to be copied into GitHub Issues.

Each issue is unassigned. Issues should be opened in priority order at the start of each milestone.

---

## Setup

| File | Title | Purpose |
|---|---|---|
| [01_repo_scaffold_review.md](issues/01_repo_scaffold_review.md) | Repo scaffold review and structure freeze | Review the initial repository structure and lock it before development begins |
| [05_config_design.md](issues/05_config_design.md) | Design configuration structure for experiments | Define the YAML config schema for model, training, and evaluation parameters |
| [11_reproducibility_checklist.md](issues/11_reproducibility_checklist.md) | Create reproducibility and rerun checklist | Define the conditions required for a full clean rerun of the project |

---

## Data

| File | Title | Purpose |
|---|---|---|
| [02_dataset_ingestion_plan.md](issues/02_dataset_ingestion_plan.md) | Dataset ingestion plan and folder contract | Document how the dataset is downloaded, structured, and stored locally |
| [03_eda_notebook_plan.md](issues/03_eda_notebook_plan.md) | Plan exploratory data analysis notebook outputs | Define the expected contents and outputs of the EDA notebook |

---

## Modeling

| File | Title | Purpose |
|---|---|---|
| [04_baseline_model_selection.md](issues/04_baseline_model_selection.md) | Define baseline model comparison strategy | Decide which pretrained architectures to compare and how |
| [09_colab_training_plan.md](issues/09_colab_training_plan.md) | Plan Colab training workflow and constraints | Plan the Colab-based training process including session limits and checkpoint strategy |

---

## Evaluation

| File | Title | Purpose |
|---|---|---|
| [06_evaluation_protocol_definition.md](issues/06_evaluation_protocol_definition.md) | Define evaluation protocol and threshold policy | Specify which metrics to compute, on which split, and what threshold to use |
| [07_visualization_outputs_plan.md](issues/07_visualization_outputs_plan.md) | Define required visual outputs for reporting | List and plan all figures needed for the final evaluation report |

---

## Explainability

| File | Title | Purpose |
|---|---|---|
| [08_gradcam_integration_plan.md](issues/08_gradcam_integration_plan.md) | Plan Grad-CAM based explainability workflow | Plan the Grad-CAM implementation and define what heatmap outputs are required |

---

## Deployment

| File | Title | Purpose |
|---|---|---|
| [10_demo_deployment_plan.md](issues/10_demo_deployment_plan.md) | Plan lightweight demo deployment path | Define the demo application design, hosting approach, and required disclaimers |

---

## Reproducibility

| File | Title | Purpose |
|---|---|---|
| [11_reproducibility_checklist.md](issues/11_reproducibility_checklist.md) | Create reproducibility and rerun checklist | Confirm that the project can be cleanly reproduced from scratch |

---

## Release

| File | Title | Purpose |
|---|---|---|
| [12_documentation_pass.md](issues/12_documentation_pass.md) | Complete documentation pass for first project milestone | Review and finalize all documentation before the first major release |
| [13_final_release_checklist.md](issues/13_final_release_checklist.md) | Final release checklist for GitHub and optional Hugging Face | Confirm all release criteria are met before tagging the final version |

---

## Suggested First Issues to Open

Open these five issues first to unblock all downstream work:

1. `01_repo_scaffold_review.md` — Locks the structure before development begins
2. `02_dataset_ingestion_plan.md` — Unblocks all data and training work
3. `05_config_design.md` — Enables reproducible experiments from the start
4. `04_baseline_model_selection.md` — Defines the modeling direction
5. `06_evaluation_protocol_definition.md` — Sets the success criteria early
