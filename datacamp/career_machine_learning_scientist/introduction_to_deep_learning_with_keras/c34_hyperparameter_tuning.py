from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import RandomizedSearchCV, KFold, cross_val_score
from sklearn.datasets import load_breast_cancer


def create_model(learning_rate, activation):
    opt = Adam(lr=learning_rate)

    model = Sequential()
    model.add(Dense(128, input_shape=(30,), activation=activation))
    model.add(Dense(256, activation=activation))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(optimizer=opt, loss="binary_crossentropy", metrics=['accuracy'])
    return model


def tuning_model_parameters(X, y):
    model = KerasClassifier(build_fn=create_model)

    params = {'activation': ["relu", "tanh"], 'batch_size': [32, 128, 256],
              'epochs': [50, 100, 200], 'learning_rate': [0.1, 0.01, 0.001]}

    # Create a randomize search cv object passing in the parameters to try
    random_search = RandomizedSearchCV(model, param_distributions=params, cv=KFold(3))

    # Running random_search.fit(X,y) would start the search,but it takes too long!
    cv_results_ = random_search.fit(X, y)
    print(cv_results_.best_score_)
    print(cv_results_.best_estimator_)
    print(cv_results_.best_params_)

    # show_results()


def show_results():
    print(
        "Best: \n"
        "0.975395 using {learning_rate: 0.001, epochs: 50, batch_size: 128, activation: relu} \n"
        "Other: \n"
        "0.956063 (0.013236) with: {learning_rate: 0.1, epochs: 200, batch_size: 32, activation: tanh} \n"
        "0.970123 (0.019838) with: {learning_rate: 0.1, epochs: 50, batch_size: 256, activation: tanh} \n"
        "0.971880 (0.006524) with: {learning_rate: 0.01, epochs: 100, batch_size: 128, activation: tanh} \n"
        "0.724077 (0.072993) with: {learning_rate: 0.1, epochs: 50, batch_size: 32, activation: relu} \n"
        "0.588752 (0.281793) with: {learning_rate: 0.1, epochs: 100, batch_size: 256, activation: relu} \n"
        "0.966608 (0.004892) with: {learning_rate: 0.001, epochs: 100, batch_size: 128, activation: tanh} \n"
        "0.952548 (0.019734) with: {learning_rate: 0.1, epochs: 50, batch_size: 256, activation: relu} \n"
        "0.971880 (0.006524) with: {learning_rate: 0.001, epochs: 200, batch_size: 128, activation: relu}\n"
        "0.968366 (0.004239) with: {learning_rate: 0.01, epochs: 100, batch_size: 32, activation: relu}\n"
        "0.910369 (0.055824) with: {learning_rate: 0.1, epochs: 100, batch_size: 128, activation: relu}")


def training_with_cross_validation(X, y):
    model = KerasClassifier(build_fn=create_model(learning_rate=0.001, activation="relu"), epochs=50,
                            batch_size=128, verbose=0)
    kfolds = cross_val_score(model, X, y, cv=3)

    print('The mean accuracy was:', kfolds.mean())
    print('With a standard deviation of:', kfolds.std())


if __name__ == "__main__":
    X, y = load_breast_cancer(return_X_y=True)
    tuning_model_parameters(X, y)
    # training_with_cross_validation(X, y)
