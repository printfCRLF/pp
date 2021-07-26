import pandas as pd


def load_stackoverflow_data():
    return pd.read_csv("data/Combined_DS_v10.csv")


def load_inargural_speech_data():
    return pd.read_csv("data/inaugural_speeches.csv")
