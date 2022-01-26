import pandas as pd
from mlxtend.preprocessing import TransactionEncoder


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


def prepare_online_retail_data():
    # df = pd.read_csv("data/test.csv")
    df = pd.read_csv("data/online_retail.csv")
    transactions = {}

    for _, row in df.iterrows():
        invoice_no = row["InvoiceNo"]
        if invoice_no not in transactions:
            transactions[invoice_no] = []

        tran = str(row["Description"])
        transactions[invoice_no].append(tran)

    # print(transactions)

    transactions_list = list(transactions.values())
    transactions_list = transactions_list[:int(len(transactions_list)/3)]
    return transactions_list


def onehot_online_retail_data(transactions):
    encoder = TransactionEncoder().fit(transactions)
    onehot = encoder.transform(transactions)
    onehot = pd.DataFrame(onehot, columns=encoder.columns_)

    onehot = onehot.sample(frac=0.3)
    print("onehot.shape", onehot.shape)

    return onehot
