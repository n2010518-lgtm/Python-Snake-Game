
"""
NEON SNAKE
Main game engine
"""

import settings
from snake import Snake
from food import Food


class Game:

    def __init__(self):
        self.reset()

    def reset(self):
        # IMPORTANT: Create snake FIRST
        self.snake = Snake()

        # Create food AFTER snake
        self.food = Food(self.snake.get_body())

        self.score = 0
        self.speed = settings.INITIAL_SPEED

        self.game_over = False
        self.won = False

    def update(self):
        if self.game_over:
            return

        next_head = self.snake.get_next_head()
        eating = self.food.is_eaten(next_head)

        x, y = next_head

        # Wall collision
        if (
            x < 0 or x >= settings.COLS
            or y < 0 or y >= settings.ROWS
        ):
            self.game_over = True
            return

        # Self collision
        body = self.snake.get_body()
        collision_body = body if eating else body[:-1]

        if next_head in collision_body:
            self.game_over = True
            return

        # Move snake
        self.snake.move(grow=eating)

        # Eat food
        if eating:
            self.score += settings.FOOD_SCORE

            spawned = self.food.spawn(self.snake.get_body())

            if not spawned:
                self.won = True
                self.game_over = True
                return

            self.speed = min(
                settings.MAX_SPEED,
                self.speed + settings.SPEED_INCREASE
            )

    def set_direction(self, direction):
        if not self.game_over:
            self.snake.change_direction(direction)

    def get_score(self):
        return self.score

    def get_speed(self):
        return self.speed

    def get_snake(self):
        return self.snake.get_body()

    def get_food(self):
        return self.food.get_position()

    def is_game_over(self):
        return self.game_over

    def is_won(self):
        return self.won

    def get_state(self):
        return {
            "snake": self.get_snake(),
            "food": self.get_food(),
            "score": self.get_score(),
            "speed": self.get_speed(),
            "game_over": self.is_game_over(),
            "won": self.is_won()
        }
