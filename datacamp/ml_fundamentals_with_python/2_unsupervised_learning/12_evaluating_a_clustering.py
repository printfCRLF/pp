import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans


def load_grains_data():
    df = pd.read_csv('data/Grains/seeds.csv')
    samples = df.iloc[:, :-1]
    varieties = df.iloc[:, -1].values
    i1 = len(varieties[varieties == 1])
    i2 = len(varieties[varieties == 2])
    i3 = len(varieties[varieties == 3])
    new_varieties = ['Kama wheat'] * i1 + ['Rosa wheat'] * i2 + ['Canadian wheat'] * i3
    return samples, new_varieties


def how_many_clusters_of_grain(samples):
    ks = range(1, 10)
    inertias = []

    for k in ks:
        model = KMeans(n_clusters=k)
        model.fit(samples)
        inertias.append(model.inertia_)

    plt.plot(ks, inertias, marker='o', linestyle='-')
    plt.xlabel('number of clusters')
    plt.ylabel('inertia')
    plt.xticks(ks)
    plt.show()


def evaluating_grain_clustering(samples, varieties):
    # Create a KMeans model with 3 clusters: model
    model = KMeans(n_clusters=3)

    # Use fit_predict to fit model and obtain cluster labels: labels
    labels = model.fit_predict(samples)

    # Create a DataFrame with labels and varieties as columns: df
    df = pd.DataFrame({'labels': labels, 'varieties': varieties})

    # Create crosstab: ct
    ct = pd.crosstab(df['labels'], df['varieties'])

    # Display ct
    print(ct)


samples, varieties = load_grains_data()
#how_many_clusters_of_grain(samples)
evaluating_grain_clustering(samples, varieties)
