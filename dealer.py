## Importing libraries
import time
import configparser

## Importing files
import translate

config = configparser.ConfigParser()
config.read("config.ini")

def dealer_rolls(cards, dealerNB):
    card = cards.pop(0)
    dealerNB += card

    print(f"{translate.translate("The Dealer rolls a")} {card}.")
    print(f"{translate.translate("The Dealer has")}: {dealerNB}.")
    
    time.sleep(1)

    return dealerNB

def reroll(cards, dealerNB):
    dealerNB = dealer_rolls(cards, dealerNB)

    dealer_max = int(config["Game"]["dealer_max"])
    while (dealerNB < dealer_max and dealerNB < 21):
        dealerNB = dealer_rolls(cards, dealerNB)        

    return dealerNB            
    