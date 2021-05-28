import numpy as np


def create_a_deck_of_cards():
    suits = ['Heart', 'Club', 'Spade', 'Diamond']
    numbers = np.arange(13)
    deck_of_cards = []
    for suit in suits:
        for number in numbers:
            deck_of_cards.append((suit, number))

    return deck_of_cards
