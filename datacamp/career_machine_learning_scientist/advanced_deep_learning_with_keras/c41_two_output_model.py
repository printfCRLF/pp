from keras.layers import Input, Dense
from keras.models import Model
from sklearn.model_selection import train_test_split
from data import load_games_tourney_enriched_data


def create_two_output_model():
    # Define the input
    input_tensor = Input(shape=(2,))
    # Define the output
    output_tensor = Dense(2)(input_tensor)
    # Create a model
    model = Model(input_tensor, output_tensor)
    # Compile the model
    model.compile(optimizer="adam", loss="mean_absolute_error")

    return model


def train_model(model, games_tourney_train):
    model.fit(games_tourney_train[['seed_diff', 'pred']],
              games_tourney_train[['score_1', 'score_2']],
              verbose=True, epochs=100, batch_size=16384)

    return model


def inspect_and_evaluate_model(model, games_tourney_train, games_tourney_test):
    # Print the model's weights
    print(model.get_weights())
    # Print the column means of the training data
    print(games_tourney_train.mean())

    # Evaluate the model on the tournament test data
    print(model.evaluate(games_tourney_test[['seed_diff', 'pred']], games_tourney_test[['score_1', 'score_2']],
                         verbose=False))


if __name__ == "__main__":
    games_tourney = load_games_tourney_enriched_data()
    games_tourney_train, games_tourney_test = train_test_split(games_tourney, test_size=0.25)
    model = create_two_output_model()
    model = train_model(model, games_tourney_train)
    inspect_and_evaluate_model(model, games_tourney_train, games_tourney_test)
