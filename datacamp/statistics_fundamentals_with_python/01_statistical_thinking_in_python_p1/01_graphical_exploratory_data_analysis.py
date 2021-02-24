import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 

versicolor_petal_length = [
    4.7, 4.5, 4.9, 4. , 4.6, 4.5, 4.7, 3.3, 4.6, 3.9, 3.5, 4.2, 4. ,
    4.7, 3.6, 4.4, 4.5, 4.1, 4.5, 3.9, 4.8, 4. , 4.9, 4.7, 4.3, 4.4,
    4.8, 5. , 4.5, 3.5, 3.8, 3.7, 3.9, 5.1, 4.5, 4.5, 4.7, 4.4, 4.1,
    4. , 4.4, 4.6, 4. , 3.3, 4.2, 4.2, 4.2, 4.3, 3. , 4.1]

setosa_petal_length  = [1.4, 1.4, 1.3, 1.5, 1.4, 1.7, 1.4, 1.5, 1.4, 1.5, 1.5, 1.6, 1.4,
       1.1, 1.2, 1.5, 1.3, 1.4, 1.7, 1.5, 1.7, 1.5, 1. , 1.7, 1.9, 1.6,
       1.6, 1.5, 1.4, 1.6, 1.6, 1.5, 1.5, 1.4, 1.5, 1.2, 1.3, 1.4, 1.3,
       1.5, 1.3, 1.3, 1.3, 1.6, 1.9, 1.4, 1.6, 1.4, 1.5, 1.4]

virginica_petal_length = [6. , 5.1, 5.9, 5.6, 5.8, 6.6, 4.5, 6.3, 5.8, 6.1, 5.1, 5.3, 5.5,
       5. , 5.1, 5.3, 5.5, 6.7, 6.9, 5. , 5.7, 4.9, 6.7, 4.9, 5.7, 6. ,
       4.8, 4.9, 5.6, 5.8, 6.1, 6.4, 5.6, 5.1, 5.6, 6.1, 5.6, 5.5, 4.8,
       5.4, 5.6, 5.1, 5.1, 5.9, 5.7, 5.2, 5. , 5.2, 5.4, 5.1]

def plotting__a_histogram_of_iris_data(): 
    n_data = len(versicolor_petal_length)
    n_bins = np.sqrt(n_data)
    n_bins = int(n_bins)

    # Plot the histogram
    sns.set()
    plt.hist(versicolor_petal_length, bins=n_bins)
    _ = plt.xlabel('petal length (cm)')
    _ = plt.ylabel('count')
    plt.show()

def bee_swarm_plot(): 
    df = pd.DataFrame()
    sns.swarmplot(x='species', y='petal length (cm)', data=df )

    _ = plt.xlabel('species')
    _ = plt.ylabel('petal length (cm)')
    plt.show()


def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)
    # x-data for the ECDF: x
    x = np.sort(data)
    # y-data for the ECDF: y
    y = np.arange(1, len(x)+1) / n
    return x, y

def plotting_ecdf(): 
    x_vers, y_vers = ecdf(versicolor_petal_length)

    _ = plt.plot(x_vers, y_vers, marker='.', linestyle='none')
    _ = plt.xlabel('petal length(cm)')
    _ = plt.ylabel('ECDF')
    plt.margins(0.02)
    plt.show()

def comparison_of_ecdfs(): 
    x_set, y_set = ecdf(setosa_petal_length)
    x_vers, y_vers = ecdf(versicolor_petal_length)
    x_virg, y_virg = ecdf(virginica_petal_length)

    # Plot all ECDFs on the same plot
    _ = plt.plot(x_set, y_set, marker='.', linestyle='none')
    _ = plt.plot(x_vers, y_vers, marker='.', linestyle='none')
    _ = plt.plot(x_virg, y_virg, marker='.', linestyle='none')

    # Annotate the plot
    plt.legend(('setosa', 'versicolor', 'virginica'), loc='lower right')
    _ = plt.xlabel('petal length (cm)')
    _ = plt.ylabel('ECDF')

    # Display the plot
    plt.show()

#plotting__a_histogram_of_iris_data()
#bee_swarm_plot()
plotting_ecdf()
#comparison_of_ecdfs()
