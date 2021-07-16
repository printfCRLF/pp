import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import VarianceThreshold
from data import load_ansur_ii_male_data, load_ansur_ii_female_data


def prepare_data():
    ansur_ii_male = load_ansur_ii_male_data().sample(500)
    ansur_ii_female = load_ansur_ii_female_data().sample(500)
    df = pd.concat([ansur_ii_male, ansur_ii_female])
    non_numeric = ['Branch', 'Gender', 'Component', "weight_kg",
                   "stature_m", "BMI_class", "Height_class"]
    ansur_df = df.drop(non_numeric, axis=1)
    return ansur_df


def lasso_regressor(ansur_df):
    X = ansur_df.drop("BMI", axis=1)
    y = ansur_df["BMI"]
    # Set the test size to 30% to get a 70-30% train test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=0)

    scaler = StandardScaler()
    # Fit the scaler on the training features and transform these in one go
    X_train_std = scaler.fit_transform(X_train)

    # Create the Lasso model
    la = Lasso()

    # Fit it to the standardized training data
    la.fit(X_train_std, y_train)

    # Transform the test set with the pre-fitted scaler
    X_test_std = scaler.transform(X_test)

    # Calculate the coefficient of determination (R squared) on X_test_std
    r_squared = la.score(X_test_std, y_test)
    print("The model can predict {0:.1%} of the variance in the test set.".format(
        r_squared))

    # Create a list that has True values when coefficients equal 0
    zero_coef = la.coef_ == 0

    # Calculate how many features have a zero coefficient
    n_ignored = sum(zero_coef)
    print("The model has ignored {} out of {} features.".format(
        n_ignored, len(la.coef_)))


def adjusting_regularization_strength(ansur_df):
    X = ansur_df.drop("BMI", axis=1)
    y = ansur_df["BMI"]
    # Set the test size to 30% to get a 70-30% train test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=0)

    # Transform the test set with the pre-fitted scaler
    scaler = StandardScaler()
    # Fit the scaler on the training features and transform these in one go
    X_train_std = scaler.fit_transform(X_train)

    # Find the highest alpha value with R-squared above 98%
    la = Lasso(0.1, random_state=0)

    # Fits the model and calculates performance stats
    la.fit(X_train_std, y_train)

    X_test_std = scaler.transform(X_test)
    r_squared = la.score(X_test_std, y_test)
    n_ignored_features = sum(la.coef_ == 0)

    # Print peformance stats
    print("The model can predict {0:.1%} of the variance in the test set.".format(
        r_squared))
    print("{} out of {} features were ignored.".format(
        n_ignored_features, len(la.coef_)))


ansur_df = prepare_data()
# lasso_regressor(ansur_df)
adjusting_regularization_strength(ansur_df)
