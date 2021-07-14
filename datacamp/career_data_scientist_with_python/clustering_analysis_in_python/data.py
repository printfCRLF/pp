import pandas as pd
from scipy.cluster.vq import whiten


def load_fifa_18_sample_data():
    return pd.read_csv("data/fifa_18_sample_data.csv")


def load_comic_con_data():
    df = pd.read_csv("data/comic_con.csv")
    df["x_scaled"] = whiten(df["x_coordinate"])
    df["y_scaled"] = whiten(df["y_coordinate"])
    return df


def load_movie_data():
    with open("data/movies_plot.csv") as f:
        lines = f.readlines()

    return lines
