import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Dates = pd.date_range('20130301', periods=6)
Df = pd.DataFrame(np.random.randn(6, 4), index=Dates, columns=list('ABCD'))

def objectCreation():
    # series
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    print(s)

    # DataFrame 123

    dates2 = pd.date_range('20130301', periods = 6)
    print(dates2)

    # Creating a DataFrame by pssing a numpy array, with a datetime index and labeled columns
    df2 = pd.DataFrame(np.random.randn(6, 4), index=dates2, columns=list('ABCD'))
    print(df2)

    # Creating a DataFrame by passing a dict of objeccts that can be converted to series-like
    df2 = pd.DataFrame({'A': 1.,
                        'B': pd.Timestamp('20130102'),
                        'C': pd.Series(1, index = list(range(4)), dtype='float32'),
                        'D': np.array([3] * 4, dtype='int32'),
                        'E': pd.Categorical(["test", "train", "test", "train"]),
                        'F': 'foo'})
    print(df2)
    return

objectCreation()