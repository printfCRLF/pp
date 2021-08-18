import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import librosa as lr
from librosa.core import stft, amplitude_to_db
from librosa.display import specshow
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score
from glob import glob
from c21_classifying_a_time_series import load_heartbeats_audio_data


def spectrograms_of_heartbeat_audio(audio, time, sfreq):
    # Prepare the STFT
    HOP_LENGTH = 2**4
    spec = stft(audio, hop_length=HOP_LENGTH, n_fft=2**7)

    # Convert into decibels
    spec_db = amplitude_to_db(spec)

    # Compare the raw audio to the spectrogram of the audio
    fig, axs = plt.subplots(2, 1, figsize=(10, 10), sharex=True)
    axs[0].plot(time, audio)
    specshow(spec_db, sr=sfreq, x_axis='time',
             y_axis='hz', hop_length=HOP_LENGTH)
    plt.show()

    return spec


def engineering_spectral_features(spec, times_spec):
    # Calculate the spectral centroid and bandwidth for the spectrogram
    spec = spec.real.astype("float32")
    bandwidths = lr.feature.spectral_bandwidth(S=spec)[0]
    centroids = lr.feature.spectral_centroid(S=spec)[0]

    # Convert spectrogram to decibels for visualization
    spec_db = amplitude_to_db(spec)

    # Display these features on top of the spectrogram
    fig, ax = plt.subplots(figsize=(10, 5))
    HOP_LENGTH = 2**4
    ax = specshow(spec_db, x_axis='time', y_axis='hz', hop_length=HOP_LENGTH)
    ax.plot(times_spec, centroids)
    ax.fill_between(times_spec, centroids - bandwidths / 2,
                    centroids + bandwidths / 2, alpha=.5)
    ax.set(ylim=[None, 6000])
    plt.show()


def combine_many_features_in_a_classifier(): 
    # Loop through each spectrogram
    bandwidths = []
    centroids = []

    for spec in spectrograms:
        # Calculate the mean spectral bandwidth
        this_mean_bandwidth = np.mean(lr.feature.spectral_bandwidth(S=spec))
        # Calculate the mean spectral centroid
        this_mean_centroid = np.mean(lr.feature.spectral_centroid(S=spec))
        # Collect the values
        bandwidths.append(this_mean_bandwidth)  
        centroids.append(this_mean_centroid)

    # Create X and y arrays
    X = np.column_stack([means, stds, maxs, tempo_mean, tempo_max, tempo_std, bandwidths, centroids])
    y = labels.reshape([-1, 1])

    # Fit the model and score on testing data
    percent_score = cross_val_score(model, X, y, cv=5)
    print(np.mean(percent_score))


if __name__ == "__main__":
    normal_filepath = "data/archive/set_b/normal__*.wav"
    abnormal_filepath = "data/archive/set_b/extrastole__*.wav"
    normal, sfreq, time = load_heartbeats_audio_data(normal_filepath, 1)
    audio = normal.iloc[:, 0].to_numpy()
    spec = spectrograms_of_heartbeat_audio(audio, time, sfreq)
    engineering_spectral_features(spec, time)
