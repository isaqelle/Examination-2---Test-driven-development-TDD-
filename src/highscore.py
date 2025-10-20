"""Module to manage highscores for the Pig Dice Game."""

import json
import os

WIDTH = 53

class HighScore:
    """Class to manage highscores: save, load, and display."""

    FILE_PATH = "highscores.json"

    def __init__(self):
        """Initialize HighScore and load scores from file."""
        self.scores = []  # list of dicts: {"name": ..., "score": ...}
        self.load()

    def add_score(self, name, score):
        """Add a new score and save it."""
        self.scores.append({"name": name, "score": score})
        self.save()

    def get_highest(self):
        """Return the entry with the highest score."""
        if not self.scores:
            return None
        return max(self.scores, key=lambda x: x["score"])

    def display_all(self):
        """Print all highscores in a formatted ASCII frame."""
        highest = self.get_highest()
        display_width = WIDTH

        print("\n╔" + "═" * (display_width - 2) + "╗")
        print("║" + " " * (display_width - 2) + "║")
        print("║" + "🏆 All-time Scores 🏆".center(display_width - 4) + "║")
        print("║" + " " * (display_width - 2) + "║")

        if self.scores:
            for entry in sorted(self.scores, key=lambda x: x["score"], reverse=True):
                line = f"{entry['name']}: {entry['score']}"
                if highest and entry == highest:
                    line += "  <- Highest!"
                print("║" + line.center(display_width - 2) + "║")
        else:
            print("║" + "No scores yet!".center(display_width - 2) + "║")

        print("║" + " " * (display_width - 2) + "║")
        print("╚" + "═" * (display_width - 2) + "╝")

    def save(self):
        """Save scores to a JSON file."""
        try:
            with open(self.FILE_PATH, "w", encoding="utf-8") as f:
                json.dump(self.scores, f)
        except OSError:
            print("Error: Could not save highscores.")

    def load(self):
        """Load scores from a JSON file."""
        if os.path.exists(self.FILE_PATH):
            try:
                with open(self.FILE_PATH, "r", encoding="utf-8") as f:
                    self.scores = json.load(f)
            except (OSError, json.JSONDecodeError):
                self.scores = []
