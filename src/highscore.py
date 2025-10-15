# highscore.py
import json
import os

class HighScore:
    FILE_PATH = "highscores.json"

    def __init__(self):
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
        """Display all scores, and highlight the highest."""
        if not self.scores:
            print("No scores yet!")
            return

        highest = self.get_highest()
        print("\n🏆 All-time Scores 🏆")
        for entry in sorted(self.scores, key=lambda x: x["score"], reverse=True):
            marker = " <- Highest!" if entry == highest else ""
            print(f"{entry['name']}: {entry['score']}{marker}")
        print()
    
    def save(self):
        """Save scores to a file."""
        try:
            with open(self.FILE_PATH, "w") as f:
                json.dump(self.scores, f)
        except OSError:
            print("Error: Could not save highscores.")

    def load(self):
        """Load scores from a file."""
        if os.path.exists(self.FILE_PATH):
            try:
                with open(self.FILE_PATH, "r") as f:
                    self.scores = json.load(f)
            except (OSError, json.JSONDecodeError):
                self.scores = []
