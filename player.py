## Importing libraries
import time

## Importing libraries
import translate

def player_rolls(cards, player_score, player_hand):
    card = cards.pop(0)

    player_score += card["value"]
    player_hand.append(card)

    print(f"{translate.translate("The Player rolls a")} {card["rank"] + card["suit"]}.")
    print(f"{translate.translate("The Player has")}: {player_score}.")
    
    time.sleep(1)

    return player_score

def reroll(cards, player_score, player_hand):
    reroll = 0

    yes_word = translate.translate("yes")
    no_word = translate.translate("no")

    while reroll == 0 and player_score < 21:
        answer = input(translate.translate("Does the Player want to hit ? (yes / no)")+": ").lower()
        if (answer == yes_word or answer == yes_word[0]):
            player_score = player_rolls(cards, player_score, player_hand)
        elif (answer == no_word or answer == no_word[0]):
            reroll = 1
        else:
            print(f"{translate.translate("Input not taken into account")}")

    return player_score

def print_cards(player_hand):
    print(" ".join(card["name"] for card in player_hand))
    