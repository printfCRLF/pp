import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from keras.models import Sequential
from keras.layers import Dense
from data import time_steps, y_positions


def specifying_a_model():
    model = Sequential()
    model.add(Dense(50, input_shape=(1,), activation='relu'))

    model.add(Dense(50, input_shape=(50,), activation="relu"))
    model.add(Dense(50, input_shape=(50,), activation="relu"))

    model.add(Dense(1))
    return model


def training(model, time_steps, y_positions):
    model.compile(optimizer="adam", loss="mse")
    print("Training started..., this can take a while:")
    model.fit(time_steps, y_positions, epochs=30)
    print("Final loss value:", model.evaluate(time_steps, y_positions))

    return model


def predict_the_orbit(model):
    twenty_min_orbit = model.predict(np.arange(-10, 11))
    plot_orbit(twenty_min_orbit)

    eighty_min_orbit = model.predict(np.arange(-40, 41))
    plot_orbit(eighty_min_orbit)


def plot_orbit(model_preds):
    axeslim = int(len(model_preds) / 2)
    plt.plot(np.arange(-axeslim, axeslim + 1), np.arange(-axeslim, axeslim + 1) ** 2, color="mediumslateblue")
    plt.plot(np.arange(-axeslim, axeslim + 1), model_preds, color="orange")
    plt.axis([-40, 41, -5, 550])
    plt.legend(["Scientist's Orbit", 'Your orbit'], loc="lower left")
    plt.title("Predicted orbit vs Scientist's Orbit")
    plt.show()


if __name__ == "__main__":
    sns.set()
    model = specifying_a_model()
    model = training(model, time_steps, y_positions)
    predict_the_orbit(model)
