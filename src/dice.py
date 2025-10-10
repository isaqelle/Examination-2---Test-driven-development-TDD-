import random

class Dice:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
        self.value = 1  # default starting value, can be whatever you prefer

    def roll(self):
        self.value = random.randint(1, self.num_sides)
        return self.value

    def __str__(self):
        return str(self.value)
