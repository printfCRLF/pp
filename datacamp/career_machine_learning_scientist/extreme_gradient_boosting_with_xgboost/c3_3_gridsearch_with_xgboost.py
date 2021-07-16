import xgboost as xgb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.metrics import mean_squared_error
from data import load_ames_housing_data_trimmed


def grid_serach_with_xgboost(X, y):
    # Create the parameter grid: gbm_param_grid
    gbm_param_grid = {
        'colsample_bytree': [0.3, 0.7],
        'n_estimators': [50],
        'max_depth': [2, 5]
    }

    # Instantiate the regressor: gbm
    gbm = xgb.XGBRegressor()

    # Perform grid search: grid_mse
    grid_mse = GridSearchCV(estimator=gbm, param_grid=gbm_param_grid,
                            scoring="neg_mean_squared_error", cv=4, verbose=1)

    # Fit grid_mse to the data
    grid_mse.fit(X, y)

    # Print the best parameters and lowest RMSE
    print("Best parameters found: ", grid_mse.best_params_)
    print("Lowest RMSE found: ", np.sqrt(np.abs(grid_mse.best_score_)))


def random_search_with_xgboost(X, y):
    # Create the parameter grid: gbm_param_grid
    gbm_param_grid = {
        'n_estimators': [25],
        'max_depth': range(2, 12)
    }

    # Instantiate the regressor: gbm
    gbm = xgb.XGBRegressor(n_estimators=10)

    # Perform random search: grid_mse
    randomized_mse = RandomizedSearchCV(estimator=gbm, param_distributions=gbm_param_grid,
                                        n_iter=5, scoring="neg_mean_squared_error", cv=4, verbose=1)

    # Fit randomized_mse to the data
    randomized_mse.fit(X, y)

    # Print the best parameters and lowest RMSE
    print("Best parameters found: ", randomized_mse.best_params_)
    print("Lowest RMSE found: ", np.sqrt(np.abs(randomized_mse.best_score_)))


df = load_ames_housing_data_trimmed()
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
grid_serach_with_xgboost(X, y)
random_search_with_xgboost(X, y)
