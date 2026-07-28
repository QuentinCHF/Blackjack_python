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
        winners, bet, doubled = play_round(cards, money, bet)

        for winner in winners:
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
    max_bet = int(config["Game"]["max_bet"])
    min_bet = int(config["Game"]["min_bet"])
    currency = config["Game"]["currency"]
    bet = 0

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
    player_hand = {
        "hand": [],
        "score": 0,
        "bet": bet
    }

    dealer_hand = {
        "hand": [],
        "score": 0
    }

    player_hand = player.dealt(cards, player_hand)
    dealer_hand = dealer.dealt(cards, dealer_hand)
    player_hand = player.dealt(cards, player_hand)
    dealer_hand = dealer.dealt_hidden(cards, dealer_hand)

    return dealer_hand, player_hand

def play_player_turn(cards, hand, money):
    doubled = False

    if hand["score"] >= 21:
        return

    while True:
        choice = player.ask_choice(hand, money)

        if (choice == "H"):
            hand = player.draw(cards, hand)

            if (hand["score"] >= 21):
                break

        elif (choice == "S"):
            break

        elif (choice == "D"):
            currency = config["Game"]["currency"]
            hand["bet"] *= 2
            print(f"{translate.translate("Bet doubled to")} {currency}{hand["bet"]}.")
            time.sleep(1)
            hand = player.draw(cards, hand)
            doubled = True
            break

        elif (choice == "P"):
            hand1, hand2 = split_hand(cards, hand);
            return [hand1, hand2], doubled, True

    return [hand], doubled, False

def play_round(cards, money, bet):
    dealer_hand, player_hand = initialized_round(cards, bet)
    player_hands = [player_hand]
    doubled = False

    i = 0
    while i < len(player_hands):
        new_hands, doubled, splitted = play_player_turn(
            cards,
            player_hands[i],
            money
        )

        player_hands[i:i+1] = new_hands

        if not splitted:
            i += 1

    dealer.reveal_hidden_card(dealer_hand)
    dealer_hand = dealer.ask_draw(cards, dealer_hand)

    winners = []

    for hand in player_hands:
        winners.append(show_result(dealer_hand, hand))


    return winners, player_hand["bet"], doubled

def show_result(dealer_hand, player_hand):
    winner = rules.get_winner(dealer_hand, player_hand)

    print(f"{translate.translate('Final Score')}: ")
    print(f"-{translate.translate('The Dealer has')}: {dealer_hand["score"]}.")
    print(f"-{translate.translate('The Player has')}: {player_hand["score"]}.")
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

def split_hand(cards, hand):
    card1 = hand["hand"][0]
    card2 = hand["hand"][1]

    hand1 = {
        "hand": [card1],
        "score": card1["value"],
        "bet": hand["bet"]
    }

    hand2 = {
        "hand": [card2],
        "score": card2["value"],
        "bet": hand["bet"]
    }

    hand1 = player.draw(cards, hand1)
    hand2 = player.draw(cards, hand2)

    return hand1, hand2
