import numpy as np
import util


def two_of_a_kind(deck_of_cards):
    # Shuffle deck & count card occurrences in the hand
    n_sims, two_kind = 10000, 0
    for i in range(n_sims):
        np.random.shuffle(deck_of_cards)
        hand, cards_in_hand = deck_of_cards[0:5], {}
        for [suite, numeric_value] in hand:
            # Count occurrences of each numeric value
            cards_in_hand[numeric_value] = cards_in_hand.get(
                numeric_value, 0) + 1

        # Condition for getting at least 2 of a kind
        if max(cards_in_hand.values()) >= 2:
            two_kind += 1

    print("Probability of seeing at least two of a kind = {} ".format(two_kind/n_sims))


def game_of_thirteen(): 
    # Pre-set constant variables
    deck, sims, coincidences = np.arange(1, 14), 10000, 0

    for _ in range(sims):
        # Draw all the cards without replacement to simulate one game
        draw = np.random.choice(deck, size=len(deck), replace=False)
        # Check if there are any coincidences
        coincidence = (draw == list(np.arange(1, 14))).any()
        if coincidence == True: 
            coincidences += 1

    # Calculate probability of winning
    prob_of_winning = 1 - coincidences / sims
    print("Probability of winning = {}".format(prob_of_winning))    


    ### line #31 (draw == list(np.arange(1, 14))).any()
    # draw = np.array([1, 11, 8, 9])
    # candidate = np.arange(1, 5)
    # draw == candidate ## yeilds [True, False, False, False]
    # any() returns True if any of the item is True

deck_of_cards = util.create_a_deck_of_cards()
two_of_a_kind(deck_of_cards)
game_of_thirteen()

