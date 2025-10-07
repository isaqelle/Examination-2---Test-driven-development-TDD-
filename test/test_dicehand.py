import pytest
from unittest.mock import MagicMock
from proj.dicehand import DiceHand

# Using MagicMock or monkeypatch lets you test predictable outputs even with randomness.

@pytest.fixture
def fixed_dicehand(monkeypatch):
    hand = DiceHand(num_dice=3)

    for die in hand.dice:
        die.roll = MagicMock(return_value=4)
    
    return hand

def test_roll_all(fixed_dicehand):
    rolls = fixed_dicehand.roll_all()
    assert rolls == [4,4,4]

def test_get_total(fixed_dicehand):
    fixed_dicehand.roll_all()
    assert fixed_dicehand.get_total() == 12
    # 4+4+4

def test_str(fixed_dicehand):
    fixed_dicehand.roll_all()
    result = str(fixed_dicehand)
    assert result == "Rolled: [4, 4, 4] (total = 12)"