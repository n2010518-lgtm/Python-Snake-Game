
"""
NEON SNAKE
Food class
"""

import random
import settings


class Food:

    def __init__(self, snake_body=None):
        self.position = None
        self.spawn(snake_body or [])

    def spawn(self, snake_body):
        available_cells = [
            (x, y)
            for x in range(settings.COLS)
            for y in range(settings.ROWS)
            if (x, y) not in snake_body
        ]

        if not available_cells:
            self.position = None
            return False

        self.position = random.choice(available_cells)
        return True

    def get_position(self):
        return self.position

    def is_eaten(self, snake_head):
        return self.position == snake_head
