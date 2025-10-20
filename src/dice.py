"""Module defining the Dice class used in the Pig Dice Game."""

import random

class Dice:
    """A class representing a single die."""

    def __init__(self, num_sides=6):
        """Initialize a new die."""
        self.num_sides = num_sides
        self.value = 1  # default starting value

    def roll(self):
        """Roll the die randomly and update its value."""
        self.value = random.randint(1, self.num_sides)
        return self.value

    def __str__(self):
        """Return a string representation of the die's current value."""
        return str(self.value)
