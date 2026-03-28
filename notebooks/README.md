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

## Notes

- Notebooks should be kept clean and reproducible before committing
- Clear all outputs before committing if the notebook contains large figures or tensors
- The `colab_setup_placeholder.ipynb` in this folder is a placeholder for the main training notebook
