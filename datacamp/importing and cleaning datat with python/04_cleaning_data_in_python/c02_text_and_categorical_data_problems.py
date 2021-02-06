import pandas as pd
import numpy as np

categories = 0
airlines = pd.read_csv('data/airlines_final.csv')

def create_categories(): 
    column_names = ['cleanliness', 'safety', 'satisfaction']
    data = [
        ['Clean', 'Neutral', 'Very satisfied'],
        ['Average', 'Very safe', 'Neutral'],
        ['Somewhat clean', 'Somewhat safe', 'Somewhat satisfied'],
        ['Somewhat dirty', 'Very unsafe', 'Somewhat unsatisfied'],
        ['Dirty', 'Somewhat  unsafe', 'Very unstaisfied']]
    return pd.DataFrame(data, columns = column_names)

def membership_constraints(): 
    inconsistent_columns = set(airlines['cleanliness']).difference(categories['cleanliness'])
    inconsistent_rows = airlines['cleanliness'].isin(inconsistent_columns)
    print('rows with inconsistent category\n', airlines[inconsistent_rows])
    print('rows with consistent category\n', airlines[~inconsistent_rows])

def categorical_variables(): 
        

    print('unique values of dest_region column\n', airlines['dest_region'].unique())
    print('unique values of dest_size column\n',airlines['dest_size'].unique())

    # Lower dest_region column and then replace "eur" with "europe"
    airlines['dest_region'] = airlines['dest_region'].str.lower()
    airlines['dest_region'] = airlines['dest_region'].replace({'eur':'europe'})

    # Create ranges for categories
    label_ranges = [0, 60, 180, np.inf]
    label_names = ['short', 'medium', 'long']

    # Create wait_type column
    airlines['wait_type'] = pd.cut(airlines['wait_min'], bins = label_ranges, 
                                    labels = label_names)

    # Create mappings and replace
    mappings = {'Monday':'weekday', 'Tuesday':'weekday', 'Wednesday': 'weekday', 
                'Thursday': 'weekday', 'Friday': 'weekday', 
                'Saturday': 'weekend', 'Sunday': 'weekend'}

    airlines['day_week'] = airlines['day'].replace(mappings)

def cleaning_text_data(): 
    airlines['full_name'] = airlines['full_name'].str.replace("Dr.","")
    airlines['full_name'] = airlines['full_name'].str.replace("Mr.","")
    airlines['full_name'] = airlines['full_name'].str.replace("Miss","")
    airlines['full_name'] = airlines['full_name'].str.replace("Ms.","")
    assert airlines['full_name'].str.contains('Ms.|Mr.|Miss|Dr.').any() == False

    resp_length = airlines['survey_response'].str.len()
    airlines_survey = airlines[resp_length > 40]
    assert airlines_survey['survey_response'].str.len().min() > 40
    print(airlines_survey['survey_response'])

categories = create_categories()
membership_constraints()
categorical_variables()
cleaning_text_data()
