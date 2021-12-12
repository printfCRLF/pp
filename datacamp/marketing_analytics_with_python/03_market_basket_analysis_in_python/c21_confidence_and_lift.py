import pandas as pd
import numpy as np
from data import prepare_books3_dataset


def recommending_books_with_support(books):
    # Compute support for Hunger and Potter
    supportHP = np.logical_and(books['Hunger'], books['Potter']).mean()

    # Compute support for Hunger and Twilight
    supportHT = np.logical_and(books['Hunger'], books['Twilight']).mean()

    # Compute support for Potter and Twilight
    supportPT = np.logical_and(books['Potter'], books['Twilight']).mean()

    # Print support values
    print("Support for Hunger Games and Harry Potter: %.2f" % supportHP)
    print("Support for Hunger Games and Twilight: %.2f" % supportHT)
    print("Support for Harry Potter and Twilight: %.2f" % supportPT)


def refining_support_with_confidence(books):
    print()
    print("should you use Harry Potter to promote Twilight or Twilight to promote Harry Potter")

    supportPT = np.logical_and(books["Potter"], books["Twilight"]).mean()
    supportP = books["Potter"].mean()
    supportT = books["Twilight"].mean()

    confidencePT = supportPT / supportP
    confidenceTP = supportPT / supportT

    print('Potter -> Twilight {0:.2f}, Twilight -> Potter{1:.2f}'.format(confidencePT, confidenceTP))


def further_refinement_with_lift(books): 
    # Compute support for Potter and Twilight
    supportPT = np.logical_and(books['Potter'], books['Twilight']).mean()
    # Compute support for Potter
    supportP = books['Potter'].mean()
    # Compute support for Twilight
    supportT = books['Twilight'].mean()
    # Compute lift
    lift = supportPT / (supportP * supportT)

    # Print lift
    print("Lift: %.2f" % lift)
    # Lift is greater than 1.0. This could give us some confidence that the association rule 
    # we recommended did not arise by random chance. 


if __name__ == "__main__":
    books = prepare_books3_dataset()
    # recommending_books_with_support(books)
    refining_support_with_confidence(books)
    further_refinement_with_lift(books)