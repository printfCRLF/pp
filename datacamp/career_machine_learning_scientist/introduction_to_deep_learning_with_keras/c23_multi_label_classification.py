import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from data import load_irrigation_machine_data


def an_irrigation_machine():
    model = Sequential()
    model.add(Dense(64, input_shape=(20,), activation="relu"))
    model.add(Dense(3, activation="sigmoid"))
    model.compile(optimizer='adam', loss="binary_crossentropy", metrics=['accuracy'])
    model.summary()

    return model


def train_with_multiple_labels(model, sensors_train, sensors_test, parcels_train, parcels_test):
    model.fit(sensors_train, parcels_train, epochs=100, validation_split=0.2)
    preds = model.predict(sensors_test)
    preds_rounded = np.round(preds)
    print('Rounded Predictions: \n', preds_rounded)
    accuracy = model.evaluate(sensors_test, parcels_test)[1]
    print('Accuracy:', accuracy)


if __name__ == "__main__":
    sns.set()
    df = load_irrigation_machine_data()
    label_columns = ["parcel_0", "parcel_1", "parcel_2"]
    features = df.drop(columns=label_columns)
    labels = df[label_columns]
    X_train, X_test, y_train, y_test = train_test_split(features, labels, stratify=labels, test_size=0.25)

    model = an_irrigation_machine()
    train_with_multiple_labels(model, X_train, X_test, y_train, y_test)
