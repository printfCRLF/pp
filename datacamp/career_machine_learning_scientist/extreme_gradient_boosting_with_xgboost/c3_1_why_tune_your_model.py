import xgboost as xgb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from data import load_ames_housing_data_trimmed


def tunning_the_number_of_boosting_rounds(X, y):
    # Create the DMatrix: housing_dmatrix
    housing_dmatrix = xgb.DMatrix(X, y)
    # Create the parameter dictionary for each tree: params
    params = {"objective": "reg:linear", "max_depth": 3}
    # Create list of number of boosting rounds
    num_rounds = [5, 10, 15]
    # Empty list to store final round rmse per XGBoost model
    final_rmse_per_round = []

    # Iterate over num_rounds and build one model per num_boost_round parameter
    for curr_num_rounds in num_rounds:
        # Perform cross-validation: cv_results
        cv_results = xgb.cv(dtrain=housing_dmatrix, params=params, nfold=3,
                            num_boost_round=curr_num_rounds, metrics="rmse", as_pandas=True, seed=123)
        # Append final round RMSE
        final_rmse_per_round.append(
            cv_results["test-rmse-mean"].tail().values[-1])

    # Print the resultant DataFrame
    num_rounds_rmses = list(zip(num_rounds, final_rmse_per_round))
    print(pd.DataFrame(num_rounds_rmses, columns=[
          "num_boosting_rounds", "rmse"]))


def early_stopping(X, y):
    # Create your housing DMatrix: housing_dmatrix
    housing_dmatrix = xgb.DMatrix(data=X, label=y)

    # Create the parameter dictionary for each tree: params
    params = {"objective": "reg:linear", "max_depth": 4}

    # Perform cross-validation with early stopping: cv_results
    cv_results = xgb.cv(dtrain=housing_dmatrix, params=params, nfold=3, num_boost_round=50,
                        early_stopping_rounds=10, metrics="rmse", as_pandas=True, seed=123)

    # Print cv_results
    print(cv_results)


df = load_ames_housing_data_trimmed()
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
# tunning_the_number_of_boosting_rounds(X, y)
early_stopping(X, y)
