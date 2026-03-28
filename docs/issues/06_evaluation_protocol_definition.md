# Title
Define evaluation protocol and threshold policy

## Type
Task

## Summary
Define the complete evaluation protocol for the Pneumonia Detection model, including which metrics are computed, on which dataset split, and what decision threshold is used. Establishing this protocol before training ensures that evaluation decisions are not influenced by observed results, which would constitute outcome bias.

## Background
Binary classifiers require a decision threshold to produce class labels from raw probability outputs. The default threshold of 0.5 may not be optimal for this task, where the cost of a false negative (missing pneumonia) is higher than a false positive. This issue defines the threshold policy and the full evaluation procedure before any model is trained.

## Deliverables
- [ ] Evaluation protocol documented in `docs/` or as a notebook section
- [ ] Primary metric identified and justified (recommended: ROC AUC + sensitivity)
- [ ] Decision threshold policy documented (default 0.5; justification required for any deviation)
- [ ] All metrics to be reported listed: accuracy, precision, recall, sensitivity, specificity, ROC AUC, confusion matrix
- [ ] Evaluation split confirmed as the held-out test set from the Kaggle download
- [ ] Reporting format agreed (table of metrics + saved figures)

## Acceptance Criteria
- [ ] Evaluation protocol is documented and committed
- [ ] Primary metric and threshold policy are explicitly stated
- [ ] All metrics listed in `docs/METRICS.md` are confirmed as in-scope for evaluation
- [ ] The evaluation split is confirmed and documented
- [ ] No evaluation decisions are deferred to after results are seen

## Dependencies
- `01_repo_scaffold_review.md`
- `02_dataset_ingestion_plan.md`
- `04_baseline_model_selection.md`

## Out of Scope
- Implementing the evaluation code (that belongs in `src/evaluation/`)
- Running evaluation on a trained model
- Threshold optimisation using the test set

## Suggested Labels
`evaluation`, `docs`

## Notes
The small validation split (8 images per class) means validation-set metric estimates will be unreliable during training. It may be appropriate to monitor training loss as the primary stopping signal and reserve the test set strictly for final evaluation. Threshold selection, if deviating from 0.5, should be performed on a validation or cross-validation set, never on the test set.
