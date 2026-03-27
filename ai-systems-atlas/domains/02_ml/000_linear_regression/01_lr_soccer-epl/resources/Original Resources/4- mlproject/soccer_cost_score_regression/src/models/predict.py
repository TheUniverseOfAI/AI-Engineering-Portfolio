from pathlib import Path
from typing import List

import joblib
import pandas as pd


def load_model(model_path: str = "models/model.joblib"):
    p = Path(model_path)
    if not p.exists():
        raise FileNotFoundError(f"Model not found at: {p.resolve()}")
    return joblib.load(p)


def predict_from_dataframe(
    df: pd.DataFrame,
    model_path: str = "models/model.joblib",
) -> pd.Series:
    model = load_model(model_path)
    preds = model.predict(df)
    return pd.Series(preds, index=df.index, name="prediction")


def predict_from_records(
    records: List[dict],
    model_path: str = "models/model.joblib",
) -> list:
    df = pd.DataFrame.from_records(records)
    preds = predict_from_dataframe(df, model_path)
    return preds.tolist()
