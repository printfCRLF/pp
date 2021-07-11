import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def linear_regression_on_appropriate_anscombe_data():
    x = [10.,  8., 13.,  9., 11., 14.,  6.,  4., 12.,  7.,  5.]
    y = [8.04, 6.95,  7.58,  8.81,  8.33,
         9.96,  7.24,  4.26, 10.84, 4.82,  5.68]

    # Perform linear regression: a, b
    a, b = np.polyfit(x, y, 1)

    # Print the slope and intercept
    print(a, b)

    # Generate theoretical x and y data: x_theor, y_theor
    x_theor = np.array([3, 15])
    y_theor = a * x_theor + b

    # Plot the Anscombe data and theoretical line
    _ = plt.plot(x, y, marker='.', linestyle='none')
    _ = plt.plot(x_theor, y_theor)

    # Label the axes
    plt.xlabel('x')
    plt.ylabel('y')

    # Show the plot
    plt.show()


def linear_regression_on_all_anscombe_data():
    anscombe_x = [[
        [10.,  8., 13.,  9., 11., 14.,  6.,  4., 12.,  7.,  5.],
        [10.,  8., 13.,  9., 11., 14.,  6.,  4., 12.,  7.,  5.]
    ], [
        [10.,  8., 13.,  9., 11., 14.,  6.,  4., 12.,  7.,  5.],
        [8.,  8.,  8.,  8.,  8.,  8.,  8., 19.,  8.,  8.,  8.]
    ]]

    anscombe_y = [[
        [8.04,  6.95,  7.58,  8.81,  8.33,  9.96,  7.24,  4.26, 10.84, 4.82,  5.68],
        [9.14, 8.14, 8.74, 8.77, 9.26, 8.1, 6.13, 3.1, 9.13, 7.26, 4.74]
    ], [
        [7.46,  6.77, 12.74,  7.11,  7.81,  8.84, 6.08,  5.39,  8.15, 6.42,  5.73],
        [6.58,  5.76,  7.71,  8.84,  8.47,  7.04,  5.25, 12.5,  5.56, 7.91,  6.89]
    ]]

    fig, axes = plt.subplots(nrows=2, ncols=2)
    for row in range(2):
        for col in range(2):
            x = anscombe_x[row][col]
            y = anscombe_y[row][col]
            a, b = np.polyfit(x, y, 1)
            print('slope:', a, 'intercept:', b)
            theo_x = np.array([min(x), max(x)])
            theo_y = a * theo_x + b
            sns.scatterplot(x=x, y=y, ax=axes[row, col])
            sns.lineplot(theo_x, theo_y, ax=axes[row, col], color="red")

    plt.show()


sns.set()
# linear_regression_on_appropriate_anscombe_data()
linear_regression_on_all_anscombe_data()
