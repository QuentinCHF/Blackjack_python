## Importing libraries
import time
import configparser

## Importing files
from src import translate

config = configparser.ConfigParser()
config.read("config.ini")

def dealer_dealt(cards, dealer_score, dealer_hand):
    card = cards.pop(0)

    print(f"{translate.translate('The Dealer is dealt a')} {card["rank"] + card["suit"]}.")
    if (card["value"] == 1 and dealer_score < 11):
       card["value"] = 11

    dealer_score += card["value"]
    dealer_hand.append(card)

    print(f"{translate.translate('The Dealer has')}: {dealer_score}.")
    time.sleep(1)

    return dealer_score

def dealer_dealt_hidden(cards, dealer_score, dealer_hand):
    card = cards.pop(0)
    
    print(f"{translate.translate('The Dealer receives a hidden card')}.")

    if (card["value"] == 1 and dealer_score < 11):
           card["value"] = 11

    dealer_score += card["value"]
    dealer_hand.append(card)

    time.sleep(1)

    return dealer_score

def reveal_hidden_card(dealer_score, dealer_hand):
    card = dealer_hand[1]
    print(f"{translate.translate('The Dealer reveals the hidden card')}: {card['rank']}{card['suit']}.")
    print(f"{translate.translate('The Dealer has')}: {dealer_score}.")
    time.sleep(1)


def dealer_draw(cards, dealer_score, dealer_hand):
    card = cards.pop(0)

    print(f"{translate.translate('The Dealer draws a')} {card["rank"] + card["suit"]}.")
    if (card["value"] == 1 and dealer_score < 11):
       card["value"] = 11

    dealer_score += card["value"]
    dealer_hand.append(card)

    print(f"{translate.translate('The Dealer has')}: {dealer_score}.")
    time.sleep(1)

    return dealer_score

def dealer_ask_draw(cards, dealer_score, dealer_hand):
    ##dealer_score = dealer_draw(cards, dealer_score, dealer_hand)

    dealer_max = int(config["Game"]["dealer_max"])
    while (dealer_score < dealer_max and dealer_score < 21):
        dealer_score = dealer_draw(cards, dealer_score, dealer_hand)        

    return dealer_score            
