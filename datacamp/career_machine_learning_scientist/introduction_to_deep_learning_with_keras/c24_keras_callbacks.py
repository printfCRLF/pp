import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping, ModelCheckpoint
from sklearn.model_selection import train_test_split
from data import load_irrigation_machine_data
from c23_multi_label_classification import an_irrigation_machine


def plot_loss(loss, val_loss):
    plt.figure()
    plt.plot(loss)
    plt.plot(val_loss)
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper right')
    plt.show()


def plot_accuracy(acc, val_acc):
    # Plot training & validation accuracy values
    plt.figure()
    plt.plot(acc)
    plt.plot(val_acc)
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper left')
    plt.show()


def the_history_callback(model, X_train, X_test, y_train, y_test):
    h_callback = model.fit(X_train, y_train, epochs=50, validation_data=(X_test, y_test))

    plot_loss(h_callback.history["loss"], h_callback.history["val_loss"])
    plot_accuracy(h_callback.history["acc"], h_callback.history["val_acc"])


def early_stopping_your_model(model, X_train, X_test, y_train, y_test):
    monitor_val_acc = EarlyStopping(monitor="val_accuracy", patience=5)
    model.fit(X_train, y_train,
              epochs=1000, validation_data=(X_test, y_test),
              callbacks=[monitor_val_acc])


def a_combination_of_callbacks(model, X_train, X_test, y_train, y_test):
    monitor_val_acc = EarlyStopping(monitor="val_accuracy", patience=3)
    modelCheckpoint = ModelCheckpoint("best_banknote_model.hdf5", save_best_only=True)

    h_callback = model.fit(X_train, y_train,
                           epochs=1000000000000,
                           callbacks=[monitor_val_acc, modelCheckpoint],
                           validation_data=(X_test, y_test))


if __name__ == "__main__":
    sns.set()
    df = load_irrigation_machine_data()
    label_columns = ["parcel_0", "parcel_1", "parcel_2"]
    features = df.drop(columns=label_columns)
    labels = df[label_columns]
    X_train, X_test, y_train, y_test = train_test_split(features, labels, stratify=labels, test_size=0.25)

    model = an_irrigation_machine()
    # the_history_callback(model, X_train, X_test, y_train, y_test)

    # early_stopping_your_model(model, X_train, X_test, y_train, y_test)

    a_combination_of_callbacks(model, X_train, X_test, y_train, y_test)