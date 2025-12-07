from classes import Dice, ScoreSheet
from constants import GAME_LOGO, SEPARATOR
from game import turn


def main():
    print(GAME_LOGO)
    print(SEPARATOR)

    game_active = True
    dice = Dice()
    score_sheet = ScoreSheet()

    while game_active:
        game_active = turn(dice, score_sheet)


if __name__ == '__main__':
    main()
