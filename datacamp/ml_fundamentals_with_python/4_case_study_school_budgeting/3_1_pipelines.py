import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import Imputer


def simple_pipeline(sample_df):
    # Split and select numeric data only, no nans
    X_train, X_test, y_train, y_test = train_test_split(sample_df[['numeric']],
                                                        pd.get_dummies(
                                                            sample_df['label']),
                                                        random_state=22)

    # Instantiate Pipeline object: pl
    pl = Pipeline([
        ('clf', OneVsRestClassifier(LogisticRegression()))
    ])

    # Fit the pipeline to the training data
    pl.fit(X_train, y_train)

    # Compute and print accuracy
    accuracy = pl.score(X_test, y_test)
    print("\nAccuracy on sample data - numeric, no nans: ", accuracy)


def pipeline_with_imputer(sample_df):
    # Create training and test sets using only numeric data
    X_train, X_test, y_train, y_test = train_test_split(sample_df[['numeric', 'with_missing']],
                                                        pd.get_dummies(
                                                            sample_df['label']),
                                                        random_state=456)

    # Insantiate Pipeline object: pl
    pl = Pipeline([
        ('imp', Imputer()),
        ('clf', OneVsRestClassifier(LogisticRegression()))
    ])

    # Fit the pipeline to the training data
    pl.fit(X_train, y_train)

    # Compute and print accuracy
    accuracy = pl.score(X_test, y_test)
    print("\nAccuracy on sample data - all numeric, incl nans: ", accuracy)
