## Importing libraries
import time
import configparser

## Importing libraries
from src import translate
from src import rules

config = configparser.ConfigParser()
config.read("config.ini")

def dealt(cards, hands):
    card = cards.pop(0)

    print(f"{translate.translate("The Player is dealt a")} {card["rank"] + card["suit"]}.")
    if (card["value"] == 1 and hands["score"] < 11):
       card["value"] = rules.ace_1_or_11()

    hands["score"] += card["value"]
    hands["hand"].append(card)

    print(f"{translate.translate("The Player has")}: {hands["score"]}.")
    time.sleep(1)

    return hands

def draw(cards, hands):
    card = cards.pop(0)

    print(f"{translate.translate("The Player draws a")} {card["rank"] + card["suit"]}.")
    if (card["value"] == 1 and hands["score"] < 11):
       card["value"] = rules.ace_1_or_11()

    hands["score"] += card["value"]
    hands["hand"].append(card)

    print(f"{translate.translate("The Player has")}: {hands["score"]}.")
    time.sleep(1)

    return hands

def ask_choice(hands, money):
    hand = hands["hand"]
    bet = hands["bet"]
    
    choices = {
        "H": "Hit",
        "S": "Stand",
    }
    if (rules.can_double_down(hand, money, bet)):
        choices["D"] = "Double Down"
    if (rules.can_split(hand, money, bet)):
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
