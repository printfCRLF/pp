from numpy import unique
from keras.layers import Input, Embedding, Flatten, Subtract
from keras.models import Model
from data import load_games_tourney_data, load_games_season_data

def define_team_lookup(games_season):
    n_teams = unique(games_season["team_1"]).shape[0]
    # Create an embedding layer
    team_lookup = Embedding(input_dim=n_teams, output_dim=1, input_length=1, name="Team-Strength")
    return team_lookup


def define_team_model(team_lookup):
    # Create an input layer for the team ID
    teamid_in = Input(shape=(1,))
    # Lookup the input in the team strength embedding layer
    strength_lookup = team_lookup(teamid_in)
    # Flatten the output
    strength_lookup_flat = Flatten()(strength_lookup)
    # Combine the operations into a single, re-usable model
    team_strength_model = Model(teamid_in, strength_lookup_flat, name='Team-Strength-Model')

    return team_strength_model


def define_two_inputs(team_strength_model):
    # Input layer for team 1
    team_in_1 = Input((1,), name="Team-1-In")
    # Separate input layer for team 2
    team_in_2 = Input((1,), name="Team-2-In")

    # Lookup team 1 in the team strength model
    team_1_strength = team_strength_model(team_in_1)
    # Lookup team 2 in the team strength model
    team_2_strength = team_strength_model(team_in_2)

    return team_in_1, team_in_2, team_1_strength, team_2_strength


def shared_layers(team_in_1, team_in_2, team_1_strength, team_2_strength):
    # Create a subtract layer using the inputs from the previous exercise
    score_diff = Subtract()([team_1_strength, team_2_strength])
    model = Model([team_in_1, team_in_2], score_diff)
    model.compile("adam", "mean_absolute_error")

    return model


def fit_predict_evaluate(games_season, games_tourney, model):
    input_1 = games_season["team_1"]
    input_2 = games_season["team_2"]

    model.fit([input_1, input_2], games_season["score_diff"],
              epochs=1, batch_size=2048, validation_split=0.1, verbose=True)

    input_1 = games_tourney["team_1"]
    input_2 = games_tourney["team_2"]
    print(model.evaluate([input_1, input_2], games_tourney["score_diff"], verbose=False))


if __name__ == "__main__":
    games_season = load_games_season_data()
    games_tourney = load_games_tourney_data()

    team_lookup = define_team_lookup(games_season)
    team_strength_model = define_team_model(team_lookup)
    team_in_1, team_in_2, team_1_strength, team_2_strength = define_two_inputs(team_strength_model)
    model = shared_layers(team_in_1, team_in_2, team_1_strength, team_2_strength)
    fit_predict_evaluate(games_season, games_tourney, model)
