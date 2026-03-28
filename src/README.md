# Source Code (`src/`)

This directory will contain all Python source modules for the project. Each subdirectory corresponds to a distinct functional area.

> No implementation files exist yet. This is a Week 1 scaffold. Source modules will be added in later milestones.

---

## Module Overview

### `src/data/`
Data loading, preprocessing, and augmentation utilities.
- Dataset class definitions (e.g., PyTorch `Dataset` subclass)
- Image transforms and normalization
- Split management and data loader construction

### `src/models/`
Model architecture definitions and loading utilities.
- Transfer learning model wrappers (EfficientNet, ResNet via `timm`)
- Model instantiation helpers
- Checkpoint loading and saving utilities

### `src/training/`
Training loop logic and supporting utilities.
- Training and validation loop functions
- Optimizer and scheduler configuration
- Loss function setup
- Early stopping logic

### `src/evaluation/`
Metric computation and evaluation utilities.
- Sensitivity, specificity, accuracy, precision, recall
- ROC AUC computation
- Confusion matrix generation
- Threshold selection logic

### `src/explainability/`
Grad-CAM and other interpretability utilities.
- Grad-CAM heatmap generation
- Heatmap overlay and visualization helpers
- False positive / false negative sample extraction

### `src/visualization/`
Plotting and figure generation utilities.
- Training curve plots
- Confusion matrix plots
- ROC curve plots
- Class distribution and sample grid figures
