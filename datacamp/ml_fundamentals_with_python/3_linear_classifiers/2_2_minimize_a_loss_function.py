from scipy.optimize import minimize
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np


def load_boston_housing_data():
    df = pd.read_csv('data/boston.csv')
    X = df.drop(columns='MEDV').values
    y = df['MEDV'].values
    return X, y


def my_loss(w, X, y):
    # The squared error, summed over training examples
    s = 0
    for i in range(y.size):
        # Get the true and predicted target values for example 'i'
        y_i_true = y[i] # for simplicity, intercept is not included here
        y_i_pred = w@X[i] # X[0] turns into w, coefficients in the my_loss function. We can use X[3], X[33] and we produce the same result. 
        s = s + (y_i_true - y_i_pred)**2
    return s


X, y = load_boston_housing_data()
# Returns the w that makes my_loss(w) smallest
w_fit = minimize(my_loss, X[0], args=(X, y)).x
print(w_fit)

# Compare with scikit-learn's LinearRegression coefficients
lr = LinearRegression(fit_intercept=False).fit(X, y)
print(lr.coef_)
