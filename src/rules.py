## Importing libraries

## Importing files
from src import translate

def end_game(dealerNB, playerNB):
    print(f"{translate.translate('Final Score')}: ")
    print(f"-{translate.translate('The Dealer has')}: {dealerNB}!")
    print(f"-{translate.translate('The Player has')}: {playerNB}!")

    if (playerNB > 21):
        print(f"{translate.translate('The Dealer won')}.")
        return 
    elif (dealerNB > 21):
        print(f"{translate.translate('The Player won')}.")
        return 

    if (dealerNB > playerNB):
        print(f"{translate.translate('The Dealer won')}.")
    elif (playerNB > dealerNB):
        print(f"{translate.translate('The Player won')}.")
    else:
        print(f"{translate.translate('No winners')}.")

    return 

def ace_1_or_11():
    ace_choice = 0

    while ace_choice == 0:
        answer = input(translate.translate("1 or 11")+": ").lower()
        if (answer == "1"):
            ace_choice = 1
            return 1
        elif (answer == "11"):
            ace_choice = 1
            return 11
        else:
            print(f"{translate.translate("Input not taken into account")}")
