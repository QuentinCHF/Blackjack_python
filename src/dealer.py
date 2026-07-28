## Importing libraries
import time
import configparser

## Importing files
from src import translate

config = configparser.ConfigParser()
config.read("config.ini")

def dealt(cards, hands):
    card = cards.pop(0)

    print(f"{translate.translate('The Dealer is dealt a')} {card["rank"] + card["suit"]}.")
    if (card["value"] == 1 and hands["score"] < 11):
       card["value"] = 11

    hands["score"] += card["value"]
    hands["hand"].append(card)

    print(f"{translate.translate('The Dealer has')}: {hands["score"]}.")
    time.sleep(1)

    return hands

def dealt_hidden(cards, hands):
    card = cards.pop(0)
    
    print(f"{translate.translate('The Dealer receives a hidden card')}.")

    if (card["value"] == 1 and hands["score"] < 11):
           card["value"] = 11

    hands["score"] += card["value"]
    hands["hand"].append(card)

    time.sleep(1)

    return hands

def reveal_hidden_card(hands):
    card = hands["hand"][1]
    print(f"{translate.translate('The Dealer reveals the hidden card')}: {card['rank']}{card['suit']}.")
    print(f"{translate.translate('The Dealer has')}: {hands["score"]}.")
    time.sleep(1)


def draw(cards, hands):
    card = cards.pop(0)

    print(f"{translate.translate('The Dealer draws a')} {card["rank"] + card["suit"]}.")
    if (card["value"] == 1 and hands["score"] < 11):
       card["value"] = 11

    hands["score"] += card["value"]
    hands["hand"].append(card)

    print(f"{translate.translate('The Dealer has')}: {hands["score"]}.")
    time.sleep(1)

    return hands

def ask_draw(cards, hands):
    dealer_max = int(config["Game"]["dealer_max"])
    while (hands["score"] < dealer_max and hands["score"] < 21):
        hands = draw(cards, hands)        

    return hands            
