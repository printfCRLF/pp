import pandas as pd
import matplotlib.pyplot as plt 
from pandas.io.json import json_normalize

api_url = "https://api.yelp.com/v3/businesses/search"
params = {'location': 'NYC', 'sort_by': 'rating', 'term': 'cafe'}
api_key = "abcd"
headers = {"Authorization": "Bearer {}".format(api_key)}

def load_json_data(): 
    pop_in_shelters = pd.read_json("dhs_daily_report.json")
    print(pop_in_shelters.describe())
import requests 

def work_with_json_orientations(): 
    try:
        df = pd.read_json("dhs_report_reformatted.json", orient="split")
        
        df["date_of_census"] = pd.to_datetime(df["date_of_census"])
        df.plot(x="date_of_census", 
                y="total_individuals_in_shelter")
        plt.show()
        
    except ValueError:
        print("pandas could not parse the JSON.")

def working_with_api(): 
    response = requests.get(api_url, headers=headers, params=params)
    data = response.json()
    print(response)
    cafes = pd.DataFrame(data["businesses"])
    print(cafes.head())

def working_with_nested_json(): 
    response = requests.get(api_url, headers=headers, params=params)
    data = response.json()  
    flat_cafes = json_normalize(data["businesses"],
                                sep="_",
                                record_path="categories",
                                meta=["name", 
                                    "alias",  
                                    "rating",
                                    ["coordinates", "latitude"], 
                                    ["coordinates", "longitude"]],
                                meta_prefix="biz_")
    # View the data
    print(flat_cafes.head())

def combining_multiple_datasets(): 
    # Merge crosswalk into cafes on their zip code fields
    cafes = pd.DataFrame()
    crosswalk = pd.DataFrame()
    pop_data = pd.DataFrame()
    
    cafes_with_pumas = cafes.merge(crosswalk,
                            left_on="location_zip_code",
                            right_on="zipcode")

    # Merge pop_data into cafes_with_pumas on puma field
    cafes_with_pop = cafes_with_pumas.merge(pop_data, 
                        left_on="puma",
                        right_on="puma")

    # View the data
    print(cafes_with_pop.head())

#working_with_api()
working_with_nested_json()

