# Tests (`tests/`)

This directory will contain unit tests and integration tests for the source modules in `src/`.

> No tests exist yet. This is a Week 1 scaffold placeholder.

---

## Planned Test Coverage

- **Data loading:** Verify that the dataset class returns correctly shaped tensors and valid labels
- **Preprocessing:** Confirm transforms produce expected image dimensions and value ranges
- **Model instantiation:** Check that models load correctly with expected output shapes
- **Metric computation:** Validate sensitivity, specificity, and ROC AUC calculations against known inputs
- **Config loading:** Ensure config files parse correctly and apply expected defaults

---

## Test Framework

Tests will use **pytest**. To run tests once they are added:

```
pytest tests/
```
