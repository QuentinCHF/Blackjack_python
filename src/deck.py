## Importing libraries
import configparser
import random

config = configparser.ConfigParser()
config.read("config.ini")

def create_deck():
    deck = []
    deck_count = int(config["Game"]["deck_count"])

    suits = [
        ("♠", "black"),
        ("♣", "black"),
        ("♥", "red"),
        ("♦", "red"),
    ]

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
        for suit, color in suits:
            for rank, value in cards:
                deck.append({
                    "rank": rank,
                    "value": value,
                    "suit": suit,
                    "color": color
                })

    return random_sort(deck)

def print_cards(cards):
    print(" ".join(card["rank"] + card["suit"] for card in cards))

def draw(deck):
    return deck.pop(0)

def card_name(card):
    return card["name"]

def card_value(card):
    return card["value"]

def hand_to_string(cards):
    ## How to use: print("cards is" + deck.hand_to_string(player_hand))
    return " ".join(card["rank"] + card["suit"] for card in cards)

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
