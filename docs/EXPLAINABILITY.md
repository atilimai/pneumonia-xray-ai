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

- The target layer for Grad-CAM will be the final convolutional feature extraction layer of the selected backbone architecture.

For the current baseline model:

Baseline model:
- `EfficientNetV2-S` (via `timm`)

Selected target Grad-CAM layer:
- `model.conv_head`

Justification:
- The final convolutional stage captures high-level semantic image features while preserving spatial information needed for Grad-CAM heatmap generation.
- Earlier layers primarily capture low-level image features (edges, textures), while deeper layers better represent pathology-related structures relevant for pneumonia classification.
- Using the final convolutional feature extraction stage follows common Grad-CAM practice and produces more interpretable activation maps.

If the architecture changes in future experiments, the target layer should be updated accordingly.

Examples:

| Model | Suggested Target Layer |
|--------|------------------------|
| EfficientNetV2-S | `model.conv_head` |
| EfficientNet-B0 | `model.conv_head` |
| ResNet-18 | `model.layer4` |
| ResNet-50 | `model.layer4` |

- Heatmaps will be generated for a representative sample of test images covering both correct and incorrect predictions.
- Overlaid images will be saved to `artifacts/figures/` and included in the evaluation report.

See `docs/issues/08_gradcam_integration_plan.md` for the implementation issue draft.

---

## Qualitative Interpretation Guidelines

### What to Look For

When reviewing Grad-CAM heatmaps for the pneumonia classifier, focus on the following indicators of model plausibility:

**Anatomically plausible activations (positive signals)**

- Heatmap is concentrated within the **lung fields** (the central and lateral zones of the chest cavity).
- For **pneumonia** predictions, activation in regions consistent with known radiological findings: lower lobe consolidation, bilateral infiltrates, or opacified areas.
- For **normal** predictions, diffuse or low-intensity activation with no strong localization to abnormal tissue.
- Activation patterns shift meaningfully between pneumonia and normal cases — the model is not activating uniformly regardless of class.

**Signs of potentially spurious activations (warning signals)**

- Strong activation concentrated on **image borders, corners, or padding** rather than the lung area.
- Heatmap highlights **text labels, annotations, or watermarks** embedded in the X-ray image.
- Activation focused on **non-lung anatomical structures** such as the spine, ribs, or diaphragm edge in a way that is inconsistent with expected pneumonia pathology.
- Identical or near-identical heatmap patterns across prediction types (TP, TN, FP, FN), suggesting the model is not attending to class-discriminating features.

**Cases to inspect closely**

- **False negatives (pneumonia predicted as normal):** Check whether the heatmap fails to highlight lung regions that a radiologist would consider abnormal.
- **False positives (normal predicted as pneumonia):** Check whether the heatmap reveals that the model is responding to an image artifact or non-pathological feature.

---

### How to Avoid Overclaiming

Grad-CAM is a diagnostic support tool for model inspection, not a clinical explanatory method. The following rules must be followed when presenting or discussing heatmap outputs.

**Do not claim clinical validity**

- Do not state that Grad-CAM heatmaps identify the location of pneumonia in a patient's lung.
- Do not present a heatmap as evidence that the model has learned clinically meaningful features. Plausible-looking activations do not confirm clinical reliability.
- Do not compare heatmap outputs to radiologist annotations or clinical ground truth unless a formal localization study has been conducted.

**Do not overinterpret individual heatmaps**

- A single heatmap that activates in a plausible lung region does not validate the model's reasoning. Consider the full sample set.
- Heatmaps are sensitive to the choice of target layer, the normalization method, and the colormap. Small changes to these settings can significantly alter the visual output.
- Grad-CAM captures the gradient signal at one forward pass; it does not reflect the model's internal representation in a mechanistic sense.

**Appropriate language when reporting results**

Use the following phrasings:

| Instead of | Use |
|---|---|
| "The model correctly identified the pneumonia region" | "The model's attention overlaps with the lung field, which is consistent with pneumonia pathology" |
| "Grad-CAM confirms the model learned clinical features" | "Grad-CAM provides qualitative evidence that the model may be attending to anatomically plausible regions" |
| "The heatmap shows where pneumonia is located" | "The heatmap highlights the regions that most influenced this prediction" |
| "This proves the model is interpretable" | "This supports qualitative inspection of the model's behavior on this sample" |

**Mandatory disclaimer**

All figures, notebooks, and report sections that include Grad-CAM outputs must include the following disclaimer:

> Grad-CAM heatmaps are a qualitative visualization tool. They indicate which image regions most influenced the model's prediction for a given input and are intended solely for model inspection purposes. These outputs have not been clinically validated and must not be used to inform any medical diagnosis or clinical decision.
