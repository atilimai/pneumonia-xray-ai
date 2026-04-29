# Model Selection Plan

## Purpose

This document defines which pretrained model architectures will be compared during the modeling phase of the pneumonia X-ray classification project.

The goal is to avoid choosing a model randomly or based only on convenience. Instead, the final architecture will be selected using measurable criteria such as validation performance, memory usage, training stability, and suitability for future experimentation.

This is a planning document only. No training experiments are implemented here.

---

## Candidate Architectures

The project will compare pretrained convolutional neural network architectures using transfer learning through the `timm` library.

The initial candidate models are:

1. EfficientNet-B0
2. ResNet-18
3. ResNet-50 as an optional extended baseline if GPU memory allows

These architectures are available through `timm` and can be instantiated with pretrained weights.

---

## Candidate 1: EfficientNet-B0

### Description

EfficientNet-B0 is a compact convolutional neural network designed to balance accuracy and efficiency.

It is a reasonable starting point because it has a relatively low parameter count while still providing strong image classification performance.

### Pros

- Low computational cost compared with larger CNN architectures.
- Suitable for Colab GPU memory limitations.
- Strong baseline for transfer learning.
- Efficient for training and inference.
- Good choice when the dataset size is limited.

### Cons

- Architecture is more complex than ResNet, which may make debugging harder.
- May require careful fine-tuning and learning rate selection.
- Performance may be sensitive to preprocessing and image resolution.

### Proposed `timm` name

`efficientnet_b0`

---

## Candidate 2: ResNet-18

### Description

ResNet-18 is a simple and lightweight residual network.

It is useful as a baseline because it is easy to understand, fast to train, and less memory-intensive than deeper ResNet models.

### Pros

- Simple architecture and easy to debug.
- Fast training time.
- Low memory usage.
- Good baseline for comparison.
- Residual connections help with stable training.

### Cons

- Lower capacity than larger architectures.
- May underperform compared with EfficientNet-B0 or ResNet-50.
- May not capture complex image patterns as strongly as deeper models.

### Proposed `timm` name

`resnet18`

---

## Candidate 3: ResNet-50

### Description

ResNet-50 is a deeper residual network than ResNet-18.

It may provide stronger feature extraction ability, but it also requires more memory and training time.

### Pros

- Higher model capacity than ResNet-18.
- Strong and widely used transfer learning baseline.
- Residual connections support stable training.
- Useful for comparing lightweight and deeper CNN models.

### Cons

- Higher GPU memory usage.
- Slower training.
- Higher risk of overfitting if the dataset is small.
- May not be suitable if Colab T4 memory becomes a limitation.

### Proposed `timm` name

`resnet50`

---

## Selection Criteria

The final architecture will be selected based on measurable criteria, not only convenience.

| Criterion | Measurement |
|---|---|
| Validation accuracy | Higher validation accuracy is better |
| Validation F1-score | Higher F1-score is better, especially if classes are imbalanced |
| Validation loss | Lower validation loss is better |
| GPU memory usage | The model must fit in Colab T4 GPU memory |
| Training time per epoch | Shorter training time is preferred if performance is similar |
| Overfitting behavior | Smaller gap between training and validation performance is preferred |
| Reproducibility | The model should be easy to instantiate and configure through `timm` |
| Practicality | The architecture should be suitable for future experimentation and reporting |

The main selection metric will be validation F1-score because pneumonia classification may involve class imbalance.

Validation accuracy will also be reported, but it will not be the only deciding metric.

---

## Fine-Tuning Strategy

### Decision

The project will use a staged transfer learning strategy consisting of:

1. Feature extraction (frozen backbone)
2. Partial fine-tuning (unfreezing last layers)

Full fine-tuning will NOT be used as the initial strategy.

---

### Selected Strategy

#### 1. Feature Extraction Phase

- Load pretrained ImageNet weights using `timm`
- Replace the final classification head with a binary classifier
- Freeze the entire pretrained backbone
- Train only the classification head for the first few epochs

This phase provides a stable baseline and prevents early overfitting.

---

#### 2. Partial Fine-Tuning Phase

- Unfreeze the last block or last few layers of the backbone
- Continue training with a lower learning rate
- Monitor:
  - validation F1-score
  - validation loss
  - overfitting behavior

This allows the model to adapt high-level features to chest X-ray images.

---

### Rejected Strategy: Full Fine-Tuning (Initial Phase)

Full fine-tuning is intentionally NOT used at the beginning because:

- The dataset is limited and imbalanced
- The validation set is extremely small (8 samples per class)
- It increases the risk of overfitting
- It requires more GPU memory and training time
- It reduces stability when comparing different architectures

Full fine-tuning may be considered later if justified by results.

---

### Consistency Requirement

To ensure fair comparison between models:

- The same fine-tuning strategy must be applied to all candidate architectures
- The same preprocessing, augmentation, optimizer, and evaluation setup must be used
- The same train/validation/test split must be preserved

---

### Rationale

This staged approach balances stability and adaptability:

- Feature extraction provides a safe and reproducible baseline
- Partial fine-tuning allows domain-specific adaptation
- Avoiding full fine-tuning initially reduces risk and improves comparability

This strategy ensures reliable and fair evaluation across EfficientNet-B0, ResNet-18, and ResNet-50.

---

## Memory Considerations

The selected architecture must fit within Google Colab T4 GPU memory.

Before full training, each candidate model should be checked with a small batch of images to estimate memory usage.

If ResNet-50 exceeds the available memory or requires an impractically small batch size, it may be removed from the final comparison.

The initial recommended comparison is:

- EfficientNet-B0
- ResNet-18

ResNet-50 can be added only if memory usage is acceptable.

---

## Planned Final Decision Rule

The final architecture will be selected using the following rule:

1. The model must successfully instantiate in `timm`.
2. The model must fit in Colab T4 GPU memory.
3. The model must complete training without instability.
4. Among valid models, the architecture with the best validation F1-score will be selected.
5. If two models have similar F1-scores, the simpler and more memory-efficient model will be preferred.
6. The final choice must be justified in the experiment report using validation metrics and resource usage.

---

## Relationship to Existing Project Documents

This document depends on:

- `01_repo_scaffold_review.md`
- `02_dataset_ingestion_plan.md`
- `05_config_design.md`

The selected model name should later be referenced from the training configuration or notebook, for example:

```yaml
model:
  name: efficientnet_b0
  pretrained: true
  num_classes: 2
