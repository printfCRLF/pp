import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from data import load_gss_data


def making_predications(gss):
    # Run a regression model with educ, educ2, age, and age2
    gss['educ2'] = gss["educ"] ** 2
    gss['age2'] = gss["age"] ** 2
    results = smf.ols('realinc ~ educ + educ2 + age + age2', data=gss).fit()

    # Make the DataFrame
    df = pd.DataFrame()
    df['educ'] = np.linspace(0, 20)
    df['age'] = 30
    df['educ2'] = df['educ']**2
    df['age2'] = df['age']**2

    # Generate and plot the predictions
    pred = results.predict(df)
    print(pred.head())

    return results, df


def visualizing_predictions(results, df):
    # Plot mean income in each age group
    plt.clf()
    grouped = gss.groupby('educ')
    mean_income_by_educ = grouped['realinc'].mean()
    plt.plot(mean_income_by_educ, 'o', alpha=0.5)

    # Plot the predictions
    pred = results.predict(df)
    plt.plot(df["educ"], pred, label='Age 30')

    # Label axes
    plt.xlabel('Education (years)')
    plt.ylabel('Income (1986 $)')
    plt.legend()
    plt.show()


gss = load_gss_data()
results, df = making_predications(gss)
visualizing_predictions(results, df)
