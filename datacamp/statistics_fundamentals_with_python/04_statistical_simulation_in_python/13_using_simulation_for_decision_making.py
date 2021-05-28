import numpy as np


def simulating_one_lottery_drawing():
    # Pre-defined constant variables
    lottery_ticket_cost, num_tickets, grand_prize = 10, 1000, 10000

    # Probability of winning
    chance_of_winning = 1/num_tickets

    # Simulate a single drawing of the lottery
    gains = [-lottery_ticket_cost, grand_prize-lottery_ticket_cost]
    probability = [1-chance_of_winning, chance_of_winning]
    outcome = np.random.choice(a=gains, size=1, p=probability, replace=True)

    print("Outcome of one drawing of the lottery is {}".format(outcome))


def should_we_buy():
    # Initialize size and simulate outcome
    lottery_ticket_cost, num_tickets, grand_prize = 10, 1000, 10000
    chance_of_winning = 1/num_tickets
    size = 2000
    payoffs = [-lottery_ticket_cost, grand_prize - lottery_ticket_cost]
    probs = [1-chance_of_winning, chance_of_winning]

    outcomes = np.random.choice(a=payoffs, size=size, p=probs, replace=True)

    # Mean of outcomes.
    answer = np.mean(outcomes)
    print("Average payoff from {} simulations = {}".format(size, answer))


def calculating_a_break_even_lottery_price():
    # Initialize simulations and cost of ticket
    sims, lottery_ticket_cost = 3000, 0,
    num_tickets, grand_prize = 1000, 10000
    chance_of_winning = 1/num_tickets

    # Use a while loop to increment `lottery_ticket_cost` till average value of outcomes falls below zero
    while 1:
        outcomes = np.random.choice([-lottery_ticket_cost, grand_prize-lottery_ticket_cost],
                                    size=sims, p=[1-chance_of_winning, chance_of_winning], replace=True)
        if outcomes.mean() < 0:
            break
        else:
            lottery_ticket_cost += 1
    answer = lottery_ticket_cost - 1

    print("The highest price at which it makes sense to buy the ticket is {}".format(answer))


#simulating_one_lottery_drawing()
#should_we_buy()
calculating_a_break_even_lottery_price()
