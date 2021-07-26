import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, StandardScaler, PowerTransformer
from data import load_stackoverflow_data


def percentage_based_outlier_removal(so_numeric_df):
    # Find the 95th quantile
    quantile = so_numeric_df['ConvertedSalary'].quantile(0.95)
    # Trim the outliers
    trimmed_df = so_numeric_df[so_numeric_df['ConvertedSalary'] < quantile]
    # The original histogram
    so_numeric_df[['ConvertedSalary']].hist()
    plt.show()
    plt.clf()
    # The trimmed histogram
    trimmed_df[['ConvertedSalary']].hist()
    plt.show()


def statistical_outlier_removal(so_numeric_df):
    # Find the mean and standard dev
    std = so_numeric_df['ConvertedSalary'].std()
    mean = so_numeric_df['ConvertedSalary'].mean()
    # Calculate the cutoff
    cut_off = std * 3
    lower, upper = mean - cut_off, mean + cut_off
    # Trim the outliers
    trimmed_df = so_numeric_df[(so_numeric_df['ConvertedSalary'] < upper) & (
        so_numeric_df['ConvertedSalary'] > lower)]
    # The trimmed box plot
    trimmed_df[['ConvertedSalary']].boxplot()
    plt.show()


df = load_stackoverflow_data()
so_numeric_df = df[["ConvertedSalary", "Age", "Years Experience"]]
# percentage_based_outlier_removal(so_numeric_df)
statistical_outlier_removal(so_numeric_df)
