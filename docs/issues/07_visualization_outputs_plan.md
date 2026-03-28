# Title
Define required visual outputs for reporting

## Type
Task

## Summary
Define and plan all visual outputs that must be produced as part of the project's evaluation and reporting phase. Having an explicit list of required figures prevents gaps in the final report and ensures all visualization work is scoped and prioritized before implementation begins.

## Background
The project needs a set of standard figures to support evaluation, explainability, and the final report. These are listed at a high level in `docs/VISUALIZATION_PLAN.md`. This issue converts that plan into a concrete deliverables checklist with format and location requirements for each figure.

## Deliverables
- [ ] Class distribution chart (per split: train, val, test) saved to `artifacts/figures/class_distribution.png`
- [ ] Sample image grid for each class saved to `artifacts/figures/sample_grid_normal.png` and `sample_grid_pneumonia.png`
- [ ] Training and validation loss curves saved to `artifacts/figures/training_curves.png`
- [ ] Training and validation accuracy curves saved to `artifacts/figures/accuracy_curves.png`
- [ ] Confusion matrix (test set) saved to `artifacts/figures/confusion_matrix_test.png`
- [ ] ROC curve with AUC annotation saved to `artifacts/figures/roc_curve.png`
- [ ] Grad-CAM gallery (true positives and true negatives) saved to `artifacts/figures/gradcam_gallery.png`
- [ ] False positive gallery saved to `artifacts/figures/false_positives.png`
- [ ] False negative gallery saved to `artifacts/figures/false_negatives.png`

## Acceptance Criteria
- [ ] All figures listed in the deliverables are present in `artifacts/figures/`
- [ ] Each figure is correctly labelled with titles, axis labels, and legends
- [ ] Figures are referenced in the evaluation report in `artifacts/reports/`
- [ ] `docs/VISUALIZATION_PLAN.md` is consistent with the final figure list

## Dependencies
- `03_eda_notebook_plan.md`
- `06_evaluation_protocol_definition.md`
- `08_gradcam_integration_plan.md`

## Out of Scope
- Interactive visualizations
- Animated plots or dashboards
- Figures for the demo application (those are handled in `10_demo_deployment_plan.md`)

## Suggested Labels
`evaluation`, `docs`

## Notes
Figures should use consistent colour schemes and font sizes for a professional final report. Seaborn and Matplotlib are the planned visualization libraries. All figures should be saved at sufficient resolution for inclusion in a written report (minimum 150 DPI).
