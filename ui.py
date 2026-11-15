import pygame


class GameUI:
    """NEON SNAKE graphical interface."""

    def __init__(self, cols, rows):

        pygame.init()

        self.width = 1100
        self.height = 820

        self.screen = pygame.display.set_mode(
            (self.width, self.height)
        )

        pygame.display.set_caption(
            "NEON SNAKE | Cyberpunk Edition"
        )

        self.clock = pygame.time.Clock()

        self.cols = cols
        self.rows = rows

        self.colors = {
            "background": (5, 8, 15),
            "panel": (12, 19, 30),
            "grid": (19, 35, 43),
            "green": (0, 255, 130),
            "dark_green": (0, 155, 85),
            "red": (255, 45, 75),
            "cyan": (0, 225, 255),
            "yellow": (255, 220, 60),
            "white": (240, 245, 255),
            "gray": (125, 145, 165),
        }

        self.title_font = pygame.font.SysFont(
            "consolas", 48, bold=True
        )

        self.large_font = pygame.font.SysFont(
            "consolas", 37, bold=True
        )

        self.font = pygame.font.SysFont(
            "consolas", 23, bold=True
        )

        self.small_font = pygame.font.SysFont(
            "consolas", 15
        )

        available_width = 980
        available_height = 560

        self.cell_size = max(
            1,
            min(
                28,
                available_width // cols,
                available_height // rows
            )
        )

        self.board_width = cols * self.cell_size
        self.board_height = rows * self.cell_size

        self.board_x = (
            self.width - self.board_width
        ) // 2

        self.board_y = 190 + (
            available_height - self.board_height
        ) // 2

    def draw_text(
        self,
        text,
        font,
        color,
        x,
        y
    ):

        surface = font.render(
            str(text),
            True,
            color
        )

        rect = surface.get_rect(
            center=(x, y)
        )

        self.screen.blit(surface, rect)

    def draw_glow_rect(
        self,
        rect,
        color,
        radius=6
    ):

        glow = pygame.Surface(
            (
                rect.width + 24,
                rect.height + 24
            ),
            pygame.SRCALPHA
        )

        for size in (20, 14, 8):

            glow_rect = pygame.Rect(
                12 - size // 2,
                12 - size // 2,
                rect.width + size,
                rect.height + size
            )

            pygame.draw.rect(
                glow,
                (*color, 18),
                glow_rect,
                border_radius=radius + 3
            )

        pygame.draw.rect(
            glow,
            (*color, 255),
            pygame.Rect(
                12,
                12,
                rect.width,
                rect.height
            ),
            border_radius=radius
        )

        self.screen.blit(
            glow,
            (rect.x - 12, rect.y - 12)
        )

    def draw_background(self):

        self.screen.fill(
            self.colors["background"]
        )

        pygame.draw.rect(
            self.screen,
            self.colors["panel"],
            (
                self.board_x - 12,
                self.board_y - 12,
                self.board_width + 24,
                self.board_height + 24
            ),
            border_radius=12
        )

        board_rect = pygame.Rect(
            self.board_x,
            self.board_y,
            self.board_width,
            self.board_height
        )

        pygame.draw.rect(
            self.screen,
            (7, 12, 20),
            board_rect
        )

        for col in range(self.cols + 1):

            x = (self.board_x
                + col * self.cell_size
            )

            pygame.draw.line(
                self.screen,
                self.colors["grid"],
                (x, self.board_y),
                (
                    x,
                    self.board_y + self.board_height
                ),
                1
            )

        for row in range(self.rows + 1):

            y = (
                self.board_y
                + row * self.cell_size
            )

            pygame.draw.line(
                self.screen,
                self.colors["grid"],
                (self.board_x, y),
                (
                    self.board_x + self.board_width,
                    y
                ),
                1
            )

        pygame.draw.rect(
            self.screen,
            self.colors["cyan"],
            board_rect,
            2,
            border_radius=4
        )

    def draw_header(self):

        self.draw_text(
            "NEON SNAKE",
            self.title_font,
            self.colors["green"],
            self.width // 2,
            55
        )

        self.draw_text(
            "CYBERPUNK ARCADE EDITION",
            self.small_font,
            self.colors["cyan"],
            self.width // 2,
            100
        )

    def draw_statistics(self, state):

        panel_y = 125
        panel_width = 210
        panel_height = 48

        centers = (320, 550, 780)

        values = (
            ("SCORE", state["score"], self.colors["green"]),
            ("BEST SCORE", state["best_score"], self.colors["cyan"]),
            ("SPEED", state["speed"], self.colors["yellow"]),
        )

        for center, item in zip(centers, values):

            label, value, color = item

            rect = pygame.Rect(
                center - panel_width // 2,
                panel_y,
                panel_width,
                panel_height
            )

            pygame.draw.rect(
                self.screen,
                self.colors["panel"],
                rect,
                border_radius=8
            )

            pygame.draw.rect(
                self.screen,
                color,
                rect,
                1,
                border_radius=8
            )

            self.draw_text(
                f"{label}: {value}",
                self.font,
                color,
                center,
                panel_y + panel_height // 2
            )

    def draw_snake(self, snake):

        for index, position in enumerate(snake):

            x, y = position

            rect = pygame.Rect(
                self.board_x + x * self.cell_size + 2,
                self.board_y + y * self.cell_size + 2,
                self.cell_size - 4,
                self.cell_size - 4
            )

            color = (
                self.colors["green"]
                if index == 0
                else self.colors["dark_green"]
            )

            self.draw_glow_rect(
                rect,
                color,
                6
            )

    def draw_food(self, food):

        x, y = food

        center = (
            self.board_x
            + x * self.cell_size
            + self.cell_size // 2,

            self.board_y
            + y * self.cell_size
            + self.cell_size // 2
        )

        radius = max(
            3,
            self.cell_size // 3
        )

        pygame.draw.circle(
            self.screen,
            (100, 10, 35),
            center,
            radius + 5
        )

        pygame.draw.circle(
            self.screen,
            self.colors["red"],
            center,
            radius
        )

        pygame.draw.circle(
            self.screen,
            self.colors["white"],
            (
                center[0] - radius // 3,
                center[1] - radius // 3
            ),
            max(1, radius // 4)
        )

    def draw_overlay(
        self,
        title,
        subtitle,
        color
    ):

        overlay = pygame.Surface(
            (self.board_width,
                self.board_height
            ),
            pygame.SRCALPHA
        )

        overlay.fill(
            (0, 0, 0, 195)
        )

        self.screen.blit(
            overlay,
            (
                self.board_x,
                self.board_y
            )
        )

        center_x = (
            self.board_x + self.board_width // 2
        )

        center_y = (
            self.board_y + self.board_height // 2
        )

        self.draw_text(
            title,
            self.large_font,
            color,
            center_x,
            center_y - 30
        )

        self.draw_text(
            subtitle,
            self.font,
            self.colors["white"],
            center_x,
            center_y + 30
        )

    def draw_controls(self):

        self.draw_text(
            "ARROWS / WASD: MOVE",
            self.small_font,
            self.colors["gray"],
            220,
            785
        )

        self.draw_text(
            "P: PAUSE",
            self.small_font,
            self.colors["cyan"],
            475,
            785
        )

        self.draw_text(
            "R: RESTART",
            self.small_font,
            self.colors["yellow"],
            650,
            785
        )

        self.draw_text(
            "ESC: EXIT",
            self.small_font,
            self.colors["gray"],
            830,
            785
        )

    def draw(self, state):

        self.draw_background()

        self.draw_header()

        self.draw_statistics(state)

        self.draw_snake(state["snake"])

        self.draw_food(state["food"])

        status = state["status"]

        if status == "ready":

            self.draw_overlay(
                "READY TO PLAY",
                "PRESS ENTER OR SPACE",
                self.colors["cyan"]
            )

        elif status == "paused":

            self.draw_overlay(
                "PAUSED",
                "PRESS P TO CONTINUE",
                self.colors["yellow"]
            )

        elif state["won"]:

            self.draw_overlay(
                "YOU WIN!",
                "PRESS SPACE TO PLAY AGAIN",
                self.colors["green"]
            )

        elif state["game_over"]:

            self.draw_overlay(
                "GAME OVER",
                "PRESS R TO RESTART",
                self.colors["red"]
            )

        self.draw_controls()

        pygame.display.flip()

    def tick(self, fps=60):

        return self.clock.tick(fps)

    def close(self):

        pygame.quit()