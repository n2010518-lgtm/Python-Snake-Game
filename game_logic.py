
from snake import Snake
from food import Food
from settings import COLS, ROWS, START_SPEED, MAX_SPEED


class GameLogic:
    def __init__(self):
        self.reset()

    def reset(self):
        self.snake = Snake()
        self.food = Food(COLS, ROWS)

        self.score = 0
        self.speed = START_SPEED
        self.game_over = False
        self.won = False

        self.food.spawn(self.snake.get_body())

    def update(self):
        if self.game_over:
            return

        new_head = self.snake.get_next_head()
        x, y = new_head

        # Проверка столкновения со стенами
        if x < 0 or x >= COLS or y < 0 or y >= ROWS:
            self.game_over = True
            return

        eating = new_head == self.food.get_position()

        body = self.snake.get_body()

        # Хвост освобождает клетку при обычном движении
        body_to_check = body if eating else body[:-1]

        # Проверка столкновения с собой
        if new_head in body_to_check:
            self.game_over = True
            return

        # Перемещение змейки
        self.snake.move(grow=eating)

        if eating:
            self.score += 10

            self.speed = min(
                START_SPEED + self.score // 50,
                MAX_SPEED
            )

            self.food.spawn(self.snake.get_body())

            if self.food.get_position() is None:
                self.game_over = True
                self.won = True
