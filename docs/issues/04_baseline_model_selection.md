# Title
Define baseline model comparison strategy

## Type
Task

## Summary
Define which pretrained model architectures will be compared during the modeling phase, what the comparison criteria are, and how the final architecture will be selected. Having a clear model selection strategy prevents ad-hoc decisions and ensures the chosen model is justified by evidence rather than convenience.

## Background
The project plans to use transfer learning with EfficientNet or ResNet architectures via the `timm` library. Before training, the candidate architectures and selection criteria should be agreed upon. This issue produces a documented model comparison plan rather than implementing training.

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
