import pandas as pd
import matplotlib.pyplot as plt
from c1_preparing_data_for_analysis import prepare_data_for_following_chapters


def tallying_violations_by_district(ri):
    # Create a frequency table of districts and violations
    print(pd.crosstab(ri.district, ri.violation))

    # Save the frequency table as 'all_zones'
    all_zones = pd.crosstab(ri.district, ri.violation)

    # Select rows 'Zone K1' through 'Zone K3'
    print(all_zones.loc["Zone K1": "Zone K3"])

    # Save the smaller table as 'k_zones'
    k_zones = all_zones.loc["Zone K1": "Zone K3"]

    # Create a stacked bar plot of 'k_zones'
    k_zones.plot(kind="bar", stacked=True)

    # Display the plot
    plt.show()


ri = prepare_data_for_following_chapters()
tallying_violations_by_district(ri)
