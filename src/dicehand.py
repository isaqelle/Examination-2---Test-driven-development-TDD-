from .dice import Dice

class DiceHand:
    """ A class to represent a hand of dice. """

    def __init__(self, num_dice=1, num_sides=6):
        """ Initialize a DiceHand with a given number of dice and sides. """
        self.dice = [Dice(num_sides) for i in range(num_dice)]
        self.last_roll = []
    
    def roll_all(self):
        """Roll all dice in the hand and store the results.

        Returns a list of integers representing the roll of each die.
        """
        self.last_roll = [die.roll() for die in self.dice]
        return self.last_roll

    def get_total(self):
        """
        Calculate the total of the last roll.

        Returns sum of the dice values in last_roll.
        """
        return sum(self.last_roll)
    
    def __str__(self):
        """Return a formatted string of the last roll and its total."""
        return f"Rolled: {self.last_roll} (total = {self.get_total()})"
