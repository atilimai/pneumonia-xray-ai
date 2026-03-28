# Project Overview — Pneumonia Detection from Chest X-Rays

## Scope

This project builds a binary image classifier to distinguish **Pneumonia** from **Normal** chest X-ray images using deep learning and transfer learning techniques. It covers dataset preparation, model training, evaluation, visual explainability (Grad-CAM), and a lightweight demo deployment.

## Out of Scope

- Multi-class classification (e.g., bacterial vs. viral pneumonia)
- Real-time inference systems or production medical deployments
- Clinical validation or regulatory compliance
- Custom dataset collection or annotation
- Federated learning or edge deployment

## Expected Deliverables

- Cleaned and preprocessed dataset pipeline
- Trained binary classification model (EfficientNet or ResNet)
- Evaluation report with sensitivity, specificity, and ROC AUC
- Grad-CAM heatmap visualizations for model interpretability
- Reproducible Colab training notebook
- Documentation covering methodology, risks, and limitations
- GitHub release with model artifacts
- Optional: Hugging Face model page and Gradio demo

## Minimum Viable Version

A working binary classifier that:
- Trains and evaluates on the Kermany et al. dataset
- Reports accuracy, sensitivity, specificity, and ROC AUC on the test split
- Produces at least a basic confusion matrix and ROC curve
- Is reproducible from a single Colab notebook

## Final Demo Vision

A lightweight interactive demo (likely hosted on Hugging Face Spaces using Gradio) where a user can upload a chest X-ray image and receive:
- A predicted label (Pneumonia / Normal) with confidence score
- A Grad-CAM heatmap overlay highlighting influential image regions
- A clear disclaimer that the tool is for educational use only
