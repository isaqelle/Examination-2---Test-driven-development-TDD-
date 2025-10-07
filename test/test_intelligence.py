import pytest
import random
from src.intelligence import Intelligence


class TestIntelligence:
    def setup_method(self):
        random.seed(0)  
        self.computer_easy = Intelligence("easy")
        self.computer_hard = Intelligence("hard")

    def test_initial_name(self):
        assert self.computer_easy.name == "Computer Agnetha"

    def test_initial_score_is_zero(self):
        assert self.computer_easy.score == 0
        assert self.computer_hard.score == 0

    def test_add_points_once(self):
        self.computer_easy.add_points(10)
        assert self.computer_easy.score == 10

    def test_add_points_multiple_times(self):
        self.computer_easy.add_points(5)
        self.computer_easy.add_points(15)
        assert self.computer_easy.score == 20

    def test_reset_score(self):
        self.computer_easy.add_points(40)
        self.computer_easy.reset_score()
        assert self.computer_easy.score == 0

    def test_reset_score_multiple_times(self):
        self.computer_hard.add_points(50)
        self.computer_hard.reset_score()
        self.computer_hard.reset_score()
        assert self.computer_hard.score == 0

    def test_easy_should_hold_when_turn_total_high(self):
        result = self.computer_easy.should_hold(12, 50)
        assert result is True

    def test_easy_random_hold_probability(self):
        holds = sum(self.computer_easy.should_hold(5, 0) for _ in range(1000))
        assert 50 < holds < 150  

    def test_hard_should_hold_when_can_win(self):
        self.computer_hard.score = 95
        result = self.computer_hard.should_hold(10, 80)
        assert result is True  

    def test_hard_should_hold_when_turn_total_high(self):
        result = self.computer_hard.should_hold(25, 50)
        assert result is True  

    def test_hard_should_hold_when_behind_and_turn_total_mid(self):
        self.computer_hard.score = 60
        result = self.computer_hard.should_hold(15, 80)
        assert result is True  

    def test_hard_should_not_hold_when_turn_total_low(self):
        self.computer_hard.score = 40
        result = self.computer_hard.should_hold(5, 60)
        assert result is False

    def test_hard_should_not_hold_when_not_behind_and_turn_total_low(self):
        self.computer_hard.score = 80
        result = self.computer_hard.should_hold(10, 50)
        assert result is False

    def test_invalid_difficulty_raises_value_error(self):
        with pytest.raises(ValueError):
            Intelligence("medium")

    def test_difficulty_is_converted_to_lowercase(self):
        comp = Intelligence("HARD")
        assert comp.difficulty == "hard"

    def test_add_zero_points_does_not_change_score(self):
        self.computer_easy.add_points(0)
        assert self.computer_easy.score == 0
