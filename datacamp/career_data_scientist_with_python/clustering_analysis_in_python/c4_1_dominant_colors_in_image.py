import matplotlib.image as img
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.cluster.vq import kmeans, vq, whiten


def extract_rgb_values_from_image():
    # Read batman image and print dimensions
    batman_image = img.imread('data/batman.jpg')
    print(batman_image.shape)

    r, g, b = [], [], []
    # Store RGB values of all pixels in lists r, g and b
    for row in batman_image:
        for pixel in row:
            temp_r, temp_g, temp_b = pixel
            r.append(temp_r)
            g.append(temp_g)
            b.append(temp_b)

    batman_df = pd.DataFrame({"red": r, "green": g, "blue": b})
    batman_df["scaled_red"] = whiten(batman_df["red"])
    batman_df["scaled_green"] = whiten(batman_df["green"])
    batman_df["scaled_blue"] = whiten(batman_df["blue"])
    return batman_df


def how_many_dominant_colors(batman_df):
    distortions = []
    num_clusters = range(1, 7)

    # Create a list of distortions from the kmeans function
    for i in num_clusters:
        cluster_centers, distortion = kmeans(
            batman_df[["scaled_red", "scaled_green", "scaled_blue"]], i)
        distortions.append(distortion)

    # Create a data frame with two lists, num_clusters and distortions
    elbow_plot = pd.DataFrame({"num_clusters": num_clusters,
                               "distortions": distortions})

    # Create a line plot of num_clusters and distortions
    sns.lineplot(x="num_clusters", y="distortions", data=elbow_plot)
    plt.xticks(num_clusters)
    plt.show()


def display_dominant_colors(batman_df):
    cluster_centers, _ = kmeans(
        batman_df[["scaled_red", "scaled_green", "scaled_blue"]], 3)

    # Get standard deviations of each color
    r_std, g_std, b_std = batman_df[['red', 'green', 'blue']].std()
    colors = []

    for cluster_center in cluster_centers:
        scaled_r, scaled_g, scaled_b = cluster_center
        # Convert each standardized value to scaled value
        colors.append((
            scaled_r * r_std / 255,
            scaled_g * g_std / 255,
            scaled_b * b_std / 255
        ))

    # Display colors of cluster centers
    plt.imshow([colors])
    plt.show()


sns.set()
batman_df = extract_rgb_values_from_image()
cluster_centers = how_many_dominant_colors(batman_df)
display_dominant_colors(batman_df)
