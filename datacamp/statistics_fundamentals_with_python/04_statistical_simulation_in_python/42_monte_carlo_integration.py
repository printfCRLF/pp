import numpy as np
import math


# Define the sim_integrate function
def sim_integrate(func, xmin, xmax, sims):
    x = np.random.uniform(xmin, xmax, sims)
    y = np.random.uniform(min(min(func(x)), 0), max(func(x)), sims)
    area = (max(y) - min(y)) * (xmax - xmin)
    result = area * sum(abs(y) < abs(func(x))) / sims
    return result


def integrating_a_simple_function():
    # Call the sim_integrate function and print results
    result = sim_integrate(func=lambda x: x*np.exp(x), xmin=0, xmax=1, sims=50)
    print("Simulated answer = {}, Actual Answer = 1".format(result))


def calculating_the_value_of_pi():
    # Initialize sims and circle_points
    sims, circle_points = 10000, 0

    for i in range(sims):
        # Generate the two coordinates of a point
        point = np.random.uniform(-1, 1, size=2)
        # if the point lies within the unit circle, increment counter
        within_circle = point[0]**2 + point[1]**2 <= 1
        if within_circle == True:
            circle_points += 1

    # Estimate pi as 4 times the avg number of points in the circle.
    pi_sim = 4 * circle_points / sims
    print("Simulated value of pi = {}".format(pi_sim))


integrating_a_simple_function()
calculating_the_value_of_pi()
