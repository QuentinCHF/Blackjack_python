## Importing libraries
import sys
import configparser
import json
import os

## Importing files
from src import game
from src import translate

config = configparser.ConfigParser()
config.read("config.ini")

def saving(save, money, bet, winner, doubled):
    blackjack_payout = float(config["Game"]["blackjack_payout"])

    save["money"] = money
    save["games_played"] += 1
    save["total_wagered"] += bet

    if (winner == "dealer"):
        save["losses"] += 1
    elif (winner == "player" and not doubled):
        save["wins"] += 1
        save["total_won"] += bet
    elif (winner == "player" and doubled):
        save["wins"] += 1
        save["total_won"] += bet
        save["double_downs"] += 1
    elif (winner == "blackjack"):
        save["wins"] += 1
        save["blackjacks"] += 1
        save["total_won"] += int(bet * blackjack_payout)
    else:
        save["pushes"] += 1

    if (money > save["highest_balance"]):
        save["highest_balance"] = money

    save_game(save)

def load_save():
    if not os.path.exists("save.json"):
        return create_new_save()

    with open("save.json", "r") as file:
        return json.load(file)

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
        "total_wagered": 0,
        "total_won": 0,
        "highest_balance": money
    }

    with open("save.json", "w", encoding="utf-8") as f:
        json.dump(datas, f, indent=4, ensure_ascii=False)

def reset_save():
    if os.path.exists("save.json"):
        os.remove("save.json")
        # print(f"save.json deleted.")
        create_new_save()
    else:
        # print(f"save.json doesn't exist.")
        pass
