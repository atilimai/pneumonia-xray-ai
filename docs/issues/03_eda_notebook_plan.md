# Title
Plan exploratory data analysis notebook outputs

## Type
Task

## Summary
Define the expected structure, outputs, and findings of the EDA notebook for the Pneumonia Detection project. A well-planned EDA establishes the evidence base for preprocessing decisions, augmentation strategy, and class imbalance handling. This issue produces the EDA notebook as a documented, committed deliverable.

## Background
The Kermany et al. dataset has known characteristics including class imbalance (~3:1 pneumonia-to-normal in training), a very small validation split, and variable image sizes. The EDA should surface these issues quantitatively and guide modeling decisions.

## Deliverables
- [ ] EDA notebook committed to `notebooks/` with clear markdown sections
- [ ] Class distribution bar chart (per split) saved to `artifacts/figures/`
- [ ] Sample image grids (one per class) saved to `artifacts/figures/`
- [ ] Image dimension statistics documented (min, max, mean width/height)
- [ ] Pixel intensity distribution summary included
- [ ] Notes on class imbalance and proposed mitigation strategy
- [ ] Confirmation that the train/val/test folder structure matches `data/README.md`

## Acceptance Criteria
- [ ] EDA notebook runs end-to-end without errors from the `data/raw/` folder
- [ ] Class distribution chart is present in `artifacts/figures/`
- [ ] Sample image grids are present in `artifacts/figures/`
- [ ] Notebook contains written observations and conclusions, not just code
- [ ] Preprocessing and augmentation decisions are justified with reference to EDA findings
- [ ] Notebook is cleaned (outputs cleared or minimal) before committing

## Dependencies
- `01_repo_scaffold_review.md`
- `02_dataset_ingestion_plan.md`

## Out of Scope
- Model training or evaluation
- Writing reusable preprocessing Python modules (those belong in `src/data/`)
- Any form of data augmentation implementation

## Suggested Labels
`data`, `docs`

## Notes
The validation split contains only 8 images per class. The EDA should flag this explicitly and the evaluation protocol should account for it. Consider noting whether a custom validation split would be more appropriate, but do not implement changes to splits without explicit agreement.
