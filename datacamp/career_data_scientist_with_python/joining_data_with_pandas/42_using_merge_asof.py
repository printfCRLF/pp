import pandas as pd
import matplotlib.pyplot as plt


def compare_stocks(jpm, wells, bac):
    # Use merge_asof() to merge jpm and wells
    jpm_wells = pd.merge_asof(jpm, wells, on="date_time", suffixes=(
        "", "_wells"), direction="nearest")

    # Use merge_asof() to merge jpm_wells and bac
    jpm_wells_bac = pd.merge_asof(jpm_wells, bac, "date_time", suffixes=(
        "_jpm", "_bac"), direction="nearest")

    # Compute price diff
    price_diffs = jpm_wells_bac.diff()

    # Plot the price diff of the close of jpm, wells and bac only
    price_diffs.plot(y=["close_jpm", "close_wells", "close_bac"])
    plt.show()


def is_recession(gdp, recession):
    # Merge gdp and recession on date using merge_asof()
    gdp_recession = pd.merge_asof(gdp, recession, on="date")

    # Create a list based on the row value of gdp_recession['econ_status']
    is_recession = ['r' if s ==
                    'recession' else 'g' for s in gdp_recession['econ_status']]

    # Plot a bar chart of gdp_recession
    gdp_recession.plot(kind="bar", y="gdp", x="date",
                       color=is_recession, rot=90)
    plt.show()
