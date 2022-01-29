import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from data import load_telco_data
from c12_preparation_for_modeling import seperate_numerical_and_categorical_columns, encoding_categorical_and_scale_numerical_variables


def split_data_into_training_and_testing(df):
    X = df.drop(axis="columns", columns=["customerID", "Churn"])
    Y = df["Churn"]

    # Split X and Y into training and testing datasets
    train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=0.25)

    # Ensure training dataset has only 75% of original X data
    print(train_X.shape[0] / X.shape[0])

    # Ensure testing dataset has only 25% of original X data
    print(test_X.shape[0] / X.shape[0])

    return train_X, test_X, train_Y, test_Y


def fit_a_tree(train_X, test_X, train_Y, test_Y):
    # Initialize the model with max_depth set at 5
    mytree = DecisionTreeClassifier(max_depth=5)

    # Fit the model on the training data
    treemodel = mytree.fit(train_X, train_Y)

    # Predict values on the testing data
    pred_Y = treemodel.predict(test_X)

    # Measure model performance on testing data
    print(accuracy_score(test_Y, pred_Y))


def predict_churn_with_decision_tree(train_X, test_X, train_Y, test_Y):
    # Initialize the Decision Tree
    clf = DecisionTreeClassifier(max_depth=7,
                                 criterion='gini',
                                 splitter='best')

    # Fit the model to the training data
    clf = clf.fit(train_X, train_Y)

    # Predict the values on test dataset
    pred_Y = clf.predict(test_X)

    # Print accuracy values
    print("Training accuracy: ", np.round(clf.score(train_X, train_Y), 3))
    print("Test accuracy: ", np.round(accuracy_score(test_Y, pred_Y), 3))


if __name__ == "__main__":
    telco_raw = load_telco_data()
    categorical, numerical = seperate_numerical_and_categorical_columns(
        telco_raw)
    df = encoding_categorical_and_scale_numerical_variables(
        telco_raw, categorical, numerical)
    train_X, test_X, train_Y, test_Y = split_data_into_training_and_testing(df)
    #fit_a_tree(train_X, test_X, train_Y, test_Y)
    predict_churn_with_decision_tree(train_X, test_X, train_Y, test_Y)
