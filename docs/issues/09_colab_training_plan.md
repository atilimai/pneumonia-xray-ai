# Title
Plan Colab training workflow and constraints

## Type
Task

## Summary
Plan the Google Colab-based training workflow for the Pneumonia Detection model, including session management, dataset access from Google Drive, checkpoint saving strategy, and known Colab constraints. Without explicit planning, Colab instability (disconnections, memory limits) can result in lost training progress.

## Background
Google Colab provides free GPU access but has significant limitations: sessions disconnect after inactivity, runtime memory is limited, and persistent storage requires Google Drive integration. This issue defines the training workflow to work reliably within these constraints.

## Deliverables
- [ ] Colab training workflow documented in `notebooks/README.md` or a dedicated section
- [ ] Google Drive mount strategy documented (dataset path, checkpoint save path)
- [ ] Checkpoint saving frequency agreed (e.g., every N epochs and on validation improvement)
- [ ] Colab GPU memory requirements estimated for each candidate architecture
- [ ] Resume-from-checkpoint strategy documented
- [ ] Training notebook outline committed to `notebooks/colab_setup_placeholder.ipynb` or a new notebook

## Acceptance Criteria
- [ ] Colab training workflow is documented end-to-end
- [ ] Drive mount paths are consistent with `data/` and `artifacts/` folder contracts
- [ ] Checkpoint saving strategy is sufficient to recover from a Colab disconnection without full retraining
- [ ] GPU memory usage is estimated for the chosen architecture and batch size
- [ ] The training notebook can be run on a fresh Colab session without manual steps beyond Drive mounting

## Dependencies
- `02_dataset_ingestion_plan.md`
- `04_baseline_model_selection.md`
- `05_config_design.md`

## Out of Scope
- Running training (this is planning only)
- Setting up local GPU training
- Kubernetes or cloud VM training

## Suggested Labels
`modeling`, `setup`

## Notes
Google Colab Pro significantly reduces the risk of session disconnections during long training runs. If the free tier is used, training should be structured to complete within approximately 12 hours. Saving checkpoints to Google Drive every 5–10 epochs and keeping the best-performing checkpoint separately are recommended practices. The `tqdm` progress bar should be used to monitor epoch progress even if Colab output is delayed.
