import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from keras.models import Sequential
from keras.layers import Dense, LeakyReLU
from sklearn.model_selection import train_test_split
from data import load_irrigation_machine_data


def get_model(act_function):
    if act_function not in ['relu', 'leaky_relu', 'sigmoid', 'tanh']:
        raise ValueError('Make sure your activation functions are named correctly!')
    print("Finishing with", act_function, "...")
    return create_model(act_function)
    # return ModelWrapper(act_function)


def create_model(act_function):
    model = Sequential()
    if act_function == "leaky_relu":
        model.add(Dense(64, input_shape=(20,)))
        model.add(LeakyReLU())
    else:
        model.add(Dense(64, input_shape=(20,), activation=act_function))
    model.add(Dense(3, activation="sigmoid"))
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

    return model


def comparing_activation_functions(X_train, X_test, y_train, y_test):
    activations = ["relu", "leaky_relu", "sigmoid", "tanh"]
    activation_results = {}
    val_loss_per_function, val_acc_per_function = {}, {}

    for act in activations:
        model = get_model(act)
        h_callback = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=20, verbose=0)
        activation_results[act] = h_callback
        val_loss = h_callback.history["val_loss"]
        val_acc = h_callback.history["val_accuracy"]
        val_loss_per_function[act] = val_loss
        val_acc_per_function[act] = val_acc

    return val_loss_per_function, val_acc_per_function


def comparing_activation_functions2(val_loss_per_function, val_acc_per_function):
    val_loss = pd.DataFrame(val_loss_per_function)
    val_loss.plot()
    plt.show()

    val_acc = pd.DataFrame(val_acc_per_function)
    val_acc.plot()
    plt.show()


if __name__ == "__main__":
    sns.set()

    df = load_irrigation_machine_data()
    label_columns = ["parcel_0", "parcel_1", "parcel_2"]
    features = df.drop(columns=label_columns)
    labels = df[label_columns]
    X_train, X_test, y_train, y_test = train_test_split(features, labels, stratify=labels, test_size=0.25)
    val_loss_per_function, val_acc_per_function = comparing_activation_functions(X_train, X_test, y_train, y_test)
    comparing_activation_functions2(val_loss_per_function, val_acc_per_function)
