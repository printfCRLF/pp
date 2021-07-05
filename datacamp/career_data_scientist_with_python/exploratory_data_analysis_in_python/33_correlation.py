import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from empiricaldist import Pmf, Cdf
from data import load_brfss_data


def computing_correlations(brfss):
    # Select columns
    columns = ['AGE', 'INCOME2', '_VEGESU1']
    subset = brfss[columns]

    # Compute the correlation matrix
    print(subset.corr())


brfss = load_brfss_data()
computing_correlations(brfss)
