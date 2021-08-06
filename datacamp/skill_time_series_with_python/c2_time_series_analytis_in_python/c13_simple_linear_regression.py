import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def looking_at_regression_r_squared():
    x = np.random.normal(loc=0.0, scale=1.0, size=1000)
    y = np.random.normal(loc=0.0, scale=1.0, size=1000)
    # a, b = -0.9, -0.005
    # y = a * x + b
    x = pd.Series(x)
    y = pd.Series(y)

    # Compute correlation of x and y
    correlation = x.corr(y)
    print("The correlation between x and y is %4.2f" % (correlation))

    # Convert the Series x to a DataFrame and name the column x
    dfx = pd.DataFrame(x, columns=['x'])

    # Add a constant to the DataFrame dfx
    dfx1 = sm.add_constant(dfx)

    # Regress y on dfx1
    result = sm.OLS(y, dfx1).fit()

    # Print out the results and look at the relationship between R-squared and the correlation above
    print(result.summary())

    plt.scatter(x, y)
    plt.show()


if __name__ == "__main__":
    sns.set()
    looking_at_regression_r_squared()
