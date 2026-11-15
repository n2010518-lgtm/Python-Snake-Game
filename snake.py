
import pygame

class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
        self.body = [(20, 15), (19, 15), (18, 15)]
        self.direction = (1, 0)
        self.next_direction = (1, 0)

    def change_direction(self, new_direction):
        if (
            new_direction[0] + self.direction[0] == 0
            and new_direction[1] + self.direction[1] == 0
        ):
            return

        self.next_direction = new_direction

    def get_next_head(self):
        x, y = self.body[0]
        dx, dy = self.next_direction
        return (x + dx, y + dy)

    def move(self, grow=False):
        self.direction = self.next_direction
        new_head = self.get_next_head()
        self.body.insert(0, new_head)

        if not grow:
            self.body.pop()

    def get_body(self):
        return self.body

    def get_head(self):
        return self.body[0]
