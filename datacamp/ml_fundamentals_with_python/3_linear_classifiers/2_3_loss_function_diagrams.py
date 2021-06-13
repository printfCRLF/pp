import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler


def log_loss(raw_model_output):
    return np.log(1+np.exp(-raw_model_output))
    # https://stats.stackexchange.com/questions/250937/which-loss-function-is-correct-for-logistic-regression


def hinge_loss(raw_model_output):
    return np.maximum(0, 1-raw_model_output)


def compare_logistic_and_hinge_loss():
    # Create a grid of values and plot
    grid = np.linspace(-2, 2, 1000)
    plt.plot(grid, log_loss(grid), label='logistic')
    plt.plot(grid, hinge_loss(grid), label='hinge')
    plt.legend()
    plt.show()


# The logistic loss, summed over training examples
def my_loss(w, X, y):
    s = 0
    for i in range(569):
        raw_model_output = w@X[i]
        s = s + log_loss(raw_model_output * y[i])
    return s


def implement_logistic_regression():
    df = load_breast_cancer()
    samples = df.data[:, :10]
    scaler = StandardScaler()
    X = scaler.fit_transform(samples)
    y = df.target
    y[y == 0] = -1

    # Returns the w that makes my_loss(w) smallest
    w_fit = minimize(my_loss, X[0], args=(X, y)).x
    print(w_fit)

    # Compare with scikit-learn's LogisticRegression
    lr = LogisticRegression(fit_intercept=False, C=1000000).fit(X, y)
    print(lr.coef_)


# compare_logistic_and_hinge_loss()
implement_logistic_regression()
