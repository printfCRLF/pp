import numpy as np


def the_conditional_urn():
    # We have an urn that contains 7 white and 6 black balls. Four balls are drawn at random.
    # We'd like to know the probability that the first and third balls are white, while the second and the fourth balls are black.
    # Initialize success, sims and urn
    success, sims = 0, 5000
    urn = ['w'] * 7 + ['b'] * 6

    for _ in range(sims):
        # Draw 4 balls without replacement
        draw = np.random.choice(urn, replace=False, size=4)
        # Count the number of successes
        if (draw == ['w', 'b', 'w', 'b']).all():
            success += 1

    print("Probability of success = {}".format(success/sims))


def birthday_problem(): 
    days = np.arange(1, 366)
    people = 2
    # Break out of the loop if probability greater than 0.5
    while (people > 0):
        prop_bds = birthday_sim(days,people)
        if prop_bds > 0.5: 
            break
        people += 1

    print("With {} people, there's a 50% chance that two share a birthday.".format(people))


def birthday_sim(days, people): 
    sims, unique_birthdays = 2000, 0 
    for _ in range(sims):
        draw = np.random.choice(days, size=people, replace=True)
        if len(draw) == len(set(draw)): 
            unique_birthdays += 1
    out = 1 - unique_birthdays / sims
    return out


the_conditional_urn()
birthday_problem()
