import os
import json
import pytest
from src.highscore import HighScore

TEST_FILE = "test_highscores.json"


@pytest.fixture(autouse=True)
def clean_test_file(monkeypatch):
    """Ensure a clean test environment for each test."""
    # Redirect FILE_PATH to a temporary test file
    monkeypatch.setattr(HighScore, "FILE_PATH", TEST_FILE)
    # Remove test file if it exists
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    yield
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


def test_initial_load_no_file():
    hs = HighScore()
    assert hs.scores == []


def test_add_score_and_save_load():
    hs = HighScore()
    hs.add_score("Alice", 100)
    assert len(hs.scores) == 1
    assert hs.scores[0] == {"name": "Alice", "score": 100}

    # Check file actually written
    assert os.path.exists(TEST_FILE)

    # Load from file again
    hs2 = HighScore()
    assert hs2.scores == [{"name": "Alice", "score": 100}]


def test_get_highest_returns_none_when_empty():
    hs = HighScore()
    assert hs.get_highest() is None


def test_get_highest_returns_correct_entry():
    hs = HighScore()
    hs.add_score("Alice", 100)
    hs.add_score("Bob", 200)
    hs.add_score("Charlie", 150)
    highest = hs.get_highest()
    assert highest["name"] == "Bob"
    assert highest["score"] == 200


def test_display_all_with_scores(capsys):
    hs = HighScore()
    hs.add_score("Alice", 50)
    hs.add_score("Bob", 100)
    hs.display_all()
    output = capsys.readouterr().out

    assert "All-time Scores" in output
    assert "Alice" in output
    assert "Bob" in output
    assert "<- Highest" in output  # should mark the highest score


def test_display_all_no_scores(capsys):
    hs = HighScore()
    hs.display_all()
    output = capsys.readouterr().out
    assert "No scores yet!" in output


def test_load_with_corrupted_json(monkeypatch):
    # Write invalid JSON
    with open(TEST_FILE, "w") as f:
        f.write("{ invalid json")

    hs = HighScore()
    assert hs.scores == []  # fallback to empty


def test_save_handles_oserror(monkeypatch):
    hs = HighScore()
    hs.add_score("Alice", 100)

    def raise_oserror(*args, **kwargs):
        raise OSError("disk full")

    monkeypatch.setattr("builtins.open", raise_oserror)
    hs.save()  # should not raise


def test_display_all_with_custom_width(monkeypatch, capsys):
    hs = HighScore()
    hs.add_score("Zoe", 75)
    # Simulate being attached to a game object
    hs.game = type("MockGame", (), {"width": 40})()
    hs.display_all()
    output = capsys.readouterr().out
    assert "Zoe" in output
    # Skip first empty line due to leading "\n"
    border_line = output.splitlines()[1]
    assert len(border_line) == 40  # top border length matches width

