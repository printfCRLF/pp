import pandas as pd
import matplotlib.pyplot as plt
from c1_preparing_data_for_analysis import prepare_data_for_following_chapters


def plotting_drug_related_stops(ri): 
    # Calculate the annual rate of drug-related stops
    print(ri.drugs_related_stop.resample("A").mean())

    # Save the annual rate of drug-related stops
    annual_drug_rate = ri.drugs_related_stop.resample("A").mean()

    # Create a line plot of 'annual_drug_rate'
    annual_drug_rate.plot()

    # Display the plot
    plt.show()    

    # Calculate and save the annual search rate
    annual_search_rate = ri.search_conducted.resample("A").mean()

    # Concatenate 'annual_drug_rate' and 'annual_search_rate'
    annual = pd.concat([annual_drug_rate, annual_search_rate], axis='columns')

    # Create subplots from 'annual'
    annual.plot(subplots=True)

    # Display the subplots
    plt.show()

ri = prepare_data_for_following_chapters()
plotting_drug_related_stops(ri)