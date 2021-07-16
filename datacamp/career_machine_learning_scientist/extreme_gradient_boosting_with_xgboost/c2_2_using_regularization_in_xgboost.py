import xgboost as xgb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from data import load_ames_housing_data_trimmed


def using_regularization(X, y):
    # Create the DMatrix: housing_dmatrix
    housing_dmatrix = xgb.DMatrix(data=X, label=y)
    reg_params = [1, 10, 100]
    # Create the initial parameter dictionary for varying l2 strength: params
    params = {"objective": "reg:linear", "max_depth": 3}
    # Create an empty list for storing rmses as a function of l2 complexity
    rmses_l2 = []
    # Iterate over reg_params
    for reg in reg_params:
        # Update l2 strength
        params["lambda"] = reg
        # Pass this updated param dictionary into cv
        cv_results_rmse = xgb.cv(dtrain=housing_dmatrix, params=params, nfold=2,
                                 num_boost_round=5, metrics="rmse", as_pandas=True, seed=123)
        # Append best rmse (final round) to rmses_l2
        rmses_l2.append(cv_results_rmse["test-rmse-mean"].tail(1).values[0])

    # Look at best rmse per l2 param
    print("Best rmse as a function of l2:")
    print(pd.DataFrame(list(zip(reg_params, rmses_l2)),
          columns=["l2", "rmse"]))


def visualizing_individual_xgboost_trees(X, y):
    # Create the DMatrix: housing_dmatrix
    housing_dmatrix = xgb.DMatrix(data=X, label=y)
    # Create the parameter dictionary: params
    params = {"objective": "reg:linear", "max_depth": 2}
    # Train the model: xg_reg
    xg_reg = xgb.train(
        params=params, dtrain=housing_dmatrix, num_boost_round=10)

    # Plot the first tree
    xgb.plot_tree(xg_reg, num_trees=0)
    plt.show()
    # Plot the fifth tree
    xgb.plot_tree(xg_reg, num_trees=4)
    plt.show()
    # Plot the last tree sideways
    xgb.plot_tree(xg_reg, num_trees=9, rankdir="LR")
    plt.show()


def visualzing_feature_importances(X, y):
    # Create the DMatrix: housing_dmatrix
    housing_dmatrix = xgb.DMatrix(data=X, label=y)

    # Create the parameter dictionary: params
    params = {"objective": "reg:linear", "max_depth": 4}

    # Train the model: xg_reg
    xg_reg = xgb.train(
        params=params, dtrain=housing_dmatrix, num_boost_round=10)

    # Plot the feature importances
    xgb.plot_importance(xg_reg)
    plt.show()


df = load_ames_housing_data_trimmed()
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
# using_regularization(X, y)
# visualizing_individual_xgboost_trees(X, y)
visualzing_feature_importances(X, y)
