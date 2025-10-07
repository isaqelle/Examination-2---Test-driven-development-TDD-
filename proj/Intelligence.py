"""
Intelligence class for computer player in Pig Dice Game. 
Supports two difficulty levels, easy and hard.

"""

import random 

class Intelligence:
    def __init__(self, difficulty = 'easy'):
        self.name = 'Computer Agnetha'
        self.score = 0
        self.difficulty = difficulty.lower()

    def add_points(self, points):
        self.score += points

    def reset_score(self):
        self.score = 0

    def should_hold(self, turn_total, opponent_score):
        """Return True if the computer player decides to hold, otherwise False. """
        if self.difficulty == 'easy':
            return turn_total >=10 or random.random() <0.1 #10% chance to randomly hold
        
        elif self.difficulty == 'hard':
            if self.score + turn_total >= 100:
                return True # win condition
            elif turn_total >= 20:
                return True # holds after building up a good turn total
            elif (100 - self.score) < (100 - opponent_score) and turn_total >= 15:
                return True #takes mild risks if behind
            else: 
                return False

        else:
            raise ValueError('Difficulty must be "easy" or "hard".')
        
