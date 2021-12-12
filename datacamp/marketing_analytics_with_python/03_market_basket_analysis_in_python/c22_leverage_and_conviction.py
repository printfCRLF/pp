import numpy as np
from data import prepare_books3_dataset
from util import conviction


def computing_conviction(books):
    # Compute support for Potter AND Hunger
    supportPH = np.logical_and(books['Potter'], books['Hunger']).mean()

    # Compute support for Potter
    supportP = books["Potter"].mean()

    # Compute support for NOT Hunger
    supportnH = 1.0 - books['Hunger'].mean()

    # Compute support for Potter and NOT Hunger
    supportPnH = supportP - supportPH

    # Compute and print conviction for Potter -> Hunger
    conviction = supportP * supportnH / supportPnH
    print("Conviction: %.2f" % conviction)


def promoting_ebooks_with_conviction(twilight, potter, hunger):
    # Compute conviction for twilight -> potter and potter -> twilight
    convictionTP = conviction(twilight, potter)
    convictionPT = conviction(potter, twilight)

    # Compute conviction for twilight -> hunger and hunger -> twilight
    convictionTH = conviction(twilight, hunger)
    convictionHT = conviction(hunger, twilight)

    # Compute conviction for potter -> hunger and hunger -> potter
    convictionPH = conviction(potter, hunger)
    convictionHP = conviction(hunger, potter)

    # Print results
    print('Harry Potter -> Twilight: ', convictionHT)
    print('Twilight -> Potter: ', convictionTP)


if __name__ == "__main__":
    books = prepare_books3_dataset()
    computing_conviction(books)

    twilight = books["Twilight"]
    potter = books["Potter"]
    hunger = books["Hunger"]
    promoting_ebooks_with_conviction(twilight, potter, hunger)
