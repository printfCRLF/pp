import pandas as pd


def load_police_data():
    return pd.read_csv("data/police.csv")


def load_weather_data():
    return pd.read_csv("data/weather.csv")
