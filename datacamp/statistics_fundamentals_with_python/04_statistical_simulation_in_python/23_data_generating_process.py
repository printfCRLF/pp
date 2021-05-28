import numpy as np


def driving_test_outcome(p_rain, p_pass):
    # Simulate whether it will rain or not
    weather = np.random.choice(['rain', 'sun'], p=[p_rain, 1 - p_rain])
    # Simulate and return whether you will pass or fail
    test_result = np.random.choice(
        ['pass', 'fail'], p=[p_pass[weather], 1 - p_pass[weather]])
    return test_result


def driving_test():
    sims, outcomes, p_rain, p_pass = 1000, [], 0.40, {'sun': 0.9, 'rain': 0.3}

    for _ in range(sims):
        outcomes.append(driving_test_outcome(p_rain, p_pass))

    # Calculate fraction of outcomes where you pass
    pass_outcomes_frac = sum([x == 'pass' for x in outcomes])/len(outcomes)
    print("Probability of Passing the driving test = {}".format(pass_outcomes_frac))


def national_elections():
    p = np.array([0.52076814, 0.67846401, 0.82731745, 0.64722761, 0.03665174,
                  0.17835411, 0.75296372, 0.22206157, 0.72778372, 0.28461556,
                  0.72545221, 0.106571, 0.09291364, 0.77535718, 0.51440142,
                  0.89604586, 0.39376099, 0.24910244, 0.92518253, 0.08165597,
                  0.4212476, 0.74123879, 0.2479099, 0.46125805, 0.19584491,
                  0.24440482, 0.349916, 0.80224624, 0.80186664, 0.82968251,
                  0.91178779, 0.51739059, 0.67338858, 0.15675863, 0.37772308,
                  0.77134621, 0.71727114, 0.92700912, 0.28386132, 0.25502498,
                  0.30081506, 0.19724585, 0.29129564, 0.56623386, 0.97681039,
                  0.96263926, 0.0548948, 0.14092758, 0.54739446, 0.54555576])
    outcomes, sims, probs = [], 1000, p

    for _ in range(sims):
        # Simulate elections in the 50 states
        election = np.random.binomial(n=1, p=probs, size=50)
        # Get average of Red wins and add to `outcomes`
        outcomes.append(np.mean(election))

    # Calculate probability of Red winning in less than 45% of the states
    prob_red_wins = sum(x < 0.45 for x in outcomes) / sims
    print("Probability of Red winning in less than 45% of the states = {}".format(
        prob_red_wins))


def fitness_goals(): 
    sims, days, outcomes = 1000, 30, []
    # Simulate steps & choose prob 
    for _ in range(sims):
        w = []
        for i in range(days):
            lam = np.random.choice([5000, 15000], p=[0.6, 0.4], size=1)
            steps = np.random.poisson(lam)
            if steps > 10000: 
                prob = [0.2, 0.8]
            elif steps < 8000: 
                prob = [0.8, 0.2]
            else:
                prob = [0.5, 0.5]
            w.append(np.random.choice([1, -1], p=prob))
        outcomes.append(sum(w))

    # Calculate fraction of outcomes where there was a weight loss
    weight_loss_outcomes_frac = sum([x < 0 for x in outcomes]) / len(outcomes)
    print("Probability of Weight Loss = {}".format(weight_loss_outcomes_frac))


# driving_test()
# national_elections()
fitness_goals()