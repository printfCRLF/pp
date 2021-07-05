import numpy as np
import matplotlib.pyplot as plt
from data import load_nsfg_data
from util import resample_rows_weighted


def exploring_the_nsft_data(nsfg):
    # Display the number of rows and columns
    nsfg.shape

    # Display the names of the columns
    nsfg.columns

    # Select column birthwgt_oz1: ounces
    ounces = nsfg['birthwgt_oz1']

    # Print the first 5 elements of ounces
    print(ounces[:5])


def clean_a_variable(nsfg):
    # Replace the value 8 with NaN
    nsfg['nbrnaliv'].replace(8, np.nan, inplace=True)

    # Print the values and their frequencies
    print(nsfg['nbrnaliv'].value_counts())


def compute_pregnancy_length(nsfg):
    # Select the columns and divide by 100
    agecon = nsfg['agecon'] / 100
    agepreg = nsfg['agepreg'] / 100

    # Compute the difference
    preg_length = agepreg - agecon

    # Compute summary statistics
    print(preg_length.describe())


def make_a_histogram(nsfg):
    agecon = nsfg['agecon'] / 100

    # Plot the histogram
    plt.hist(agecon, bins=20, histtype='step')

    # Label the axes
    plt.xlabel('Age at conception')
    plt.ylabel('Number of pregnancies')

    # Show the figure
    plt.show()


def compute_the_birth_weight(nsfg):
    # Resample the data
    nsfg = resample_rows_weighted(nsfg, 'wgt2013_2015')

    # Clean the weight variables
    pounds = nsfg['birthwgt_lb1'].replace([98, 99], np.nan)
    ounces = nsfg['birthwgt_oz1'].replace([98, 99], np.nan)

    # Compute total birth weight
    birth_weight = pounds + ounces/16

    # Create a Boolean Series for full-term babies
    full_term = nsfg["prglngth"] >= 37

    # Select the weights of full-term babies
    full_term_weight = birth_weight[full_term]

    # Compute the mean weight of full-term babies
    print(full_term_weight.mean())


def filter_on_single_vs_multiple_birth(nsfg):
    # Resample the data
    nsfg = resample_rows_weighted(nsfg, 'wgt2013_2015')

    # Clean the weight variables
    pounds = nsfg['birthwgt_lb1'].replace([98, 99], np.nan)
    ounces = nsfg['birthwgt_oz1'].replace([98, 99], np.nan)

    # Compute total birth weight
    birth_weight = pounds + ounces/16

    # Filter full-term babies
    full_term = nsfg['prglngth'] >= 37

    # Filter single births
    single = nsfg["nbrnaliv"] == 1

    # Compute birth weight for single full-term babies
    single_full_term_weight = birth_weight[full_term & single]
    print('Single full-term mean:', single_full_term_weight.mean())

    # Compute birth weight for multiple full-term babies
    mult_full_term_weight = birth_weight[full_term & ~single]
    print('Multiple full-term mean:', mult_full_term_weight.mean())


nsfg = load_nsfg_data()
# exploring_the_nsft_data(nsfg)
# clean_a_variable(nsfg)
# compute_pregnancy_length(nsfg)
# make_a_histogram(nsfg)
compute_the_birth_weight(nsfg)
filter_on_single_vs_multiple_birth(nsfg)
