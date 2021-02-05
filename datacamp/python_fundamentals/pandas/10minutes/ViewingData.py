import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Dates = pd.date_range('20130301', periods=6)
Df = pd.DataFrame(np.random.randn(6, 4), index=Dates, columns=list('ABCD'))


def viewingData():
    # see the top and bottom rows of the frame
    print(Df.head())
    print(Df.tail(3))

    # display the index, columns, and the underlying numpy data
    print(Df.index)
    print(Df.columns)
    print(Df.values)

    # Describe shows a quick statistic summary of your data
    print(Df.describe())

    # Transposing your data
    print(Df.T)
    return

viewingData()