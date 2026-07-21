## Importing libraries
import configparser
import random

config = configparser.ConfigParser()
config.read("config.ini")

def create_deck():
    deck = []
    deck_count = int(config["Game"]["deck_count"])

    for _ in range(deck_count):

        # As
        for _ in range(4):
            deck.append({"name": "A", "value": 1})

        # 2 à 10
        for value in range(2, 11):
            for _ in range(4):
                deck.append({"name": str(value), "value": value})

        # Valet, Dame, Roi
        for face in ["J", "Q", "K"]:
            for _ in range(4):
                deck.append({"name": face, "value": 10})
                
    deck = random_sort(deck)

    return deck

'''
logos = (♠ ♥ ♦ ♣)
def create_deck():
    deck = []
    deck_count = int(config["Game"]["deck_count"])

    cards = [
        ("A", 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
        ("5", 5),
        ("6", 6),
        ("7", 7),
        ("8", 8),
        ("9", 9),
        ("10", 10),
        ("J", 10),
        ("Q", 10),
        ("K", 10),
    ]

    for _ in range(deck_count):
        for name, value in cards:
            for _ in range(4):
                deck.append({
                    "name": name,
                    "value": value
                })

    return deck
'''

def print_cards(cards):
    print(" ".join(card["name"] for card in cards))

def draw(deck):
    return deck.pop(0)

def card_name(card):
    return card["name"]

def card_value(card):
    return card["value"]

def hand_to_string(hand):
    return " ".join(card["name"] for card in hand)

##----------------------------------------
## Different types of sorting
##----------------------------------------
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
