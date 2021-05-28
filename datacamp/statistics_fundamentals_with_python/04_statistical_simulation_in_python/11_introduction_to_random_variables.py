import numpy as np
from util import create_a_deck_of_cards

def poisson_random_variable():
    # Initialize seed and parameters
    np.random.seed(123)
    lam, size_1, size_2 = 5, 3, 1000

    # Draw samples & calculate absolute difference between lambda and sample mean
    samples_1 = np.random.poisson(lam, size_1)
    samples_2 = np.random.poisson(lam, size_2)
    answer_1 = abs(np.mean(samples_1) - lam)
    answer_2 = abs(np.mean(samples_2) - lam)

    print("|Lambda - sample mean| with {} samples is {} and with {} samples is {}. ".format(
        size_1, answer_1, size_2, answer_2))





def shuffle_a_deck_of_cards(deck_of_cards): 
    # Shuffle the deck
    np.random.shuffle(deck_of_cards)

    # Print out the top three cards
    card_choices_after_shuffle = deck_of_cards[:3]
    print(card_choices_after_shuffle)


poisson_random_variable()
deck_of_card = create_a_deck_of_cards()
shuffle_a_deck_of_cards(deck_of_card)