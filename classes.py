import random
from typing import Dict, OrderedDict

from constants import RED, YELLOW, GREEN, BLUE, RESET


class Die:
    def __init__(self, color: str):
        self.value = 0
        self.color = color
        self.active = True

    def roll(self):
        if not self.active:
            raise Exception('Die is not active')
        else:
            self.value = random.randint(1, 6)

    def retire(self):
        self.active = False

    def __str__(self):
        return str(self.value)


class Cell:
    def __init__(self, value: int):
        self.value = value
        self.active = True
        self.checked = False

    def __str__(self):
        return f"{self.value} = {'X' if self.checked else 'O'}"

    def check(self):
        self.checked = True
        self.retire()

    def retire(self):
        self.active = False


class Dice:
    def __init__(self):
        self.white1 = Die('white')
        self.white2 = Die('white')
        self.red = Die('red')
        self.yellow = Die('yellow')
        self.green = Die('green')
        self.blue = Die('blue')

    def roll(self, verbose: bool = False):
        if verbose:
            print('Rolling dice!\n')
        self.white1.roll()
        self.white2.roll()
        self.red.roll()
        self.yellow.roll()
        self.green.roll()
        self.blue.roll()

    def show(self):
        if self.white1.active:
            print(f'White 1: {self.white1}')
        if self.white2.active:
            print(f'White 2: {self.white2}')
        if self.red.active:
            print(f'Red: {self.red}')
        if self.yellow.active:
            print(f'Yellow: {self.yellow}')
        if self.green.active:
            print(f'Green: {self.green}')
        if self.blue.active:
            print(f'Blue: {self.blue}')


class ScoreSheet:
    def __init__(self):
        self.score = 0
        self.rows = OrderedDict()
        for color in ['red', 'yellow', 'green', 'blue']:
            self.rows[color] = OrderedDict()
        for value in range(2, 13):
            self.rows['red'][value] = Cell(value)
            self.rows['yellow'][value] = Cell(value)
        for value in range(12, 1, -1):
            self.rows['green'][value] = Cell(value)
            self.rows['blue'][value] = Cell(value)

    def show(self):
        print(
            f'\n{RED}{[str(cell) for cell in self.rows["red"].values()]}{RESET}'
        )
        print(
            f'\n{YELLOW}{[str(cell) for cell in self.rows["yellow"].values()]}{RESET}'
        )
        print(
            f'\n{GREEN}{[str(cell) for cell in self.rows["green"].values()]}{RESET}'
        )
        print(
            f'\n{BLUE}{[str(cell) for cell in self.rows["blue"].values()]}{RESET}'
        )
        print(f'\nScore: {self.score}')

    def retire_row(self, color: str):
        pass

    def penalty(self):
        print('\nNo cell to check!\n')
        self.score -= 5
        pass

    def play_all_dice(self, dice: Dice):
        pass

    def play_white_dice(self, white1: Die, white2: Die):
        possible_checks = {
            'red': [],
            'yellow': [],
            'green': [],
            'blue': [],
        }
        for color, cells in self.rows.items():
            for cell in cells.values():
                if cell.value == white1.value + white2.value:
                    if cell.active:
                        possible_checks[color].append(cell)
        # for now, just take the first one
        cell_to_check = None
        for color in possible_checks:
            if len(possible_checks[color]) > 0:
                cell_to_check = possible_checks[color][0]
                self.rows[color][cell_to_check.value].check()
                print(
                    f'{eval(color.upper())}Checking {cell_to_check.value}{RESET}'
                )
                for cell in self.rows[color].values():
                    if cell.value == cell_to_check.value:
                        break
                    cell.retire()
                break
        if not cell_to_check:
            self.penalty()
