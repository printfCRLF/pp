import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


def importing_data_for_supervised_learning():
    # Read the CSV file into a DataFrame: df
    df = pd.read_csv('data/gm_2008_region.csv')

    # Create arrays for features and target variable
    y = df['fertility']
    X = df['life']

    # Print the dimensions of y and X before reshaping
    print("Dimensions of y before reshaping: ", y.shape)
    print("Dimensions of X before reshaping: ", X.shape)

    # Reshape X and y
    y_reshaped = y.values.reshape(-1, 1)
    X_reshaped = X.values.reshape(-1, 1)

    # Print the dimensions of y_reshaped and X_reshaped
    print("Dimensions of y after reshaping: ", y_reshaped.shape)
    print("Dimensions of X after reshaping: ", X_reshaped.shape)
    return y_reshaped, X_reshaped


def fit_predict_between_fertility_life(X_fertility, y):
    _ = plt.plot(X_fertility, y, marker='.',
                 linestyle='none', markerfacecolor='blue')
    _ = plt.xlabel('fertility')
    _ = plt.ylabel('life expectancy')
    # Create the regressor: reg
    reg = LinearRegression()

    # Create the prediction space
    prediction_space = np.linspace(
        min(X_fertility), max(X_fertility)).reshape(-1, 1)

    # Fit the model to the data
    reg.fit(X_fertility, y)

    # Compute predictions over the prediction space: y_pred
    y_pred = reg.predict(prediction_space)

    # Print R^2
    print(reg.score(X_fertility, y))

    # Plot regression line
    plt.plot(prediction_space, y_pred, color='black', linewidth=3)
    plt.show()


def regression_for_all_features():
    df = pd.read_csv('data/gm_2008_region.csv')
    X = df.drop(columns=['life', 'Region']).values
    y = df['life'].values

    # Create training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42)

    # Create the regressor: reg_all
    reg_all = LinearRegression()

    # Fit the regressor to the training data
    reg_all.fit(X_train, y_train)

    # Predict on the test data: y_pred
    y_pred = reg_all.predict(X_test)

    # Compute and print R^2 and RMSE
    print("R^2: {}".format(reg_all.score(X_test, y_test)))
    rmse = np.sqrt(mean_squared_error(y_pred, y_test))
    print("Root Mean Squared Error: {}".format(rmse))


sns.set()
# X_fertility, y = importing_data_for_supervised_learning()
# fit_predict_between_fertility_life(X_fertility, y)
regression_for_all_features()
