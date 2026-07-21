## Importing libraries
import configparser
import random

config = configparser.ConfigParser()
config.read("config.ini")

def create_deck():
    cards = []
    deck_count = int(config["Game"]["deck_count"])

    for _ in range(deck_count):
        # As à 9
        for value in range(1, 10):
            cards.extend([value] * 4)

        # 10, Valet, Dame, Roi
        cards.extend([10] * 16)

    cards = random_sort(cards)

    return cards

def print_cards(cards):
    print(cards)


def random_sort(cards):
    result = list(cards)
    random.shuffle(result)

    return result

def DESC_sort(cards):
    result = list(cards)
    result.sort()
    result.reverse()

    return result

def ASC_sort(cards):
    result = list(cards)
    result.sort()

    return result