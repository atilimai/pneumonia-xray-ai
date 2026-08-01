# Colab Training Plan

This document explains how we plan to train the pneumonia model on Google Colab.
The idea is that when someone opens a fresh Colab session, they should be able to
follow one place instead of digging through separate files. It is a planning
document, so it does not actually run training. Local GPU setups and cloud VMs
are not covered here.

Related files:
- `notebooks/colab_training.ipynb` - the actual notebook
- `notebooks/README.md` - step by step workflow
- `docs/CHECKPOINT_STRATEGY.md` and `docs/RESUME_STRATEGY.md` - saving/resuming
- `docs/06_model_selection_plan.md` - GPU memory numbers

## Why we need a plan for Colab

Colab gives free GPUs but it is not very stable, so we have to be careful:

- Free sessions get killed after about 12 hours, and also disconnect if the
  notebook is idle for a while.
- Everything under `/content/` is deleted when the session ends. So anything we
  want to keep has to be saved to Google Drive.
- The GPU (usually a Tesla T4, around 15 GB) is limited, so the model and batch
  size have to fit in that memory.

If we don't plan for this, a disconnect at epoch 40 means we lose everything and
start again from zero. The checkpoint strategy below is there to avoid that.

## The workflow

The steps below are what the training notebook does:

1. Start a runtime with GPU (Runtime > Change runtime type > GPU) and check that
   the GPU is actually available.
2. Clone the repo into Colab (or use an existing copy) and install the packages
   from `requirements.txt`.
3. Mount Google Drive so checkpoints and figures are saved somewhere permanent.
4. Get the dataset. This is either downloaded from Kaggle or read from a copy
   already on Drive (see below).
5. Load the config files from `configs/` instead of hardcoding hyperparameters.
6. Set the random seed (see `docs/RANDOM_SEED_POLICY.md`).
7. Train. During training we save a "latest" checkpoint every few epochs and a
   separate "best" checkpoint to Drive.
8. Evaluate the best checkpoint on the test set and save the figures to Drive.

The only manual thing beyond opening the notebook is mounting Drive (and typing
the Kaggle token if the Kaggle download is used).

## Google Drive

Since the runtime storage is temporary, checkpoints and figures have to go to
Drive. Mounting is just:

```python
from google.colab import drive
drive.mount('/content/drive')
```

We keep the paths in one setup cell so they are easy to change later:

```python
import os

DRIVE_ROOT     = "/content/drive/MyDrive/pneumonia-xray-ai"
DATASET_PATH   = os.path.join(DRIVE_ROOT, "data/raw/chest_xray")
CHECKPOINT_DIR = os.path.join(DRIVE_ROOT, "artifacts/checkpoints")
FIGURES_DIR    = os.path.join(DRIVE_ROOT, "artifacts/figures")

os.makedirs(CHECKPOINT_DIR, exist_ok=True)
os.makedirs(FIGURES_DIR, exist_ok=True)
```

The Drive folders follow the same layout as the repo (`data/raw/chest_xray/`,
`artifacts/checkpoints/`, `artifacts/figures/`), so files line up between Colab
and a local checkout. The full Drive folder tree with the train/val/test and
NORMAL/PNEUMONIA folders is written out in `notebooks/README.md`.

## Getting the dataset

Only one of these is needed:

- Kaggle download (what `colab_training.ipynb` uses): the notebook asks for a
  Kaggle API token and downloads the Chest X-Ray (Pneumonia) dataset straight
  into the runtime. Nothing needs to be prepared on Drive first.
- Drive copy: if the dataset is already on Drive, just point `DATASET_PATH` at
  it and skip the download.

Either way, checkpoints and figures still get saved to Drive.

## Saving checkpoints

The details are in `docs/CHECKPOINT_STRATEGY.md`. Short version:

- Best model: overwrite `best_model.pth` only when the validation metric gets
  better (val loss, or val sensitivity / ROC AUC depending on the evaluation
  protocol).
- Latest model: save `checkpoint_latest.pth` every 5 to 10 epochs, and only keep
  the most recent one so Drive doesn't fill up.
- Save straight to Drive, because local Colab storage can disappear at any time.

## Resuming after a disconnect

Details in `docs/RESUME_STRATEGY.md`. The idea:

1. When the session starts, look in the Drive checkpoint folder for the latest
   checkpoint.
2. If there is one, load the weights, the optimizer/scheduler state, and the last
   epoch number.
3. Continue training from the next epoch.

One thing to be careful about: for resume to actually work, the periodic
checkpoint has to include the optimizer/scheduler state and the epoch number,
not just `model.state_dict()`. The current loop mainly saves the weights, so this
part needs to be extended when resume is actually implemented.

## GPU memory per model

These numbers are from `docs/06_model_selection_plan.md`, measured on a Colab T4
at 224x224 with a single training step. Rough guide:

| Model | batch 8 | batch 16 | batch 32 |
|---|---|---|---|
| resnet18 | ~300 MB | ~470 MB | ~810 MB |
| resnet50 | ~830 MB | ~1500 MB | ~2880 MB |
| tf_efficientnetv2_s | ~1300 MB | ~2520 MB | ~4880 MB |

All of them fit on a T4 at these batch sizes. `tf_efficientnetv2_s` is the model
we picked to start with (see `docs/issues/04_baseline_model_selection.md`). Real
training uses a bit more memory than these numbers because of data loading and
augmentation, so it is good to leave some room.

## Notebook outline

`notebooks/colab_training.ipynb` is the notebook that is committed and runnable.
Roughly it goes:

1. Intro and how to run it
2. Clone repo and install packages
3. Imports
4. Kaggle dataset download and folder check
5. Load config from `configs/`
6. Seed setup
7. Device and runtime mode
8. Transforms and datasets
9. DataLoaders (with an option for small subsets to test quickly)
10. Build the model with `timm`
11. Loss, optimizer, scheduler
12. Train/validation functions
13. Training loop that saves latest + best checkpoints
14. Save history and plot loss/accuracy curves
15. Final test evaluation with the best checkpoint

## Some notes

- Colab Pro helps a lot for long runs. On the free tier, try to keep total
  training under about 12 hours.
- Start each run from a fresh runtime to avoid weird memory/dependency issues.
- Clear the notebook outputs before committing so the repo stays clean.
- A `tqdm` progress bar is useful since Colab sometimes delays the printed output.
- If some model only fits with a tiny batch size, it is better to drop it than to
  train with a bad batch size.
