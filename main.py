## Importing libraries
import sys
import configparser

## Importing files
from src import dealer
from src import deck
from src import game
from src import player
from src import rules
from src import translate

config = configparser.ConfigParser()
config.read("config.ini")

def main():
    cards = deck.create_deck()

    dealer_score = 0
    player_score = 0

    dealer_hand = []
    player_hand = []
    
    dealer_score = dealer.dealer_rolls(cards, dealer_score, dealer_hand)
    player_score = player.player_rolls(cards, player_score, player_hand)
    player_score = player.player_rolls(cards, player_score, player_hand)

    player_score = player.reroll(cards, player_score, player_hand)
    dealer_score = dealer.reroll(cards, dealer_score, dealer_hand)

    rules.end_game(dealer_score, player_score)

    return 0


## By default, execute the main function...
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{translate.translate("Game interrupted")}.")
        sys.exit(0)
