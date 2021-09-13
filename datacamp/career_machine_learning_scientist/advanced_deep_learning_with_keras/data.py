import pandas as pd

def load_basketball_data():
    return pd.read_csv("data/basketball_data/games_tourney.csv")