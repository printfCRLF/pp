from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
from keras.callbacks import EarlyStopping
from data import load_titanic_data


def validation_dataset(predictors, target):
    # Save the number of columns in predictors: n_cols
    n_cols = predictors.shape[1]
    input_shape = (n_cols,)

    # Specify the model
    model = Sequential()
    model.add(Dense(100, activation='relu', input_shape=input_shape))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(2, activation='softmax'))

    # Compile the model
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy', metrics=['accuracy'])

    # Fit the model
    hist = model.fit(predictors, target, validation_split=0.3)


def early_stopping(predictors, target):
    # Save the number of columns in predictors: n_cols
    n_cols = predictors.shape[1]
    input_shape = (n_cols,)

    # Specify the model
    model = Sequential()
    model.add(Dense(100, activation='relu', input_shape=input_shape))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(2, activation='softmax'))

    # Compile the model
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy', metrics=['accuracy'])

    # Define early_stopping_monitor
    early_stopping_monitor = EarlyStopping(patience=2)

    # Fit the model
    model.fit(predictors, target, validation_split=0.3, epochs=30,
              callbacks=[early_stopping_monitor])


predictors, target = load_titanic_data()
#validation_dataset(predictors, target)
early_stopping(predictors, target)
