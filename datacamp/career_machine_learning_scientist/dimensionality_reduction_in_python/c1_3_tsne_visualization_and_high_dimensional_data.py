import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from data import load_ansur_ii_male_data, load_ansur_ii_female_data


def fitting_tsne_to_ansur_data(df):
    # Non-numerical columns in the dataset
    non_numeric = ['Branch', 'Gender', 'Component', "weight_kg",
                   "stature_m", "BMI", "BMI_class", "Height_class"]

    # Drop the non-numerical columns from df
    df_numeric = df.drop(non_numeric, axis=1)

    # Create a t-SNE model with learning rate 50
    m = TSNE(learning_rate=50)

    # Fit and transform the t-SNE model on the numeric dataset
    tsne_features = m.fit_transform(df_numeric)
    print(tsne_features.shape)

    return tsne_features


def tsne_visualization_of_dimensionality(df, tsne_features):
    df["x"] = tsne_features[:, 0]
    df["y"] = tsne_features[:, 1]
    # Color the points according to Army Component
    sns.scatterplot(x="x", y="y", hue="Component", data=df)
    # Show the plot
    plt.show()

    # Color the points by Army Branch
    sns.scatterplot(x="x", y="y", hue="Branch", data=df)
    plt.show()

    # Color the points by Gender
    sns.scatterplot(x="x", y="y", hue="Gender", data=df)
    plt.show()


ansur_ii_male = load_ansur_ii_male_data()
ansur_ii_female = load_ansur_ii_female_data()
df = pd.concat([ansur_ii_male, ansur_ii_female])
tsne_features = fitting_tsne_to_ansur_data(df)
tsne_visualization_of_dimensionality(df, tsne_features)
