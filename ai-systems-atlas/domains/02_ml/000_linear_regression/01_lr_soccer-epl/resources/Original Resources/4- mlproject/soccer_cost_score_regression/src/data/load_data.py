from pathlib import Path
from typing import Union

import pandas as pd


def load_data(path_or_url: str) -> pd.DataFrame:
    """Load CSV from local path or URL into a DataFrame."""
    if path_or_url.startswith("http://") or path_or_url.startswith("https://"):
        return pd.read_csv(path_or_url)

    p = Path(path_or_url)
    if not p.exists():
        raise FileNotFoundError(f"Dataset not found at: {p.resolve()}")
    return pd.read_csv(p)
