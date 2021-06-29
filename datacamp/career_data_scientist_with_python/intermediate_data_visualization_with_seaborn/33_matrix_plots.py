import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data import load_daily_show_guests_data


def creating_heat_map(df):
    # Create a crosstab table of the data
    pd_crosstab = pd.crosstab(df["Group"], df["YEAR"])
    print(pd_crosstab)

    # Plot a heatmap of the table
    sns.heatmap(pd_crosstab)

    # Rotate tick marks for visibility
    plt.yticks(rotation=0)
    plt.xticks(rotation=90)

    plt.show()


def customizing_heat_map(df): 
    # Create the crosstab DataFrame
    pd_crosstab = pd.crosstab(df["Group"], df["YEAR"])

    # Plot a heatmap of the table with no color bar and using the BuGn palette
    sns.heatmap(pd_crosstab, cbar=False, cmap="BuGn", linewidths=0.3)

    # Rotate tick marks for visibility
    plt.yticks(rotation=0)
    plt.xticks(rotation=90)

    #Show the plot
    plt.show()
    plt.clf()    


df = load_daily_show_guests_data()
# creating_heat_map(df)
customizing_heat_map(df)