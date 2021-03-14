import numpy as np
import matplotlib.pyplot as plt
import util
import pandas as pd 
from statsmodels.formula.api import ols

# Complete the function to convert C to F
def convert_scale(temps_C):
    (freeze_C, boil_C) = (0, 100)
    (freeze_F, boil_F) = (32, 212)
    change_in_C = boil_C - freeze_C
    change_in_F = boil_F - freeze_F
    slope = change_in_F / change_in_C
    intercept = freeze_F - freeze_C
    temps_F = 32 + (9 / 5 * temps_C)
    return temps_F


def linear_propertionality():
    # Use the convert function to compute values of F and plot them
    temps_C = np.linspace(0, 100, 101)
    temps_F = convert_scale(temps_C)
    fig = plot_temperatures(temps_C, temps_F)


def plot_temperatures(temps_C, temps_F):
    font_options = {"family": "Arial", "size": 16}
    plt.rc("font", **font_options)
    fig, axis = plt.subplots(figsize=(16, 4))
    axis.plot(temps_C, temps_F)
    axis.set_xlabel("Temperature (Celsius)")
    axis.set_ylabel("Temperature (Fahrenheit)")
    axis.grid()
    plt.show()
    return fig


def plot_velocity_timeseries(times, velocities):
    fig, axis = plt.subplots()
    axis.plot(
        times, velocities, linestyle=" ", marker=".", color="black", label="Velocities"
    )
    axis.axhline(
        np.mean(velocities), color="red", alpha=0.5, lw=4, label="Mean Velocity"
    )
    axis.grid(True, which="both")
    axis.set_ylabel("Instantaneous Velocity (Kilometers / Hours)")
    axis.set_xlabel("Time (Hours)")
    axis.set_ylim([0, 100])
    fig.tight_layout()
    fig.legend(loc="upper center")
    plt.show()
    return fig


def slope_and_rate_of_change():
    distances = np.array(
        [
            0.13536211,
            4.11568697,
            8.28931902,
            12.41058595,
            16.73878397,
            20.64153844,
            25.14540098,
            29.10323276,
            33.35991992,
            37.47921914,
            41.78850899,
            45.66165494,
            49.9731319,
            54.13466214,
            58.42781412,
            62.40834239,
            66.65229765,
            70.76017847,
            75.00351781,
            79.2152346,
            83.24161507,
            87.59539364,
            91.74179923,
            95.87520786,
            100.07507133,
        ]
    )

    times = np.array(
        [
            0.0,
            0.08333333,
            0.16666667,
            0.25,
            0.33333333,
            0.41666667,
            0.5,
            0.58333333,
            0.66666667,
            0.75,
            0.83333333,
            0.91666667,
            1.0,
            1.08333333,
            1.16666667,
            1.25,
            1.33333333,
            1.41666667,
            1.5,
            1.58333333,
            1.66666667,
            1.75,
            1.83333333,
            1.91666667,
            2.0,
        ]
    )

    # Compute an array of velocities as the slope between each point
    diff_distances = np.diff(distances)
    diff_times = np.diff(times)
    velocities = diff_distances / diff_times

    # Chracterize the center and spread of the velocities
    v_avg = np.mean(velocities)
    v_max = np.max(velocities)
    v_min = np.min(velocities)
    v_range = v_max - v_min

    # Plot the distribution of velocities
    fig = plot_velocity_timeseries(times[1:], velocities)


def intercept_and_starting_points(): 
    df = pd.read_csv("./data/solution_data.csv", skiprows=5)
    print(df)
    model_fit = ols(formula="masses ~ volumes", data=df)
    model_fit = model_fit.fit()

    # Extract the model parameter values, and assign them to a0, a1
    a0 = model_fit.params['Intercept']
    a1 = model_fit.params['volumes']

    # Print model parameter values with meaningful names, and compare to summary()
    print( "container_mass   = {:0.4f}".format(a0) )
    print( "solution_density = {:0.4f}".format(a1) )
    print( model_fit.summary() )    

#linear_propertionality()
#slope_and_rate_of_change()
intercept_and_starting_points()

