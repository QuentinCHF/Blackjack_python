## Importing libraries
import time
import configparser

## Importing libraries
from src import translate
from src import rules
from src import constants

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

def ask_choice(hand, dealer_hand, money):
    choices = {
        "H": "Hit",
        "S": "Stand",
    }
    if (rules.can_double_down(hand, money)):
        choices["D"] = "Double Down"
    if (rules.can_split(hand, money)):
        choices["P"] = "Split"
    if (rules.can_insurance(hand, dealer_hand, money)):
        choices["I"] = "Insurance"

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

def ask_insurance(hand, money, bet):
    if (bet // 2 < money):
        yes_word = translate.translate("yes")
        no_word = translate.translate("no")
    
        while (True):
            answer = input(f"{translate.translate("Insurance")} ? {translate.translate("(yes / no)")}: ").lower()
            if (answer == yes_word or answer == yes_word[0]):
                money -= bet // 2
                hand["insurance"] = bet // 2
                hand["actions"].append(constants.ACTION_INSURANCE)
                return hand, money
            elif (answer == no_word or answer == no_word[0]):
                return hand, money
            else:
                print(f"{translate.translate("Invalid input")}.")
