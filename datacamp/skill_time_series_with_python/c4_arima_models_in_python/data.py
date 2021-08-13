import pandas as pd


def load_earth_quake_data():
    earthquake = pd.read_csv('data/earthquakes.xls', usecols=[0, 2],
                             parse_dates=['date'], index_col='date')
    return earthquake
