# Import cars data
import pandas as pd


def loop_over_dataframe(cars):
    for label, row in cars.iterrows():
        print(label)
        print(row)


def cars_per_capita(cars):
    for country, row in cars.iterrows():
        print("{}: {}".format(country, row["cars_per_cap"]))


def add_column(cars):
    for lab, row in cars.iterrows():
        cars.loc[lab, "COUNTRY"] = row["country"].upper()
    print(cars)


def apply_method(cars):
    for label, row in cars.iterrows():
        cars["COUNTRY"] = cars["country"].apply(str.upper)


if __name__ == "__main__":
    cars = pd.read_csv('cars.csv', index_col=0)
    # loop_over_dataframe(cars)
    # cars_per_capita(cars)
    # add_column(cars)
    apply_method(cars)
