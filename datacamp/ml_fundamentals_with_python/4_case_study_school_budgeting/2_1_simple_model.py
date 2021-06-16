import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import seaborn as sns
from util import compute_log_loss, score_submission
from multilabel import multilabel_train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier


def loading_budget_data():
    # https://github.com/datacamp/course-resources-ml-with-experts-budgets
    # https://github.com/drivendata/boxplots-for-education-1st-place
    df_all = pd.read_csv('data/TrainingData.csv', index_col=0)
    # df = df_all.sample(1560 * 20)
    df = df_all
    # print(df.info())
    print(df.describe())

    NUMERIC_COLUMNS = ['FTE', 'Total']
    LABELS = ['Function', 'Use', 'Sharing', 'Reporting', 'Student_Type',
              'Position_Type', 'Object_Type', 'Pre_K', 'Operating_Status']
    return df, NUMERIC_COLUMNS, LABELS


def train_test_split_fit_score(df, NUMERIC_COLUMNS, LABELS):
    # Create the new DataFrame: numeric_data_only
    numeric_data_only = df[NUMERIC_COLUMNS].fillna(-1000)

    # Get labels and convert to dummy variables: label_dummies
    label_dummies = pd.get_dummies(df[LABELS])

    # Create training and test sets
    X_train, X_test, y_train, y_test = multilabel_train_test_split(numeric_data_only,
                                                                   label_dummies,
                                                                   size=0.2,
                                                                   seed=123)

    # Important: If I don't take sample, the classification will take too much time to run.
    # By taking samples on the training and holdout dataset, the score_submission and _multi_multi_log_loss function
    # will fail the assertion as it compares the indices from the files in Amazon S3

    X_train = X_train.sample(1040)
    X_test = X_test.sample(520)
    y_train = y_train.sample(1040)
    y_test = y_test.sample(520)

    # Print the info
    print("X_train info:")
    print(X_train.info())
    print("\nX_test info:")
    print(X_test.info())
    print("\ny_train info:")
    print(y_train.info())
    print("\ny_test info:")
    print(y_test.info())

    # Instantiate the classifier: clf
    clf = OneVsRestClassifier(LogisticRegression())

    # Fit the classifier to the training data
    clf.fit(X_train, y_train)

    # Print the accuracy
    print("Accuracy: {}".format(clf.score(X_test, y_test)))
    return X_train, X_test, y_train, y_test


def predict_holdout_data(NUMERIC_COLUMNS, LABELS, X_train, y_train):
    # Instantiate the classifier: clf
    clf = OneVsRestClassifier(LogisticRegression())

    # Fit it to the training data
    clf.fit(X_train, y_train)

    # Load the holdout data: holdout
    holdout_all = pd.read_csv('data/TestData.csv', index_col=0)
    holdout = holdout_all.sample(2000)
    # Generate predictions: predictions
    predictions = clf.predict_proba(holdout[NUMERIC_COLUMNS].fillna(-1000))
    return holdout, predictions


def submit_result(df, LABELS, holdout, predictions):
    # Format predictions in DataFrame: prediction_df
    prediction_df = pd.DataFrame(columns=pd.get_dummies(df[LABELS]).columns,
                                 index=holdout.index,
                                 data=predictions)

    # Save prediction_df to csv
    prediction_df.to_csv('data/predictions.csv')

    # Submit the predictions for scoring: score
    score = score_submission(pred_path='data/predictions.csv')

    # Print score
    print('Your model, trained with numeric data only, yields logloss score: {}'.format(score))





budget_data, NUMERIC_COLUMNS, LABELS = loading_budget_data()
X_train, X_test, y_train, y_test = train_test_split_fit_score(
    budget_data, NUMERIC_COLUMNS, LABELS)
holdout, predictions = predict_holdout_data(
    NUMERIC_COLUMNS, LABELS, X_train, y_train)
submit_result(budget_data, LABELS, holdout, predictions)
