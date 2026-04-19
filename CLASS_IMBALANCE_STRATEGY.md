# Class Imbalance and Pre-processing Strategy Report

## 1. Observations Derived from Exploratory Data Analysis (EDA) Outputs
Based on the exploratory data analysis (EDA) outputs generated in Figures 32 and 34, we identified critical dataset characteristics requiring urgent attention prior to commencing model training:

* **Severe Class Imbalance:** The training set exhibits a highly skewed distribution. There is an approximate 1:3 ratio between classes (~1,300 NORMAL images versus ~3,900 PNEUMONIA images). If left unaddressed, the model will develop a strong bias towards the majority class (Pneumonia), which will yield high accuracy and recall, but result in unacceptably low specificity (false positives for healthy patients).

* **Insufficient Validation Set:** The current validation set contains only 16 images in total (8 per class). This sample size is not statistically significant and will not provide reliable criteria for model evaluation or early stopping during training.
* **High Dimensional Variability:** Image dimensions vary significantly across the dataset, ranging from a minimum of 384x127 pixels to a maximum of 2916x2713 pixels.

## 2. Recommended Reduction Strategies
To ensure a robust and unbiased model, we can apply the following strict guidelines for the training pipeline:

### A. Algorithmic Reduction (Loss Weighting)
* **Action:** Apply class weights within the PyTorch loss function.

***Details:*** We will use `BCEWithLogitsLoss(pos_weight=...)` or a weighted `CrossEntropyLoss`. By assigning a higher penalty (approximately three times as high) for misclassifying the minority ‘NORMAL’ class, we prevent the network from optimising equally for both classes and stop the majority class from collapsing.

### B. Data-Level Reduction (Augmentation and Rescaling)
* **Targeted Augmentation:** Apply basic transformations within the PyTorch `DataLoader` (e.g., slight rotations up to 10 degrees, horizontal flips, and contrast adjustments) to increase the variance of the training data and prevent overfitting.

* **Standardised Resizing:** All inputs must be resized and normalised to a uniform resolution (e.g., 224x224 or 512x512) to ensure they conform to the expected input format of the selected transfer learning architectures (ResNet50 / EfficientNet) and to address excessive variance in raw dimensions.

### C. Data Split Revision
* **Action:** Reallocate the training/validation splits.

* **Details:** We must reallocate a portion of the training data (e.g., 10–15%) to the validation set. A validation set comprising at least several hundred images is essential to ensure that our training curves (loss/accuracy) accurately reflect real-world generalisation.
