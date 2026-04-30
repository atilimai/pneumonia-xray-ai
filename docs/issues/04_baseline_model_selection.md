# Title
Define baseline model comparison strategy

## Type
Task

## Summary
Define which pretrained model architectures will be compared during the modeling phase, what the comparison criteria are, and how the final architecture will be selected. Having a clear model selection strategy prevents ad-hoc decisions and ensures the chosen model is justified by evidence rather than convenience.

## Background
The project plans to use transfer learning with EfficientNet or ResNet architectures via the `timm` library. Before training, the candidate architectures and selection criteria should be agreed upon. This issue produces a documented model comparison plan rather than implementing training.

## Candidate Architectures

### 1. EfficientNet-B0

**Rationale:**  
EfficientNet-B0 is included as a strong lightweight baseline because it offers a good balance between performance and computational efficiency. It has a relatively low parameter count compared with larger CNN architectures while maintaining strong ImageNet transfer learning performance.

**Pros:**
- Lower memory usage, suitable for Google Colab T4 GPU
- Strong efficiency-to-performance balance
- Faster training compared with larger models
- Available directly in `timm`

**Cons:**
- Lower capacity than newer EfficientNetV2 variants
- Slightly more complex than ResNet for debugging
- May underperform compared with newer architectures on difficult visual patterns

### 2. ResNet-18

**Rationale:**  
ResNet-18 is included as a lightweight classical CNN baseline. It is widely used, easy to debug, and provides a simple reference point for transfer learning experiments.

**Pros:**
- Very lightweight and fast to train
- Excellent compatibility with limited GPU memory
- Simple architecture and easy debugging
- Useful baseline for comparison

**Cons:**
- Lower representational capacity than deeper or newer models
- May underperform compared with EfficientNet and ConvNeXt models
- Less efficient accuracy scaling compared with newer architectures

### 3. ResNet-50

**Rationale:**  
ResNet-50 is included as a stronger residual network baseline. It allows comparison between lightweight and deeper ResNet architectures.

**Pros:**
- Higher capacity than ResNet-18
- Strong transfer learning performance
- Well-established architecture in medical imaging research
- Available directly in `timm`

**Cons:**
- Higher memory consumption than ResNet-18 and EfficientNet-B0
- Slower training in Colab environments
- Greater risk of overfitting on limited datasets

### 4. EfficientNetV2-S

**Rationale:**  
EfficientNetV2-S is included as a newer EfficientNet-family model designed to improve training efficiency and performance compared with earlier EfficientNet variants. It is a strong candidate when the project needs a balance between accuracy, parameter efficiency, and practical Colab training constraints.

**Pros:**
- Newer and more efficient than the original EfficientNet family
- Strong transfer learning candidate for image classification
- Better representational capacity than very small baselines
- Available through `timm`

**Cons:**
- Heavier than EfficientNet-B0
- May require more GPU memory and longer training time
- Needs validation on the project dataset before final adoption

### 5. ConvNeXt-Tiny

**Rationale:**  
ConvNeXt-Tiny is included as a modern CNN architecture that updates traditional convolutional networks using design ideas inspired by transformer-era models. It provides a useful comparison against both ResNet and EfficientNet models.

**Pros:**
- More modern architecture than ResNet
- Strong image classification performance
- Compatible with `timm`
- Useful comparison point between classic CNNs and transformer-style models

**Cons:**
- More computationally demanding than lightweight baselines
- May be unnecessary if EfficientNetV2-S provides similar performance with lower cost
- Needs memory testing in Colab before being selected

### 6. ViT-B/16

**Rationale:**  
ViT-B/16 is included as a transformer-based candidate architecture. It provides a different modeling approach from CNN-based architectures and can help determine whether transformer-style visual representations are useful for this dataset.

**Pros:**
- Modern transformer-based architecture
- Strong transfer learning performance on many image classification tasks
- Available through `timm`
- Useful as a comparison against CNN-based models

**Cons:**
- Usually requires more data and compute than lightweight CNNs
- May be less efficient in a limited Colab GPU environment
- Could overfit if the dataset size and validation split are insufficient

## Candidate Architecture Comparison

| Model | Model Type | Relative Size | Expected Compute Cost | Colab Suitability | Main Role |
|---|---|---:|---:|---:|---|
| ResNet-18 | Classical CNN | Low | Low | High | Simple lightweight baseline |
| ResNet-50 | Classical CNN | Medium | Medium | Medium | Stronger ResNet baseline |
| EfficientNet-B0 | Efficient CNN | Low | Low-Medium | High | Efficient fallback baseline |
| EfficientNetV2-S | Efficient CNN | Medium | Medium | Medium-High | Recommended starting model |
| ConvNeXt-Tiny | Modern CNN | Medium | Medium-High | Medium | Modern CNN comparison |
| ViT-B/16 | Vision Transformer | High | High | Low-Medium | Transformer-based comparison |

## Selection Metrics

The candidate architectures should later be compared using metrics suitable for imbalanced binary classification:

- Average Precision / PR AUC
- ROC AUC
- Sensitivity / Recall for the pneumonia class
- Precision
- F1-score
- Parameter count
- Colab GPU memory usage
- Training time and inference time

Because this project is a binary classification task rather than an object detection task, Average Precision / PR AUC is more appropriate than object-detection mAP. However, Average Precision provides a similar ranking-focused view of model performance under class imbalance.

## Selected Starting Model

### EfficientNetV2-S

EfficientNetV2-S is selected as the recommended starting model for the first baseline experiment.

**Reasoning:**
- It is newer than EfficientNet-B0 and designed for improved training efficiency.
- It offers a strong balance between performance and computational cost.
- It is available through `timm` with pretrained ImageNet weights.
- It should provide stronger representational capacity than ResNet-18 while being more efficient than heavier alternatives.
- It is more practical for limited GPU environments than larger transformer-based models such as ViT-B/16.

## Deliverables
- [ ] List of candidate architectures with rationale (e.g., EfficientNet-B0, ResNet-50, ResNet-18)
- [ ] Selection criteria documented (e.g., ROC AUC, sensitivity, parameter count, Colab memory fit)
- [ ] Pretrained weights source documented (`timm` ImageNet weights)
- [ ] Final layer modification strategy documented (replace classification head for binary output)
- [ ] Decision on fine-tuning strategy documented (feature extraction only vs. partial fine-tuning vs. full fine-tuning)
- [ ] Findings written up in `docs/` or as a notebook section

## Acceptance Criteria
- [ ] At least two candidate architectures are documented with pros and cons
- [ ] Selection criteria are explicitly stated and measurable
- [ ] Fine-tuning strategy is agreed and documented before training begins
- [ ] The chosen architecture can be instantiated in `timm` and fits in Colab GPU memory
- [ ] Documentation is committed and referenced from the training config or notebook

## Dependencies
- `01_repo_scaffold_review.md`
- `02_dataset_ingestion_plan.md`
- `05_config_design.md`

## Out of Scope
- Implementing the training loop
- Running experiments (this is planning only)
- Custom architecture design

## Suggested Labels
`modeling`, `docs`

## Notes
EfficientNet-B0 is a reasonable starting point due to its low parameter count and strong ImageNet performance. ResNet-18 or ResNet-50 provides a simpler baseline for comparison. Both are available in `timm` with pretrained weights. Memory usage on Colab T4 GPU should be estimated before committing to a specific architecture.
