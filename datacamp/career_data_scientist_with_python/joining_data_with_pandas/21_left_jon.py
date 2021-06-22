from data import load_movies, load_taglines


def enriching_a_dataset(movies, taglines):
    toy_story = movies[movies["title"].str.contains("Toy Story")]
    # Merge the toy_story and taglines tables with a left join
    toystory_tag = toy_story.merge(taglines, on='id', how='left')

    # Print the rows and shape of toystory_tag
    print(toystory_tag)
    print(toystory_tag.shape)

    # Merge the toy_story and taglines tables with a inner join
    toystory_tag = toy_story.merge(taglines, on="id")

    # Print the rows and shape of toystory_tag
    print(toystory_tag)
    print(toystory_tag.shape)


movies = load_movies()
taglines = load_taglines()
enriching_a_dataset(movies, taglines)
