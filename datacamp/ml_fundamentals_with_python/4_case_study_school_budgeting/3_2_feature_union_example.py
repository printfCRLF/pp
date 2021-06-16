import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import Imputer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import FeatureUnion


def preprocessing_text_features(sample_df):
    # Split out only the text data
    X_train, X_test, y_train, y_test = train_test_split(sample_df['text'],
                                                        pd.get_dummies(sample_df['label']), random_state=456)

    # Instantiate Pipeline object: pl
    pl = Pipeline([
        ('vec', CountVectorizer()),
        ('clf', OneVsRestClassifier(LogisticRegression()))
    ])

    # Fit to the training data
    pl.fit(X_train, y_train)

    # Compute and print accuracy
    accuracy = pl.score(X_test, y_test)
    print("\nAccuracy on sample data - just text data: ", accuracy)


def function_transformer_example(sample_df):
    # Obtain the text data: get_text_data
    get_text_data = FunctionTransformer(lambda x: x['text'], validate=False)

    # Obtain the numeric data: get_numeric_data
    get_numeric_data = FunctionTransformer(
        lambda x: x[['numeric', 'with_missing']], validate=False)

    # Fit and transform the text data: just_text_data
    just_text_data = get_text_data.fit_transform(sample_df)

    # Fit and transform the numeric data: just_numeric_data
    just_numeric_data = get_numeric_data.fit_transform(sample_df)

    # Print head to check results
    print('Text Data')
    print(just_text_data.head())
    print('\nNumeric Data')
    print(just_numeric_data.head())

    X_train, X_test, y_train, y_test = train_test_split(sample_df[['numeric', 'with_missing', 'text']],
                                                        pd.get_dummies(
                                                            sample_df['label']),
                                                        random_state=22)

    # Create a FeatureUnion with nested pipeline: process_and_join_features
    process_and_join_features = FeatureUnion(
        transformer_list=[
            ('numeric_features', Pipeline([
                ('selector', get_numeric_data),
                ('imputer', Imputer())
            ])),
            ('text_features', Pipeline([
                ('selector', get_text_data),
                ('vectorizer', CountVectorizer())
            ]))
        ]
    )

    # Instantiate nested pipeline: pl
    pl = Pipeline([
        ('union', process_and_join_features),
        ('clf', OneVsRestClassifier(LogisticRegression()))
    ])
