import numpy as np


# Initialize variables
cost = 5000
rain = np.random.normal(loc=50, scale=15)

# Corn Production Model


def corn_produced(rain, cost):
    mean_corn = 100 * cost ** 0.1 * rain ** 0.2
    corn = np.random.poisson(mean_corn)
    return corn


# Simulate and print corn production
corn_result = corn_produced(rain, cost)
print("Simulated Corn Production = {}".format(corn_result))


def corn_demanded(price):
    mean_corn = 1000 - 8*price
    corn = np.random.poisson(abs(mean_corn))
    return corn


# Function to calculate profits
def profits(cost):
    rain = np.random.normal(50, 15)
    price = np.random.normal(40, 10)
    supply = corn_produced(rain, cost)
    demand = corn_demanded(price)
    equil_short = supply <= demand
    if equil_short == True:
        tmp = supply*price - cost
        return tmp
    else:
        tmp2 = demand*price - cost
        return tmp2


result = profits(cost)
print("Simulated profit = {}".format(result))


# Initialize results and cost_levels variables
sims, results = 1000, {}
cost_levels = np.arange(100, 5100, 100)

# For each cost level, simulate profits and store mean profit
for cost in cost_levels:
    tmp_profits = []
    for i in range(sims):
        tmp_profits.append(profits(cost))
    results[cost] = np.mean(tmp_profits)

# Get the cost that maximizes average profit
cost_max = [x for x in results.keys() if results[x] ==
            max(results.values())][0]
print("Average profit is maximized when cost = {}".format(cost_max))
