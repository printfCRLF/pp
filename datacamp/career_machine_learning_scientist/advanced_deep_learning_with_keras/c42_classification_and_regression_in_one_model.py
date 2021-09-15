from keras.layers import Input, Dense
from keras.models import Model
from sklearn.model_selection import train_test_split
from keras.optimizers import Adam
from scipy.special import expit as sigmoid
from data import load_games_tourney_enriched_data


def create_model():
    # Create an input layer with 2 columns
    input_tensor = Input(shape=(2,))
    # Create the first output
    output_tensor_1 = Dense(1, activation="linear", use_bias=False)(input_tensor)
    # Create the second output (use the first output as input here)
    output_tensor_2 = Dense(1, activation="sigmoid", use_bias=False)(output_tensor_1)
    # Create a model with 2 outputs
    model = Model(input_tensor, [output_tensor_1, output_tensor_2])

    return model


def compile_and_fit_model(model, games_tourney_train):
    # Compile the model with 2 losses and the Adam optimzer with a higher learning rate
    model.compile(loss=['mean_absolute_error', 'binary_crossentropy'], optimizer=Adam(lr=0.01))

    # Fit the model to the tournament training data, with 2 inputs and 2 outputs
    model.fit(games_tourney_train[['seed_diff', 'pred']],
              [games_tourney_train[['score_diff']], games_tourney_train[['won']]],
              epochs=10,
              verbose=True,
              batch_size=16384)

    return model


def inspect_and_evaluate_model(model, games_tourney_train, games_tourney_test):
    # Print the model weights
    print(model.get_weights())
    # Print the training data means
    print(games_tourney_train.mean())

    weight = 0.14
    # Print the approximate win probability predicted close game
    print(sigmoid(1 * weight))
    # Print the approximate win probability predicted blowout game
    print(sigmoid(10 * weight))

    # Evaluate the model on new data
    print(model.evaluate(games_tourney_test[['seed_diff', 'pred']],
                         [games_tourney_test[['score_diff']], games_tourney_test[['won']]], verbose=False))


if __name__ == "__main__":
    games_tourney = load_games_tourney_enriched_data()
    games_tourney_train, games_tourney_test = train_test_split(games_tourney, test_size=0.25)
    model = create_model()
    model = compile_and_fit_model(model, games_tourney_train)
    inspect_and_evaluate_model(model, games_tourney_train, games_tourney_test)
