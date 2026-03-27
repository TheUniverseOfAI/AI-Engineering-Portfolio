import argparse
from pathlib import Path

import yaml
from joblib import dump
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

from src.data.load_data import load_data
from src.features.preprocess import (
    select_features_and_target,
    apply_target_transform,
    train_test_split_xy,
)
from src.utils.logger import get_logger


def train_from_config(config_path: str) -> dict:
    logger = get_logger("train")

    cfg_path = Path(config_path)
    if not cfg_path.exists():
        raise FileNotFoundError(f"Config file not found at: {cfg_path.resolve()}")

    logger.info(f"Loading config from: {cfg_path}")
    with cfg_path.open("r") as f:
        cfg = yaml.safe_load(f)

    dataset_path = cfg["dataset_path"]
    feature_columns = cfg["feature_columns"]
    target_column = cfg["target_column"]
    task_type = cfg.get("task_type", "regression")
    target_transform = cfg.get("target_transform", "none")
    test_size = cfg.get("test_size", 0.25)
    random_state = cfg.get("random_state", 42)
    model_output = cfg["model_output"]

    if task_type != "regression":
        raise ValueError(f"Only 'regression' is supported in this template. Got: {task_type}")

    logger.info("Loading data...")
    df = load_data(dataset_path)
    logger.info(f"Loaded dataframe with shape: {df.shape}")

    logger.info("Selecting features and target...")
    X, y = select_features_and_target(df, feature_columns, target_column)

    logger.info(f"Applying target transform: {target_transform}")
    y_transformed = apply_target_transform(y, target_transform)

    logger.info("Splitting train/test...")
    X_train, X_test, y_train, y_test = train_test_split_xy(
        X, y_transformed, test_size=test_size, random_state=random_state
    )

    logger.info("Training LinearRegression model...")
    model = LinearRegression()
    model.fit(X_train, y_train)

    logger.info("Evaluating model...")
    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)
    r2 = r2_score(y_test, preds)
    logger.info(f"R²: {r2:.4f}, MSE: {mse:.4f}")

    logger.info(f"Saving model to: {model_output}")
    Path(model_output).parent.mkdir(parents=True, exist_ok=True)
    dump(model, model_output)

    metrics = {"r2": float(r2), "mse": float(mse)}
    return metrics


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train a regression model from config.")
    parser.add_argument(
        "--config",
        "-c",
        type=str,
        required=True,
        help="Path to YAML config file.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    train_from_config(args.config)
