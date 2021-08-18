import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import librosa as lr
from glob import glob


def insepcting_the_classification_data():
    data_dir = "data/archive/set_a"
    # List all the wav files in the folder
    audio_files = glob(data_dir + '/*.wav')

    # Read in the first audio file, create the time array
    audio, sfreq = lr.load(audio_files[3])
    time = np.arange(0, len(audio)) / sfreq

    # Plot audio over time
    fig, ax = plt.subplots()
    ax.plot(time, audio)
    ax.set(xlabel='Time (s)', ylabel='Sound Amplitude')
    plt.show()


def inspecting_the_regression_data():
    # Read in the data
    data = pd.read_csv('data/prices.csv', index_col=0)

    # Convert the index of the DataFrame to datetime
    data.index = pd.to_datetime(data.index)

    data = data.pivot_table(values="close", index=data.index, columns="symbol")
    data = data.loc[:, ["AAPL", "FB", "NFLX", "V", "XOM"]]
    print(data.head())

    # Loop through each column, plot its values over time
    fig, ax = plt.subplots()
    for column in data.columns:
        data[column].plot(ax=ax, label=column)
    ax.legend()
    plt.show()


if __name__ == "__main__":
    sns.set()
    # insepcting_the_classification_data()
    inspecting_the_regression_data()
