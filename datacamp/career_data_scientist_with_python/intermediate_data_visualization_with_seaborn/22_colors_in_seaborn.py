import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data import load_fy18_4050_data


def color_codes(df):
    # Set style, enable color code, and create a magenta distplot
    sns.set(color_codes=True)
    sns.distplot(df['fmr_3'], color='m')
    plt.show()


def using_default_palettes(df):
    # Loop through differences between bright and colorblind palettes
    for p in ['bright', 'colorblind']:
        sns.set_palette(p)
        sns.distplot(df['fmr_3'])
        plt.show()

        # Clear the plots
        plt.clf()


def creating_custom_palettes():
    sns.palplot(sns.color_palette("Purples", 8))
    plt.show()

    sns.palplot(sns.color_palette("husl", 10))
    plt.show()

    sns.palplot(sns.color_palette("coolwarm", 6))
    plt.show()


housing_data = load_fy18_4050_data()
# color_codes(housing_data)
# using_default_palettes(housing_data)

creating_custom_palettes()
