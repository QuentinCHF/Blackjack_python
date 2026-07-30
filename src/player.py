## Importing libraries
import time
import configparser

## Importing libraries
from src import translate
from src import rules

config = configparser.ConfigParser()
config.read("config.ini")

def dealt(cards, hand):
    card = cards.pop(0)

    print(f"{translate.translate("The Player is dealt a")} {card["rank"] + card["suit"]}.")
    if (card["value"] == 1 and hand["score"] < 11):
       card["value"] = rules.ace_1_or_11()

    hand["score"] += card["value"]
    hand["hand"].append(card)

    print(f"{translate.translate("The Player has")}: {hand["score"]}.")
    time.sleep(1)

    return hand

def draw(cards, hand):
    card = cards.pop(0)

    print(f"{translate.translate("The Player draws a")} {card["rank"] + card["suit"]}.")
    if (card["value"] == 1 and hand["score"] < 11):
       card["value"] = rules.ace_1_or_11()

    hand["score"] += card["value"]
    hand["hand"].append(card)

    print(f"{translate.translate("The Player has")}: {hand["score"]}.")
    time.sleep(1)

    return hand

def ask_choice(hand, money):
    bet = hand["bet"]

    choices = {
        "H": "Hit",
        "S": "Stand",
    }
    if (rules.can_double_down(hand, money, bet)):
        choices["D"] = "Double Down"
    if (rules.can_split(hand, money, bet)):
        choices["P"] = "Split"

    while (True):
        if ("id" in hand):
            print(f"--- {translate.translate("Hand")} {hand["id"]} ---")
            ## print(f"\n--- {hand['name']} ---")

        print(f"{translate.translate("Choose an action")}: ")

        for key, value in choices.items():
            print(f"({key}) {translate.translate(value)}")

        answer = input("> ").strip().upper()

        if (answer in choices):
            return answer

        print(f"{translate.translate("Invalid input")}.")
