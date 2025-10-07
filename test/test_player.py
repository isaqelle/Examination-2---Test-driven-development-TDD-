import pytest
from proj.player import Player

class TestPlayer:
    def setup_method(self):
        self.player = Player("Isabelle")

    def test_initial_name(self):
        self.player.name == "Isabelle"

    def test_initial_score_is_zero(self):
        assert self.player.score == 0

    def test_add_points_once(self):
        self.player.add_points(5)
        assert self.player.score == 5

    def test_add_points_multiple_times(self):
        self.player.add_points(5)
        self.player.add_points(10)
        assert self.player.score == 15

    def test_add_zero_points(self):
        self.player.add_points(0)
        assert self.player.score == 0

    def test_reset_score_after_points(self):
        self.player.add_points(12)
        self.player.reset_score()
        assert self.player.score == 0


    def test_reset_score_multiple_times(self):
        self.player.add_points(50)
        self.player.reset_score()
        self.player.reset_score()
        assert self.player.score == 0

    def test_str_method_format(self):
        self.player.add_points(25)
        result = str(self.player)
        assert result == "Isabelle: 25 points"

    def test_str_after_reset(self):
        self.player.add_points(10)
        self.player.reset_score()
        assert str(self.player) == "Isabelle: 0 points"

    def test_score_increases_incrementally(self):
        for i in range(1,6):
            self.player.add_points(i)
        assert self.player.score == sum(range(1,6))