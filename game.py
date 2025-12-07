from classes import Die, Dice, ScoreSheet
from constants import SEPARATOR, ACTIONS


def turn(dice: Dice, score_sheet: ScoreSheet) -> bool:

    user_input = input(ACTIONS)

    if user_input == 'Q':
        return False

    else:
        if user_input == 'S':
            print('\n')
            score_sheet.show()

        if user_input == 'R':
            print('\n')
            dice.roll(verbose=True)
            dice.show()
            score_sheet.play_all_dice(dice)
            # todo: implement

        if user_input == 'O':
            print('\n')
            white_dice = input('Which white dice? ')
            (white1_value, white2_value) = white_dice.split(',')
            white1 = Die('white')
            white1.value = int(white1_value)
            white2 = Die('white')
            white2.value = int(white2_value)
            score_sheet.play_white_dice(white1, white2)
            # todo: implement

        if user_input == 'C':
            print('\n')
            color = input('Which color? ')
            score_sheet.retire_row(color)
            score_sheet.show()

        print(SEPARATOR)
        input('Press enter to continue...')
        return True
