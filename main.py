## Importing libraries
import sys

## Importing files
from src import game
from src import translate

def main():
    game.game_loop()
    return 0

## By default, execute the main function...
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{translate.translate("Game interrupted")}.")
        sys.exit(0)
