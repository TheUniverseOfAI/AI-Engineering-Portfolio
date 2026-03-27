import pandas as pd

from src.features.preprocess import (
    select_features_and_target,
    apply_target_transform,
    train_test_split_xy,
)


def test_select_features_and_target_and_split():
    df = pd.DataFrame(
        {
            "feature_1": [1, 2, 3, 4],
            "feature_2": [10, 20, 30, 40],
            "target": [0.1, 0.2, 0.3, 0.4],
        }
    )

    X, y = select_features_and_target(df, ["feature_1", "feature_2"], "target")
    assert X.shape == (4, 2)
    assert y.shape == (4,)

    X_train, X_test, y_train, y_test = train_test_split_xy(X, y, test_size=0.5, random_state=42)
    assert len(X_train) == len(y_train) == 2
    assert len(X_test) == len(y_test) == 2


def test_apply_target_transform():
    s = pd.Series([1.0, 4.0, 9.0])

    none_t = apply_target_transform(s, "none")
    assert (none_t == s).all()

    log_t = apply_target_transform(s, "log")
    assert (log_t > 0).all()

    sqrt_t = apply_target_transform(s, "sqrt")
    assert (sqrt_t == pd.Series([1.0, 2.0, 3.0])).all()
