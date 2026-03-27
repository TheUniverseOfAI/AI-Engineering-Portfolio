# EPL Soccer Cost vs Score Regression (Template Conversion)

This project is a **cleaned-up, production-style version** of your notebook
`regression_part_1.ipynb`, implemented using the generic regression template.

It models the relationship between **team Cost** and **Season Score** in the
English Premier League (EPL).

## 🔧 What this project does

- Reads the EPL soccer CSV: `data/raw/EPL_Soccer_MLR_LR.csv`
- Uses `Cost` as the single feature
- Uses `Score` as the regression target
- Applies a **sqrt transform** to the target (as in your notebook)
- Trains a `LinearRegression` model
- Evaluates with R² and MSE
- Saves the model to `models/epl_soccer_cost_score.joblib`
- Logs details to `logs/app.log`

## 📂 Project Structure (same template)

```text
soccer_cost_score_regression/
├── configs/
│   └── config.yaml
├── data/
│   └── raw/
│       └── EPL_Soccer_MLR_LR.csv      # <-- you must place this file here
├── logs/
├── models/
├── notebooks/
│   └── EDA.ipynb
├── src/
│   ├── data/
│   ├── features/
│   ├── models/
│   └── utils/
├── tests/
├── requirements.txt
└── README.md
```

## 📥 Prepare the data

Download your EPL soccer CSV (same one used in the notebook) and place it here:

```text
data/raw/EPL_Soccer_MLR_LR.csv
```

The filename must match **exactly** (or update `configs/config.yaml`).

## ▶️ How to run training

```bash
python -m venv .venv
source .venv/bin/activate        # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

python -m src.models.train --config configs/config.yaml
```

This will:

1. Load `data/raw/EPL_Soccer_MLR_LR.csv`
2. Use `Cost` as feature, `Score` as target
3. Apply sqrt transform to `Score`
4. Split train/test (75% / 25%, random_state=100)
5. Train `LinearRegression`
6. Print R² and MSE
7. Save model to `models/epl_soccer_cost_score.joblib`
8. Write logs into `logs/app.log`

## 🔁 Reusing this as a Template

For another regression project, you can copy this repo and change only:

- `configs/config.yaml` (dataset path, features, target, transform)
- The data file in `data/raw`

All core code under `src/` stays the same.



# 📘 Regression Fundamentals — Educational Overview

This project is based on the curriculum covering essential regression concepts.

## What Will You Learn?

- What is Regression?
- Types of Regression
- Mean, Variance, Standard Deviation
- Correlation vs Causation
- Observational vs Experimental Data
- Formula for Regression
- Building Simple Linear Regression
- Interpolation & Extrapolation
- Lurking Variables
- Least Squares Estimates
- Gauss-Markov Theorem
- Point Estimators in Regression
- Sampling Distributions of Coefficients
- F-Statistics
- ANOVA Partitioning
- Coefficient of Determination (R²)
- Diagnostic & Remedial Measures

## Project Overview

Regression is one of the foundational techniques in Machine Learning. This project introduces key statistical foundations and demonstrates them through practical examples using soccer player data.

## Aim

Provide a gentle introduction to regression fundamentals and build a simple linear regression model in Python.

## Data Description

Dataset: **Soccer Player Dataset**

- Contains info about players from various clubs
- 10 features including the target variable: **Score**

## Tech Stack

- **Language:** Python
- **Libraries:** pandas, statsmodels, seaborn, matplotlib, sklearn, scipy

## Approach Summary

This project:
- Begins with real-life regression examples
- Introduces simple & multiple regression
- Builds statistical background (formulas, estimators, distributions)
- Implements regression in Python
- Covers interpolation/extrapolation, errors, lurking variables
- Explains R², ANOVA, F-statistics
- Ends with diagnostics and remedial measures
