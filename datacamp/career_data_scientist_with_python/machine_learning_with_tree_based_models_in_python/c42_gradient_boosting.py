from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error as MSE
from sklearn.model_selection import train_test_split
from data import load_bike_sharing_data


def gradient_boosting_in_action(X_train, X_test, y_train, y_test): 
    # Instantiate gb
    gb = GradientBoostingRegressor(max_depth=4, n_estimators=200, random_state=2)
    # Fit gb to the training set
    gb.fit(X_train, y_train)

    # Predict test set labels
    y_pred = gb.predict(X_test)
    # Compute MSE
    mse_test = MSE(y_test, y_pred)
    # Compute RMSE
    rmse_test = mse_test**(1/2)
    # Print RMSE
    print('Test set RMSE of gb: {:.3f}'.format(rmse_test))


bikes = load_bike_sharing_data()
X = bikes.drop(columns=["cnt"])
y = bikes["cnt"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
gradient_boosting_in_action(X_train, X_test, y_train, y_test)