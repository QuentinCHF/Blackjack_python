## Importing libraries
import time
import configparser

## Importing files
import translate

config = configparser.ConfigParser()
config.read("config.ini")

def dealer_rolls(cards, dealer_score, dealer_hand):
    card = cards.pop(0)

    dealer_score += card["value"]
    dealer_hand.append(card)

    print(f"{translate.translate('The Dealer rolls a')} {card['name']}.")
    print(f"{translate.translate('The Dealer has')}: {dealer_score}.")

    time.sleep(1)

    return dealer_score

def reroll(cards, dealer_score, dealer_hand):
    dealer_score = dealer_rolls(cards, dealer_score, dealer_hand)

    dealer_max = int(config["Game"]["dealer_max"])
    while (dealer_score < dealer_max and dealer_score < 21):
        dealer_score = dealer_rolls(cards, dealer_score, dealer_hand)        

    return dealer_score            
    
def print_cards(dealer_hand):
    print(" ".join(card["name"] for card in dealer_hand))
