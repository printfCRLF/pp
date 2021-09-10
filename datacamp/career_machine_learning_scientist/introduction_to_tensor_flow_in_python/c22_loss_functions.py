import tensorflow as tf
from tensorflow import keras


def model(scalar, features):
    return scalar * features


def loss_function(scalar, features, targets):
    predictions = model(scalar, features)
    return keras.losses.mae(targets, predictions)


def modifying_the_loss_function():
    scalar = tf.Variable(1.0, dtype=tf.float32)
    print("loss function outputs", loss_function(
        scalar, [1.0, 2.0, 3.0], [1.5, 2.5, 3.5]).numpy())


if __name__ == "__main__":
    modifying_the_loss_function()
