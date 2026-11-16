
# NEON SNAKE — Backend API

## 1. Overview

This backend contains the complete game logic.

The frontend should only display the game and handle user input.

The backend controls:
- Snake movement
- Food generation
- Collision detection
- Score calculation
- Game speed
- Game states
- High score storage

## 2. Importing the game

```python
from game import Game

game = Game()
```

## 3. Game states

The game has four states:

| State | Description |
|---|---|
| ready | Waiting for the player |
| playing | Game is running |
| paused | Game is paused |
| game_over | Game has ended |

Get current state:

```python
game.get_status()
```

## 4. Game controls

Start:

```python
game.start()
```

Pause:

```python
game.pause()
```

Resume:

```python
game.resume()
```

Toggle pause:

```python
game.toggle_pause()
```

Restart:

```python
game.reset()
```

## 5. Snake controls

Directions:

```python
game.set_direction((0, -1))  # Up
game.set_direction((0, 1))   # Down
game.set_direction((-1, 0))  # Left
game.set_direction((1, 0))   # Right
```

The backend prevents reversing directly into the opposite direction.

## 6. Updating the game

Call update once per game tick:

```python
game.update()
```

The frontend should control the update frequency using:

```python
game.get_speed()
```

## 7. Getting game information

Current score:

```python
game.get_score()
```

Best score:

```python
game.get_best_score()
```

Snake coordinates:

```python
game.get_snake()
```

Food coordinates:

```python
game.get_food()
```

Game speed:

```python
game.get_speed()
```

Game status:

```python
game.get_status()
```

## 8. Complete game state

Get all information at once:

```python
state = game.get_state()

print(state)
```

Example:

```python
{
    "snake": [(14, 10), (13, 10), (12, 10)],
    "food": (4, 7),
    "score": 0,
    "best_score": 10,
    "speed": 8,
    "status": "ready",
    "game_over": False,
    "won": False
}
```

## 9. Game over and victory

Check whether the game ended:

```python
game.is_game_over()
```

Check whether the player won:

```python
game.is_won()
```

## 10. Important integration rules

1. Do not implement snake movement in the frontend.
2. Do not calculate scores in the frontend.
3. Do not generate food in the frontend.
4. Use game.update() to advance the game.
5. Use game.get_state() to retrieve data for rendering.
6. Use game.set_direction() for keyboard input.
7. Keep frontend and backend logic separate.

## 11. Dependencies

Install dependencies:

```bash
pip install -r requirements.txt
```

The backend game logic does not require Pygame.

---

Backend developer: NEON SNAKE Team

