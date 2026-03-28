# Explainability — Grad-CAM

## What Is Grad-CAM?

**Gradient-weighted Class Activation Mapping (Grad-CAM)** is a technique for producing visual explanations of convolutional neural network predictions. It generates a heatmap that highlights the regions of an input image that most strongly influenced the model's prediction for a given class.

Grad-CAM works by computing the gradient of the predicted class score with respect to the feature maps of a target convolutional layer. These gradients are used to weight the feature maps, and the result is upsampled and overlaid onto the original image as a color heatmap.

---

## How Grad-CAM Will Be Used in This Project

Grad-CAM will be applied to the trained pneumonia classifier to produce heatmap overlays on chest X-ray images. The goals are:

1. **Qualitative inspection:** Verify that the model is attending to clinically plausible regions (e.g., lung fields) rather than image artifacts, labels, or borders.
2. **Error analysis:** Examine Grad-CAM outputs for false positive and false negative cases to understand failure modes.
3. **Visual reporting:** Include a gallery of Grad-CAM heatmaps in the final project report.

---

## Important Limitations

- Grad-CAM is a **qualitative** tool, not a quantitative diagnostic method.
- Activation heatmaps do not guarantee that the model has learned clinically meaningful features.
- The highlighted regions should **never** be interpreted as a clinical finding or used to inform medical decisions.
- This project does not claim any clinical reliability for Grad-CAM outputs.

---

## Implementation Plan

- The target layer for Grad-CAM will be the final convolutional layer of the backbone (e.g., the last `Conv2d` block of EfficientNet or ResNet).
- Heatmaps will be generated for a representative sample of test images covering both correct and incorrect predictions.
- Overlaid images will be saved to `artifacts/figures/` and included in the evaluation report.

See `docs/issues/08_gradcam_integration_plan.md` for the implementation issue draft.
