## Importing libraries

## Importing files
from src import translate

def get_winner(dealer_score, player_score, dealer_hand, player_hand):
    player_blackjack = is_blackjack(player_hand)
    dealer_blackjack = is_blackjack(dealer_hand)

    if (player_blackjack and dealer_blackjack):
        return "push"
    elif (player_blackjack):
        return "blackjack"
    elif (dealer_blackjack):
        return "dealer"
    
    if (player_score > 21):
        return "dealer"
    elif (dealer_score > 21):
        return "player"

    if (dealer_score > player_score):
        return "dealer"
    elif (player_score > dealer_score):
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
            print(f"{translate.translate("Invalid input")}")

def is_blackjack(hand):
    if (len(hand) != 2):
        return False

    ranks = [card["rank"] for card in hand]

    return "A" in ranks and any(rank in ["10", "J", "Q", "K"] for rank in ranks)
