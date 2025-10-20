"""Module defining the computer player Agnetha for the Pig Dice Game."""

import random

class Intelligence:
    """Computer player AI for Pig Dice Game (easy or hard difficulty)."""

    def __init__(self, difficulty='easy'):
        """Initialize computer player with difficulty ('easy' or 'hard')."""
        difficulty = difficulty.lower()
        if difficulty not in ['easy', 'hard']:
            raise ValueError('Difficulty must be "easy" or "hard".')
        self.name = 'Computer Agnetha'
        self.score = 0
        self.difficulty = difficulty

    def add_points(self, points):
        """Add points to the computer's score."""
        self.score += points

    def reset_score(self):
        """Reset the computer's score to zero."""
        self.score = 0

    def should_hold(self, turn_total, opponent_score):
        """Decide whether to hold based on difficulty and scores."""
        if self.difficulty == 'easy':
            return turn_total >= 10 or random.random() < 0.1

        # Hard difficulty logic
        if self.difficulty == 'hard':
            if self.score + turn_total >= 100:
                return True
            if self.score < opponent_score and turn_total >= 15:
                return True
            if turn_total >= 20:
                return True
            return False
