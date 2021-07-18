import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split, cross_val_score
import data


def five_fold_cross_validation(X, y):
    # Create a linear regression object: reg
    reg = LinearRegression()

    # Compute 5-fold cross-validation scores: cv_scores
    cv_scores = cross_val_score(reg, X, y, cv=5)

    # Print the 5-fold cross-validation scores
    print(cv_scores)

    print("Average 5-Fold CV Score: {}".format(np.mean(cv_scores)))


def k_fold_cv_comparison(X, y):
    # Create a linear regression object: reg
    reg = LinearRegression()

    # Perform 3-fold CV
    cvscores_3 = cross_val_score(reg, X, y, cv=3)
    print("Average 3-Fold CV score: {0}", np.mean(cvscores_3))

    # Perform 10-fold CV
    cvscores_10 = cross_val_score(reg, X, y, cv=10)
    print("Average 10-Fold CV score: {0}", np.mean(cvscores_10))


X, y = data.load_gm_data()
five_fold_cross_validation(X, y)
# k_fold_cv_comparison(X, y)
