"""
Intelligence class for computer player in Pig Dice Game. 
Supports two difficulty levels, easy and hard.

"""
import pytest 
import random 

class Intelligence:
    def __init__(self, difficulty = 'easy'):
        difficulty = difficulty.lower()
        if difficulty not in ['easy', 'hard']:
            raise ValueError('Difficulty must be "easy" or "hard".')
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
            elif self.score < opponent_score and turn_total >= 15:
                return True # take a moderate risk if behind
            elif turn_total >= 20:
                return True # holds after building up a good turn total
            else: 
                return False
