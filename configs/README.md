# Configs (`configs/`)

This directory contains YAML configuration files for the pneumonia X-ray project.  
The purpose of these files is to keep experiment settings separate from source code so that runs are easier to reproduce, compare, and modify.

## Directory Structure

- `configs/model/`  
  Contains model-related configuration files such as architecture name, input size, number of classes, and model-specific options.

- `configs/training/`  
  Contains training-related configuration files such as batch size, number of epochs, learning rate, optimizer settings, scheduler settings, and random seed.

- `configs/evaluation/`  
  Contains evaluation-related configuration files such as metrics, thresholds, dataset split selection, and output/reporting options.

- `configs/config.yaml`  
  Optional top-level configuration entry point for selecting or combining model, training, and evaluation configs if needed by the project later.

## Format Conventions

- Configuration files should use YAML format.
- Keys should use lowercase `snake_case`.
- The initial schema should remain simple and easy to read.
- Prefer clear and mostly flat key names unless nesting improves clarity.
- Model, training, and evaluation settings should be kept in separate files.
- Config files are committed to the repository because they serve as both documentation and functional experiment inputs.

## Suggested Schema

### Model Config Schema

Model config files describe the model definition and input assumptions.

Suggested fields:
- `model_name`: string  
- `input_channels`: integer  
- `input_height`: integer  
- `input_width`: integer  
- `num_classes`: integer  
- `pretrained`: boolean  
- `dropout`: float

Example:

```yaml
model_name: resnet18
input_channels: 1
input_height: 224
input_width: 224
num_classes: 2
pretrained: true
dropout: 0.3
```

### Training Config Schema

Training config files describe hyperparameters and training behavior.

Suggested fields:
- `batch_size`: integer  
- `epochs`: integer  
- `learning_rate`: float  
- `optimizer`: string  
- `weight_decay`: float  
- `scheduler`: string  
- `early_stopping_patience`: integer  
- `checkpoint_save_frequency`: integer  
- `seed`: integer

Example:

```yaml
batch_size: 32
epochs: 20
learning_rate: 0.001
optimizer: adam
weight_decay: 0.0001
scheduler: step_lr
early_stopping_patience: 5
checkpoint_save_frequency: 1
seed: 42
```

### Evaluation Config Schema

Evaluation config files describe how model performance is measured and reported.

Suggested fields:
- `split`: string  
- `decision_threshold`: float  
- `metrics`: list  
- `save_predictions`: boolean  
- `save_confusion_matrix`: boolean  
- `output_dir`: string

Example:

```yaml
split: validation
decision_threshold: 0.5
metrics:
  - accuracy
  - precision
  - recall
  - f1
save_predictions: true
save_confusion_matrix: true
output_dir: artifacts/evaluation
```

## Notes

The initial config design should stay simple so that the rest of the codebase can rely on a stable and understandable structure.  
If configuration composition becomes necessary later, tools such as Hydra or OmegaConf can be considered, but plain YAML is sufficient for the current project stage.
