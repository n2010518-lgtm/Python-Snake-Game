
import tempfile
import unittest
from pathlib import Path

from highscore import HighScore
from game import Game


class TestHighScore(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.file_path = Path(self.temp_dir.name) / "highscore.json"

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_initial_record_is_zero(self):
        record = HighScore(self.file_path)

        self.assertEqual(record.get_best_score(), 0)

    def test_save_and_load_record(self):
        record = HighScore(self.file_path)
        record.update(150)

        loaded_record = HighScore(self.file_path)

        self.assertEqual(loaded_record.get_best_score(), 150)

    def test_lower_score_does_not_replace_record(self):
        record = HighScore(self.file_path)

        record.update(200)
        record.update(100)

        self.assertEqual(record.get_best_score(), 200)

    def test_game_saves_record_after_eating(self):
        game = Game(highscore_file=self.file_path)
        game.start()

        game.food.position = game.snake.get_next_head()
        game.update()

        self.assertEqual(game.get_best_score(), 10)

        new_game = Game(highscore_file=self.file_path)

        self.assertEqual(new_game.get_best_score(), 10)


if __name__ == "__main__":
    unittest.main()

