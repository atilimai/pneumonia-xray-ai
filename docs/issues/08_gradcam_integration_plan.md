# Title
Plan Grad-CAM based explainability workflow

## Type
Task

## Summary
Plan the Grad-CAM explainability workflow for the Pneumonia Detection model, including the target layer selection, the image samples to visualize, and the output format. Grad-CAM heatmaps provide qualitative insight into which regions of a chest X-ray influenced the model's decision. This issue defines the plan before any implementation begins.

## Background
Grad-CAM (Gradient-weighted Class Activation Mapping) produces heatmap overlays that highlight spatially influential regions in a CNN's input image for a given prediction. For this project, Grad-CAM will be applied to the trained model's final convolutional layer and used to inspect whether activations align with clinically plausible lung regions or with image artifacts. See `docs/EXPLAINABILITY.md` for context.

## Deliverables
- [ ] Target layer for Grad-CAM identified and documented (e.g., last convolutional block of EfficientNet or ResNet)
- [ ] List of test image samples selected for visualization (minimum: 5 true positives, 5 true negatives, 5 false positives, 5 false negatives)
- [ ] Heatmap overlay format agreed (original image + Grad-CAM overlay side-by-side)
- [ ] Output filenames and save location defined (`artifacts/figures/gradcam_*`)
- [ ] Qualitative interpretation guidelines documented (what to look for, how to avoid overclaiming)
- [ ] Medical disclaimer language agreed for inclusion in the report and any demo

## Acceptance Criteria
- [ ] Grad-CAM plan is documented and committed
- [ ] Target layer choice is justified relative to the chosen model architecture
- [ ] Sample selection covers true positives, true negatives, false positives, and false negatives
- [ ] Heatmap output format is clearly defined
- [ ] Documentation explicitly states that Grad-CAM outputs are qualitative and not clinically validated

## Dependencies
- `04_baseline_model_selection.md`
- `06_evaluation_protocol_definition.md`

## Out of Scope
- Implementing the Grad-CAM code (belongs in `src/explainability/`)
- Quantitative evaluation of explainability (e.g., insertion/deletion metrics)
- Using Grad-CAM outputs to retrain or adjust the model

## Suggested Labels
`explainability`, `docs`

## Notes
The `torchcam` or `pytorch-grad-cam` library provides Grad-CAM implementations compatible with `timm` models and is worth evaluating before writing a custom implementation. The target layer must be accessible by name in the chosen model architecture. For EfficientNet, this is typically the last `Conv2dNormAct` block. Heatmap color maps should be consistent across the gallery (e.g., `jet` or `RdBu`).
