# Configs (`configs/`)

This directory will contain configuration files that define experiment parameters for model training, evaluation, and data preprocessing.

Using config files separates hyperparameters from source code, making experiments reproducible and easy to compare.

> No config files exist yet. This is a Week 1 scaffold.

---

## Planned Config Files

### `configs/model/`
Parameters related to the model architecture.
- Model name (e.g., `efficientnet_b0`, `resnet50`)
- Pretrained weights flag
- Number of output classes
- Input image size

### `configs/training/`
Parameters controlling the training process.
- Number of epochs
- Batch size
- Learning rate and scheduler type
- Optimizer choice and weight decay
- Augmentation settings
- Checkpoint save frequency
- Early stopping patience

### `configs/evaluation/`
Parameters for the evaluation and inference phase.
- Decision threshold for binary classification
- Metrics to compute
- Test split path
- Output directory for figures and reports

---

## Format

Config files will likely be written in **YAML** format for readability and compatibility with common ML configuration libraries.
