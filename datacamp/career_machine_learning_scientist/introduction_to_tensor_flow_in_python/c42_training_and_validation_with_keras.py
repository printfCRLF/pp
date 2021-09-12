import numpy as np
import tensorflow as tf
from tensorflow import keras
from data import load_slmnist_data


def training_with_keras(sign_language_features, sign_language_labels):
    model = keras.Sequential()
    model.add(keras.layers.Dense(16, activation='relu', input_shape=(784,)))
    model.add(keras.layers.Dense(4, activation="softmax"))
    model.compile('SGD', loss='categorical_crossentropy')
    model.fit(sign_language_features, sign_language_labels, epochs=5)


def metrics_and_validation_with_keras(sign_language_features, sign_language_labels):
    model = keras.Sequential()
    model.add(keras.layers.Dense(32, activation="sigmoid", input_shape=(784,)))
    model.add(keras.layers.Dense(4, activation='softmax'))
    model.compile(optimizer='RMSprop', loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(sign_language_features, sign_language_labels, epochs=10, validation_split=0.1)


def overfitting_detection(sign_language_features, sign_language_labels):
    model = keras.Sequential()
    model.add(keras.layers.Dense(1024, activation="relu", input_shape=(784,)))
    model.add(keras.layers.Dense(4, activation='softmax'))
    model.compile(optimizer=keras.optimizers.Adam(lr=0.001),
                  loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(sign_language_features, sign_language_labels, epochs=50, validation_split=0.5)


def evaluating_models():
    small_train = small_model.evaluate(train_features, train_labels)
    small_test = small_model.evaluate(test_features, test_labels)
    large_train = large_model.evaluate(train_features, train_labels)
    large_test = large_model.evaluate(test_features, test_labels)

    # Print losses
    print('\n Small - Train: {}, Test: {}'.format(small_train, small_test))
    print('Large - Train: {}, Test: {}'.format(large_train, large_test))


if __name__ == "__main__":
    df = load_slmnist_data()
    sign_language_features = df.iloc[:, 1:].values.astype(np.float32)
    num_of_obs = sign_language_features.shape[0]
    sign_language_labels = np.zeros(shape=(num_of_obs, 4))
    for i, value in df.iloc[:, 0].items():
        sign_language_labels[i, value] = 1.0

    # metrics_and_validation_with_keras(sign_language_features, sign_language_labels)
    overfitting_detection(sign_language_features, sign_language_labels)
