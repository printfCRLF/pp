import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from util import get_slope, get_mse


def calculating_slopes():
    input_data = np.array([1, 2, 3])
    weights = np.array([0, 2, 1])
    target = 0

    # Calculate the predictions: preds
    preds = (input_data * weights).sum()
    # Calculate the error: error
    error = preds - target
    # Calculate the slope: slope
    slope = 2 * input_data * error
    # Print the slope
    print(slope)


def improving_modeL_weights():
    input_data = np.array([1, 2, 3])
    weights = np.array([0, 2, 1])
    target = 0
    # Set the learning rate: learning_rate
    learning_rate = 0.01

    # Calculate the predictions: preds
    preds = (weights * input_data).sum()
    # Calculate the error: error
    error = preds - target
    # Calculate the slope: slope
    slope = 2 * input_data * error

    # Update the weights: weights_updated
    weights_updated = weights - learning_rate * slope
    # Get updated predictions: preds_updated
    preds_updated = (weights_updated * input_data).sum()
    # Calculate updated error: error_updated
    error_updated = preds_updated - target

    # Print the original error
    print(error)
    # Print the updated error
    print(error_updated)


def making_multiple_updates_to_weights():
    input_data = np.array([1, 2, 3])
    weights = np.array([0, 2, 1])
    target = 0

    n_updates = 20
    mse_hist = []

    for i in range(n_updates):
        slope = get_slope(input_data, target, weights)
        weights = weights - 0.01 * slope
        mse = get_mse(input_data, target, weights)
        mse_hist.append(mse)

    _ = plt.plot(mse_hist)
    _ = plt.xlabel('Iterations')
    _ = plt.ylabel('Mean Squared Error')
    _ = plt.show()
    print(mse_hist)


sns.set()
# calculating_slopes()
# improving_modeL_weights()
making_multiple_updates_to_weights()
