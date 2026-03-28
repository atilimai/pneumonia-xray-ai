# Artifacts (`artifacts/`)

This directory stores generated outputs produced during training, evaluation, and visualization. These files are **not source code** and are generally excluded from version control.

> ⚠️ Most files in this directory are ignored by `.gitignore`. Only `.gitkeep` placeholders are committed to preserve the folder structure.

---

## Subdirectories

### `artifacts/checkpoints/`
Model checkpoint files saved during or after training.
- PyTorch `.pt` or `.pth` files
- Named by epoch or best-performing state
- Should be archived or uploaded to Hugging Face Hub for sharing

### `artifacts/logs/`
Training logs and metric histories.
- Per-epoch loss and accuracy values
- CSV or JSON format for programmatic access
- TensorBoard or W&B event files if applicable

### `artifacts/figures/`
All saved plots and visualizations.
- Training and validation loss/accuracy curves
- Confusion matrix plots
- ROC curves
- Grad-CAM heatmap galleries
- Class distribution and sample image grids

### `artifacts/reports/`
Summary evaluation reports produced at the end of training or evaluation runs.
- Markdown or PDF summaries of model performance
- Tables of metrics across experiments
- Notes on configurations used

---

## Version Control Policy

Generated files should **not** be committed directly to the repository. Use one of the following approaches for sharing artifacts:
- GitHub Releases (for final model weights and reports)
- Hugging Face Hub (for model checkpoints)
- Git LFS (if committing binary files is necessary)
