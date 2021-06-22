import matplotlib.pyplot as plt
from data import load_movies, load_movie_to_genres, load_crews, load_casts


def find_scifi_only_movies(movies, movie_to_genres):
    action_movies = movie_to_genres[movie_to_genres["genre"] == "Action"]
    scifi_movies = movie_to_genres[movie_to_genres["genre"]
                                   == "Science Fiction"]

    # Merge action_movies to the scifi_movies with right join
    action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right',
                                       suffixes=('_act', '_sci'))

    # From action_scifi, select only the rows where the genre_act column is null
    scifi_only = action_scifi[action_scifi['genre_act'].isnull()]

    # Merge the movies and scifi_only tables with an inner join
    movies_and_scifi_only = movies.merge(
        scifi_only, left_on="id", right_on="movie_id", how="inner")

    # Print the first few rows and shape of movies_and_scifi_only
    print(movies_and_scifi_only.head())
    print(movies_and_scifi_only.shape)


def popular_genres(movies, movie_to_genres):
    pop_movies = movies.sort_values("popularity", ascending=False)[:10]
    # Use right join to merge the movie_to_genres and pop_movies tables
    genres_movies = movie_to_genres.merge(pop_movies, how='right',
                                          left_on="movie_id",
                                          right_on="id")

    # Count the number of genres
    genre_count = genres_movies.groupby('genre').agg({'id': 'count'})

    # Plot a bar chart of the genre_count
    genre_count.plot(kind='bar')
    plt.show()


def actors_played_in_only_one_movie(movies, casts):
    iron_1_mid = movies[movies["title"] == "Iron Man"].iloc[0, 0]
    iron_2_mid = movies[movies["title"] == "Iron Man 2"].iloc[0, 0]

    iron_1_actors = casts[casts["movie_id"] == iron_1_mid]
    iron_2_actors = casts[casts["movie_id"] == iron_2_mid]

    # Merge iron_1_actors to iron_2_actors on id with outer join using suffixes
    iron_1_and_2 = iron_1_actors.merge(iron_2_actors,
                                       on="id",
                                       how="outer",
                                       suffixes=["_1", "_2"])

    # Create an index that returns true if name_1 or name_2 are null
    m = ((iron_1_and_2['name_1'].isnull()) |
         (iron_1_and_2['name_2'].isnull()))

    # Print the first few rows of iron_1_and_2
    print(iron_1_and_2[m].head())


movies = load_movies()
movie_to_genres = load_movie_to_genres()
# find_scifi_only_movies(movies, movie_to_genres)

# popular_genres(movies, movie_to_genres)

casts = load_casts()
actors_played_in_only_one_movie(movies, casts)
