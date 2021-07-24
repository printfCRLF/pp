import pandas as pd


def load_volunteer_data():
    return pd.read_csv("data/volunteer_opportunities.csv")


def load_wine_data():
    return pd.read_csv("data/wine_types.csv")


def load_ufo_data():
    return pd.read_csv("data/ufo_sightings_large.csv")


def load_hiking_data():
    return pd.read_json("data/hiking.json")


