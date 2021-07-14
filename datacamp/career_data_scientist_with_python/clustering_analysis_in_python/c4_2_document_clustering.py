from data import load_movie_data
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.cluster.vq import kmeans


def create_tfidf_matrix(plots):
    # Initialize TfidfVectorizer
    tfidf_vectorizer = TfidfVectorizer(max_df=0.75, max_features=50,
                                       min_df=0.1)

    # Use the .fit_transform() method on the list plots
    tfidf_matrix = tfidf_vectorizer.fit_transform(plots)

    num_clusters = 2

    # Generate cluster centers through the kmeans function
    cluster_centers, distortion = kmeans(tfidf_matrix.todense(), num_clusters)

    # Generate terms from the tfidf_vectorizer object
    terms = tfidf_vectorizer.get_feature_names()

    for i in range(num_clusters):
        # Sort the terms and print top 3 terms
        center_terms = dict(zip(terms, list(cluster_centers[i])))
        sorted_terms = sorted(center_terms, key=center_terms.get, reverse=True)
        print(sorted_terms[:3])


plots = load_movie_data()
create_tfidf_matrix(plots)
