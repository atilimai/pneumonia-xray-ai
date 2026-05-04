# Metrics to be Reported (Issue #60)

For the Pneumonia Detection project, the following metrics will be strictly tracked, logged, and reported for all baseline model experiments to ensure a comprehensive evaluation:

* **Accuracy:** The overall correctness of the model across both Normal and Pneumonia classes.
* **Precision:** The accuracy of positive (Pneumonia) predictions.
* **Recall / Sensitivity:** The model's ability to find all actual Pneumonia cases (Our primary metric for this medical task).
* **Specificity:** The model's ability to correctly identify Normal (healthy) cases without false alarms.
* **ROC AUC:** The model's ability to distinguish between the two classes across all possible decision thresholds.
* **Confusion Matrix:** A detailed tabular breakdown of True Positives, False Positives, True Negatives, and False Negatives.

All experimental results must include these exact metrics for proper comparison.
