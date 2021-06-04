import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC


def load_voting_data():
    columns = ['party', 'infants', 'water', 'budget', 'physician', 'salvador', 'religious', 'satellite', 'aid', 'missile',
               'immigration', 'synfuels', 'education', 'superfund', 'crime', 'duty_free_exports', 'eaa_rsa']
    df = pd.read_csv('data/house-votes-84.csv')
    df.columns = columns
    return df


def dropping_missing_data(df):
    # Convert '?' to NaN
    df[df == '?'] = np.nan

    # Print the number of NaNs
    print(df.isnull().sum())

    # Print shape of original DataFrame
    print("Shape of Original DataFrame: {}".format(df.shape))

    # Drop missing values and print shape of new DataFrame
    df = df.dropna()

    # Print shape of new DataFrame
    print("Shape of DataFrame After Dropping All Rows with Missing Values: {}".format(df.shape))


def imputing_missing_data_in_a_ml_pipeline(df):
    X = df.drop(columns=['party'])
    X[X == '?'] = np.nan
    X[X == 'y'] = 1
    X[X == 'n'] = 0
    y = df['party']
    # print(X.head())
    # print(y.head())

    # Setup the pipeline steps: steps
    steps = [('imputation', SimpleImputer(missing_values=np.nan, strategy='most_frequent')),
             ('SVM', SVC())]

    # Create the pipeline: pipeline
    pipeline = Pipeline(steps)

    # Create training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42)

    # Fit the pipeline to the train set
    pipeline.fit(X_train, y_train)

    # Predict the labels of the test set
    y_pred = pipeline.predict(X_test)

    # Compute metrics
    print(classification_report(y_test, y_pred))


df = load_voting_data()
# dropping_missing_data(df)
imputing_missing_data_in_a_ml_pipeline(df)
