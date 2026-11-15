
"""
NEON SNAKE
High Score Manager
"""

import json
from pathlib import Path


class HighScore:

    def __init__(self, file_path="highscore.json"):
        self.file_path = Path(file_path)
        self.best_score = self.load()

    def load(self):
        """Load saved record from JSON."""

        if not self.file_path.exists():
            return 0

        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                data = json.load(file)

            score = data.get("best_score", 0)

            if type(score) is not int or score < 0:
                return 0

            return score

        except (OSError, json.JSONDecodeError, AttributeError):
            return 0

    def save(self):
        """Save record safely."""

        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        temporary_file = self.file_path.with_suffix(".tmp")

        with temporary_file.open("w", encoding="utf-8") as file:
            json.dump(
                {"best_score": self.best_score},
                file,
                indent=4
            )

        temporary_file.replace(self.file_path)

    def update(self, score):
        """Update record if new score is higher."""

        if score > self.best_score:
            self.best_score = score
            self.save()
            return True

        return False

    def get_best_score(self):
        return self.best_score
