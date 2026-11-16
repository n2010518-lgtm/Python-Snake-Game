
import unittest

from game import Game


class TestSnakeGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_game_initialization(self):
        self.assertEqual(self.game.get_score(), 0)
        self.assertEqual(self.game.get_status(), "ready")
        self.assertEqual(len(self.game.get_snake()), 3)

    def test_game_start(self):
        self.game.start()

        self.assertTrue(self.game.is_playing())

    def test_snake_moves_right(self):
        self.game.start()

        old_head = self.game.get_snake()[0]
        self.game.update()
        new_head = self.game.get_snake()[0]

        self.assertEqual(
            new_head,
            (old_head[0] + 1, old_head[1])
        )

    def test_snake_eats_food(self):
        self.game.start()

        self.game.food.position = self.game.snake.get_next_head()
        self.game.update()

        self.assertEqual(self.game.get_score(), 10)
        self.assertEqual(len(self.game.get_snake()), 4)

    def test_food_does_not_spawn_inside_snake(self):
        body = self.game.get_snake()
        food = self.game.get_food()

        self.assertNotIn(food, body)

    def test_wall_collision(self):
        self.game.start()

        for _ in range(14):
            self.game.update()

        self.assertTrue(self.game.is_game_over())
        self.assertEqual(self.game.get_status(), "game_over")

    def test_pause_and_resume(self):
        self.game.start()
        self.game.pause()

        self.assertTrue(self.game.is_paused())

        old_body = self.game.get_snake()
        self.game.update()

        # Snake must not move while paused
        self.assertEqual(self.game.get_snake(), old_body)

        self.game.resume()

        self.assertTrue(self.game.is_playing())

    def test_reset_game(self):
        self.game.start()
        self.game.score = 100
        self.game.reset()

        self.assertEqual(self.game.get_score(), 0)
        self.assertEqual(self.game.get_status(), "ready")
        self.assertEqual(len(self.game.get_snake()), 3)


if __name__ == "__main__":
    unittest.main()
