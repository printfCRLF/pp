import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import VarianceThreshold, RFE
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from data import load_diabetes_data


def build_a_random_forest_model(X, y):
    # Perform a 75% training and 25% test data split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=0)

    # Fit the random forest model to the training data
    rf = RandomForestClassifier(random_state=0)
    rf.fit(X_train, y_train)

    # Calculate the accuracy
    acc = accuracy_score(rf.predict(X_test), y_test)
    # Print the importances per feature
    print(dict(zip(X.columns, rf.feature_importances_.round(2))))
    # Print accuracy
    print("{0:.1%} accuracy on test set.".format(acc))

    return rf


def random_forest_for_feature_selection(X, y, rf):
    # Create a mask for features importances above the threshold
    mask = rf.feature_importances_ > 0.15
    # Apply the mask to the feature dataset X
    reduced_X = X.loc[:, mask]
    # prints out the selected column names
    print(reduced_X.columns)


def recursive_feature_elimination_with_random_forest(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=0)

    # Set the feature eliminator to remove 2 features on each step
    rfe = RFE(estimator=RandomForestClassifier(),
              n_features_to_select=2, step=2, verbose=1)

    # Fit the model to the training data
    rfe.fit(X_train, y_train)

    # Create a mask
    mask = rfe.support_

    # Apply the mask to the feature dataset X and print the result
    reduced_X = X.loc[:, mask]
    print(reduced_X.columns)


df = load_diabetes_data()
X = df.drop("test", axis=1)
y = df["test"].apply(lambda x: 1 if x == "positive" else 0)
rf = build_a_random_forest_model(X, y)
random_forest_for_feature_selection(X, y, rf)
recursive_feature_elimination_with_random_forest(X, y)
