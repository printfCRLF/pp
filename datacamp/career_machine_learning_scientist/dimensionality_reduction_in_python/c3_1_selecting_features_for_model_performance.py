import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import VarianceThreshold, RFE
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from data import load_diabetes_data


def predict_with_logistic_regression(df):
    X = df.drop("test", axis=1)
    y = df["test"].apply(lambda x: 1 if x == "positive" else 0)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    # Fit the scaler on the training features and transform these in one go
    scaler = StandardScaler()
    X_train_std = scaler.fit_transform(X_train)

    # Fit the logistic regression model on the scaled training data
    lr = LogisticRegression()
    lr.fit(X_train_std, y_train)

    # Scale the test features
    X_test_std = scaler.transform(X_test)

    # Predict diabetes presence on the scaled test set
    y_pred = lr.predict(X_test_std)

    # Prints accuracy metrics and feature coefficients
    print("{0:.1%} accuracy on test set.".format(
        accuracy_score(y_test, y_pred)))
    print(dict(zip(X.columns, abs(lr.coef_[0]).round(2))))


def manual_recursive_feature_elimination(diabetes_df):
    # Only keep the feature with the highest coefficient
    X = diabetes_df[['glucose']]
    y = df["test"].apply(lambda x: 1 if x == "positive" else 0)

    # Performs a 25-75% train test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=0)

    # Scales features and fits the logistic regression model to the data
    scaler = StandardScaler()
    lr = LogisticRegression()
    lr.fit(scaler.fit_transform(X_train), y_train)

    # Calculates the accuracy on the test set and prints coefficients
    acc = accuracy_score(y_test, lr.predict(scaler.transform(X_test)))
    print("{0:.1%} accuracy on test set.".format(acc))
    print(dict(zip(X.columns, abs(lr.coef_[0]).round(2))))


def automatic_recursive_feature_elimination(df):
    X = df.drop("test", axis=1)
    y = df["test"].apply(lambda x: 1 if x == "positive" else 0)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    # Create the RFE with a LogisticRegression estimator and 3 features to select
    rfe = RFE(estimator=LogisticRegression(),
              n_features_to_select=3, verbose=1)

    # Fits the eliminator to the data
    rfe.fit(X_train, y_train)

    # Print the features and their ranking (high = dropped early on)
    print(dict(zip(X.columns, rfe.ranking_)))

    # Print the features that are not eliminated
    print(X.columns[rfe.support_])

    # Calculates the test set accuracy
    acc = accuracy_score(y_test, rfe.predict(X_test))
    print("{0:.1%} accuracy on test set.".format(acc))


df = load_diabetes_data()
predict_with_logistic_regression(df)
manual_recursive_feature_elimination(df)
automatic_recursive_feature_elimination(df)
