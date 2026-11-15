
"""
NEON SNAKE
Snake class
"""

import settings


class Snake:

    def __init__(self):
        self.reset()

    def reset(self):
        center_x = settings.COLS // 2
        center_y = settings.ROWS // 2

        self.body = [
            (center_x, center_y),
            (center_x - 1, center_y),
            (center_x - 2, center_y)
        ]

        self.direction = (1, 0)
        self.next_direction = (1, 0)

    def change_direction(self, direction):
        dx, dy = direction

        # Only allow horizontal or vertical movement
        if abs(dx) + abs(dy) != 1:
            return

        current_dx, current_dy = self.direction

        # Prevent moving backwards
        if (dx, dy) == (-current_dx, -current_dy):
            return

        self.next_direction = direction

    def get_next_head(self):
        head_x, head_y = self.body[0]
        dx, dy = self.next_direction

        return (head_x + dx, head_y + dy)

    def move(self, grow=False):
        self.direction = self.next_direction

        new_head = self.get_next_head()
        self.body.insert(0, new_head)

        if not grow:
            self.body.pop()

        return new_head

    def get_body(self):
        return self.body.copy()

    def get_head(self):
        return self.body[0]

    def check_wall_collision(self):
        x, y = self.get_head()

        return (
            x < 0 or
            x >= settings.COLS or
            y < 0 or
            y >= settings.ROWS
        )

    def check_self_collision(self):
        return self.get_head() in self.body[1:]
