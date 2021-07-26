import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from data import load_stackoverflow_data


def what_does_your_data_look_like(so_numeric_df):
    # Create a histogram
    so_numeric_df.hist()
    plt.show()

    # Create a boxplot of two columns
    so_numeric_df[['Age', 'Years Experience']].boxplot()
    plt.show()

    # Create a boxplot of ConvertedSalary
    so_numeric_df[["ConvertedSalary"]].boxplot()
    plt.show()


def what_does_your_data_look_like2(so_numeric_df):
    # Plot pairwise relationships
    sns.pairplot(so_numeric_df)
    # Show plot
    plt.show()

    # Print summary statistics
    print(so_numeric_df.describe())


df = load_stackoverflow_data()
so_numeric_df = df[["ConvertedSalary", "Age", "Years Experience"]]
# what_does_your_data_look_like(so_numeric_df)
what_does_your_data_look_like2(so_numeric_df)
