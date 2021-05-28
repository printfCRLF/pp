import numpy as np


# Initialize click-through rate and signup rate dictionaries
ct_rate = {'low': 0.01, 'high': np.random.uniform(low=0.01, high=1.2*0.01)}
su_rate = {'low': 0.2, 'high': np.random.uniform(low=0.2, high=1.2*0.2)}


def get_signups(cost, ct_rate, su_rate, sims):
    lam = np.random.normal(loc=100000, scale=2000, size=sims)
    # Simulate impressions(poisson), clicks(binomial) and signups(binomial)
    impressions = np.random.poisson(lam=lam)
    clicks = np.random.binomial(impressions, p=ct_rate[cost])
    signups = np.random.binomial(clicks, p=su_rate[cost])
    return signups


print("Simulated Signups = {}".format(get_signups('high', ct_rate, su_rate, 1)))


def get_revenue(signups):
    rev = []
    np.random.seed(123)
    for s in signups:
        # Model purchases as binomial, purchase_values as exponential
        purchases = np.random.binomial(s, p=0.1)
        purchase_values = np.random.exponential(scale=1000, size=purchases)

        # Append to revenue the sum of all purchase values.
        rev.append(np.sum(purchase_values))
    return rev


print("Simulated Revenue = ${}".format(
    get_revenue(get_signups('low', ct_rate, su_rate, 1))[0]))


# Initialize cost_diff
sims, cost_diff = 10000, 3000

# Get revenue when the cost is 'low' and when the cost is 'high'
rev_low = get_revenue(get_signups('low', ct_rate, su_rate, sims))
rev_high = get_revenue(get_signups('high', ct_rate, su_rate, sims))

# calculate fraction of times rev_high - rev_low is less than cost_diff
frac = sum(rev_high[i] - rev_low[i] <
           cost_diff for i in range(len(rev_high))) / sims
print("Probability of losing money = {}".format(frac))
