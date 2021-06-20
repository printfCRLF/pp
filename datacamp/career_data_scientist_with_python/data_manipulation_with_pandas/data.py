import pandas as pd
import pickle


def load_homelessness_data():
    df = pd.read_csv("data/homelessness.csv")
    return df


def load_sales_data():
    df = pd.read_csv("data/sales_subset.csv")
    return df


def load_temperature_data():
    df = pd.read_csv("data/temperatures.csv", parse_dates=["date"])
    return df


def load_avocado_data():
    infile = open("data/avoplotto.pkl", 'rb')
    new_dict = pickle.load(infile)
    infile.close()
    df = pd.DataFrame(new_dict)
    return df
