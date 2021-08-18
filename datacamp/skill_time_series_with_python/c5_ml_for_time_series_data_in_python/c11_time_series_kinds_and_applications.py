import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import h5py


def plotting_a_time_series():
    df1 = pd.read_csv("data/prices.csv", usecols=[0, 1, 2])
    close = df1[df1["symbol"] == "AAPL"]["close"].to_numpy()
    index = np.arange(0, len(close))
    data = pd.DataFrame({"symbol": index, "data_values": close})

    print(data.head())
    print(data.describe())

    # https://docs.h5py.org/en/stable/quick.html
    filename = "data/audio_munged.hdf5"
    # with pd.HDFStore(filename) as h5:
    #     print(h5.keys())
    #     df = pd.concat(map(h5.get, h5.keys()), axis=1)
    #     print(df.head())

    filename = "data/audio_munged.hdf5"
    df2 = pd.read_hdf("data/audio_munged.hdf5", key="/h5io/key_data")
    index = df2.index
    data_values = df2.iloc[:, 30]
    data2 = pd.DataFrame({"time": index, "data_values": data_values})

    fig, axes = plt.subplots(2, 1, figsize=(5, 10))
    data.iloc[:1000].plot(y="data_values", ax=axes[0])
    data2.iloc[:1000].plot(y="data_values", ax=axes[1])
    plt.show()


if __name__ == "__main__":
    sns.set()
    plotting_a_time_series()
