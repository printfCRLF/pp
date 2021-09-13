import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from keras.engine.training import Model
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input
from sklearn.datasets import load_digits


def building_a_cnn_model():
    model = Sequential()
    model.add(Conv2D(32, kernel_size=3, input_shape=(28, 28, 1), activation='relu'))
    model.add(Conv2D(16, kernel_size=3, activation="relu"))
    model.add(Flatten())
    model.add(Dense(10, activation='softmax'))

    return model


def looking_at_covoluations(model, X_test):
    first_layer_output = model.layers[0].output
    first_layer_model = Model(inputs=model.layers[0].input, outputs=first_layer_output)
    activations = first_layer_model.predict(X_test)

    fig, axs = plt.subplots(2, 1)
    axs[0].matshow(activations[0, :, :, 14], cmap='viridis')
    axs[1].matshow(activations[0, :, :, 17], cmap='viridis')
    plt.show()


def something_else():
    img = image.load_img("data/dog.png", target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_expanded = np.expand_dims(img_array, axis=0)
    img_ready = preprocess_input(img_expanded)
    return img_ready


if __name__ == "__main__":
    X_test = np.load("data/Digits/digits_pixels.npy")
    print(X_test.shape)
