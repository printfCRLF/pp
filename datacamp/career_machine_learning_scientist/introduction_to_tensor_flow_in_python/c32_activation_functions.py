import tensorflow as tf
from tensorflow import keras
from data import load_credit_data


def binary_classification_problems(df):
    bill_amounts = df[["BILL_AMT1", "BILL_AMT2", "BILL_AMT3"]]
    default = df["default.payment.next.month"].values.reshape(-1, 1)
    inputs = tf.constant(bill_amounts, tf.float32)

    dense1 = keras.layers.Dense(3, activation='relu')(inputs)
    dense2 = keras.layers.Dense(2, activation="relu")(dense1)
    outputs = keras.layers.Dense(1, activation="sigmoid")(dense2)

    # Print error for first five examples
    error = default[:5] - outputs.numpy()[:5]
    print(error)


def multiclass_classification_problems(df):
    borrower_features = df[["BILL_AMT1", "BILL_AMT2", "BILL_AMT3", "BILL_AMT4", "BILL_AMT5",
                       "PAY_AMT1", "PAY_AMT2", "PAY_AMT3", "PAY_AMT4", "PAY_AMT5"]]

    inputs = tf.constant(borrower_features, tf.float32)
    dense1 = keras.layers.Dense(10, activation='sigmoid')(inputs)
    dense2 = keras.layers.Dense(8, activation="relu")(dense1)
    outputs = keras.layers.Dense(6, activation="softmax")(dense2)

    # Print first five predictions
    print(outputs.numpy()[:5])

if __name__ == "__main__":
    df = load_credit_data()
    # binary_classification_problems(df)
    multiclass_classification_problems(df)