import numpy as np
import tensorflow as tf
import tensorflow.keras as keras


def the_linear_algebra_of_dense_layers():
    borrower_features = np.array([[2., 2., 43.]], dtype=np.float32)
    bias1 = tf.Variable(1.0)
    weights1 = tf.Variable(tf.ones((3, 2)))
    product1 = tf.matmul(borrower_features, weights1)
    dense1 = keras.activations.sigmoid(product1 + bias1)

    bias2 = tf.Variable(1.0)
    weights2 = tf.Variable(tf.ones((2, 1)))
    product2 = tf.matmul(dense1, weights2)

    prediction = keras.activations.sigmoid(product2 + bias2)
    print('\n prediction: {}'.format(prediction.numpy()[0, 0]))
    print('\n actual: 1')


def low_leveL_approach_with_multiple_examples():
    borrower_features = tf.constant(
        [[3., 3., 23.],
         [2., 1., 24.],
         [1., 1., 49.],
         [1., 1., 49.],
         [2., 1., 29.]])
    weights1 = tf.Variable(
        [[-0.6, 0.6],
         [0.8, -0.3],
         [-0.09, -0.08]])
    bias1 = tf.constant([0.1], dtype=tf.float32)

    products1 = tf.matmul(borrower_features, weights1)
    dense1 = keras.activations.sigmoid(products1 + bias1)

    print('\n shape of borrower_features: ', borrower_features.shape)
    print('\n shape of weights1: ', weights1.shape)
    print('\n shape of bias1: ', bias1.shape)
    print('\n shape of dense1: ', dense1.shape)


def using_the_dense_layer_api():
    borrower_features = tf.ones((100, 10))
    dense1 = keras.layers.Dense(7, activation="sigmoid")(borrower_features)
    dense2 = keras.layers.Dense(3, activation="sigmoid")(dense1)
    predictions = keras.layers.Dense(1, activation="sigmoid")(dense2)

    # Print the shapes of dense1, dense2, and predictions
    print('\n shape of dense1: ', dense1.shape)
    print('\n shape of dense2: ', dense2.shape)
    print('\n shape of predictions: ', predictions.shape)


if __name__ == "__main__":
    # the_linear_algebra_of_dense_layers()
    # low_leveL_approach_with_multiple_examples()
    using_the_dense_layer_api()
