from proj import Dice
# This class handles the rolls of the dice.
# It has three methods:
#   roll_all()
#       - rolls all dice and stores the result
#   get_total()
#       - sum of rolls
#   __str__() 
#       - string for printing results formatting

class DiceHand:
    def __init__(self, num_dice=1, num_sides=6):
        self.dice = [Dice(num_sides) for i in range(num_dice)]
        self.last_roll = []
    
    def roll_all(self):
        self.last_roll = [die.roll() for die in self.dice]
        return self.last_roll

    def get_total(self):
        return sum(self.last_roll)
    
    def __str__(self):
        return f"Rolled: {self.last_roll} (total = {self.get_total()})"