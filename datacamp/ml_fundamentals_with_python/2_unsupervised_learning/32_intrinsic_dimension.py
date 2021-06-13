from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt
import data


def the_first_principal_component(grains):
    # Make a scatter plot of the untransformed points
    plt.scatter(grains[:, 0], grains[:, 1])

    # Create a PCA instance: model
    model = PCA()

    # Fit model to points
    model.fit(grains)

    # Get the mean of the grain samples: mean
    mean = model.mean_

    # Get the first principal component: first_pc
    first_pc = model.components_[0, :]

    # Plot first_pc as an arrow, starting at mean
    plt.arrow(mean[0], mean[1], first_pc[0],
              first_pc[1], color='red', width=0.01)

    # Keep axes on same scale
    plt.axis('equal')
    plt.show()


def variance_of_the_pca_features(samples):
    # Create scaler: scaler
    scaler = StandardScaler()

    # Create a PCA instance: pca
    pca = PCA()

    # Create pipeline: pipeline
    pipeline = make_pipeline(scaler, pca)

    # Fit the pipeline to 'samples'
    pipeline.fit(samples)

    # Plot the explained variances
    features = range(pca.n_components_)
    plt.bar(features, pca.explained_variance_)
    plt.xlabel('PCA feature')
    plt.ylabel('variance')
    plt.xticks(features)
    plt.show()


# grains = data.load_grain_width_length_from_file()
# the_first_principal_component(grains)
fish_samples, _ = data.load_fish_data()
variance_of_the_pca_features(fish_samples)
