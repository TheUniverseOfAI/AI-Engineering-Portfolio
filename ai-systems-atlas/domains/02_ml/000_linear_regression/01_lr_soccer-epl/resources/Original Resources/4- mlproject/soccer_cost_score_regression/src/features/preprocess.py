from typing import List, Tuple

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


def select_features_and_target(
    df: pd.DataFrame,
    feature_columns: List[str],
    target_column: str,
) -> Tuple[pd.DataFrame, pd.Series]:
    """Select feature matrix X and target vector y from a DataFrame."""
    missing_features = [col for col in feature_columns if col not in df.columns]
    if missing_features:
        raise KeyError(f"Missing feature columns in dataframe: {missing_features}")

    if target_column not in df.columns:
        raise KeyError(f"Target column '{target_column}' not found in dataframe")

    X = df[feature_columns]
    y = df[target_column]
    return X, y


def apply_target_transform(y: pd.Series, method: str) -> pd.Series:
    """Apply a simple transform to the target for regression.

    Supported:
      - "none": return y unchanged
      - "log":  log1p transform
      - "sqrt": square-root transform
    """
    if method == "none":
        return y
    if method == "log":
        # log1p is safer for small values (log(1 + y))
        return np.log1p(y)
    if method == "sqrt":
        return np.sqrt(y)

    raise ValueError(f"Unsupported target_transform method: {method}")


def train_test_split_xy(
    X: pd.DataFrame,
    y: pd.Series,
    test_size: float = 0.25,
    random_state: int = 42,
):
    """Wrapper around train_test_split for convenience."""
    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
    )
