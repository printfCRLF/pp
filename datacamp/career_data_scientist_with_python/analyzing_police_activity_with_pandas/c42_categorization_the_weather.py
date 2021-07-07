import pandas as pd
import matplotlib.pyplot as plt
from pandas.api.types import CategoricalDtype
from c1_preparing_data_for_analysis import prepare_data_for_following_chapters
from data import load_weather_data


def counting_bad_weather_conditions(weather):
    # Copy 'WT01' through 'WT22' to a new DataFrame
    WT = weather.loc[:, "WT01":"WT22"]

    # Calculate the sum of each row in 'WT'
    weather['bad_conditions'] = WT.sum(axis="columns")

    # Replace missing values in 'bad_conditions' with '0'
    weather['bad_conditions'] = weather.bad_conditions.fillna(0).astype('int')

    # Create a histogram to visualize 'bad_conditions'
    weather['bad_conditions'].plot(kind="hist")

    # Display the plot
    plt.show()

    return weather


def rating_the_weather_condition(weather):
    # Count the unique values in 'bad_conditions' and sort the index
    print(weather.bad_conditions.value_counts().sort_index())

    # Create a dictionary that maps integers to strings
    mapping = {0: 'good', 1: 'bad', 2: 'bad', 3: 'bad', 4: 'bad',
               5: 'worse', 6: 'worse', 7: 'worse', 8: 'worse', 9: 'worse'}

    # Convert the 'bad_conditions' integers to strings using the 'mapping'
    weather['rating'] = weather.bad_conditions.map(mapping)

    # Count the unique values in 'rating'
    print(weather.rating.value_counts())

    return weather


def changing_data_type_to_category(weather):
    # Create a list of weather ratings in logical order
    cats = ['good', 'bad', 'worse']
    cat_type = CategoricalDtype(categories=cats, ordered=True)

    # Change the data type of 'rating' to category
    weather['rating'] = weather.rating.astype(cat_type)

    # Examine the head of 'rating'
    print(weather['rating'].head())

    return weather


def prepare_weather_dataset():
    weather = load_weather_data()
    weather = counting_bad_weather_conditions(weather)
    weather = rating_the_weather_condition(weather)
    return changing_data_type_to_category(weather)


