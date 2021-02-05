import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Dates = pd.date_range('20130301', periods=6)
Df = pd.DataFrame(np.random.randn(6, 4), index=Dates, columns=list('ABCD'))

def selection():

    def getting() :
        # selecting a single column, which yields a Series, equivalent to df.A
        print(Df['A'])

        # selecting via [], which slices the rows
        print(Df[0: 3])
        return

    def selectionByLabel():
        # getting a cross section using a label
        print(Df.loc[Dates[0]])

        # selecting on a multi-axis by label
        print(Df.loc[:, ['A', 'B']])

        # showing label slicing, both endpoints are included
        print(Df.loc['20130302': '20130304', ['A', 'B']])

        # reduction in the dimensions of the returned object
        print(Df.loc['20130302', ['A', 'B']])

        # getting a scalar value
        print(Df.loc[Dates[0], 'A'])
        print(Df.at[Dates[0], 'A'])
        return

    def selectionByPosition():
        # select via the position of the passed integers
        print(Df.iloc[3])
        print(Df.iloc[3:5, 0: 2])
        print(Df.iloc[[1, 2, 3], [0, 2]])

        # for slicing rows explicitly
        print(Df.iloc[1:3, :])

        # slicing columns explicitly
        print(Df.iloc[:, 1:3])
        return

    def booleanIndexing():
        print(Df)
        # boolean filter on a single column
        print(Df[Df.A > 0])

        # boolean filter on the entire df
        print(Df[Df > 0])

        # isin()
        df2 = Df.copy()
        df2['E'] = ['one', 'one','two','three','four','three']
        twoAndFour = df2[df2['E'].isin(['two', 'four'])]
        print(twoAndFour)

        return

    def setting():
        # different setting methods
        s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))
        Df.at[Dates[0], 'A'] = 0
        Df.iat[0, 1] = 0
        Df.loc[:, 'D'] = np.array([5] * len(Df))
        print(Df)

        # a where operation with setting
        df2 = Df.copy()
        df2[df2 > 0] = -df2
        print(df2)

        return

    #getting()
    #selectionByLabel()
    #selectionByPosition()
    #booleanIndexing()
    setting()

    return

selection()
