## Importing libraries
import configparser

## Importing files
from src import translate

config = configparser.ConfigParser()
config.read("config.ini")

def get_winner(dealer_hands, player_hands):
    player_blackjack = is_blackjack(player_hands["hand"])
    dealer_blackjack = is_blackjack(dealer_hands["hand"])

    if (player_blackjack and dealer_blackjack):
        return "push"
    elif (player_blackjack):
        return "blackjack"
    elif (dealer_blackjack):
        return "dealer"
    
    if (player_hands["score"] > 21):
        return "dealer"
    elif (dealer_hands["score"] > 21):
        return "player"

    if (dealer_hands["score"] > player_hands["score"]):
        return "dealer"
    elif (player_hands["score"] > dealer_hands["score"]):
        return "player"

    return "push"

def ace_1_or_11():
    ace_choice = 0

    while ace_choice == 0:
        answer = input(translate.translate("1 or 11")+": ").lower()
        if (answer == "1"):
            ace_choice = 1
            return 1
        elif (answer == "11"):
            ace_choice = 1
            return 11
        else:
            print(f"{translate.translate("Invalid input")}.")

def is_blackjack(hand):
    if (len(hand) != 2):
        return False

    ranks = [card["rank"] for card in hand]

    return "A" in ranks and any(rank in ["10", "J", "Q", "K"] for rank in ranks)

def can_double_down(hand, money, bet):
    double_after_split = config.getboolean("Game", "double_after_split")
    
    if (len(hand) > 2):
        return False
    if (bet * 2 > money):
        return False

    return True

def can_split(hand, money, bet):
    if (len(hand) > 2):
            return False
    if (bet * 2 > money):
        return False
    
    return hand[0]["value"] == hand[1]["value"]
