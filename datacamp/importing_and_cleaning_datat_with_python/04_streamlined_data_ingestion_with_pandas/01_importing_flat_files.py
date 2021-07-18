# Import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt


def get_data_from_csv():
    data = pd.read_csv('data/vt_tax_data_2016.csv')
    print(data.head())


def get_data_from_other_flat_files():
    data = pd.read_csv('vt_tax_data_2016.tsv', sep='\t')
    counts = data.groupby("agi_stub").N1.sum()
    counts.plot.bar()
    plt.show()


def import_a_subset_of_columns():
    cols = ['zipcode', 'agi_stub', 'mars1', 'MARS2', 'NUMDEP']
    data = pd.read_csv("vt_tax_data_2016.csv", usecols=cols)
    print(data.groupby("agi_stub").sum())


def import_a_file_in_chunks():
    vt_data_next500 = pd.read_csv("vt_tax_data_2016.csv",
                                  skiprows=500,
                                  nrows=500,
                                  header=None,
                                  names=list(vt_data_first500))
    print(vt_data_first500.head())
    print(vt_data_next500.head())


def specify_data_types():
    data_types = {'agi_stub': "category",
                  'zipcode': str}
    null_values = {'zipcode': 0}
    data = pd.read_csv("data/vt_tax_data_2016.csv", dtype=data_types, na_values=null_values)
    print(data.dtypes.head())
    print(data[data.zipcode.isna()])

def skip_bad_data(): 
    try:
        data = pd.read_csv("data/vt_tax_data_2016_corrupt.csv", 
                            error_bad_lines=False, 
                            warn_bad_lines=True)       
        print(data.head())
        
    except pd.io.common.CParserError:
        print("Your data contained rows that could not be parsed.")

#specify_data_types()
#skip_bad_data()
