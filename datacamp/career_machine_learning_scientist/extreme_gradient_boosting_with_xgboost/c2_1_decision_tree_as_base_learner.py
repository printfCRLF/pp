import xgboost as xgb
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from data import load_ames_housing_data_trimmed


def decision_tree_as_base_learners(X, y):
    # Create the training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=123)

    # Instantiate the XGBRegressor: xg_reg
    xg_reg = xgb.XGBRegressor(objective="reg:linear",
                              n_estimators=10, seed=123)

    # Fit the regressor to the training set
    xg_reg.fit(X_train, y_train)

    # Predict the labels of the test set: preds
    preds = xg_reg.predict(X_test)

    # Compute the rmse: rmse
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    print("RMSE: %f" % (rmse))


def linear_base_learners(X, y):
    # Create the training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=123)

    # Convert the training and testing sets into DMatrixes: DM_train, DM_test
    DM_train = xgb.DMatrix(data=X_train, label=y_train)
    DM_test = xgb.DMatrix(data=X_test, label=y_test)

    # Create the parameter dictionary: params
    params = {"booster": "gblinear", "objective": "reg:linear"}

    # Train the model: xg_reg
    xg_reg = xgb.train(params=params, dtrain=DM_train, num_boost_round=5)

    # Predict the labels of the test set: preds
    preds = xg_reg.predict(DM_test)

    # Compute and print the RMSE
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    print("RMSE: %f" % (rmse))


def evaluating_model_quality(X, y):
    # Create the DMatrix: housing_dmatrix
    housing_dmatrix = xgb.DMatrix(data=X, label=y)

    # Create the parameter dictionary: params
    params = {"objective": "reg:linear", "max_depth": 4}
    # Perform cross-validation: cv_results
    cv_results = xgb.cv(dtrain=housing_dmatrix, params=params, nfold=4,
                        num_boost_round=5, metrics="rmse", as_pandas=True, seed=123)
    # Print cv_results
    print(cv_results)

    # Extract and print final boosting round metric
    print((cv_results["test-rmse-mean"]).tail(1))

    # Perform cross-validation: cv_results
    cv_results = xgb.cv(dtrain=housing_dmatrix, params=params, nfold=4,
                        num_boost_round=5, metrics="mae", as_pandas=True, seed=123)
    # Print cv_results
    print(cv_results)
    # Extract and print final boosting round metric
    print((cv_results["test-mae-mean"]).tail(1))


df = load_ames_housing_data_trimmed()
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
# decision_tree_as_base_learners(X, y)
# linear_base_learners(X, y)
evaluating_model_quality(X, y)
