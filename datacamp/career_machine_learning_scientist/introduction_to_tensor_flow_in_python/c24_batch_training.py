import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Define the model
def linear_regression(intercept, slope, features):
    return intercept + slope * features

def loss_function(intercept, slope, targets, features):
    predictions = linear_regression(intercept, slope, features)
    return keras.losses.mse(targets, predictions)
    
def training_a_linear_model_in_batches():
    # Define the intercept and slope
    intercept = tf.Variable(10.0, tf.float32)
    slope = tf.Variable(0.5, tf.float32)

    # Initialize Adam optimizer
    opt = keras.optimizers.Adam()

    # Load data in batches
    for batch in pd.read_csv('data/kc_house_data.csv', chunksize=100):
        size_batch = np.array(batch['sqft_lot'], np.float32)

        # Extract the price values for the current batch
        price_batch = np.array(batch['price'], np.float32)

        # Complete the loss, fill in the variable list, and minimize
        opt.minimize(lambda: loss_function(intercept, slope, price_batch, size_batch), var_list=[intercept, slope])

    # Print trained parameters
    print(intercept.numpy(), slope.numpy())

if __name__ == "__main__":
    training_a_linear_model_in_batches()