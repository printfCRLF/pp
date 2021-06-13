# Import PCA
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy import stats
import matplotlib.pyplot as plt
import data


def dimension_reduction_of_fish_measurement(samples):
    scaler = StandardScaler()
    scaled_samples = scaler.fit_transform(samples)
    
    _ = plt.bar(range(0, 6), stats.describe(samples).mean)
    _ = plt.title("fish samples original")
    _ = plt.xlabel("features")
    _ = plt.ylabel("mean value")    
    plt.show()

    _ = plt.bar(range(0, 6), stats.describe(samples).variance)
    _ = plt.title("fish samples original")
    _ = plt.xlabel("features")
    _ = plt.ylabel("variance value")    
    plt.show()

    _ = plt.bar(range(0, 6), stats.describe(scaled_samples).mean)
    _ = plt.title("fish samples scaled")
    _ = plt.xlabel("features")
    _ = plt.ylabel("mean value")    
    plt.show()

    _ = plt.bar(range(0, 6), stats.describe(scaled_samples).variance)
    _ = plt.title("fish samples scaled")
    _ = plt.xlabel("features")
    _ = plt.ylabel("variance value")    
    plt.show()

    # Create a PCA model with 2 components: pca
    pca = PCA(n_components=2)

    # Fit the PCA instance to the scaled samples
    pca.fit(scaled_samples)

    # Transform the scaled samples: pca_features
    pca_features = pca.transform(scaled_samples)

    # Print the shape of pca_features
    print(pca_features.shape)


def tdidf_word_frequency_array():
    documents = ['cats say meow', 'dogs say woof', 'dogs chase cats']

    # Create a TfidfVectorizer: tfidf
    tfidf = TfidfVectorizer()

    # Apply fit_transform to document: csr_mat
    csr_mat = tfidf.fit_transform(documents)

    # Print result of toarray() method
    print(csr_mat.toarray())

    # Get the words: words
    words = tfidf.get_feature_names()

    # Print words
    print(words)


fish_samples, _ = data.load_fish_data()
dimension_reduction_of_fish_measurement(fish_samples)
# tdidf_word_frequency_array()
