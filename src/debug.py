## Importing libraries
import configparser
import sys

## Importing files

config = configparser.ConfigParser()
config.read("config.ini")

def check_debug(cards):
    debug_enabled = config.getboolean("Debug", "enabled")
    scenario = config["Debug"]["scenario"]
    if (debug_enabled):
        print("/!\\ DEBUG MODE /!\\")
        apply_scenario(cards, scenario)

    return cards

def apply_scenario(cards, scenario):
    if (scenario == "blackjack_player"):
        player1 = find_card(cards, "A", "♠")
        player2 = find_card(cards, "K", "♦")
        dealer1 = find_card(cards, "9", "♣")
        dealer2 = find_card(cards, "8", "♥")
    elif (scenario == "blackjack_dealer"):
        player1 = find_card(cards, "9", "♠")
        player2 = find_card(cards, "8", "♦")
        dealer1 = find_card(cards, "A", "♣")
        dealer2 = find_card(cards, "K", "♥")
    elif (scenario == "push_18"):
        player1 = find_card(cards, "10", "♠")
        player2 = find_card(cards, "8", "♦")
        dealer1 = find_card(cards, "9", "♣")
        dealer2 = find_card(cards, "9", "♥")
    elif (scenario == "player_20"):
        player1 = find_card(cards, "10", "♠")
        player2 = find_card(cards, "K", "♦")
        dealer1 = find_card(cards, "9", "♣")
        dealer2 = find_card(cards, "8", "♥")
    elif (scenario == "dealer_20"):
            player1 = find_card(cards, "9", "♣")
            player2 = find_card(cards, "8", "♥")
            dealer1 = find_card(cards, "10", "♠")
            dealer2 = find_card(cards, "K", "♦")
    elif (scenario == "split_player"):
        player1 = find_card(cards, "2", "♠")
        player2 = find_card(cards, "2", "♦")
        dealer1 = find_card(cards, "9", "♣")
        dealer2 = find_card(cards, "8", "♥")
    else:
        print(f"Unknown debug scenario: '{scenario}'.")
        sys.exit(0)
        return cards

    cards.remove(player1)
    cards.remove(dealer1)
    cards.remove(player2)
    cards.remove(dealer2)

    cards.insert(0, player1)
    cards.insert(1, dealer1)
    cards.insert(2, player2)
    cards.insert(3, dealer2)

    return cards

def find_card(cards, rank, suit):
    for card in cards:
        if card["rank"] == rank and card["suit"] == suit:
            return card
