from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
from data import load_titanic_data


def changing_optimization_parameters(predictors, target):
    # Create list of learning rates: lr_to_test
    lr_to_test = [.000001, 0.01, 1]

    # Loop over learning rates
    for lr in lr_to_test:
        print('\n\nTesting model with learning rate: %f\n' % lr)

        # Build new model to test, unaffected by previous models
        model = get_new_model()

        # Create SGD optimizer with specified learning rate: my_optimizer
        my_optimizer = SGD(lr=lr)

        # Compile the model
        model.compile(optimizer=my_optimizer, loss='categorical_crossentropy')

        # Fit the model
        model.fit(predictors, target)


def get_new_model(input_shape=(10,)):
    model = Sequential()
    model.add(Dense(100, activation='relu', input_shape=input_shape))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(2, activation='softmax'))
    return(model)


predictors, target = load_titanic_data()
changing_optimization_parameters(predictors, target)
