## Importing libraries
import configparser

## Importing files
from src import dealer
from src import deck
from src import player
from src import rules
from src import translate

config = configparser.ConfigParser()
config.read("config.ini")

def game_loop():
    money = int(config["Game"]["starting_money"])

    while money > 0:
        bet = ask_bet(money)
        winner = play_round()
        money = update_balance(money, bet, winner)
        show_balance(money)

        if (money <= 0):
            print(f"{translate.translate("Game over")} ! {translate.translate("You are out of money")}.")
            break

        if (ask_replay() == False):
            break

def ask_bet(money):
    bet = 0
    max_bet = int(config["Game"]["max_bet"])
    min_bet = int(config["Game"]["min_bet"])
    currency = config["Game"]["currency"]

    show_balance(money)

    while True:
        answer = input(translate.translate("Place your bet") + ": ")

        try:
            bet = int(answer)
        except ValueError:
            print(f"{translate.translate("Invalid input")}.")
            continue

        if (bet > money):
            print(translate.translate("Insufficient funds") + ".")
        elif (bet > max_bet):
            print(f"{translate.translate("The maximum allowed bet is")} {currency}{max_bet}.")
        elif (bet < min_bet):
            print(f"{translate.translate("The minimum allowed bet is")} {currency}{min_bet}.")
        else:
            return bet

def play_round():
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

    return show_result(dealer_score, player_score, dealer_hand, player_hand)

def show_result(dealer_score, player_score, dealer_hand, player_hand):
    winner = rules.get_winner(dealer_score, player_score, dealer_hand, player_hand)

    print(f"{translate.translate('Final Score')}: ")
    print(f"-{translate.translate('The Dealer has')}: {dealer_score}!")
    print(f"-{translate.translate('The Player has')}: {player_score}!")

    if winner == "dealer":
        print(f"{translate.translate('The Dealer won')}.")
    elif winner == "player" or winner == "blackjack":
        print(f"{translate.translate('The Player won')}.")
    else:
        print(f"{translate.translate('No winners')}.")

    return winner

def show_balance(money):
    currency = config["Game"]["currency"]

    print(f"{translate.translate("Current balance")}: {currency}{money}.")
    print()

def update_balance(money, bet, winner):
    blackjack_payout = float(config["Game"]["blackjack_payout"])

    if (winner == "dealer"):
        money -= bet
    elif (winner == "player"):
        money += bet
    elif (winner == "blackjack"):
        money += int(bet * blackjack_payout)

    return money

def ask_replay():
    yes_word = translate.translate("yes")
    no_word = translate.translate("no")

    while (True):
        answer = input(f"{translate.translate("Play another round")} ? {translate.translate("(yes / no)")}: ").lower()
        if (answer == yes_word or answer == yes_word[0]):
            return True
        elif (answer == no_word or answer == no_word[0]):
            print(f"{translate.translate("See you next time")} !")
            return False
        else:
            print(f"{translate.translate("Invalid input")}.")
