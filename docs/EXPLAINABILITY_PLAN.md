# Grad-CAM Explainability Workflow & Naming Conventions

To maintain a clean, reproducible, and easily parsable workspace during the Explainable AI (XAI) phase, all Grad-CAM heatmap outputs must adhere to the following strict saving locations and naming conventions.

## 1. Save Location
All generated Grad-CAM overlays must be saved in the following directory:
`artifacts/figures/`

## 2. Naming Convention
Output filenames must strictly follow this template:
`gradcam_[true_label]_pred_[predicted_label]_[image_id].png`

### Parameters:
* **true_label:** The actual ground truth of the image (`normal` or `pneumonia`).
* **predicted_label:** The class predicted by our model (`normal` or `pneumonia`).
* **image_id:** The unique identifier or original filename of the test image (without the original extension).

## 3. Examples
* **True Positive (Correct):** `artifacts/figures/gradcam_pneumonia_pred_pneumonia_person1946_bacteria_4875.png`
* **True Negative (Correct):** `artifacts/figures/gradcam_normal_pred_normal_IM-0115-0001.png`
* **False Negative (Critical Error):** `artifacts/figures/gradcam_pneumonia_pred_normal_person1946_bacteria_4875.png`

Adhering to this convention will allow us to easily write automated scripts to filter and review False Negatives vs. True Positives during our final error analysis.
