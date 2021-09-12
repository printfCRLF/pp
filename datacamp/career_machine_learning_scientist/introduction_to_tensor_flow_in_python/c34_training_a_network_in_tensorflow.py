import numpy as np
import tensorflow as tf
from tensorflow import keras
from data import load_credit_data
from sklearn.model_selection import train_test_split

df = load_credit_data()
features = df.drop(columns=["ID", "default.payment.next.month"])
label = df["default.payment.next.month"]

X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.25, stratify=label, random_state=42)
borrower_features = X_train.values.astype(np.float32)
default = y_train.values.reshape(-1, 1).astype(np.float32)
test_features = X_test.values.astype(np.float32)
test_targets = y_test.values.reshape(-1).astype(np.float32)


def initialization_in_tensorflow():
    w1 = tf.Variable(tf.random.normal([23, 7]))
    b1 = tf.Variable(tf.ones([7]))
    w2 = tf.Variable(tf.random.normal([7, 1]))
    b2 = tf.Variable(0.0)

    return w1, b1, w2, b2


def model(w1, b1, w2, b2, features=borrower_features):
    # Apply relu activation functions to layer 1
    # features = np.array(features, dtype=np.float32)
    layer1 = keras.activations.relu(tf.matmul(features, w1) + b1)
    # Apply dropout rate of 0.25
    dropout = keras.layers.Dropout(0.25)(layer1)
    return keras.activations.sigmoid(tf.matmul(dropout, w2) + b2)


def loss_function(w1, b1, w2, b2, features=borrower_features, targets=default):
    predictions = model(w1, b1, w2, b2)
    return keras.losses.binary_crossentropy(targets, predictions)


def training_neural_networks_with_tensorflow(w1, b1, w2, b2, test_features, test_targets):
    opt = tf.optimizers.Adam()
    # Train the model
    for j in range(100):
        # Complete the optimizer
        opt.minimize(lambda: loss_function(w1, b1, w2, b2),
                     var_list=[w1, b1, w2, b2])

    model_predictions = model(w1, b1, w2, b2, test_features)
    print(tf.math.confusion_matrix(test_targets, model_predictions))


if __name__ == "__main__":
    w1, b1, w2, b2 = initialization_in_tensorflow()
    training_neural_networks_with_tensorflow(w1, b1, w2, b2, test_features, test_targets)
