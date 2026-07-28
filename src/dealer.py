## Importing libraries
import time
import configparser

## Importing files
from src import translate

config = configparser.ConfigParser()
config.read("config.ini")

def dealt(cards, hand):
    card = cards.pop(0)

    print(f"{translate.translate('The Dealer is dealt a')} {card["rank"] + card["suit"]}.")
    if (card["value"] == 1 and hand["score"] < 11):
       card["value"] = 11

    hand["score"] += card["value"]
    hand["hand"].append(card)

    print(f"{translate.translate('The Dealer has')}: {hand["score"]}.")
    time.sleep(1)

    return hand

def dealt_hidden(cards, hand):
    card = cards.pop(0)
    
    print(f"{translate.translate('The Dealer receives a hidden card')}.")

    if (card["value"] == 1 and hand["score"] < 11):
           card["value"] = 11

    hand["score"] += card["value"]
    hand["hand"].append(card)

    time.sleep(1)

    return hand

def reveal_hidden_card(hand):
    card = hand["hand"][1]
    print(f"{translate.translate('The Dealer reveals the hidden card')}: {card['rank']}{card['suit']}.")
    print(f"{translate.translate('The Dealer has')}: {hand["score"]}.")
    time.sleep(1)


def draw(cards, hand):
    card = cards.pop(0)

    print(f"{translate.translate('The Dealer draws a')} {card["rank"] + card["suit"]}.")
    if (card["value"] == 1 and hand["score"] < 11):
       card["value"] = 11

    hand["score"] += card["value"]
    hand["hand"].append(card)

    print(f"{translate.translate('The Dealer has')}: {hand["score"]}.")
    time.sleep(1)

    return hand

def ask_draw(cards, hand):
    dealer_max = int(config["Game"]["dealer_max"])
    while (hand["score"] < dealer_max and hand["score"] < 21):
        hand = draw(cards, hand)        

    return hand            
