import pandas as pd


def load_nsfg_data():
    return pd.read_hdf("data/nsfg.hdf5")


def load_gss_data():
    return pd.read_hdf("data/gss.hdf5")


def load_brfss_data():
    return pd.read_hdf("data/brfss.hdf5")
