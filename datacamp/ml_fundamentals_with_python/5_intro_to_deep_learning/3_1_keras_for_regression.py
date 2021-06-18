import numpy as np
import pandas as pd
import keras
from keras.layers import Dense
from keras.models import Sequential
from scipy import stats

def load_data():
    df = pd.read_csv('data/hourly_wages.csv')
    predictors = df.drop(['wage_per_hour'], axis=1).values
    target = df['wage_per_hour'].values
    print(stats.describe(predictors))
    print(stats.describe(target))
    return predictors, target


def build_compile_fit_predict(predictors, target):
    # Save the number of columns in predictors: n_cols
    n_cols = predictors.shape[1]
    # Set up the model: model
    model = Sequential()
    # Add the first layer
    model.add(Dense(50, activation='relu', input_shape=(n_cols,)))
    # Add the second layer
    model.add(Dense(32, activation='relu'))
    # Add the output layer
    model.add(Dense(1))

    # Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Fit the model
    model.fit(predictors, target)


predictors, target = load_data()
build_compile_fit_predict(predictors, target)
