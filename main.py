## Importing libraries
import sys
import configparser

## Importing files
import dealer
import player
import sort
import win_condition


config = configparser.ConfigParser()
config.read("config.ini")


def main():
    cards = []
    deck_count = int(config["Game"]["deck_count"])
    for _ in range(deck_count):
        for value in range(1, 11):
            cards.extend([value] * 4)

    cards = sort.random_sort(cards)
    ##print(cards)


    playerNB = 0
    dealerNB = 0


    dealerNB = dealer.dealer_rolls(cards, dealerNB)
    playerNB = player.player_rolls(cards, playerNB)
    playerNB = player.player_rolls(cards, playerNB)


    playerNB = player.reroll(cards, playerNB)
    dealerNB = dealer.reroll(cards, dealerNB)


    win_condition.end_game(dealerNB, playerNB)


    return 0


## By default, execute the main function...
if __name__ == "__main__":
    main()
