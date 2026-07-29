## Importing libraries
import sys
import configparser
import json
import os

## Importing files
from src import game
from src import translate
from src import constants

config = configparser.ConfigParser()
config.read("config.ini")

def saving(save, money, hand, winner):
    blackjack_payout = float(config["Game"]["blackjack_payout"])

    bet = hand["bet"]
    actions = hand["actions"]

    save["money"] = money
    save["total_wagered"] += bet

    if winner == "dealer":
        save["losses"] += 1

    elif winner == "player":
        save["wins"] += 1
        save["total_won"] += bet
        if (constants.ACTION_DOUBLE in actions):
            save["double_downs"] += 1
        if (constants.ACTION_SPLIT in actions):
            save["splits"] += 1

    elif winner == "blackjack":
        save["wins"] += 1
        save["blackjacks"] += 1
        save["total_won"] += int(bet * blackjack_payout)

    else:
        save["pushes"] += 1

    if money > save["highest_balance"]:
        save["highest_balance"] = money

    save_game(save)

def game_played(save):
    save["games_played"] += 1
    save_game(save)

def load_save():
    if not os.path.exists("save.json"):
        return create_new_save()

    with open("save.json", "r") as file:
        save = json.load(file)

    if save["money"] <= 0:
        print(f"{translate.translate("No money left")}. {translate.translate("Starting a new game")}.")
        return create_new_save()

    return save

def save_game(save):
    with open("save.json", "w") as file:
        json.dump(save, file, indent=4)

def create_new_save():
    money = int(config["Game"]["starting_money"])

    datas = {
        "money": money,
        "games_played": 0,
        "wins": 0,
        "losses": 0,
        "pushes": 0,
        "blackjacks": 0,
        "double_downs": 0,
        "split": 0,
        "total_wagered": 0,
        "total_won": 0,
        "highest_balance": money
    }

    with open("save.json", "w", encoding="utf-8") as f:
        json.dump(datas, f, indent=4, ensure_ascii=False)

    return datas

def reset_save():
    if os.path.exists("save.json"):
        os.remove("save.json")
        create_new_save()
    else:
        pass
