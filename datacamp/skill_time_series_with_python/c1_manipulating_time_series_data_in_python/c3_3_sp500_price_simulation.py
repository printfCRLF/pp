from numpy.random import normal, seed, choice
from scipy.stats import norm
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def random_walk_1():
    # Set seed here
    seed(42)

    # Create random_walk
    random_walk = normal(loc=.001, scale=.01, size=2500)
    # Convert random_walk to pd.series
    random_walk = pd.Series(random_walk)
    # Create random_prices
    random_prices = random_walk.add(1).cumprod()
    # Plot random_prices here
    random_prices.mul(1000).plot()
    plt.show()


def random_walk_2():
    seed(42)
    df = pd.read_csv("data/stock_data/fb.csv")
    fb = df.iloc[:, 1]

    # Calculate daily_returns here
    daily_returns = fb.pct_change().dropna()

    # Get n_obs
    n_obs = daily_returns.count()

    # Create random_walk
    random_walk = choice(daily_returns, n_obs)

    # Convert random_walk to pd.series
    random_walk = pd.Series(random_walk)

    # Plot random_walk distribution
    sns.distplot(random_walk)
    plt.show()


def random_walk_3():
    df = pd.read_csv("data/stock_data/fb.csv")
    df.columns = ["date", "price"]
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)
    print(df.info())
    fb = df

    # Calculate daily_returns here
    seed(42)
    daily_returns = fb.price.pct_change().dropna()
    # Get n_obs
    n_obs = daily_returns.count()
    # Create random_walk
    random_walk = choice(daily_returns, n_obs)
    # Convert random_walk to pd.series
    random_walk = pd.Series(random_walk, index=fb.index[1:])

    # Select fb start price here
    start = fb.price.first('D')
    # Add 1 to random walk and append to start
    random_walk = random_walk.add(1)
    random_price = start.append(random_walk)
    # Calculate cumulative product here
    random_price = random_price.cumprod()

    # Insert into fb and plot
    fb['random'] = random_price
    fb.plot()
    plt.show()


def random_walk_4():
    df = pd.read_csv("data/stock_data/fb.csv")
    df.columns = ["date", "price"]
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)
    print(df.info())
    fb = df

    for i in range(10):
        fb[f"random{i}"] = generate_random_price(fb["price"])
        fb[f"random{i}"].plot(linewidth=1, alpha=0.7)

    fb["price"].plot(linewidth=3, color="black")
    plt.show()


def generate_random_price(prices):
    # Calculate daily_returns here
    daily_returns = prices.pct_change().dropna()
    # Select fb start price here
    start = prices.first('D')
    # Get n_obs
    n_obs = daily_returns.count()

    # Create random_walk
    random_walk = choice(daily_returns, n_obs)
    # Convert random_walk to pd.series
    random_walk = pd.Series(random_walk, index=prices.index[1:])

    # Add 1 to random walk and append to start
    random_walk = random_walk.add(1)
    random_price = start.append(random_walk)
    # Calculate cumulative product here
    random_price = random_price.cumprod()

    return random_price


if __name__ == "__main__":
    sns.set()
    # random_walk_1()
    # random_walk_2()
    # random_walk_3()
    random_walk_4()
