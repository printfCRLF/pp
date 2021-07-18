import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import randint
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression, ElasticNet
from sklearn.metrics import mean_squared_error, confusion_matrix, classification_report, roc_curve, roc_auc_score
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, RandomizedSearchCV
import data


def holdout_set_classification(X, y):
    # Create the hyperparameter grid
    c_space = np.logspace(-5, 8, 15)
    param_grid = {'C': c_space, 'penalty': ['l1', 'l2']}

    # Instantiate the logistic regression classifier: logreg
    logreg = LogisticRegression()

    # Create train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.4, random_state=42)

    # Instantiate the GridSearchCV object: logreg_cv
    logreg_cv = GridSearchCV(logreg, param_grid, cv=5)

    # Fit it to the training data
    logreg_cv.fit(X_train, y_train)

    # Print the optimal parameters and best score
    print("Tuned Logistic Regression Parameter: {}".format(logreg_cv.best_params_))
    print("Tuned Logistic Regression Accuracy: {}".format(logreg_cv.best_score_))


def hold_out_set_regression(X, y):
    # Create train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.4, random_state=42)

    # Create the hyperparameter grid
    l1_space = np.linspace(0, 1, 30)
    param_grid = {'l1_ratio': l1_space}

    # Instantiate the ElasticNet regressor: elastic_net
    elastic_net = ElasticNet()

    # Setup the GridSearchCV object: gm_cv
    gm_cv = GridSearchCV(elastic_net, param_grid, cv=5)

    # Fit it to the training data
    gm_cv.fit(X_train, y_train)

    # Predict on the test set and compute metrics
    y_pred = gm_cv.predict(X_test)
    r2 = gm_cv.score(X_test, y_test)
    mse = mean_squared_error(y_test, y_pred)
    print("Tuned ElasticNet l1 ratio: {}".format(gm_cv.best_params_))
    print("Tuned ElasticNet R squared: {}".format(r2))
    print("Tuned ElasticNet MSE: {}".format(mse))


df = pd.read_csv('data/diabetes.csv')
X = df.drop(columns=['diabetes'])
y = df['diabetes']
holdout_set_classification(X, y)
hold_out_set_regression(X, y)
