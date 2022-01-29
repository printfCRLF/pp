import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score
from data import load_telco_data
from c12_preparation_for_modeling import seperate_numerical_and_categorical_columns, encoding_categorical_and_scale_numerical_variables
from c21_churn_prediction_fundamentals import explore_churn_and_split_data, seperate_features_and_target_variable


def fit_logistic_regression_model(train_X, train_Y, test_X, test_Y):
    logreg = LogisticRegression()

    # Fit logistic regression on training data
    logreg.fit(train_X, train_Y)

    # Predict churn labels on testing data
    pred_test_Y = logreg.predict(test_X)

    # Calculate accuracy score on testing data
    test_accuracy = accuracy_score(test_Y, pred_test_Y)

    # Print test accuracy score rounded to 4 decimals
    print('Test accuracy:', round(test_accuracy, 4))


def l1_regularization(train_X, train_Y, test_X, test_Y):
    # Initialize logistic regression instance
    logreg = LogisticRegression(penalty='l1', C=0.025, solver='liblinear')

    # Fit the model on training data
    logreg.fit(train_X, train_Y)

    # Predict churn values on test data
    pred_test_Y = logreg.predict(test_X)

    # Print the accuracy score on test data
    print('Test accuracy:', round(accuracy_score(test_Y, pred_test_Y), 4))


def identify_optimal_l1_penalty_coefficient(train_X, train_Y, test_X, test_Y):
    C = [1, 0.5, 0.25, 0.1, 0.05, 0.025, 0.01, 0.005, 0.0025]
    l1_metrics = np.array([
        [1., 0., 0.],
        [0.5, 0., 0.],
        [0.25, 0., 0.],
        [0.1, 0., 0.],
        [0.05, 0., 0.],
        [0.025, 0., 0.],
        [0.01, 0., 0.],
        [0.005, 0., 0.],
        [0.0025, 0., 0.]])

    # Run a for loop over the range of C list length
    for index in range(0, len(C)):
        # Initialize and fit Logistic Regression with the C candidate
        logreg = LogisticRegression(
            penalty='l1', C=C[index], solver='liblinear')
        logreg.fit(train_X, train_Y)
        # Predict churn on the testing data
        pred_test_Y = logreg.predict(test_X)
        # Create non-zero count and recall score columns
        l1_metrics[index, 1] = np.count_nonzero(logreg.coef_)
        l1_metrics[index, 2] = recall_score(test_Y, pred_test_Y, pos_label="Yes")

    # Name the columns and print the array as pandas DataFrame
    col_names = ['C', 'Non-Zero Coeffs', 'Recall']
    print(pd.DataFrame(l1_metrics, columns=col_names))


if __name__ == "__main__":
    telco_raw = load_telco_data()
    categorical, numerical = seperate_numerical_and_categorical_columns(
        telco_raw)
    telcom = encoding_categorical_and_scale_numerical_variables(
        telco_raw, categorical, numerical)
    train, test = explore_churn_and_split_data(telcom)
    train_X, train_Y, test_X, test_Y = seperate_features_and_target_variable(
        telcom, train, test)
    # fit_logistic_regression_model(train_X, train_Y, test_X, test_Y)
    l1_regularization(train_X, train_Y, test_X, test_Y)
    identify_optimal_l1_penalty_coefficient(train_X, train_Y, test_X, test_Y)
