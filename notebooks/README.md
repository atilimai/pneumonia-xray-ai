# Notebooks

This directory contains Jupyter notebooks for the full project workflow. Notebooks are intended to be run on **Google Colab** using a GPU runtime.

---

## Planned Notebooks

### 1. Exploratory Data Analysis (EDA)
- Class distribution visualization (Pneumonia vs Normal counts)
- Sample image grids for each class
- Image dimension and channel statistics
- Discussion of class imbalance and proposed mitigation strategy
- Train/val/test split verification

### 2. Colab Training
- Environment setup (dependency installation, drive mounting)
- Dataset loading and preprocessing pipeline
- Transfer learning model definition (EfficientNet or ResNet via `timm`)
- Training loop with logging
- Training and validation loss/accuracy curves
- Model checkpoint saving

### 3. Evaluation
- Loading a saved checkpoint for inference
- Computing metrics: accuracy, precision, recall, sensitivity, specificity, ROC AUC
- Confusion matrix visualization
- ROC curve plot
- Error analysis: false positive and false negative galleries

### 4. Grad-CAM Visualization
- Loading a trained model and test images
- Generating Grad-CAM heatmaps for selected examples
- Overlaying heatmaps on original X-ray images
- Qualitative interpretation of highlighted regions
- Disclaimer: outputs are for educational inspection only

---

---

## Google Drive Mount Strategy

All persistent storage during Colab training — dataset files and model checkpoints — must be kept on Google Drive. The Colab runtime's local `/content/` directory is wiped on every session disconnect.

### 1. Mounting Google Drive

Add this cell at the top of every training notebook:

```python
from google.colab import drive
drive.mount('/content/drive')
```

After mounting, Google Drive is accessible at `/content/drive/MyDrive/`.

### 2. Expected Drive Folder Layout

Create the following structure inside your Google Drive before starting training:

```
MyDrive/
└── pneumonia-xray-ai/
    ├── data/
    │   └── raw/
    │       └── chest_xray/
    │           ├── train/
    │           │   ├── NORMAL/
    │           │   └── PNEUMONIA/
    │           ├── val/
    │           │   ├── NORMAL/
    │           │   └── PNEUMONIA/
    │           └── test/
    │               ├── NORMAL/
    │               └── PNEUMONIA/
    └── artifacts/
        ├── checkpoints/
        └── figures/
```

### 3. Path Mapping

| Purpose | Drive path | Local repo equivalent |
|---|---|---|
| Dataset root | `/content/drive/MyDrive/pneumonia-xray-ai/data/raw/chest_xray/` | `data/raw/chest_xray/` |
| Checkpoint directory | `/content/drive/MyDrive/pneumonia-xray-ai/artifacts/checkpoints/` | `artifacts/checkpoints/` |
| Saved figures | `/content/drive/MyDrive/pneumonia-xray-ai/artifacts/figures/` | `artifacts/figures/` |

### 4. Path Constants in Notebooks

Define all Drive paths as constants in a dedicated setup cell so they are easy to update in one place:

```python
import os

DRIVE_ROOT      = "/content/drive/MyDrive/pneumonia-xray-ai"
DATASET_PATH    = os.path.join(DRIVE_ROOT, "data/raw/chest_xray")
CHECKPOINT_DIR  = os.path.join(DRIVE_ROOT, "artifacts/checkpoints")
FIGURES_DIR     = os.path.join(DRIVE_ROOT, "artifacts/figures")

# Create directories if they don't already exist
os.makedirs(CHECKPOINT_DIR, exist_ok=True)
os.makedirs(FIGURES_DIR, exist_ok=True)
```

### 5. Checkpoint Save Convention

Checkpoints must be saved to `CHECKPOINT_DIR` using a filename that encodes the epoch and validation metric so the best run can be identified after a disconnection:

```python
# Save every N epochs
checkpoint_path = os.path.join(CHECKPOINT_DIR, f"checkpoint_epoch{epoch:03d}.pt")
torch.save(model.state_dict(), checkpoint_path)

# Separately keep the best checkpoint by validation loss
best_checkpoint_path = os.path.join(CHECKPOINT_DIR, "best_model.pt")
if val_loss < best_val_loss:
    best_val_loss = val_loss
    torch.save(model.state_dict(), best_checkpoint_path)
```

Keep only the most recent N periodic checkpoints and always keep `best_model.pt`. This avoids filling Drive storage during long runs.

---

## Notes

- Notebooks should be kept clean and reproducible before committing
- Clear all outputs before committing if the notebook contains large figures or tensors
- The `colab_setup_placeholder.ipynb` in this folder is a placeholder for the main training notebook
