import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import librosa as lr
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score
from glob import glob
from c21_classifying_a_time_series import load_heartbeats_audio_data


def calculating_the_envelope_of_sound(audio):
    fig, axes = plt.subplots(3, 1, sharex=True)
    # Plot the raw data first
    audio.plot(figsize=(10, 5), ax=axes[0])

    # Rectify the audio signal
    audio_rectified = audio.apply(np.abs)
    # Plot the result
    audio_rectified.plot(figsize=(10, 5), ax=axes[1])

    # Smooth by applying a rolling mean
    audio_rectified_smooth = audio_rectified.rolling(50).mean()
    # Plot the result
    audio_rectified_smooth.plot(figsize=(10, 5), ax=axes[2])
    plt.show()

    return audio_rectified_smooth


def calculating_features_from_the_envelope():
    normal, sfreq, time = load_heartbeats_audio_data(normal_filepath, 40)
    abnormal, sfreq, time = load_heartbeats_audio_data(abnormal_filepath, 40)
    df = pd.concat([normal, abnormal], axis=1)
    y = ["normal"] * 40 + ["abnormal"] * 40

    audio_rectified = df.apply(np.abs)
    audio_rectified_smooth = audio_rectified.rolling(50).mean()
    # Calculate stats
    means = np.mean(audio_rectified_smooth, axis=0)
    stds = np.std(audio_rectified_smooth, axis=0)
    maxs = np.max(audio_rectified_smooth, axis=0)

    # Create the X and y arrays
    X = np.column_stack([means, stds, maxs])
    # y = labels.reshape([-1, 1])

    # Fit the model and score on testing data
    model = LinearSVC()
    percent_score = cross_val_score(model, X, y, cv=5)
    print(np.mean(percent_score))

    return df, y, means, stds, maxs


def derivative_features_tempogram(audio, y, means, stds, maxs):
    # Calculate the tempo of the sounds
    tempos = []
    for col, i_audio in audio.items():
        tempos.append(lr.beat.tempo(i_audio.values, sr=sfreq,
                      hop_length=2**6, aggregate=None))

    # Convert the list to an array so you can manipulate it more easily
    tempos = np.array(tempos)

    # Calculate statistics of each tempo
    tempos_mean = tempos.mean(axis=-1)
    tempos_std = tempos.std(axis=-1)
    tempos_max = tempos.max(axis=-1)

    # Create the X and y arrays
    X = np.column_stack(
        [means, stds, maxs, tempos_mean, tempos_std, tempos_max])
    # y = labels.reshape([-1, 1])

    # Fit the model and score on testing data
    model = LinearSVC()
    percent_score = cross_val_score(model, X, y, cv=5)
    print(np.mean(percent_score))


if __name__ == "__main__":
    normal_filepath = "data/archive/set_b/normal__*.wav"
    abnormal_filepath = "data/archive/set_b/extrastole__*.wav"
    normal, sfreq, time = load_heartbeats_audio_data(normal_filepath, 1)

    # calculating_the_envelope_of_sound(normal)

    df, y, means, stds, maxs = calculating_features_from_the_envelope()
    derivative_features_tempogram(df, y, means, stds, maxs)
