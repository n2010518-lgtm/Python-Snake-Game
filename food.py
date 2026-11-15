

import random


class Food:
    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.position = None

    def spawn(self, snake_body):
        free_cells = [
            (x, y)
            for x in range(self.columns)
            for y in range(self.rows)
            if (x, y) not in snake_body
        ]

        if free_cells:
            self.position = random.choice(free_cells)
        else:
            self.position = None

    def get_position(self):
        return self.position
