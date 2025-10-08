""""
Player class for Pig Dice Game
Represents a human player and tracks their score.
"""


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_points(self, points):
        self.score += points

    # Reset the player's score to zero.
    def reset_score(self):
        self.score = 0
    #A summary of the player's current score.
    def __str__(self):
        return f"{self.name}: {self.score} points"