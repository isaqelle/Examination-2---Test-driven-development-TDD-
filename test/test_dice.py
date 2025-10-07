# import pytest
# from proj import Dice

# def test_roll_returns_int():
#     dice = Dice()
#     result = dice.roll()
#     assert isinstance(result, int), "Roll should return an integer"

# def test_roll_in_range():
#     dice = Dice()
#     for _ in range(100):  # roll multiple times
#         result = dice.roll()
#         assert 1 <= result <= 6, "Roll should be between 1 and 6"

# def test_custom_sides():
#     dice = Dice(num_sides=20)
#     for _ in range(100):
#         result = dice.roll()
#         assert 1 <= result <= 20, "Roll should be within the custom number of sides"


import unittest

import Dice from Dice


class Test_Dice_Roll(unittest.TestCase):

    def test_init_default_object(self):
        """Instantiate an object and check its properties"""
        res = Dice()
        exp = Dice
        self.assertIsInstance(res, exp)

    def test_roll_dice(self):
        """Test roll dice"""
        dice = Dice()
        res = dice.roll()
        exp = 1 <= res <= 6
        self.assertTrue(exp)