# Pretrained Weights Source

## Summary

All baseline models in this project are initialized with weights pretrained on **ImageNet-1k** via the [`timm`](https://github.com/huggingface/pytorch-image-models) (PyTorch Image Models) library.

In the model config files, this is expressed as:

```yaml
pretrained: true
pretrained_weights: "imagenet"
pretrained_source: "timm"
```

---

## Why Pretrained Weights?

Training a CNN from scratch on a dataset the size of the Chest X-Ray dataset (~5,800 images) would lead to severe overfitting. ImageNet pretrained weights give the model a strong starting point:

- **Low-level features** (edges, textures, gradients) transfer well from natural images to X-rays.
- **Faster convergence** — fewer epochs needed to reach useful performance.
- **Better generalization** on small medical datasets where data augmentation alone is insufficient.

This approach is standard practice in medical imaging literature and is consistent with the project's Colab memory and compute constraints.

---

## How `timm` Provides Weights

When `pretrained=True` is passed to `timm.create_model()`, the library downloads the corresponding checkpoint from HuggingFace Hub on first use and caches it locally. No manual download is required.

```python
import timm

model = timm.create_model("efficientnet_b0", pretrained=True, num_classes=1)
# Downloads: https://huggingface.co/timm/efficientnet_b0.ra_in1k
```

All weights used in this project are **publicly available, non-commercial ImageNet checkpoints** distributed by the `timm` maintainers.

---

## Candidate Models and Their Checkpoints

| Architecture    | `timm` model name      | Pretrained Dataset | Top-1 Acc (ImageNet) |
|-----------------|------------------------|--------------------|----------------------|
| EfficientNet-B0 | `efficientnet_b0`      | ImageNet-1k        | ~77.7%               |
| ResNet-18       | `resnet18`             | ImageNet-1k        | ~69.8%               |
| ResNet-50       | `resnet50`             | ImageNet-1k        | ~80.4%               |

The final model head (classifier layer) is replaced for binary pneumonia classification (`num_classes=1` with sigmoid, or `num_classes=2` with softmax) — the pretrained backbone weights are kept intact at initialization.

---

## References

- `timm` library: https://github.com/huggingface/pytorch-image-models
- ImageNet dataset: https://www.image-net.org/
- Related config: [`configs/model/base.yaml`](../configs/model/base.yaml)
- Model selection criteria: [`docs/MODEL_SELECTION_CRITERIA.md`](MODEL_SELECTION_CRITERIA.md)
