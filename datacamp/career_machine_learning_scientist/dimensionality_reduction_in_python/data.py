import pandas as pd


def load_pokemon_data():
    return pd.read_csv("data/pokemon.csv")


def load_ansur_ii_female_data():
    return pd.read_csv("data/ANSUR_II_FEMALE.csv")


def load_ansur_ii_male_data():
    return pd.read_csv("data/ANSUR_II_MALE.csv")


def load_school_data():
    return pd.read_csv("data/Public_Schools2.csv")


def load_diabetes_data():
    return pd.read_csv("data/PimaIndians.csv")
