import pandas as pd
import matplotlib.pyplot as plt
from data import load_sp500, load_gdp, load_population


def correlation_between_gdp_and_sp500(gdp, sp500):
    is_usa = gdp["country code"] == "USA"
    year_2010_through_2018 = (gdp["year"] >= 2010) & (gdp["year"] <= 2018)
    us_gdp = gdp[is_usa & year_2010_through_2018]

    # Use merge_ordered() to merge gdp and sp500, interpolate missing value
    gdp_sp500 = pd.merge_ordered(us_gdp, sp500, left_on='year', right_on='date',
                                 how='left',  fill_method='ffill')

    # Subset the gdp and returns columns
    gdp_returns = gdp_sp500[["gdp", "returns"]]

    # Print gdp_returns correlation
    print(gdp_returns.corr())


def philips_curve(inflation, unemployment):
    # Use merge_ordered() to merge inflation, unemployment with inner join
    inflation_unemploy = pd.merge_ordered(
        inflation, unemployment, on="date", how="inner")

    # Print inflation_unemploy
    print(inflation_unemploy)

    # Plot a scatter plot of unemployment_rate vs cpi of inflation_unemploy
    inflation_unemploy.plot(x="unemployment_rate", y="cpi", kind="scatter")
    plt.show()


def merge_ordered(gdp, pop):
    # Merge gdp and pop on date and country with fill and notice rows 2 and 3
    ctry_date = pd.merge_ordered(
        gdp, pop, on=["date", "country"], fill_method='ffill')

    # Print ctry_date
    print(ctry_date)

    # Merge gdp and pop on country and date with fill
    date_ctry = pd.merge_ordered(
        gdp, pop, on=["country", "date"], fill_method="ffill")

    # Print date_ctry
    print(date_ctry)


gdp = load_gdp()
sp500 = load_sp500()
correlation_between_gdp_and_sp500(gdp, sp500)
