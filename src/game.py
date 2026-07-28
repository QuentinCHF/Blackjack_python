## Importing libraries
import configparser
import time

## Importing files
from src import dealer
from src import debug
from src import deck
from src import player
from src import rules
from src import save
from src import translate

config = configparser.ConfigParser()
config.read("config.ini")
game_save = save.load_save()

def game_loop():
    money = game_save["money"]
    auto_restart = config.getboolean("Game", "auto_restart")

    cards = deck.create_deck()
    cards = debug.check_debug(cards)

    while money > 0:
        bet = ask_bet(money)
        winner, bet, doubled = play_round(cards, money, bet)
        money = update_balance(money, bet, winner)

        save.saving(game_save, money, bet, winner, doubled)

        if (money <= 0):
            show_balance(money)
            print(f"{translate.translate("Game over")} ! {translate.translate("You are out of money")}.")
            break

        cards = deck.check_shuffle(cards)

        if (auto_restart == False):
            show_balance(money)
            if (ask_replay() == False):
                break

def ask_bet(money):
    bet = 0
    max_bet = int(config["Game"]["max_bet"])
    min_bet = int(config["Game"]["min_bet"])
    currency = config["Game"]["currency"]

    show_balance(money)

    while True:
        answer = input(f"{translate.translate("Place your bet")}: {currency}")

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

def initialized_round(cards, bet):
    player_hands = {
        "hand": [],
        "score": 0,
        "bet": bet
    }

    dealer_hands = {
        "hand": [],
        "score": 0
    }

    player_hands = player.dealt(cards, player_hands)
    dealer_hands = dealer.dealt(cards, dealer_hands)
    player_hands = player.dealt(cards, player_hands)
    dealer_hands = dealer.dealt_hidden(cards, dealer_hands)

    return dealer_hands, player_hands

def play_round(cards, money, bet):
    dealer_hands, player_hands = initialized_round(cards, bet)
    doubled = False

    if player_hands["score"] < 21:
        while True:
            choice = player.ask_choice(player_hands, money)

            if (choice == "H"):
                player_hands = player.draw(cards, player_hands)

                if player_hands["score"] >= 21:
                    break

            elif (choice == "S"):
                break

            elif (choice == "D"):
                currency = config["Game"]["currency"]
                player_hands["bet"] *= 2
                print(f"{translate.translate("Bet doubled to")} {currency}{player_hands["bet"]}.")
                time.sleep(1)
                player_hands = player.draw(cards, player_hands)
                doubled = True
                break

            elif (choice == "P"):
                print("Spilt not available yet...")

    dealer.reveal_hidden_card(dealer_hands)
    dealer_hands = dealer.ask_draw(cards, dealer_hands)

    return show_result(dealer_hands, player_hands), player_hands["bet"], doubled

def show_result(dealer_hands, player_hands):
    winner = rules.get_winner(dealer_hands, player_hands)

    print(f"{translate.translate('Final Score')}: ")
    print(f"-{translate.translate('The Dealer has')}: {dealer_hands["score"]}.")
    print(f"-{translate.translate('The Player has')}: {player_hands["score"]}.")

    print()

    if (winner == "dealer"):
        print(f"{translate.translate('The Dealer won')}.")
    elif (winner == "player" or winner == "blackjack"):
        print(f"{translate.translate('The Player won')}.")
    else:
        print(f"{translate.translate('No winners')}.")

    print()

    return winner

def show_balance(money):
    currency = config["Game"]["currency"]

    print(f"{translate.translate("Current balance")}: {currency}{money}.")
    print()

def format_money(amount):
    currency = config["Game"]["currency"]
    return (f"{currency}{amount}")

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
