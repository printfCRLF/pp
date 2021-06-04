import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def load_voting_data():
    columns = ['party', 'infants', 'water', 'budget', 'physician', 'salvador', 'religious', 'satellite', 'aid', 'missile',
               'immigration', 'synfuels', 'education', 'superfund', 'crime', 'duty_free_exports', 'eaa_rsa']
    df = pd.read_csv('data/house-votes-84.csv')
    df.columns = columns
    # print(df.head(10))
    # print(df.info())
    # print(df.describe())
    return df


def visual_eda(df):
    # df['education'].describe()
    plt.figure()
    sns.countplot(x='education', hue='party', data=df, palette='RdBu')
    print(plt.xticks())
    plt.xticks([0, 1, 2], ['Yes', 'No', 'N/A'])
    plt.show()

    sns.countplot(x='satellite', hue='party', data=df, palette='RdBu')
    print(plt.xticks())
    plt.xticks([0, 1, 2], ['No', 'Yes', 'N/A'])
    plt.show()

    sns.countplot(x='missile', hue='party', data=df, palette='RdBu')
    print(plt.xticks())
    plt.xticks([0, 1, 2], ['No', 'Yes', 'N/A'])
    plt.show()


plt.style.use('ggplot')
df = load_voting_data()
visual_eda(df)
