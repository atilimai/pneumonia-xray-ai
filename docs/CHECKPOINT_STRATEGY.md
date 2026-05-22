# Model Checkpoint & Saving Strategy

Given the volatility of Google Colab environments (unexpected runtime disconnects) and local disk constraints, we have agreed on the following strict checkpointing frequency and logic:

## 1. Save on Validation Improvement ("Best Model")
* **Rule:** The primary model checkpoint will ONLY be saved when there is an improvement in our target validation metric.
* **Target Metric:** Validation Loss (or highest Val Sensitivity/ROC AUC as defined in our evaluation protocol).
* **Action:** Overwrite the `best_model.pth` (or `.h5`) file.
* **Reasoning:** This ensures we capture the model at its peak generalization capability before any overfitting begins, adhering to the Early Stopping principle.

## 2. Periodic Fallback Saves ("Latest Model")
* **Rule:** Save a secondary checkpoint every **5 epochs** regardless of performance.
* **Action:** Save as `checkpoint_latest.pth`. 
* **Storage Constraint:** To prevent Colab's local disk from running Out of Storage (OOS), we will only keep the *most recent* fallback checkpoint. Older periodic checkpoints will be deleted programmatically.
* **Reasoning:** If the Colab session crashes at epoch 43, we can resume training from epoch 40 (`checkpoint_latest.pth`) instead of starting from scratch at epoch 0.

## 3. Remote Sync (Highly Recommended)
* **Rule:** All saved checkpoints (`best_model.pth` and `checkpoint_latest.pth`) must be synced to Google Drive or logged as artifacts in Weights & Biases (W&B) immediately after saving. Local Colab storage is ephemeral and must not be trusted.
