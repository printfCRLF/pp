import pandas as pd


def load_nsfg_data():
    return pd.read_hdf("data/nsfg.hdf5")
