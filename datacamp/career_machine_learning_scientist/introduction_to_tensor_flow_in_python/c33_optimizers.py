import math
import tensorflow as tf
from tensorflow import keras


def loss_function(x):
    return 4.0 * math.cos(x - 1) + tf.divide(math.cos(2.0 * math.pi * x), x)


def the_danger_of_local_minima():
    x_1 = tf.Variable(6.0, tf.float32)
    x_2 = tf.Variable(0.3, tf.float32)

    opt = keras.optimizers.SGD(learning_rate=0.01)

    for j in range(100):
        opt.minimize(lambda: loss_function(x_1), var_list=[x_1])
        opt.minimize(lambda: loss_function(x_2), var_list=[x_2])

    print(x_1.numpy(), x_2.numpy())


def avoid_local_minima():
    x_1 = tf.Variable(0.05, tf.float32)
    x_2 = tf.Variable(0.05, tf.float32)

    opt_1 = keras.optimizers.RMSprop(learning_rate=0.01, momentum=0.99)
    opt_2 = keras.optimizers.RMSprop(learning_rate=0.01, momentum=0.00)

    for j in range(100):
        opt_1.minimize(lambda: loss_function(x_1), var_list=[x_1])
        opt_2.minimize(lambda: loss_function(x_2), var_list=[x_2])

    print(x_1.numpy(), x_2.numpy())


if __name__ == "__main__":
    the_danger_of_local_minima()
    avoid_local_minima()