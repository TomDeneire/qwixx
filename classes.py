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
        print(f'White 1: {self.white1}')
        print(f'White 2: {self.white2}')
        print(f'Red: {self.red}')
        print(f'Blue: {self.blue}')
        print(f'Green: {self.green}')
