from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as MSE
from data import load_automobile_data

X, y = load_automobile_data()
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2)


def train_your_first_regression_tree(X_train, X_test, y_train, y_test):
    # Instantiate dt
    dt = DecisionTreeRegressor(
        max_depth=8, min_samples_leaf=0.13, random_state=3)
    # Fit dt to the training set
    dt.fit(X_train, y_train)
    return dt


def evaluate_the_regression_tree(X_train, X_test, y_train, y_test, dt):
    # Compute y_pred
    y_pred = dt.predict(X_test)
    # Compute mse_dt
    mse_dt = MSE(y_test, y_pred)
    # Compute rmse_dt
    rmse_dt = mse_dt**(1/2)
    # Print rmse_dt
    print("Test set RMSE of dt: {:.2f}".format(rmse_dt))

    return rmse_dt


def linear_regression_vs_regression_tree(X_train, X_test, y_train, y_test, rmse_dt):
    # Instatiate logreg
    lr = LinearRegression(fit_intercept=True, normalize=False)
    lr.fit(X_train, y_train)
    y_pred_lr = lr.predict(X_test)

    # Compute mse_lr
    mse_lr = MSE(y_pred_lr, y_test)

    # Compute rmse_lr
    rmse_lr = mse_lr**(1/2)

    # Print rmse_lr
    print('Linear Regression test set RMSE: {:.2f}'.format(rmse_lr))

    # Print rmse_dt
    print('Regression Tree test set RMSE: {:.2f}'.format(rmse_dt))


dt = train_your_first_regression_tree(X_train, X_test, y_train, y_test)
rmse_dt = evaluate_the_regression_tree(X_train, X_test, y_train, y_test, dt)
linear_regression_vs_regression_tree(X_train, X_test, y_train, y_test, rmse_dt)
