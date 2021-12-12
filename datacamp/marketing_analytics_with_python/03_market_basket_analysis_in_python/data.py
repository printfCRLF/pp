import pandas as pd


def prepare_books3_dataset():
    df = pd.read_csv("data/goodbooks-10k-master/ratings.csv")
    books_3 = df[df["book_id"].isin([1, 2, 3])]
    # print(books_3.head())
    # print(books_3.info())

    books = books_3.pivot_table(
        index=["user_id"], values="rating", columns=["book_id"])
    books = books.notna()
    books.reset_index(drop=True, inplace=True)
    books.columns = ["Hunger", "Potter", "Twilight"]

    # print(books.head())
    # print(books.info())
    # print(books.sum())
    return books


def prepare_books5_dataset():
    df = pd.read_csv("data/goodbooks-10k-master/ratings.csv")
    books_5 = df[df["book_id"].isin([1, 2, 3, 4, 5])]

    books = books_5.pivot_table(
        index=["user_id"], values="rating", columns=["book_id"])
    books = books.notna()
    books.reset_index(drop=True, inplace=True)
    books.columns = ["Hunger", "Potter", "Twilight", "Mockingbird",  "Gatsby"]

    return books
