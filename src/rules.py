## Importing libraries
import configparser

## Importing files
from src import translate
from src import constants

config = configparser.ConfigParser()
config.read("config.ini")

def get_winner(dealer_hand, player_hand):
    player_blackjack = is_blackjack(player_hand["hand"])
    dealer_blackjack = is_blackjack(dealer_hand["hand"])

    if (player_blackjack and dealer_blackjack):
        return "push"
    elif (player_blackjack):
        return "blackjack"
    elif (dealer_blackjack):
        return "dealer"
    
    if (player_hand["score"] > 21):
        return "dealer"
    elif (dealer_hand["score"] > 21):
        return "player"

    if (dealer_hand["score"] > player_hand["score"]):
        return "dealer"
    elif (player_hand["score"] > dealer_hand["score"]):
        return "player"

    return "push"

def ace_1_or_11():
    ace_choice = 0

    while ace_choice == 0:
        answer = input(translate.translate('1 or 11')+": ").lower()
        if (answer == '1'):
            ace_choice = 1
            return 1
        elif (answer == '11'):
            ace_choice = 1
            return 11
        else:
            print(f"{translate.translate('Invalid input')}.")

def is_blackjack(hand):
    if (len(hand) != 2):
        return False

    ranks = [card["rank"] for card in hand]

    return "A" in ranks and any(rank in ["10", "J", "Q", "K"] for rank in ranks)

def can_double_down(hand, money, bet):
    double_after_split = config.getboolean("Game", "double_after_split")
    
    if (constants.ACTION_SPLIT in hand["actions"] and not double_after_split):
        return False
    if (len(hand["hand"]) > 2):
        return False
    if (bet > money):
        return False

    return True

def can_split(hand, money, bet):
    if (len(hand["hand"]) > 2):
            return False
    if (bet > money):
        return False
    
    return hand["hand"][0]["value"] == hand["hand"][1]["value"]
