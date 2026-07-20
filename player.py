## Importing libraries
import time

## Importing libraries
import translate

def player_rolls(cards, playerNB):
    card = cards.pop(0)
    playerNB += card

    print(f"{translate.translate("The Player rolls a")} {card}.")
    print(f"{translate.translate("The Player has")}: {playerNB}.")
    
    time.sleep(1)

    return playerNB

def reroll(cards, playerNB):
    reroll = 0

    yes_word = translate.translate("yes")
    no_word = translate.translate("no")

    while reroll == 0 and playerNB < 21:
        answer = input(translate.translate("Does the Player want to hit ? (yes / no)")+": ").lower()
        if (answer == yes_word or answer == yes_word[0]):
            playerNB = player_rolls(cards, playerNB)
        elif (answer == no_word or answer == no_word[0]):
            reroll = 1
        else:
            print(f"{translate.translate("Input not taken into account")}")

    return playerNB            
    