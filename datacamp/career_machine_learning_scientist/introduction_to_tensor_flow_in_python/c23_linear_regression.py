import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from data import load_house_data


def linear_regression(intercept, slope, features):
    return slope * features + intercept


def loss_function(intercept, slope, features, targets):
    predictions = linear_regression(intercept, slope, features)

    return keras.losses.mse(targets, predictions)


def set_up_linear_regression():
    features = tf.constant([1.0, 2.0, 3.0])
    targets = tf.constant([5.0, 7.0, 9.0])
    # Compute the loss for different slope and intercept values
    print(loss_function(3.3, 2.2, features, targets).numpy())
    print(loss_function(3.0, 2.0, features, targets).numpy())


def plot_results(intercept, slope, size_log, price_log):
    size_range = np.linspace(6, 130, 100)
    price_pred = [intercept+slope*s for s in size_range]
    plt.scatter(size_log, price_log, color='black')
    plt.plot(size_range, price_pred, linewidth=3.0, color='red')
    plt.xlabel('log(size)')
    plt.ylabel('log(price)')
    plt.title('Scatterplot of data and fitted regression line')
    plt.show()


def training_a_linear_model(size_log, price_log):
    intercept = tf.Variable(5.0)
    slope = tf.Variable(0.001)

    # Initialize an Adam optimizer
    opt = keras.optimizers.Adam(0.5)

    for j in range(100):
        # Apply minimize, pass the loss function, and supply the variables
        opt.minimize(lambda: loss_function(intercept, slope, size_log, price_log),
                     var_list=[intercept, slope])

        # Print every 10th value of the loss
        if j % 10 == 0:
            print(loss_function(intercept, slope, size_log, price_log).numpy())

    # Plot data and regression line
    plot_results(intercept, slope, size_log, price_log)


if __name__ == "__main__":
    df = load_house_data()
    size_log = df["sqft_living"].apply(lambda x: np.sqrt(x))
    price_log = df["price"].apply(lambda x: np.sqrt(x))
    # set_up_linear_regression()
    training_a_linear_model(size_log, price_log)
