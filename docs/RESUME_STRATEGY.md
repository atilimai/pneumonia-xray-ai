## Resume-from-Checkpoint Strategy (#89)

Google Colab environments are prone to sudden disconnections and have a strict runtime limit (approx. 12 hours on the free tier). To prevent losing training progress, a robust checkpointing and resumption strategy is implemented.

### 1. Storage and Backup Location
* **Google Drive Mounting:** Google Drive must be mounted at the beginning of the Colab session (`/content/drive`).
* **Artifacts Directory:** Checkpoints must be saved directly to a persistent Google Drive directory (e.g., `/content/drive/MyDrive/pneumonia_project/artifacts/checkpoints/`) rather than the local Colab disk.

### 2. Saving Frequency and Strategy
* **Periodic Checkpoints:** The model state, optimizer state, and current epoch number must be saved **every 5 to 10 epochs**. These files should be named systematically (e.g., `checkpoint_epoch_*.pth`).
* **Best Model Isolation:** The best-performing model based on validation metrics must always be saved separately as `best_model.pth` to ensure the top weights are never overwritten by later subpar epochs.

### 3. Resumption Logic Workflow
When a session disconnects and a fresh Colab environment is provisioned, the training pipeline must automatically support recovery:
1. **Check for Existing Progress:** The script checks the persistent Google Drive folder for the latest `checkpoint_epoch_*.pth`.
2. **State Restoration:** If a checkpoint is found, the system:
   * Loads the model weights via `model.load_state_dict()`.
   * Restores the optimizer and scheduler configurations to preserve the learning rate state.
   * Extracts the last completed epoch number.
3. **Seamless Resumption:** Training resumes safely from `last_completed_epoch + 1`, preventing any redundant computation.


