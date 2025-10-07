import random

# This class has one method, roll(). 
# The class implements a dice with 6 sides.
# The method then rolls the dice and it will result in a number beteween 1-6.
# The number gets returned.

class Dice:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return random.randint(1, self.num_sides)