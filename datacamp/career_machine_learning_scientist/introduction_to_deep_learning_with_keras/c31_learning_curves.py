import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from data import load_irrigation_machine_data
from sklearn.datasets import load_digits


def learning_the_digits(X_train):
    model = Sequential()
    model.add(Dense(16, input_shape=(64,), activation="relu"))
    model.add(Dense(10, activation="softmax"))
    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
    print(model.predict(X_train))

    return model


def is_the_model_overfitting(model, X_train, X_test, y_train, y_test):
    h_callback = model.fit(X_train, y_train, epochs=60, validation_data=(X_test, y_test), verbose=0)
    plot_loss(h_callback.history['loss'], h_callback.history['val_loss'])


def plot_loss(loss, val_loss):
    plt.figure()
    plt.plot(loss)
    plt.plot(val_loss)
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper right')
    plt.show()


def do_we_need_more_data(model, X_train, X_test, y_train, y_test):
    training_sizes = np.array([125, 502, 879, 1255])
    initial_weights = model.get_weights()
    train_accs, test_accs = [], []

    for size in training_sizes:
        # Get a fraction of training data (we only care about the training data)
        X_train_frac, y_train_frac = X_train[:size], y_train[:size]

        # Reset the model to the initial weights and train it on the new training data fraction
        early_stop = EarlyStopping(monitor="loss", patience=1)
        model.set_weights(initial_weights)
        model.fit(X_train_frac, y_train_frac, epochs=50, callbacks=[early_stop])

        # Evaluate and store both: the training data fraction and the complete test set results
        train_accs.append(model.evaluate(X_train_frac, y_train_frac)[1])
        test_accs.append(model.evaluate(X_test, y_test)[1])

    # Plot train vs test accuracies
    plot_results(train_accs, test_accs, training_sizes)


def plot_results(train_accs, test_accs, training_sizes):
    plt.plot(training_sizes, train_accs, 'o-', label="Training Accuracy")
    plt.plot(training_sizes, test_accs, 'o-', label="Test Accuracy")
    plt.title('Accuracy vs Number of training samples')
    plt.xlabel('# of training samples')
    plt.ylabel('Accuracy')
    plt.legend(loc="best")
    plt.show()


if __name__ == "__main__":
    sns.set()

    # todo convert y using one_hot_encoder
    X, y = load_digits(return_X_y=True)
    y_cat = pd.Categorical(y)
    y_cats = to_categorical(y_cat.codes)

    X_train, X_test, y_train, y_test = train_test_split(X, y_cats, stratify=y_cats, test_size=0.3)
    model = learning_the_digits(X_train)
    is_the_model_overfitting(model, X_train, X_test, y_train, y_test)
    do_we_need_more_data(model, X_train, X_test, y_train, y_test)
