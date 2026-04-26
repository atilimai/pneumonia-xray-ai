To systematically evaluate and select the best baseline model for our Pneumonia Detection task, we have established the following selection criteria. Since this is a medical imaging project operating under specific hardware constraints, accuracy alone is insufficient.

Models will be ranked and selected based on the following prioritized metrics:

## 1. Primary Clinical Metric: Sensitivity (Recall)
* **Priority:** HIGH
* **Reasoning:** In medical diagnostics, a False Negative (missing a patient with pneumonia) is significantly more dangerous than a False Positive. The baseline model must maximize Sensitivity for the 'PNEUMONIA' class to ensure the lowest possible miss rate.

## 2. Overall Discriminative Power: ROC AUC
* **Priority:** HIGH
* **Reasoning:** The Area Under the Receiver Operating Characteristic Curve (ROC AUC) will help us evaluate the model's overall ability to distinguish between NORMAL and PNEUMONIA classes, regardless of the classification threshold. This is especially crucial given our class imbalance.

## 3. Hardware & Practical Constraints
* **Colab Memory Fit (VRAM Limit):** * **Constraint:** The model must train comfortably within the Google Colab free tier limits (approx. 15GB T4 GPU VRAM) with a reasonable batch size (e.g., 16 or 32). Models causing `CUDA Out of Memory` errors will be rejected.
* **Parameter Count:** * **Constraint:** We will prioritize lightweight architectures (e.g., ResNet18, ResNet50, EfficientNet-B0/B1) over massive ones. A smaller parameter count reduces training time, prevents overfitting on our limited dataset, and satisfies the Colab memory constraint.

## 4. Evaluation Methodology
All candidate models will be tracked and compared using **Weights & Biases (W&B)**. The final selection will be made by comparing the W&B dashboards for the aforementioned metrics on the validation and test splits.
