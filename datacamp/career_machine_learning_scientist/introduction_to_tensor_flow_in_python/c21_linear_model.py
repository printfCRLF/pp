import pandas as pd
import numpy as np
import tensorflow as tf


def load_data_using_pandas():
    # Assign the path to a string variable named data_path
    data_path = 'data/kc_house_data.csv'
    # Load the dataset as a dataframe named housing
    housing = pd.read_csv(data_path)
    # Print the price column of housing
    print(housing["price"])

    return housing


def setting_the_data_type(housing):
    # Use a numpy array to define price as a 32-bit float
    price = np.array(housing['price'], np.float32)
    # Define waterfront as a Boolean using cast
    waterfront = tf.cast(housing['waterfront'], tf.bool)
    # Print price and waterfront
    print(price)
    print(waterfront)


if __name__ == "__main__":
    housing = load_data_using_pandas()
    setting_the_data_type(housing)
