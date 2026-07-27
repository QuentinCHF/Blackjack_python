## Importing libraries
import time
import configparser

## Importing libraries
from src import translate
from src import rules

config = configparser.ConfigParser()
config.read("config.ini")

def dealt(cards, player_score, player_hand):
    card = cards.pop(0)

    print(f"{translate.translate("The Player is dealt a")} {card["rank"] + card["suit"]}.")
    if (card["value"] == 1 and player_score < 11):
       card["value"] = rules.ace_1_or_11()

    player_score += card["value"]
    player_hand.append(card)

    print(f"{translate.translate("The Player has")}: {player_score}.")
    time.sleep(1)

    return player_score

def draw(cards, player_score, player_hand):
    card = cards.pop(0)

    print(f"{translate.translate("The Player draws a")} {card["rank"] + card["suit"]}.")
    if (card["value"] == 1 and player_score < 11):
       card["value"] = rules.ace_1_or_11()

    player_score += card["value"]
    player_hand.append(card)

    print(f"{translate.translate("The Player has")}: {player_score}.")
    time.sleep(1)

    return player_score

def ask_draw(cards, player_score, player_hand):
    reroll = 0

    yes_word = translate.translate("yes")
    no_word = translate.translate("no")

    while reroll == 0 and player_score < 21:
        answer = input(translate.translate("Does the Player want to hit")+" ? "+translate.translate("(yes / no)")+": ").lower()
        if (answer == yes_word or answer == yes_word[0]):
            player_score = draw(cards, player_score, player_hand)
        elif (answer == no_word or answer == no_word[0]):
            reroll = 1
        else:
            print(f"{translate.translate("Invalid input")}.")

    return player_score

def ask_double_down(cards, player_score, player_hand, money, bet):
    currency = config["Game"]["currency"]

    if (len(player_hand) > 2):
        return player_score, bet, False

    yes_word = translate.translate("yes")
    no_word = translate.translate("no")

    while (True):
        answer = input(translate.translate("Double down")+" ? "+translate.translate("(yes / no)")+": ").lower()
        if (answer == yes_word or answer == yes_word[0]):
            if (bet * 2 > money):
                print(f"{translate.translate("You don't have enough money to double down")}.")
                time.sleep(1)
                return player_score, bet, False
            else:
                bet *= 2
                print(f"{translate.translate("Bet doubled to")} {currency}{bet}.")
                time.sleep(1)
                player_score = draw(cards, player_score, player_hand)
                return player_score, bet, True
        elif (answer == no_word or answer == no_word[0]):
            return player_score, bet, False
        else:
            print(f"{translate.translate("Invalid input")}.")

def ask_choice(hand, money, bet):

    choices = {
        "H": "Hit",
        "S": "Stand",
    }

    if (rules.can_double_down(hand, money, bet)):
        choices["D"] = "Double Down"

    if (rules.can_split()):
        choices["P"] = "Split"

    while (True):

        print()
        print(f"{translate.translate("Choose an action")}: ")

        for key, value in choices.items():
            print(f"({key}) {translate.translate(value)}")

        answer = input("> ").strip().upper()

        if (answer in choices):
            return answer

        print(f"{translate.translate("Invalid input")}.")
