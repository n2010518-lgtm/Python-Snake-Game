
"""
NEON SNAKE
Main game engine
"""

from enum import Enum

import settings
from snake import Snake
from food import Food
from highscore import HighScore


class GameStatus(Enum):
    READY = "ready"
    PLAYING = "playing"
    PAUSED = "paused"
    GAME_OVER = "game_over"


class Game:

    def __init__(self, highscore_file="highscore.json"):
        self.highscore = HighScore(highscore_file)
        self.reset()

    def reset(self):
        """Create a new game and reset all values."""

        self.snake = Snake()
        self.food = Food(self.snake.get_body())

        self.score = 0
        self.speed = settings.INITIAL_SPEED

        self.status = GameStatus.READY
        self.won = False

    def start(self):
        """Start the game."""

        if self.status == GameStatus.READY:
            self.status = GameStatus.PLAYING

    def pause(self):
        """Pause the game."""

        if self.status == GameStatus.PLAYING:
            self.status = GameStatus.PAUSED

    def resume(self):
        """Resume a paused game."""

        if self.status == GameStatus.PAUSED:
            self.status = GameStatus.PLAYING

    def toggle_pause(self):
        """Switch between playing and paused."""

        if self.status == GameStatus.PLAYING:
            self.pause()
        elif self.status == GameStatus.PAUSED:
            self.resume()

    def update(self):
        """Update one game step."""

        if self.status != GameStatus.PLAYING:
            return

        next_head = self.snake.get_next_head()
        eating = self.food.is_eaten(next_head)

        x, y = next_head

        # Wall collision
        if (
            x < 0 or x >= settings.COLS
            or y < 0 or y >= settings.ROWS
        ):
            self.status = GameStatus.GAME_OVER
            return

        # Self collision
        body = self.snake.get_body()
        collision_body = body if eating else body[:-1]

        if next_head in collision_body:
            self.status = GameStatus.GAME_OVER
            return

        # Move snake
        self.snake.move(grow=eating)

        # Eat food
        if eating:
            self.score += settings.FOOD_SCORE

            # Update saved record
            self.highscore.update(self.score)

            # Spawn new food
            spawned = self.food.spawn(self.snake.get_body())

            if not spawned:
                self.won = True
                self.status = GameStatus.GAME_OVER
                return

            # Increase game speed
            self.speed = min(
                settings.MAX_SPEED,
                self.speed + settings.SPEED_INCREASE
            )

    def set_direction(self, direction):
        """Change snake direction."""

        if self.status == GameStatus.PLAYING:
            self.snake.change_direction(direction)

    def get_score(self):
        return self.score

    def get_best_score(self):
        return self.highscore.get_best_score()

    def get_speed(self):
        return self.speed

    def get_snake(self):
        return self.snake.get_body()

    def get_food(self):
        return self.food.get_position()

    def get_status(self):
        return self.status.value

    def is_game_over(self):
        return self.status == GameStatus.GAME_OVER

    def is_won(self):
        return self.won

    def is_playing(self):
        return self.status == GameStatus.PLAYING

    def is_paused(self):
        return self.status == GameStatus.PAUSED

    def get_state(self):
        """Return all data needed by the interface."""

        return {
            "snake": self.get_snake(),
            "food": self.get_food(),
            "score": self.get_score(),
            "best_score": self.get_best_score(),
            "speed": self.get_speed(),
            "status": self.get_status(),
            "game_over": self.is_game_over(),
            "won": self.is_won()
        }
