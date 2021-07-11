import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from util import ecdf, draw_bs_reps, draw_bs_pairs_linreg
from data import rainfall, nohitter_times, illiteracy, fertility


def visualizing_bootstrap_samples():
    for _ in range(50):
        bs_sample = np.random.choice(rainfall, size=len(rainfall))
        x, y = ecdf(bs_sample)
        _ = plt.plot(x, y, marker='.', linestyle='none',
                     color='gray', alpha=0.1)

    x, y = ecdf(rainfall)
    _ = plt.plot(x, y, marker='.')
    plt.margins(0.02)
    _ = plt.xlabel('yearly rainfall (mm)')
    _ = plt.ylabel('ECDF')
    plt.show()


sns.set()
visualizing_bootstrap_samples()
