import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from data import load_darts_data


def a_multi_class_model():
    # Instantiate a sequential model
    model = Sequential()

    # Add 3 dense layers of 128, 64 and 32 neurons each
    model.add(Dense(128, input_shape=(2,), activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(32, activation='relu'))
    # Add a dense layer with as many neurons as competitors
    model.add(Dense(4, activation="softmax"))

    # Compile your model using categorical_crossentropy loss
    model.compile(loss="categorical_crossentropy", optimizer='adam', metrics=['accuracy'])

    return model


def prepare_your_dataset(darts):
    darts.competitor = pd.Categorical(darts.competitor)
    darts.competitor = darts.competitor.cat.codes
    print('Label encoded competitors: \n', darts.competitor.head())

    coordinates = darts.drop(['competitor'], axis=1)
    competitors = to_categorical(darts.competitor)
    print('One-hot encoded competitors: \n', competitors)

    return coordinates, competitors


def training_on_darts_throwers(model, coord_train, coord_test, competitors_train, competitors_test):
    model.fit(coord_train, competitors_train, epochs=200)
    accuracy = model.evaluate(coord_test, competitors_test)[1]
    print('Accuracy:', accuracy)

    return model


def soft_max_predictions(model):
    coords_small_test = pd.DataFrame({
        "xCoord": [0.2090482, 0.08210314, 0.19816544, -0.34865965, 0.21472635],
        "yCoord": [-0.07739811, -0.72140734, -0.67464642, 0.03508617, 0.18389446]
    })
    competitors_small_test = np.array([[0., 0., 1., 0.],
                                       [0., 0., 0., 1.],
                                       [0., 0., 0., 1.],
                                       [1., 0., 0., 0.],
                                       [0., 0., 1., 0.]])
    preds = model.predict(coords_small_test)

    print("{:45} | {}".format('Raw Model Predictions', 'True labels'))
    for i, pred in enumerate(preds):
        print("{} | {}".format(pred, competitors_small_test[i]))

    preds_chosen = [np.argmax(pred) for pred in preds]

    print("{:10} | {}".format('Rounded Model Predictions', 'True labels'))
    for i, pred in enumerate(preds_chosen):
        print("{:25} | {}".format(pred, competitors_small_test[i]))


if __name__ == "__main__":
    sns.set()
    darts = load_darts_data()
    model = a_multi_class_model()
    coordinates, competitors = prepare_your_dataset(darts)
    X_train, X_test, y_train, y_test = train_test_split(coordinates, competitors, stratify=competitors, test_size=0.25)

    model = training_on_darts_throwers(model, X_train, X_test, y_train, y_test)
    soft_max_predictions(model)
