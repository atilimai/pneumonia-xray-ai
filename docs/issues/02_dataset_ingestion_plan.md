# Title
Dataset ingestion plan and folder contract

## Type
Task

## Summary
Define and document the process for downloading, verifying, and placing the Kermany et al. chest X-ray dataset into the correct local folder structure. This establishes the data contract that all downstream notebooks and source modules will depend on. Without a clear folder contract, data loading code cannot be written consistently.

## Background
The dataset is available on Kaggle as "Chest X-Ray Images (Pneumonia)" by Kermany et al. It must be downloaded manually and placed under `data/raw/` according to the structure defined in `data/README.md`. The dataset must not be committed to the repository. This issue ensures the folder contract is clearly documented, verified, and understood.

## Deliverables
- [ ] `data/README.md` updated to reflect the exact expected folder structure after download
- [ ] Expected file counts per split documented (train, val, test; per class)
- [ ] Class imbalance ratios documented in `docs/DATASET.md`
- [ ] Folder contract agreed and referenced from `src/data/` module design
- [ ] Verification checklist for confirming dataset integrity (expected counts, no missing files)
- [ ] `.gitignore` confirmed to exclude all files under `data/raw/`, `data/interim/`, `data/processed/`

## Acceptance Criteria
- [ ] `data/README.md` contains the exact expected post-download folder structure
- [ ] Class counts and imbalance ratio for train/val/test splits are documented
- [ ] `docs/DATASET.md` reflects current understanding of the dataset's properties
- [ ] No dataset files appear in `git status` or `git ls-files`
- [ ] A developer can follow `data/README.md` alone to correctly place the dataset

## Dependencies
- `01_repo_scaffold_review.md`

## Out of Scope
- Writing data loading Python code
- Preprocessing or transforming the dataset
- Downloading the dataset as part of CI or automation

## Suggested Labels
`data`, `setup`, `docs`

## Notes
The Kaggle dataset has a known issue with a very small validation split (8 images per class). This limitation should be noted explicitly. The train/val/test split boundaries from the original Kaggle download must be preserved to avoid data leakage.
