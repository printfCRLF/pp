import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from keras.models import Sequential
from keras.layers import Dense


def building_an_autoencoder(X_test, y_test):
    autoencoder = Sequential()
    autoencoder.add(Dense(32, input_shape=(784,), activation="relu"))
    autoencoder.add(Dense(784, activation="sigmoid"))
    autoencoder.compile(optimizer="adadelta", loss="binary_crossentropy")
    autoencoder.summary()

    autoencoder.fit(X_test, y_test)

    return autoencoder


def denosing_like_an_auto_encoder(autoencoder, X_test_noise, y_test):
    encoder = Sequential()
    encoder.add(autoencoder.layers[0])

    # Encode the noisy images and show the encodings for your favorite number [0-9]
    encodings = encoder.predict(X_test_noise)
    show_encodings(X_test_noise, y_test, encodings, number=1)

    # Predict on the noisy images with your autoencoder
    decoded_imgs = autoencoder.predict(X_test_noise)

    # Plot noisy vs decoded images
    compare_plot(X_test_noise, decoded_imgs)


def show_encodings(X_test_noise, y_test, encoded_imgs, number=1):
    n = 5  # how many digits we will display
    original = X_test_noise
    original = original[np.where(y_test == number)]
    encoded_imgs = encoded_imgs[np.where(y_test == number)]
    plt.figure(figsize=(20, 4))
    # plt.title('Original '+str(number)+' vs Encoded representation')
    for i in range(min(n, len(original))):
        # display original imgs
        ax = plt.subplot(2, n, i + 1)
        plt.imshow(original[i].reshape(28, 28))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        # display encoded imgs
        ax = plt.subplot(2, n, i + 1 + n)
        plt.imshow(np.tile(encoded_imgs[i], (32, 1)))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
    plt.show()


def compare_plot(original, decoded_imgs):
    n = 4  # How many digits we will display
    plt.figure(figsize=(20, 4))
    for i in range(n):
        # Display original
        ax = plt.subplot(2, n, i + 1)
        plt.imshow(original[i].reshape(28, 28))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        # Display reconstruction
        ax = plt.subplot(2, n, i + 1 + n)
        plt.imshow(decoded_imgs[i].reshape(28, 28))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
    plt.title('Noisy vs Decoded images')
    plt.show()


if __name__ == "__main__":
    sns.set()

    X_test_noise = np.load("data/MNIST/X_test_MNIST_noise.npy")
    X_test = np.load("data/MNIST/X_test_MNIST.npy")
    y_test = np.load("data/MNIST/y_test_MNIST.npy")
    autoencoder = building_an_autoencoder(X_test, y_test)
    denosing_like_an_auto_encoder(autoencoder, X_test_noise, y_test)
