import numpy as np


def throwing_a_fair_die():
    # Define die outcomes and probabilities
    die, probabilities, throws = [1, 2, 3, 4, 5, 6], [
        1/6, 1/6, 1/6, 1/6, 1/6, 1/6], 1

    # Use np.random.choice to throw the die once and record the outcome
    outcome = np.random.choice(die, size=throws, p=probabilities)
    print("Outcome of the throw: {}".format(outcome[0]))


def throwing_two_fair_dice():
    # Initialize number of dice, simulate & record outcome
    die, probabilities, num_dice = [1, 2, 3, 4, 5, 6], [
        1/6, 1/6, 1/6, 1/6, 1/6, 1/6], 2
    outcomes = np.random.choice(die, size=num_dice, p=probabilities)

    # Win if the two dice show the same number
    if outcomes[0] == outcomes[1]:
        answer = 'win'
    else:
        answer = 'lose'

    print("The dice show {} and {}. You {}!".format(
        outcomes[0], outcomes[1], answer))


def simulating_the_dice_game():
    # Initialize model parameters & simulate dice throw
    die, probabilities, num_dice = [1, 2, 3, 4, 5, 6], [
        1/6, 1/6, 1/6, 1/6, 1/6, 1/6], 2
    sims, wins = 100, 0

    for i in range(sims):
        outcomes = np.random.choice(die, 2, p=probabilities)
        # Increment `wins` by 1 if the dice show same number
        if outcomes[0] == outcomes[1]:
            wins = wins + 1

    print("In {} games, you win {} times".format(sims, wins))


throwing_a_fair_die()
# throwing_two_fair_dice()
# simulating_the_dice_game()
