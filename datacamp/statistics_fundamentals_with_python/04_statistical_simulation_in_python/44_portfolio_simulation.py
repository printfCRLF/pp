import numpy as np


# rates is a Normal random variable and has size equal to number of years
def portfolio_return(yrs, avg_return, sd_of_return, principal):
    np.random.seed(123)
    rates = np.random.normal(loc=avg_return, scale=sd_of_return, size=yrs)
    # Calculate the return at the end of the period
    end_return = principal
    for x in rates:
        end_return = end_return*(1+x)
    return end_return


def portfolio_simulation1():
    result = portfolio_return(yrs=5, avg_return=0.07,
                              sd_of_return=0.15, principal=1000)
    print("Portfolio return after 5 years = {}".format(result))


def portfolio_simulation2():
    # Run 1,000 iterations and store the results
    sims, rets = 1000, []

    for i in range(sims):
        rets.append(portfolio_return(yrs=10, avg_return=0.07,
                                     sd_of_return=0.3, principal=10000))

    # Calculate the 95% CI
    lower_ci = np.percentile(rets, 2.5)
    upper_ci = np.percentile(rets, 97.5)
    print("95% CI of Returns: Lower = {}, Upper = {}".format(lower_ci, upper_ci))


def portfolio_simulation3():
    sims = 1000
    rets_stock, rets_bond = [], []

    for i in range(sims):
        rets_stock.append(portfolio_return(
            yrs=10, avg_return=0.07, sd_of_return=0.3, principal=10000))
        rets_bond.append(portfolio_return(
            yrs=10, avg_return=0.04, sd_of_return=0.1, principal=10000))

    # Calculate the 25th percentile of the distributions and the amount you'd lose or gain
    rets_stock_perc = np.percentile(rets_stock, 25)
    rets_bond_perc = np.percentile(rets_bond, 25)
    additional_returns = rets_stock_perc - rets_bond_perc
    print("Sticking to stocks gets you an additional return of {}".format(
        additional_returns))


#portfolio_simulation1()
#portfolio_simulation2()
portfolio_simulation3()
