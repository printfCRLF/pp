import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Dates = pd.date_range('20130301', periods=6)
Df = pd.DataFrame(np.random.randn(6, 4), index=Dates, columns=list('ABCD'))
Df.loc[:, 'D'] = np.array([5] * len(Df))

def stats():
    print(Df)
    print(Df.mean())
    print(Df.mean(1))

    # axis along which the means are computed. 0 along the indices and 1 along the columns
    # +------------+---------+--------+
    # |     | A         | B         |
    # +------------+---------+---------
    # | 0   | 0.626386  | 1.52325   | ----axis = 1 - ---->
    # +------------+---------+--------+
    # |     |
    #       | axis = 0 |
    #       ↓         ↓
    return

def apply():

    print(Df)

    # cumulative sum
    print(Df.apply(func=np.cumsum, axis=0))

    print(Df.apply(lambda x: x.max() - x.min()))
    return

#stats()
apply()
