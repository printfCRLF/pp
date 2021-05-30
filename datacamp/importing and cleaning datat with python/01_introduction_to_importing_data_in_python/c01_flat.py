import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def p01_text_files():
    file = open('data/moby_dick.txt', mode='r')

    print(file.read())

    print("file closed?", file.closed)

    file.close()

    print("file closed?", file.closed)

    with open('data/moby_dick.txt') as file:
        print(file.readline())
        print(file.readline())
        print(file.readline())


def p02_flat_files():
    file = 'digits.csv'
    digits = np.loadtxt(file, delimiter=',')
    print(type(digits))
    im = digits[21, 1:]
    im_sq = np.reshape(im, (28, 28))
    plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
    plt.show()

    print(digits)


def p03_import_flat_files_using_numpy():
    file = 'data/seaslug.txt'
    data = np.loadtxt(file, delimiter='\t', dtype=str)
    print(data[0])

    # Import data as floats and skip the first row: data_float
    # first row is string, rest of the rows are float. If we import the entire file as float,
    # error will be thrown when converting the first row. Therefore, skiprows = 1
    data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)

    # Print the 10th element of data_float
    print(data_float[9])

    # Plot a scatterplot of the data
    plt.scatter(data_float[:, 0], data_float[:, 1])
    plt.xlabel('time (min.)')
    plt.ylabel('percentage of larvae')
    plt.show()

    data1 = np.genfromtxt('data/titanic_sub.csv',
                          delimiter=',', names=True, dtype=None)
    print(data1['Survived'][-4:])

    data2 = np.recfromcsv('data/titanic_sub.csv')
    print(data2[1])


def p04_import_flat_files_using_pandas1():
    df = pd.read_csv('data/titanic_sub.csv')
    print(df.head())


def p04_import_flat_files_using_pandas2():
    file = 'digits.csv'
    data = pd.read_csv(file, header=None, nrows=5)
    data_array = data.values
    print(type(data_array))


def p04_import_flat_files_using_pandas3():
    file = 'digits.csv'
    data = pd.read_csv(file, header=None, nrows=5)
    data_array = data.values
    print(type(data_array))


def p04_import_flat_files_using_pandas4():
    file = 'data/titanic_sub.csv'
    data = pd.read_csv(file, sep='\t', comment='#', na_values='Nothing')
    print(data.head())

    # Plot 'Age' variable in a histogram
    pd.DataFrame.hist(data[['Age']])
    plt.xlabel('Age (years)')
    plt.ylabel('count')
    plt.show()

# p01_text_files()
# p02_flat_files()
# p03_import_flat_files_using_numpy()
# p04_import_flat_files_using_pandas1()
# p04_import_flat_files_using_pandas4()
