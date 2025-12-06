from classes import Dice
from constants import GAME_LOGO


def main():
    print(f'Hello from \n{GAME_LOGO}')
    print('Rolling dice...')
    dice = Dice()
    dice.roll()
    dice.show()
    dice.roll()
    dice.show()


if __name__ == '__main__':
    main()
