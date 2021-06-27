import pandas as pd


def load_world_data():
    return pd.read_csv("data/countries-of-the-world.csv")


def load_survey_data():
    return pd.read_csv("data/young-people-survey-responses.csv")


def load_student_data():
    return pd.read_csv("data/student-alcohol-consumption.csv")


def load_mpg_data():
    return pd.read_csv("data/mpg.csv")
