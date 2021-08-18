import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import librosa as lr
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from glob import glob


def many_repetitions_of_sounds(normal, abnormal, sfreq):
    fig, axs = plt.subplots(3, 2, figsize=(15, 7), sharex=True, sharey=True)
    # Calculate the time array
    time = np.arange(normal.shape[0]) / sfreq

    # Stack the normal/abnormal audio so you can loop and plot
    stacked_audio = np.hstack([normal, abnormal]).T

    # Loop through each audio file / ax object and plot
    # .T.ravel() transposes the array, then unravels it into a 1-D vector for looping
    for iaudio, ax in zip(stacked_audio, axs.T.ravel()):
        ax.plot(time, iaudio)

    axs[0, 0].set(title="Normal Heartbeats")
    axs[0, 1].set(title="Abnormal Heartbeats")
    plt.tight_layout()
    plt.show()


def load_heartbeats_audio_data(filepath, n_samples):
    audio_files = glob(filepath)
    length = 8820
    sfreq = 2205
    time = np.arange(0, length) / sfreq
    normal = pd.DataFrame({"time": time})
    normal.set_index("time", inplace=True)
    n_files = len(audio_files)
    rng = np.random.default_rng()
    idx = rng.choice(n_files, size=n_samples, replace=False)
    for i in idx:
        audio, sfreq = lr.load(audio_files[i])
        audio = audio[:length]
        normal[i] = audio
    return normal, sfreq, time


def invariance_in_time(normal_filepath, abnormal_filepath):
    normal, sfreq, time = load_heartbeats_audio_data(normal_filepath, 10)
    abnormal, sfreq, time = load_heartbeats_audio_data(abnormal_filepath, 10)
    # Average across the audio files of each DataFrame
    mean_normal = np.mean(normal, axis=1)
    mean_abnormal = np.mean(abnormal, axis=1)

    # Plot each average over time
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3), sharey=True)
    ax1.plot(time, mean_normal)
    ax1.set(title="Normal Data")
    ax2.plot(time, mean_abnormal)
    ax2.set(title="Abnormal Data")
    plt.show()


def build_a_classification_model(normal_filepath, abnormal_filepath):
    normal, sfreq, time = load_heartbeats_audio_data(normal_filepath, 40)
    abnormal, sfreq, time = load_heartbeats_audio_data(abnormal_filepath, 40)
    X = pd.concat([normal.T, abnormal.T])
    y = ["normal"] * 40 + ["abnormal"] * 40
    X.index = range(80)

    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)
    # Initialize and fit the model
    model = LinearSVC()
    model.fit(X_train, y_train)

    # Generate predictions and score them manually
    predictions = model.predict(X_test)
    print(sum(predictions == y_test) / len(y_test))


if __name__ == "__main__":
    normal_filepath = "data/archive/set_b/normal__*.wav"
    abnormal_filepath = "data/archive/set_b/extrastole__*.wav"
    sns.set()
    # normal, sfreq, time = load_heartbeats_audio_data(normal_filepath, 3)
    # abnormal, sfreq, time = load_heartbeats_audio_data(abnormal_filepath, 3)
    # many_repetitions_of_sounds(normal, abnormal, sfreq)

    # invariance_in_time(normal_filepath, abnormal_filepath)

    build_a_classification_model(normal_filepath, abnormal_filepath)
