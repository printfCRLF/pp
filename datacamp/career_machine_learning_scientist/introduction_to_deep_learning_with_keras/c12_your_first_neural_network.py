from keras.models import Sequential
from keras.layers import Dense


def hello_nets():
    model = Sequential()
    model.add(Dense(10, input_shape=(2,), activation="relu"))
    model.add(Dense(1))
    model.summary()


def counting_parameters():
    model = Sequential()
    model.add(Dense(5, input_shape=(3,), activation="relu"))
    model.add(Dense(1))
    model.summary()


def build_as_shown():
    model = Sequential()
    model.add(Dense(3, input_shape=(2,)))
    model.add(Dense(1))


if __name__ == "__main__":
    hello_nets()
    counting_parameters()
    build_as_shown()
