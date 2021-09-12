import numpy as np
import tensorflow as tf
from data import load_house_data


def preparing_to_train_with_estimators(housing):
    # Define feature columns for bedrooms and bathrooms
    bedrooms = tf.feature_column.numeric_column("bedrooms")
    bathrooms = tf.feature_column.numeric_column("bathrooms")

    def input_fn():
        # Define the labels
        labels = np.array(housing["price"])
        # Define the features
        features = {'bedrooms': np.array(housing['bedrooms']),
                    'bathrooms': np.array(housing["bathrooms"])}
        return features, labels

    # Define the list of feature columns
    feature_list = [bedrooms, bathrooms]
    # Define the model and set the number of steps
    model = tf.estimator.LinearRegressor(feature_columns=feature_list)
    model.train(input_fn, steps=2)


if __name__ == "__main__":
    housing = load_house_data()
    preparing_to_train_with_estimators(housing)
