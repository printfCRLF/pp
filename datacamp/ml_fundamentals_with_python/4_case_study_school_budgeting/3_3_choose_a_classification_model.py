import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.impute import SimpleImputer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import FeatureUnion
from multilabel import multilabel_train_test_split
from util import combine_text_columns
from sklearn.ensemble import RandomForestClassifier


def loading_budget_data():
    # https://github.com/datacamp/course-resources-ml-with-experts-budgets
    # https://github.com/drivendata/boxplots-for-education-1st-place
    df_all = pd.read_csv('data/TrainingData.csv', index_col=0)
    df = df_all.sample(1560 * 20)
    #df = df_all
    # print(df.info())
    print(df.describe())

    LABELS = ['Function', 'Use', 'Sharing', 'Reporting', 'Student_Type',
              'Position_Type', 'Object_Type', 'Pre_K', 'Operating_Status']
    NON_LABELS = ['Object_Description', 'Text_2', 'SubFund_Description',
                  'Job_Title_Description', 'Text_3', 'Text_4',
                  'Sub_Object_Description', 'Location_Description', 'FTE',
                  'Function_Description', 'Facility_or_Department', 'Position_Extra',
                  'Total', 'Program_Description', 'Fund_Description', 'Text_1']
    NUMERIC_COLUMNS = ['FTE', 'Total']

    return df, LABELS, NON_LABELS, NUMERIC_COLUMNS


def use_function_transformer_on_dataset(df, LABELS, NON_LABELS, NUMERIC_COLUMNS):
    # Get the dummy encoding of the labels
    dummy_labels = pd.get_dummies(df[LABELS])

    # Get the columns that are features in the original df
    NON_LABELS = [c for c in df.columns if c not in LABELS]

    # Split into training and test sets
    X_train, X_test, y_train, y_test = multilabel_train_test_split(df[NON_LABELS],
                                                                   dummy_labels,
                                                                   0.2,
                                                                   min_count=0,
                                                                   seed=123)

    # Preprocess the text data: get_text_data
    get_text_data = FunctionTransformer(combine_text_columns, validate=False)

    # Preprocess the numeric data: get_numeric_data
    get_numeric_data = FunctionTransformer(
        lambda x: x[NUMERIC_COLUMNS], validate=False)

    return X_train, X_test, y_train, y_test, get_text_data, get_numeric_data


def create_a_pipeline(X_train, X_test, y_train, y_test, get_text_data, get_numeric_data):
    # Complete the pipeline: pl
    pl = Pipeline([
        ('union', FeatureUnion(
            transformer_list=[
                ('numeric_features', Pipeline([
                    ('selector', get_numeric_data),
                    ('imputer', SimpleImputer())
                ])),
                ('text_features', Pipeline([
                    ('selector', get_text_data),
                    ('vectorizer', CountVectorizer())
                ]))
            ]
        )),
        ('clf', OneVsRestClassifier(LogisticRegression()))
    ])

    # Fit to the training data
    pl.fit(X_train, y_train)

    # Compute and print accuracy
    accuracy = pl.score(X_test, y_test)
    print("\nAccuracy on budget dataset: ", accuracy)


def try_random_forest(X_train, X_test, y_train, y_test,
                      get_text_data, get_numeric_data):
    # Edit model step in pipeline
    pl = Pipeline([
        ('union', FeatureUnion(
            transformer_list=[
                ('numeric_features', Pipeline([
                    ('selector', get_numeric_data),
                    ('imputer', SimpleImputer())
                ])),
                ('text_features', Pipeline([
                    ('selector', get_text_data),
                    ('vectorizer', CountVectorizer())
                ]))
            ]
        )),
        ('clf', RandomForestClassifier())
    ])

    # Fit to the training data
    pl.fit(X_train, y_train)

    # Compute and print accuracy
    accuracy = pl.score(X_test, y_test)
    print("\nAccuracy on budget dataset: ", accuracy)


def try_random_forest_with_tunned_parameters(X_train, X_test, y_train, y_test,
                                             get_text_data, get_numeric_data):
    # Edit model step in pipeline
    pl = Pipeline([
        ('union', FeatureUnion(
            transformer_list=[
                ('numeric_features', Pipeline([
                    ('selector', get_numeric_data),
                    ('imputer', SimpleImputer())
                ])),
                ('text_features', Pipeline([
                    ('selector', get_text_data),
                    ('vectorizer', CountVectorizer())
                ]))
            ]
        )),
        ('clf', RandomForestClassifier(n_estimators=15))
    ])

    # Fit to the training data
    pl.fit(X_train, y_train)

    # Compute and print accuracy
    accuracy = pl.score(X_test, y_test)
    print("\nAccuracy on budget dataset: ", accuracy)


df, LABELS, NON_LABELS, NUMERIC_COLUMNS = loading_budget_data()
X_train, X_test, y_train, y_test, get_text_data, get_numeric_data = use_function_transformer_on_dataset(
    df, LABELS, NON_LABELS, NUMERIC_COLUMNS)
#create_a_pipeline(X_train, X_test, y_train, y_test,get_text_data, get_numeric_data)
# try_random_forest(X_train, X_test, y_train, y_test,
#                   get_text_data, get_numeric_data)
try_random_forest_with_tunned_parameters(X_train, X_test, y_train, y_test,
                                         get_text_data, get_numeric_data)
