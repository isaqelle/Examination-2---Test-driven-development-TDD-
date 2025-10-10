import pytest
import unittest
from src.dice import Dice



class Test_Dice_Roll(unittest.TestCase):

    def test_init_default_object(self):
        res = Dice()
        exp = Dice
        self.assertIsInstance(res, exp)

    def test_roll_dice(self):
        dice = Dice()
        res = dice.roll()
        exp = 1 <= res <= 6
        self.assertTrue(exp)