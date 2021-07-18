from fuzzywuzzy import process
import pandas as pd 
import recordlinkage

restaurants = pd.read_csv('data/restaurants_L2_dirty.csv')
restaurants_new = pd.read_csv('data/restaurants_L2.csv')

def comparing_strings(): 
    unique_types = restaurants['cuisine_type'].unique()
    print(process.extract('asian', unique_types, limit = len(unique_types)))
    print(process.extract('american', unique_types, limit = len(unique_types)))
    print(process.extract('italian', unique_types, limit = len(unique_types)))

   # Iterate through categories
    for cuisine in categories:  
        # Create a list of matches, comparing cuisine with the cuisine_type column
        matches = process.extract(cuisine, restaurants['cuisine_type'], limit=len(restaurants.cuisine_type))

        # Iterate through the list of matches
        for match in matches:
            # Check whether the similarity score is greater than or equal to 80
            if match[1] >= 80:
                # If it is, select all rows where the cuisine_type is spelled this way, and set them to the correct cuisine
                restaurants.loc[restaurants['cuisine_type'] == match[0]] = cuisine
        
    # Inspect the final result
    restaurants['cuisine_type'].unique()

def generating_pairs_linkage_data(): 
    indexer = recordlinkage.Index()
    indexer.block('cuisine_type')
    pairs = indexer.index(restaurants, restaurants_new)

    comp_cl = recordlinkage.Compare()
    comp_cl.exact('city', 'city', label='city')
    comp_cl.exact('cuisine_type', 'cuisine_type', label='cuisine_type')
    comp_cl.string('name', 'name', label='name', threshold = 0.8) 

    potential_matches = comp_cl.compute(pairs, restaurants, restaurants_new)
    print(potential_matches)

    matches = potential_matches[potential_matches.sum(axis = 1) >= 3]
    matching_indices = matches.index.get_level_values(1)
    non_dup = restaurants_new[~restaurants_new.index.isin(matching_indices)]
    full_restaurants = restaurants.append(non_dup)
    print(full_restaurants)

#comparing_strings()
generating_pairs()