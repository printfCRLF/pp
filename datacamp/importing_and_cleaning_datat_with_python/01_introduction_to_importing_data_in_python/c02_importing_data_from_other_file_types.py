import pickle 
import pandas as pd
from sas7bdat import SAS7BDAT
import matplotlib.pyplot as plt
import h5py
import scipy.io

def loading_a_pickled_file(): 
    with open('data.pkl', mode='rb') as file: 
        d = pickle.load(file)
    print(d)
    print(type(d))

def customize_your_spreadsheet_import(): 
    file_name = 'data/battledeath.xlsx'
    xls = pd.ExcelFile(file_name)
    print(xls.sheet_names)
    xls = pd.ExcelFile(file_name)
    df1 = xls.parse(0, skiprows=1, names=['Country', 'AAM due to War (2002)'])
    print(df1.head())
    df2 = xls.parse(1, usecols=[0], skiprows=[0], names=['Country'])
    print(df2.head())

def importing_sas_files(): 
    with SAS7BDAT('data/sales.sas7bdat') as file: 
        df_sas = file.to_data_frame()
    
    print(df_sas.head())
    print(df_sas.info())

    pd.DataFrame.hist(df_sas[['P']])
    plt.ylabel('count')
    plt.show()

def importing_stata_file(): 
    df = pd.read_stata('data/disarea.dta')
    print(df.head())

    # Plot histogram of one column of the DataFrame
    pd.DataFrame.hist(df[['disa10']])
    plt.xlabel('Extent of disease')
    plt.ylabel('Number of countries')
    plt.show()

def importing_hdf5_file(): 
    data = h5py.File('data/L-L1_LOSC_4_V1-1126259446-32.hdf5', 'r')
    print(type(data))
    for key in data.keys():
        print(key)

    group = data['strain']
    for key in group.keys():
        print(key)

    strain = data['strain']['Strain'].value
    num_samples = 10000
    time = np.arange(0, 1, 1/num_samples)

    plt.plot(time, strain[:num_samples])
    plt.xlabel('GPS Time (s)')
    plt.ylabel('strain')
    plt.show()

def importing_matlab_files(): 
    mat = scipy.io.loadmat('data/ja_data2.mat')
    print(type(mat))
    print(mat.keys())  
    print(type(mat['CYratioCyt']))
    print(mat['CYratioCyt'].shape)

    data = mat['CYratioCyt'][25, 5:]
    fig = plt.figure()
    plt.plot(data)
    plt.xlabel('time (min.)')
    plt.ylabel('normalized fluorescence (measure of expression)')
    plt.show()

#loading_a_pickled_file()
#customize_your_spreadsheet_import()
#importing_sas_files()
#importing_stata_file()
#importing_hdf5_file()
importing_matlab_files()