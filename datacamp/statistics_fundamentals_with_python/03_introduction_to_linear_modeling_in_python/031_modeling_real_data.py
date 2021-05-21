import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from sklearn.linear_model import LinearRegression
from statsmodels.formula.api import ols


def linear_model_in_anthroplogy():
    df = pd.read_csv("./data/femur_data.csv")
    legs = df["length"].to_numpy()
    heights = df["height"].to_numpy()
    model = LinearRegression(fit_intercept=False)

    # Prepare the measured data arrays and fit the model to them
    legs = legs.reshape(len(legs), 1)
    heights = heights.reshape(len(heights), 1)
    model.fit(legs, heights)

    # Use the fitted model to make a prediction for the found femur
    fossil_leg = 50.7
    fossil_height = model.predict([[fossil_leg]])
    print("Predicted fossil height = {:0.2f} cm".format(fossil_height[0, 0]))


def linear_model_in_oceanography():
    df = pd.read_csv("./data/sea_level_data.csv", skiprows=6)
    years = df["year"].to_numpy()
    years = years.reshape(len(years), 1)
    levels = df["sea_level_inches"].to_numpy()
    levels = levels.reshape(len(levels), 1)

    model = LinearRegression(fit_intercept=True)
    model.fit(years, levels)

    # Use model to make a prediction for one year, 2100
    future_year = 2100
    future_level = model.predict([[future_year]])
    print(
        "Prediction: year = {}, level = {:.02f}".format(
            future_year, future_level[0, 0])
    )

    # Use model to predict for many years, and over-plot with measured data
    years_forecast = np.linspace(1970, 2100, 131).reshape(-1, 1)
    levels_forecast = model.predict(years_forecast)
    fig = plot_data_and_forecast(
        years, levels, years_forecast, levels_forecast)


def plot_data_and_forecast(years, levels, years_forecast, levels_forecast):
    """
    Purpose:
        Over-plot the forecast data with the measured data used to fit the model
    Args:
        years (np.array): independent ("x") variable of measured data set
        levels (np.array): dependent ("y") variable of measured data set
        years_forecast (np.array): independent ("x") variable of forecast/modeled data
        levels_forecast (np.array): dependent ("y") variable of forecast/modeled data
    Returns:
        fig (matplotlib.figure): matplotlib figure object containing the plot
    """
    font_options = {"family": "Arial", "size": 16}
    plt.rc("font", **font_options)
    fig, axis = plt.subplots(figsize=(8, 4))
    axis.plot(years, levels, color="black",
              linestyle=" ", marker="o", label="Data")
    axis.plot(
        years_forecast, levels_forecast, marker=".", color="red", label="Forecast"
    )
    axis.grid(True, which="both")
    axis.axhline(0, color="black")
    axis.axvline(0, color="black")
    axis.xaxis.set_major_locator(ticker.MultipleLocator(50.0))
    axis.xaxis.set_minor_locator(ticker.MultipleLocator(10.0))
    axis.yaxis.set_major_locator(ticker.MultipleLocator(5.0))
    axis.yaxis.set_minor_locator(ticker.MultipleLocator(1.0))
    axis.set_ylim([0, 20])
    axis.set_xlim([1965, 2105])
    axis.set_ylabel("Sea Level Change (inches)")
    axis.set_xlabel("Time (years)")
    axis.set_title("Global Average Sea Level Change")
    axis.legend()
    plt.show()
    return fig


def linear_model_in_cosmology():
    df = pd.read_csv("./data/hubble_data.csv", skiprows=8)

    # Fit the model, based on the form of the formula
    model_fit = ols(formula="velocities ~ distances", data=df).fit()

    # Extract the model parameters and associated "errors" or uncertainties
    a0 = model_fit.params['Intercept']
    a1 = model_fit.params['distances']
    e0 = model_fit.bse['Intercept']
    e1 = model_fit.bse['distances']

    # Print the results
    print(
        'For slope a1={:.02f}, the uncertainty in a1 is {:.02f}'.format(a1, e1))
    print(
        'For intercept a0={:.02f}, the uncertainty in a0 is {:.02f}'.format(a0, e0))


# linear_model_in_anthroplogy()
# linear_model_in_oceanography()
linear_model_in_cosmology()
