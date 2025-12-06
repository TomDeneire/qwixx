import random


class Die:
    def __init__(self, color: str):
        self.value = None
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


class Dice:
    def __init__(self):
        self.white1 = Die('white')
        self.white2 = Die('white')
        self.red = Die('red')
        self.blue = Die('blue')
        self.green = Die('green')

    def roll(self):
        self.white1.roll()
        self.white2.roll()
        self.red.roll()
        self.blue.roll()
        self.green.roll()

    def show(self):
        if self.white1.active:
            print(f'White 1: {self.white1}')
        if self.white2.active:
            print(f'White 2: {self.white2}')
        if self.red.active:
            print(f'Red: {self.red}')
        if self.blue.active:
            print(f'Blue: {self.blue}')
        if self.green.active:
            print(f'Green: {self.green}')
