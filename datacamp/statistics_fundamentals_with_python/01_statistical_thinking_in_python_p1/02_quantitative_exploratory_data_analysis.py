import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn import datasets
from util import ecdf

sns.set()
# save load_iris() sklearn dataset to iris
# if you'd like to check dataset type use: type(load_iris())
# if you'd like to view list of attributes use: dir(load_iris())
iris = datasets.load_iris()

# np.c_ is the numpy concatenate function
# which is used to concat iris['data'] and iris['target'] arrays 
# for pandas column argument: concat iris['feature_names'] list
# and string list (in this case one string); you can make this anything you'd like..  
# the original dataset would probably call this ['Species']
df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                    columns= iris['feature_names'] + ['species'])

versicolor_petal_length = df.loc[df['species'] == 1.0]['petal length (cm)']
versicolor_petal_width = df.loc[df['species'] == 1.0]['petal width (cm)']

def comparing_percentiles_to_ECDF(): 
    percentiles = np.array([2.5, 25, 50, 75, 97.5])
    ptiles_vers = np.percentile(versicolor_petal_length, percentiles)
    print(ptiles_vers)

    x_vers, y_vers = ecdf(versicolor_petal_length)
    _ = plt.plot(x_vers, y_vers, '.')
    _ = plt.xlabel('petal length (cm)')
    _ = plt.ylabel('ECDF')

    # Overlay percentiles as red diamonds.
    _ = plt.plot(ptiles_vers, percentiles/100, marker='D', color='red',
            linestyle='none')

    # Show the plot
    plt.show()

def box_and_whisker_plot(): 
    _ = sns.boxplot(x='species', y='petal length (cm)', data=df)

    _ = plt.xlabel('species')
    _ = plt.ylabel('petal length (cm)')
    plt.show()

def variance_and_standard_deviation(arr): 
    differences = arr - np.mean(arr)
    diff_sq = differences ** 2
    variance_explicit = np.mean(diff_sq)
    variance_np = np.var(arr)
    print('two variances:', variance_explicit, variance_np)    

    variance = np.var(arr)
    print('two standard deviations:', np.sqrt(variance), np.std(arr))

def covariance_and_pearson_correlation_coefficient(): 
    _ = plt.plot(versicolor_petal_length, versicolor_petal_width, marker='.', linestyle='none')
    _ = plt.xlabel('petal length (cm)')
    _ = plt.ylabel('petal width (cm)')
    plt.show()

def compute_covariance(): 
    covariance_matrix = np.cov(versicolor_petal_length, versicolor_petal_width)
    print(covariance_matrix)
    petal_cov = covariance_matrix[0, 1]
    print(petal_cov)

def pearson_r(x, y): 
    """Compute Pearson correlation coefficient between two arrays."""
    corr_mat = np.corrcoef(x, y)
    return corr_mat[0,1]

def computing_pearson_correlation_coefficient(): 
    corr_mat = np.corrcoef(versicolor_petal_length, versicolor_petal_width)
    print(corr_mat[0,1])
    
comparing_percentiles_to_ECDF()
#box_and_whisker_plot()
#variance_and_standard_deviation(versicolor_petal_length)
#covariance_and_pearson_correlation_coefficient()
#compute_covariance()
#computing_pearson_correlation_coefficient()


