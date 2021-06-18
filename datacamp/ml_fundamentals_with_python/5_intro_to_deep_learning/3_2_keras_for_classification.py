import keras
import numpy as np
import pandas as pd
from keras.layers import Dense
from keras.models import Sequential
from keras.utils import to_categorical
from scipy import stats


def load_data():
    df = pd.read_csv('data/titanic_all_numeric.csv')
    df['age_was_missing'] = df['age_was_missing'].astype(int)
    target = to_categorical(df['survived'])
    predictors = df.drop(['survived'], axis=1).values
    # print(stats.describe(predictors))
    # print(stats.describe(target))
    return predictors, target


def build_compile_fit_predict(predictors, target):
    n_cols = predictors.shape[1]
    # Set up the model
    model = Sequential()
    # Add the first layer
    model.add(Dense(32, activation='relu', input_shape=(n_cols,)))
    # Add the output layer
    model.add(Dense(2, activation='softmax'))
    # Compile the model
    model.compile(optimizer='sgd', loss='categorical_crossentropy',
                  metrics=['accuracy'])
    # Fit the model
    model.fit(predictors, target)

    return model


def making_predictions(model):
    pred_data = np.array([
        [2, 34.0, 0, 0, 13.0, 1, False, 0, 0, 1],
        [2, 31.0, 1, 1, 26.25, 0, False, 0, 0, 1],
        [1, 11.0, 1, 2, 120.0, 1, False, 0, 0, 1],
        [3, 0.42, 0, 1, 8.5167, 1, False, 1, 0, 0],
        [3, 27.0, 0, 0, 6.975, 1, False, 0, 0, 1]
    ])

    # Calculate predictions: predictions
    predictions = model.predict(pred_data)

    # Calculate predicted probability of survival: predicted_prob_true
    predicted_prob_true = predictions[:, 1]

    # print predicted_prob_true
    print(predicted_prob_true)


predictors, target = load_data()
model = build_compile_fit_predict(predictors, target)
making_predictions(model)
