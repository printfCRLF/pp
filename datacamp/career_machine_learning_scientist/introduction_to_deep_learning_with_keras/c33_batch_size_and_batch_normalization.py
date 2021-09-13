from keras.models import Sequential
from keras.layers import Dense
from keras.layers import BatchNormalization
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def get_model():
    model = Sequential()
    model.add(Dense(4, input_shape=(2,), activation='relu'))
    model.add(Dense(1, activation="sigmoid"))
    model.compile('sgd', 'binary_crossentropy', metrics=['accuracy'])
    return model


def changing_batch_size():
    model = get_model()
    model.fit(X_train, y_train, epochs=5, batch_size=1)
    print("\n The accuracy when using a batch of size 1 is: ",
          model.evaluate(X_test, y_test)[1])

    model = get_model()
    model.fit(X_train, y_train, epochs=5, batch_size=X_train.shape[0])
    print("\n The accuracy when using the whole training set as batch-size was: ",
          model.evaluate(X_test, y_test)[1])


def batch_normalization():
    batchnorm_model = Sequential()
    batchnorm_model.add(Dense(50, input_shape=(64,), activation='relu', kernel_initializer='normal'))
    batchnorm_model.add(BatchNormalization())
    batchnorm_model.add(Dense(50, activation='relu', kernel_initializer='normal'))
    batchnorm_model.add(BatchNormalization())
    batchnorm_model.add(Dense(50, activation='relu', kernel_initializer='normal'))
    batchnorm_model.add(BatchNormalization())
    batchnorm_model.add(Dense(10, activation='softmax', kernel_initializer='normal'))

    # Compile your model with sgd
    batchnorm_model.compile(optimizer="sgd", loss='categorical_crossentropy', metrics=['accuracy'])


def compare_histories_acc(h1, h2):
    plt.plot(h1.history['acc'])
    plt.plot(h1.history['val_acc'])
    plt.plot(h2.history['acc'])
    plt.plot(h2.history['val_acc'])
    plt.title("Batch Normalization Effects")
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend(['Train', 'Test', 'Train with Batch Normalization', 'Test with Batch Normalization'], loc='best')
    plt.show()


def batch_nomralization_effects():
    # Train your standard model, storing its history callback
    h1_callback = standard_model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, verbose=0)
    # Train the batch normalized model you recently built, store its history callback
    h2_callback = batchnorm_model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, verbose=0)
    # Call compare_histories_acc passing in both model histories
    compare_histories_acc(h1_callback, h2_callback)
