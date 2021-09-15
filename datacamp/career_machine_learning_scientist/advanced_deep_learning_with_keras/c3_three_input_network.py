from keras.layers import Input, Dense, Concatenate
from keras.models import Model
from sklearn.model_selection import train_test_split
from c2_two_input_networks import define_team_model, define_team_lookup
from data import load_games_tourney_enriched_data, load_games_season_data


def make_an_input_layer_home_vs_away(team_strength_model):
    # Create an Input for each team
    team_in_1 = Input(shape=(1,), name='Team-1-In')
    team_in_2 = Input(shape=(1,), name='Team-2-In')
    # Create an input for home vs away
    home_in = Input(shape=(1,), name='Home-In')

    # Lookup the team inputs in the team strength model
    team_1_strength = team_strength_model(team_in_1)
    team_2_strength = team_strength_model(team_in_2)
    # Combine the team strengths with the home input using a Concatenate layer, then add a Dense layer
    out = Concatenate()([team_1_strength, team_2_strength, home_in])
    out = Dense(1)(out)
    # Make a Model
    model = Model([team_in_1, team_in_2, home_in], out)
    # Compile the model
    model.compile(optimizer="adam", loss="mean_absolute_error")
    return model


def fit_the_model_and_evaluate(model, games_season, games_tourney):
    # Fit the model to the games_season dataset
    model.fit([games_season["team_1"], games_season["team_2"], games_season["home"]],
              games_season["score_diff"],
              epochs=1,
              verbose=True,
              validation_split=0.1,
              batch_size=2048)

    # Evaluate the model on the games_tourney dataset
    print(model.evaluate([games_tourney["team_1"], games_tourney["team_2"], games_tourney["home"]],
                         games_tourney["score_diff"], verbose=False))


def stacking_models(games_tourney_train, games_tourney_test):
    input_tensor = Input((3,))
    output_tensor = Dense(1)(input_tensor)
    model = Model(input_tensor, output_tensor)
    model.compile(optimizer="adam", loss="mean_absolute_error")

    model.fit(games_tourney_train[['home', 'seed_diff', 'pred']], games_tourney_train['score_diff'],
              epochs=1, verbose=True)

    # Evaluate the model on the games_tourney_test dataset
    print(model.evaluate(games_tourney_test[["home", "seed_diff", "pred"]],
                         games_tourney_test["score_diff"], verbose=False))


if __name__ == "__main__":
    games_season = load_games_season_data()
    games_tourney = load_games_tourney_enriched_data()

    team_lookup = define_team_lookup(games_season)
    team_strength_model = define_team_model(team_lookup)

    model = make_an_input_layer_home_vs_away(team_strength_model)
    fit_the_model_and_evaluate(model, games_season, games_tourney)

    games_tourney_train, games_tourney_test = train_test_split(games_tourney, test_size=0.25)
    stacking_models(games_tourney_train, games_tourney_test)
