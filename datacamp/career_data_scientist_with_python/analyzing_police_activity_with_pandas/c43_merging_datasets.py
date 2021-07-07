import pandas as pd
import matplotlib.pyplot as plt
from pandas.api.types import CategoricalDtype
from c1_preparing_data_for_analysis import prepare_data_for_following_chapters
from c42_categorization_the_weather import prepare_weather_dataset


def merging_datasets():
    ri = prepare_data_for_following_chapters()
    weather = prepare_weather_dataset()

    # Reset the index of 'ri'
    ri.reset_index(inplace=True)

    # Examine the head of 'ri'
    print(ri.head())

    # Create a DataFrame from the 'DATE' and 'rating' columns
    weather_rating = weather[['DATE', 'rating']]

    # Examine the head of 'weather_rating'
    print(weather_rating.head())

    # Examine the shape of 'ri'
    print(ri.shape)

    # Merge 'ri' and 'weather_rating' using a left join
    ri_weather = pd.merge(left=ri, right=weather_rating,
                          left_on='stop_date', right_on='DATE', how='left')

    # Examine the shape of 'ri_weather'
    print(ri_weather.shape)

    # Set 'stop_datetime' as the index of 'ri_weather'
    ri_weather.set_index('stop_datetime', inplace=True)

    return ri_weather
