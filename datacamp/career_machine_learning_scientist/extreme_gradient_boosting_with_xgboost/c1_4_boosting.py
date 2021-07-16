import xgboost as xgb
import numpy as np
from sklearn.model_selection import train_test_split
from data import load_ridesharing_churn_data


def measuring_accuracy_and_auc(churn_data):
    # Create arrays for the features and the target: X, y
    X, y = churn_data.iloc[:, :-1], churn_data.iloc[:, -1]

    # Create the DMatrix from X and y: churn_dmatrix
    churn_dmatrix = xgb.DMatrix(data=X, label=y)

    # Create the parameter dictionary: params
    params = {"objective": "reg:logistic", "max_depth": 3}

    # Perform cross-validation: cv_results
    cv_results = xgb.cv(dtrain=churn_dmatrix, params=params,
                        nfold=3, num_boost_round=5,
                        metrics="error", as_pandas=True, seed=123)

    # Print cv_results
    print(cv_results)
    # Print the accuracy
    print(((1-cv_results["test-error-mean"]).iloc[-1]))

    # Perform cross_validation: cv_results
    cv_results = xgb.cv(dtrain=churn_dmatrix, params=params,
                        nfold=3, num_boost_round=5,
                        metrics="auc", as_pandas=True, seed=123)
    # Print cv_results
    print(cv_results)
    # Print the AUC
    print((cv_results["test-auc-mean"]).iloc[-1])


churn_data = load_ridesharing_churn_data()
measuring_accuracy_and_auc(churn_data)
