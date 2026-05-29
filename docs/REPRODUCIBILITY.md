# Reproducibility Checklist

This document defines reproducibility requirements for rerunning the Pneumonia Detection project from scratch.

## Hyperparameter Configuration Policy

All experiment hyperparameters must be stored in configuration files under `configs/` rather than hardcoded directly in notebooks.

### Config Files

The project uses the following configuration files:

- `configs/model/base.yaml`
- `configs/training/base.yaml`
- `configs/evaluation/base.yaml`

### Model Hyperparameters

Model-related settings are stored in `configs/model/base.yaml`, including:

- model architecture
- model library
- pretrained weights flag
- number of output classes
- input channels
- image size
- pooling strategy
- dropout rate
- backbone freezing policy
- classification head type
- checkpoint path

### Training Hyperparameters

Training-related settings are stored in `configs/training/base.yaml`, including:

- random seed
- image size
- number of workers
- batch size
- number of epochs
- device
- mixed precision setting
- optimizer type
- learning rate
- weight decay
- scheduler configuration
- loss function
- class imbalance weighting
- augmentation settings
- regularization settings
- early stopping configuration
- checkpointing behavior
- logging frequency

### Evaluation Hyperparameters

Evaluation-related settings are stored in `configs/evaluation/base.yaml`, including:

- evaluation split
- positive and negative class definitions
- decision threshold
- threshold policy
- required prediction columns
- metrics to compute
- output file paths
- plot settings

### Notebook Policy

Training and evaluation notebooks should load hyperparameters from the relevant config files instead of defining them manually.

Allowed notebook behavior:

```python
config = load_config("configs/training/base.yaml")

```

Discouraged notebook behavior:

```python
batch_size = 32
learning_rate = 0.001
num_epochs = 50
```

### Confirmation

The current config structure centralizes the main model, training, and evaluation hyperparameters under `configs/`.

Before final release, training and evaluation notebooks should be checked to confirm that they reference these config files rather than hardcoding experiment settings directly in notebook cells.

If any hyperparameter is temporarily hardcoded during experimentation, it must be moved into the appropriate config file before final reporting or release.
