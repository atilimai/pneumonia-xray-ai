# Random Seed & Reproducibility Policy

As part of our Reproducibility and Rerun Checklist (#12), it is mandatory to enforce deterministic behavior across all model training and evaluation scripts. This ensures that our experiments yield consistent, reproducible results across different Colab sessions and team members.

## The Global Seed
Our official project seed is **`42`**.

## Application Areas
All scripts must explicitly set this seed for the following operations:

### 1. Data Split Seed
Whenever splitting data into Train/Val/Test or shuffling datasets, the random state must be fixed.
* **Example:** `train_test_split(..., random_state=42)`

### 2. Model Initialization Seed
To ensure neural network weights are initialized consistently across runs, seeds must be set for all relevant libraries before building the model.
* **PyTorch:** `torch.manual_seed(42)`
* **NumPy:** `np.random.seed(42)`
* **Python Native:** `random.seed(42)`

### 3. Augmentation Seed
Data augmentations (e.g., random rotations, flips) must be deterministic per epoch if possible, or seeded via the DataLoader worker functions to ensure the exact same transformations are applied if an experiment is rerun.

## Global Seeding Snippet
Please copy and paste the following snippet at the top of your Colab notebooks or training scripts:

```python
import random
import numpy as np
import torch

def set_global_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False

set_global_seed(42)
