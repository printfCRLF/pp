import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from data import load_ansur_ii_male_data, load_ansur_ii_female_data, load_pokemon_data


def removing_feature_without_variance(pokemon_df):
    # Leave this list as is
    number_cols = ['HP', 'Attack', 'Defense']
    # Remove the feature without variance from this list
    non_number_cols = ['Name', 'Type 1']

    # Create a new dataframe by subselecting the chosen features
    df_selected = pokemon_df[number_cols + non_number_cols]
    # Prints the first 5 lines of the new dataframe
    print(df_selected.head())


def visually_detecting_redundant_features1(ansur_ii_male, ansur_ii_female):
    columns = ["Gender", "weight_kg", "stature_m"]
    ansur_df_1 = pd.concat([ansur_ii_male[columns].sample(
        100), ansur_ii_female[columns].sample(100)])
    ansur_df_1["body_height"] = ansur_df_1["stature_m"]

    # Create a pairplot and color the points using the 'Gender' feature
    sns.pairplot(ansur_df_1, hue="Gender", diag_kind='hist')
    # Show the plot
    plt.show()
    # Remove one of the redundant features
    reduced_df = ansur_df_1.drop("stature_m", axis=1)
    # Create a pairplot and color the points using the 'Gender' feature
    sns.pairplot(reduced_df, hue='Gender')
    # Show the plot
    plt.show()


def visually_detecting_redundant_features1(ansur_ii_male, ansur_ii_female):
    columns = ["Gender", "footlength", "headlength"]
    ansur_df_2 = pd.concat([ansur_ii_male[columns].sample(
        100), ansur_ii_female[columns].sample(100)])
    ansur_df_2["n_legs"] = 2

    # Create a pairplot and color the points using the 'Gender' feature
    sns.pairplot(ansur_df_2, hue="Gender", diag_kind='hist')
    # Show the plot
    plt.show()
    # Remove the redundant feature
    reduced_df = ansur_df_2.drop("n_legs", axis=1)
    # Create a pairplot and color the points using the 'Gender' feature
    sns.pairplot(reduced_df, hue='Gender', diag_kind='hist')
    # Show the plot
    plt.show()


sns.set()
# pokemon_df = load_pokemon_data()
# removing_feature_without_variance(pokemon_df)

ansur_ii_male = load_ansur_ii_male_data()
ansur_ii_female = load_ansur_ii_female_data()
# visually_detecting_redundant_features1(ansur_ii_male, ansur_ii_female)
visually_detecting_redundant_features1(ansur_ii_male, ansur_ii_female)
