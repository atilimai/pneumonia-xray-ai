# Title
Create reproducibility and rerun checklist

## Type
Task

## Summary
Define and document the conditions required for a full, clean rerun of the project from scratch. Reproducibility is a core requirement for research credibility. This issue produces a checklist that can be verified before the final release to confirm the project can be reproduced by anyone with access to the repository and the dataset.

## Background
Reproducibility failures in ML projects are common and often caused by missing random seeds, undocumented preprocessing decisions, untracked config changes, or environment dependency drift. This checklist captures all the conditions that must be met for the Pneumonia Detection project to be reliably reproducible.

## Deliverables
- [ ] Random seed policy documented and committed (data split seed, model init seed, augmentation seed)
- [ ] All hyperparameters confirmed to be in config files rather than hardcoded in notebooks
- [ ] `requirements.txt` updated with pinned versions of all dependencies used in training
- [ ] Dataset version confirmed and documented (Kaggle download date or version hash if available)
- [ ] Training notebook runs end-to-end on a fresh Colab session without modification
- [ ] Evaluation notebook reproduces reported metrics when run with the saved checkpoint
- [ ] Reproducibility checklist committed to `docs/` or as a section in the README

## Acceptance Criteria
- [ ] All random seeds are set and documented
- [ ] All hyperparameters are in config files and the training notebook references those configs
- [ ] `requirements.txt` contains version-pinned dependencies used in the final training run
- [ ] A second person (or a fresh environment) can reproduce the reported metrics within a defined tolerance
- [ ] The reproducibility checklist is committed and all items are checked off before the final release

## Dependencies
- `05_config_design.md`
- `09_colab_training_plan.md`
- `06_evaluation_protocol_definition.md`

## Out of Scope
- Bit-exact reproducibility across different hardware or CUDA versions (document this as a known limitation)
- Reproducing results without access to the Kaggle dataset

## Suggested Labels
`setup`, `docs`, `release`

## Notes
Full bit-exact reproducibility is not achievable across different GPU hardware due to non-deterministic CUDA operations. The reproducibility goal should be defined as: metrics within ±1% of reported values when rerun with the same hardware class (e.g., Colab T4 GPU). Document this tolerance explicitly. CUDA determinism flags (`torch.backends.cudnn.deterministic = True`) can help but may slow training.
