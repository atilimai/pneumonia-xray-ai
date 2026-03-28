# Title
Design configuration structure for experiments

## Type
Task

## Summary
Design and document the YAML configuration schema for model, training, and evaluation parameters. A well-designed config structure separates hyperparameters from code, making experiments reproducible and easy to compare. This issue defines the config schema and creates initial placeholder config files before any training begins.

## Background
The project uses `configs/model/`, `configs/training/`, and `configs/evaluation/` directories. Without an agreed config schema, source code cannot be written consistently and experiments cannot be reliably reproduced. This issue ensures the config design is in place before modeling work starts.

## Deliverables
- [ ] Config schema documented in `configs/README.md`
- [ ] Initial `configs/model/base.yaml` placeholder file with all expected keys and example values
- [ ] Initial `configs/training/base.yaml` placeholder file with all expected keys and example values
- [ ] Initial `configs/evaluation/base.yaml` placeholder file with all expected keys and example values
- [ ] Config loading approach agreed (e.g., `PyYAML`, `OmegaConf`, or `Hydra`) and documented

## Acceptance Criteria
- [ ] All three config directories contain at least one example YAML file
- [ ] Config schema covers: model name, image size, batch size, learning rate, epochs, augmentation flags, metrics to compute, and decision threshold
- [ ] `configs/README.md` is updated to describe the schema and format
- [ ] Config files are valid YAML (no syntax errors)
- [ ] The config design is consistent with the model selection decisions from `04_baseline_model_selection.md`

## Dependencies
- `01_repo_scaffold_review.md`
- `04_baseline_model_selection.md`

## Out of Scope
- Implementing config loading code in `src/`
- Running training with configs
- Supporting multiple config formats simultaneously

## Suggested Labels
`setup`, `modeling`

## Notes
Consider keeping the initial config design simple. A flat YAML file with clearly named keys is easier to use than a heavily nested schema. `OmegaConf` or `Hydra` are good options if config composition is needed later, but plain `PyYAML` is sufficient for a minimal implementation. Config files must be committed to the repository — they are documentation as much as they are functional inputs.
