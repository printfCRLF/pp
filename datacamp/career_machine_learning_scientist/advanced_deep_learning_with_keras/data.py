import pandas as pd


def load_games_tourney_data():
    return pd.read_csv("data/basketball_data/games_tourney.csv")


def load_games_tourney_enriched_data():
    return pd.read_csv("data/basketball_data/games_season_enriched.csv")


def load_games_season_data():
    return pd.read_csv("data/basketball_data/games_season.csv")
