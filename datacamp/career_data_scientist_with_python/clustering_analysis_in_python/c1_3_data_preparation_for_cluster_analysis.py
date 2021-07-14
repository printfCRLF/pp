import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.vq import whiten
from data import load_fifa_18_sample_data


def normalize_basic_list_data(goals_for):
    # Use the whiten() function to standardize the data
    scaled_data = whiten(goals_for)
    print(scaled_data)
    return scaled_data


def visualize_normalized_data(goals_for, scaled_data):
    # Plot original data
    plt.plot(goals_for, label='original')
    # Plot scaled data
    plt.plot(scaled_data, label='scaled')
    # Show the legend in the plot
    plt.legend()
    # Display the plot
    plt.show()


def normalization_of_small_numbers():
    # Prepare data
    rate_cuts = [0.0025, 0.001, -0.0005, -0.001, -0.0005,
                 0.0025, -0.001, -0.0015, -0.001, 0.0005]
    # Use the whiten() function to standardize the data
    scaled_data = whiten(rate_cuts)
    # Plot original data
    plt.plot(rate_cuts, label='original')
    # Plot scaled data
    plt.plot(scaled_data, label='scaled')
    plt.legend()
    plt.show()


def fifa_normalized_data(fifa):
    # Scale wage and value
    fifa['scaled_wage'] = whiten(fifa['eur_wage'])
    fifa['scaled_value'] = whiten(fifa['eur_value'])

    # Plot the two columns in a scatter plot
    fifa.plot(x='scaled_wage', y='scaled_value', kind='scatter')
    plt.show()

    # Check mean and standard deviation of scaled values
    print(fifa[['scaled_wage', 'scaled_value']].describe())


sns.set()
# goals_for = np.array([4, 3, 2, 3, 1, 1, 2, 0, 1, 4], dtype=float)
# scaled_data = normalize_basic_list_data(goals_for)
# visualize_normalized_data(goals_for, scaled_data)
# normalization_of_small_numbers()
fifa = load_fifa_18_sample_data()
fifa_normalized_data(fifa)
