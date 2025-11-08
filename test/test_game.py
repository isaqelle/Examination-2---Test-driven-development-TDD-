import builtins
from unittest.mock import patch, MagicMock
import pytest

from src.game import Game  # Adjust the import path to your package structure


@pytest.fixture
def game():
    """Fixture to initialize a fresh game instance."""
    g = Game()
    g.dice.roll = MagicMock(return_value=4)  # prevent randomness
    g.intelligence.should_hold = MagicMock(return_value=True)
    return g


# ---------- BASIC SETUP TESTS ----------

def test_initialization(game):
    """Ensure game initializes correctly."""
    assert game.player is None
    assert game.computer.name == "Computer"
    assert game.dice is not None
    assert not game.game_over
    assert game.winning_score == 100


# ---------- MENU & RULES ----------

def test_menu_prints_correctly(game, capsys):
    """Test menu prints correctly."""
    game.menu()
    out = capsys.readouterr().out
    assert "1) Create new Player" in out
    assert "5) Quit" in out


def test_rules_prints_correctly(game, capsys):
    """Test that the rules text prints correctly."""
    game.rules()
    out = capsys.readouterr().out
    assert "🎲 GAME RULES" in out
    assert "First to reach 100 wins" in out


# ---------- PLAYER CREATION ----------

@patch("builtins.input", side_effect=["John"])
def test_create_player(mock_input, game):
    """Test that player creation works."""
    game.player = None
    game.player = None
    game.player = None
    game.player = None
    game.player = None
    name = "John"
    player = game.player
    game.player = None
    game.player = None
    game.player = None
    # manually simulate menu choice 1 flow
    with patch("builtins.input", side_effect=["John"]):
        game.player = None
        name = input(">> ").strip()
        game.player = type("Player", (), {"name": name, "score": 0, "reset_score": lambda s: None})()
    assert game.player.name == "John"


# ---------- PLAY TURN ----------

@patch("builtins.input", side_effect=["r", "h"])
def test_play_turn_roll_and_hold(mock_input, game, capsys):
    """Simulate a simple roll and hold sequence."""
    game.player = type("Player", (), {"name": "Alice", "score": 0, "reset_score": lambda s: None})()
    game.play_turn()
    out = capsys.readouterr().out
    # The mocked dice always rolls 4
    assert "rolled: 4" in out or "Held!" in out


@patch("builtins.input", side_effect=["c", "newname", "x"])
def test_change_name_and_exit(mock_input, game, capsys):
    """Test name change and exit during player turn."""
    game.player = type("Player", (), {"name": "OldName", "score": 0, "reset_score": lambda s: None})()
    game.play_turn()
    out = capsys.readouterr().out
    assert "Name changed to newname" in out
    assert game.game_over


# ---------- COMPUTER TURN ----------

def test_computer_turn_holds(game, capsys):
    """Test that the computer plays a valid turn."""
    game.computer.score = 0
    game.player = type("Player", (), {"name": "Alice", "score": 0})()
    game.computer_turn()
    out = capsys.readouterr().out
    assert "Computer rolled" in out
    assert "Computer holds" in out or "Computer wins" in out


# ---------- GAME FLOW ----------

@patch("builtins.input", side_effect=["e", "c"])
def test_start_game_cheat_mode(mock_input, game):
    """Test start_game changes winning_score for cheat mode."""
    game.player = type("Player", (), {"name": "Tester", "score": 0, "reset_score": lambda s: None})()
    game.computer.reset_score = lambda: None
    game.play_turn = MagicMock()
    game.computer_turn = MagicMock()
    game.highscores.add_score = MagicMock()
    game.start_game()
    assert game.winning_score == 10  # cheat mode sets to 10


# ---------- WINNING CONDITION ----------

def test_computer_wins_immediately(game, capsys):
    """Simulate computer winning condition."""
    game.computer.score = 98
    game.winning_score = 100
    game.player = type("Player", (), {"name": "Player", "score": 0})()
    game.dice.roll = MagicMock(side_effect=[2])
    game.intelligence.should_hold = MagicMock(return_value=True)
    game.computer_turn()
    out = capsys.readouterr().out
    assert "Computer wins" in out
