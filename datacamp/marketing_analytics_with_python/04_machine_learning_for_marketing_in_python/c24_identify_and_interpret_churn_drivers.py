import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score
from data import load_telco_data
from c12_preparation_for_modeling import seperate_numerical_and_categorical_columns, encoding_categorical_and_scale_numerical_variables
from c21_churn_prediction_fundamentals import explore_churn_and_split_data, seperate_features_and_target_variable


def explore_logistic_regression_coefficients(train_X, train_Y, test_X, test_Y):
    logreg = LogisticRegression(penalty='l1', C=0.025, solver='liblinear')
    logreg.fit(train_X, train_Y)

    # Combine feature names and coefficients into pandas DataFrame
    feature_names = pd.DataFrame(train_X.columns, columns=['Feature'])
    log_coef = pd.DataFrame(np.transpose(logreg.coef_),
                            columns=['Coefficient'])
    coefficients = pd.concat([feature_names, log_coef], axis=1)

    # Calculate exponent of the logistic regression coefficients
    coefficients['Exp_Coefficient'] = np.exp(coefficients['Coefficient'])

    # Remove coefficients that are equal to zero
    coefficients = coefficients[coefficients['Coefficient'] != 0]

    # Print the values sorted by the exponent coefficient
    print(coefficients.sort_values(by=['Exp_Coefficient']))


if __name__ == "__main__":
    telco_raw = load_telco_data()
    categorical, numerical = seperate_numerical_and_categorical_columns(
        telco_raw)
    telcom = encoding_categorical_and_scale_numerical_variables(
        telco_raw, categorical, numerical)
    train, test = explore_churn_and_split_data(telcom)
    train_X, train_Y, test_X, test_Y = seperate_features_and_target_variable(
        telcom, train, test)
    explore_logistic_regression_coefficients(train_X, train_Y, test_X, test_Y)
