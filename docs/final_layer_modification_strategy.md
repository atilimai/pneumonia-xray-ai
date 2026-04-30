# Final Layer Modification Strategy (Issue #53)

As part of the baseline model comparison strategy, here is the documentation for the final layer modification:

We will use a basic transfer learning approach to transition our multi-class pretrained models (EfficientNet/ResNet) to binary classification. 

**Strategy:**
1. **Model:** Use the selected pretrained architecture from the `timm` library.
2. **Freeze:** Freeze all existing deep layers to retain their high-dimensional feature extraction capabilities.
3. **Modify Head:** Remove the original 1000-class classification head (`model.fc` or `model.classifier`).
4. **Binary Classifier:** Replace it with a new, untrained binary classifier (2 outputs for Normal vs. Pneumonia).

This approach removes the need for training huge models from scratch while retaining high accuracy.
