# Explainability — Grad-CAM

## What Is Grad-CAM?
**Gradient-weighted Class Activation Mapping (Grad-CAM)** is a technique for producing visual explanations of convolutional neural network predictions. It generates a heatmap that highlights the regions of an input image that most strongly influenced the model's prediction for a given class.

Grad-CAM works by computing the gradient of the predicted class score with respect to the feature maps of a target convolutional layer. These gradients are used to weight the feature maps, and the result is upsampled and overlaid onto the original image as a color heatmap.

---

## How Grad-CAM Is Used in This Project
Grad-CAM is applied to the trained pneumonia classifier to produce heatmap overlays on chest X-ray images. It serves the following purposes:

1. **Qualitative inspection:** Verifying that the model is attending to clinically plausible regions (e.g., lung fields) rather than image artifacts, labels, or borders.
2. **Error analysis:** Examining Grad-CAM outputs for false positive and false negative cases to understand failure modes.
3. **Visual reporting:** Including a gallery of Grad-CAM heatmaps in the evaluation reports and final interactive demo.

---

## Important Limitations
- Grad-CAM is a **qualitative** tool, not a quantitative diagnostic method.
- Activation heatmaps do not guarantee that the model has learned clinically meaningful features.
- The highlighted regions should **never** be interpreted as a clinical finding or used to inform medical decisions.
- This project does not claim any clinical reliability for Grad-CAM outputs.

---

## Implementation Details
The target layer for Grad-CAM is the final convolutional feature extraction layer of the selected backbone architecture. 

* **Implemented Model:** `EfficientNetV2-S` (via `timm`)
* **Selected Target Grad-CAM Layer:** `model.conv_head`

**Justification:**
The final convolutional stage captures high-level semantic image features while preserving spatial information needed for Grad-CAM heatmap generation. Earlier layers primarily capture low-level image features (edges, textures), while deeper layers better represent pathology-related structures relevant for pneumonia classification. 

### Target Layer Reference Table
If the architecture changes in future experiments, the target layer is updated as follows:

| Model | Target Layer Used |
|--------|------------------------|
| EfficientNetV2-S | `model.conv_head` |
| EfficientNet-B0 | `model.conv_head` |
| ResNet-18 | `model.layer4` |
| ResNet-50 | `model.layer4` |

Heatmaps are generated for a representative sample of test images covering both correct and incorrect predictions. All overlaid images are saved to `artifacts/figures/` and integrated into the evaluation phase.

---

## Qualitative Interpretation Guidelines

### What to Look For
When reviewing Grad-CAM heatmaps for the pneumonia classifier, focus on the following indicators of model plausibility:

**Anatomically plausible activations (positive signals)**
- Heatmap is concentrated within the **lung fields** (the central and lateral zones of the chest cavity).
- For **pneumonia** predictions, activation is in regions consistent with known radiological findings: lower lobe consolidation, bilateral infiltrates, or opacified areas.
- For **normal** predictions, diffuse or low-intensity activation occurs with no strong localization to abnormal tissue.

**Signs of potentially spurious activations (warning signals)**
- Strong activation concentrated on **image borders, corners, or padding** rather than the lung area.
- Heatmap highlights **text labels, annotations, or watermarks** embedded in the X-ray image.
- Activation focuses on **non-lung anatomical structures** such as the spine, ribs, or diaphragm edge.

---

### How to Avoid Overclaiming
Grad-CAM is a diagnostic support tool for model inspection, not a clinical explanatory method. The following rules are strictly followed across the project.

| Instead of | Use |
|---|---|
| "The model correctly identified the pneumonia region" | "The model's attention overlaps with the lung field, which is consistent with pneumonia pathology" |
| "Grad-CAM confirms the model learned clinical features" | "Grad-CAM provides qualitative evidence that the model may be attending to anatomically plausible regions" |
| "The heatmap shows where pneumonia is located" | "The heatmap highlights the regions that most influenced this prediction" |

> ⚠️ **Mandatory Disclaimer:** Grad-CAM heatmaps are a qualitative visualization tool. They indicate which image regions most influenced the model's prediction for a given input and are intended solely for model inspection purposes. These outputs have not been clinically validated and must not be used to inform any medical diagnosis or clinical decision.
