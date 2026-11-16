import pygame

import settings

from game import Game
from ui import GameUI


def main():

    # Create backend game engine
    game = Game()

    # Create graphical interface
    ui = GameUI(
        settings.COLS,
        settings.ROWS
    )

    running = True

    # Keyboard directions
    directions = {

        pygame.K_UP: (0, -1),
        pygame.K_w: (0, -1),

        pygame.K_DOWN: (0, 1),
        pygame.K_s: (0, 1),

        pygame.K_LEFT: (-1, 0),
        pygame.K_a: (-1, 0),

        pygame.K_RIGHT: (1, 0),
        pygame.K_d: (1, 0),

    }

    # Time accumulator
    accumulator = 0.0

    while running:

        # Measure elapsed frame time
        delta_time = ui.tick(60) / 1000.0

        # Prevent excessive catch-up updates
        delta_time = min(delta_time, 0.25)

        # Process keyboard and window events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False

            elif event.type == pygame.KEYDOWN:

                # Exit
                if event.key == pygame.K_ESCAPE:

                    running = False

                # Start or play again
                elif event.key in (
                    pygame.K_RETURN,
                    pygame.K_SPACE
                ):

                    if game.get_status() == "ready":

                        game.start()

                    elif game.is_game_over():

                        game.reset()
                        game.start()

                    accumulator = 0.0

                # Pause
                elif event.key == pygame.K_p:

                    game.toggle_pause()

                    accumulator = 0.0

                # Restart
                elif event.key == pygame.K_r:

                    game.reset()
                    game.start()

                    accumulator = 0.0

                # Movement
                elif event.key in directions:

                    if game.is_playing():

                        game.set_direction(
                            directions[event.key]
                        )

        # Update game using backend speed
        if game.is_playing():

            accumulator += delta_time

            interval = 1.0 / max(
                1,
                game.get_speed()
            )

            while (
                accumulator >= interval
                and game.is_playing()
            ):

                game.update()

                accumulator -= interval

        else:

            accumulator = 0.0

        # Get current backend data
        state = game.get_state()

        # Draw everything
        ui.draw(state)

    # Close application
    ui.close()


if __name__ == "__main__":

    main()