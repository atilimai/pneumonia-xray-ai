from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


def select_samples(group_df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    return group_df.head(n).copy()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Select test image samples for visualization."
    )

    parser.add_argument(
        "--predictions-csv",
        type=str,
        default="artifacts/predictions/test_predictions.csv",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.5,
    )
    parser.add_argument(
        "--output-csv",
        type=str,
        default="artifacts/reports/test_visualization_samples.csv",
    )
    parser.add_argument(
        "--samples-per-group",
        type=int,
        default=5,
    )

    args = parser.parse_args()

    predictions_path = Path(args.predictions_csv)
    output_path = Path(args.output_csv)

    if not predictions_path.exists():
        raise FileNotFoundError(f"Predictions CSV not found: {predictions_path}")

    df = pd.read_csv(predictions_path)

    required_columns = {"image_path", "y_true", "y_prob"}
    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")

    df["y_true"] = df["y_true"].astype(int)
    df["y_prob"] = df["y_prob"].astype(float)
    df["y_pred"] = (df["y_prob"] >= args.threshold).astype(int)

    groups = {
        "true_positive": df[(df["y_true"] == 1) & (df["y_pred"] == 1)],
        "true_negative": df[(df["y_true"] == 0) & (df["y_pred"] == 0)],
        "false_positive": df[(df["y_true"] == 0) & (df["y_pred"] == 1)],
        "false_negative": df[(df["y_true"] == 1) & (df["y_pred"] == 0)],
    }

    selected_parts = []

    for group_name, group_df in groups.items():
        selected = select_samples(group_df, n=args.samples_per_group)
        selected.insert(0, "sample_group", group_name)
        selected_parts.append(selected)

        print(f"{group_name}: selected {len(selected)} / requested {args.samples_per_group}")

    selected_df = pd.concat(selected_parts, ignore_index=True)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    selected_df.to_csv(output_path, index=False)

    print(f"Saved selected samples to: {output_path}")


if __name__ == "__main__":
    main()