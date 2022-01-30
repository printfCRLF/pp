
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
from data import load_c1_data
from util import get_date_int
from c13_cohort_metrics import assign_monthly_acquisition_cohort, calculate_time_offset_in_months,  calculate_retention, calculate_average_price


def visualize_average_quantity_metrics(retention):
    # Initialize an 8 by 6 inches plot figure
    plt.figure(figsize=(8, 6))

    # Add a title
    plt.title('Retention by Monthly Cohorts')

    y_tick_labels = retention.index.to_series().astype("string")

    # Create the heatmap
    sns.heatmap(data=retention, annot=True,
                cmap='Blues', yticklabels=y_tick_labels)
    plt.show()


if __name__ == "__main__":
    online = load_c1_data()
    assign_monthly_acquisition_cohort(online)
    calculate_time_offset_in_months(online)
    retention = calculate_retention(online)
    visualize_average_quantity_metrics(retention)
