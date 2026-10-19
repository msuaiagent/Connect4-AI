# Week 4: Bringing the Game to Life

Over the past three weeks, you've built the core of your Connect 4 game.

You now have:

- A board.
- Move validation.
- Piece placement.
- Win detection.
- Draw detection.
- Game state management.
- Player turns.
- A complete game engine.

However, everything currently exists inside the terminal.

This week, you'll give your game a graphical interface using **Pygame**.

By the end of this week, you'll be able to watch your Connect 4 game play on a real game window.

---

# Learning Objectives

By the end of this week, you should be able to:

- Create a basic Pygame window.
- Understand the Pygame game loop.
- Draw rectangles and circles.
- Display text on the screen.
- Create a renderer separate from the game engine.
- Connect a graphical interface to an existing game engine.
- Understand why rendering and game logic should remain separate.

---

# What You'll Build

This week you'll create:

```text
connect4/
└── renderer.py
```

You'll also update:

```text
run.py
```

At this point, your own `StudentAgent` does **not** exist yet. You will create that in Week 5.

For now, both players will use the provided `RandomAgent` so that you can test the game engine and graphical interface.

---

# What Is Pygame?

**Pygame** is a Python library designed for creating games and multimedia applications.

We'll use it to:

- Create the game window.
- Draw the board.
- Draw the pieces.
- Display text.
- Handle window events.
- Control the game's display.

Pygame is responsible for what the player **sees**.

It does not decide how the game works.

---

# Why Separate Rendering From Game Logic?

Imagine that your game engine contains hundreds of lines of code.

Now imagine changing the game's appearance required changing all of that code.

That would quickly become difficult to manage.

Instead, we'll separate the responsibilities:

```text
Game Engine
     │
     │ Game State
     ▼
 Renderer
     │
     ▼
 Screen
```

The `Game` decides **what is happening**.

The `Renderer` decides **how it looks**.

This is another example of separating responsibilities between different parts of a program.

---

# Task 1 – Import Pygame

Create:

```text
connect4/renderer.py
```

Start by importing Pygame and the constants we'll need.

---

## TODO

Import:

- `pygame`
- `Board`
- Display constants
- Player constants

Try creating the imports yourself.

---

## Solution

```python
import pygame

from .board import Board
from .constants import (
    BLACK,
    BLUE,
    COLS,
    HEIGHT,
    PLAYER_ONE,
    PLAYER_TWO,
    RED,
    ROWS,
    SQUARE_SIZE,
    WHITE,
    WIDTH,
    WINDOW_TITLE,
    YELLOW,
)
```

---

# Task 2 – Create the Renderer

The Renderer needs somewhere to draw.

We'll create a class called:

```python
Renderer
```

Its constructor will:

1. Initialize Pygame.
2. Create the game window.
3. Set the window title.
4. Create a font for displaying text.

---

## TODO

Create:

```python
class Renderer:
```

Then create an `__init__()` method.

---

## Solution

```python
class Renderer:

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode(
            (WIDTH, HEIGHT)
        )

        pygame.display.set_caption(
            WINDOW_TITLE
        )

        self.font = pygame.font.SysFont(
            "Arial",
            36,
        )
```

---

# Task 3 – Drawing the Board

Now we need to draw the Connect 4 board.

Each position will be represented by a square.

---

## TODO

Create:

```python
_draw_board(board)
```

The method should:

1. Clear the screen.
2. Loop through every row.
3. Loop through every column.
4. Draw a blue rectangle for each position.

Hint:

Use:

```python
pygame.draw.rect()
```

Try implementing it yourself.

---

## Solution

```python
def _draw_board(self, board: Board):

    self.screen.fill(BLACK)

    for row in range(ROWS):

        for col in range(COLS):

            x = col * SQUARE_SIZE
            y = (row + 1) * SQUARE_SIZE

            pygame.draw.rect(
                self.screen,
                BLUE,
                (
                    x,
                    y,
                    SQUARE_SIZE,
                    SQUARE_SIZE,
                ),
            )
```

---

# Why Does the Board Start at `row + 1`?

We want to reserve the top section of the window for game information.

So instead of:

```python
y = row * SQUARE_SIZE
```

we use:

```python
y = (row + 1) * SQUARE_SIZE
```

This moves the board down by one square.

Later, we'll use this space to display information such as:

```text
Random AI's Turn
```

---

# Task 4 – Drawing the Game Pieces

The board is now visible, but all of its positions are empty.

We need to draw the pieces stored in the `Board`.

We'll use:

- Black for empty positions.
- Red for Player One.
- Yellow for Player Two.

---

## TODO

Inside `_draw_board()`:

1. Read the value of the current position.
2. Decide which colour should be used.
3. Draw a circle in the centre of the square.

Try implementing it yourself.

---

## Solution

Add the following inside the nested loops, after drawing the blue rectangle:

```python
piece = board[row][col]

colour = BLACK

if piece == PLAYER_ONE:
    colour = RED

elif piece == PLAYER_TWO:
    colour = YELLOW

pygame.draw.circle(
    self.screen,
    colour,
    (
        x + SQUARE_SIZE // 2,
        y + SQUARE_SIZE // 2,
    ),
    SQUARE_SIZE // 2 - 8,
)
```

---

# Why Do We Draw Circles?

Although the board is made from rectangles, the playing pieces are circular.

Every circle is drawn in the centre of its square.

The calculation:

```python
x + SQUARE_SIZE // 2
```

moves the circle to the horizontal centre of the square.

Similarly,

```python
y + SQUARE_SIZE // 2
```

moves it to the vertical centre.

---

# Task 5 – Drawing the Game Status

Players should know what is happening during the game.

We'll use the top section of the window to display a message.

For example:

```text
Random AI's Turn
```

or:

```text
Random AI Wins!
```

---

## TODO

Create:

```python
_draw_status(game)
```

The method should:

1. Clear the top section.
2. Determine what message should be displayed.
3. Create a text surface.
4. Draw the text on the screen.

Try implementing it yourself first.

---

## Solution

```python
def _draw_status(self, game):

    pygame.draw.rect(
        self.screen,
        BLACK,
        (
            0,
            0,
            WIDTH,
            SQUARE_SIZE,
        ),
    )

    if game.game_over:

        if game.winner == PLAYER_ONE:

            text = f"{game.player_one.name} Wins!"

        elif game.winner == PLAYER_TWO:

            text = f"{game.player_two.name} Wins!"

        else:

            text = "Draw!"

    else:

        text = f"{game.current_agent.name}'s Turn"

    label = self.font.render(
        text,
        True,
        WHITE,
    )

    self.screen.blit(
        label,
        (20, 25),
    )
```

Notice that we use `game.player_one` and `game.player_two`.

These are the player attributes used by the `Game` class from Week 3.

---

# Task 6 – Creating the Main Draw Method

So far, we've created separate methods for:

- Drawing the board.
- Drawing the pieces.
- Drawing the status.

It would be convenient to have one method that updates the entire screen.

---

## TODO

Create:

```python
draw(game)
```

It should:

1. Draw the board.
2. Draw the status.
3. Update the display.

Try implementing it yourself.

---

## Solution

```python
def draw(self, game):

    self._draw_board(game.board)

    self._draw_status(game)

    pygame.display.flip()
```

---

# What Does `pygame.display.flip()` Do?

Pygame doesn't immediately show every drawing operation on the screen.

Instead, your program draws the new frame and then updates the display.

```python
pygame.display.flip()
```

tells Pygame:

> "Show the frame we've just drawn."

This happens repeatedly while the game is running.

---

# Task 7 – Handling the Window

A game window needs to respond when the user tries to close it.

We'll create a method to check for window events.

---

## TODO

Create:

```python
handle_events()
```

It should:

- Check for Pygame events.
- Return `False` if the user closes the window.
- Otherwise return `True`.

Try implementing it yourself.

---

## Solution

```python
def handle_events(self):

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            return False

    return True
```

---

# Task 8 – Closing Pygame

When the program finishes, Pygame should be shut down properly.

Create:

```python
close()
```

---

## Solution

```python
def close(self):

    pygame.quit()
```

---

# Complete `renderer.py`

If you got stuck, compare your implementation with the complete file below.

```python
"""
renderer.py

Responsible for drawing the Connect 4 board.

This class NEVER changes the game.
It only visualizes the current game state.
"""

from __future__ import annotations

import pygame

from .board import Board
from .constants import (
    ROWS,
    COLS,
    SQUARE_SIZE,
    WIDTH,
    HEIGHT,
    WINDOW_TITLE,
    BLACK,
    BLUE,
    RED,
    YELLOW,
    WHITE,
    PLAYER_ONE,
    PLAYER_TWO,
)


class Renderer:
    """Handles all rendering using pygame."""

    def __init__(self) -> None:

        pygame.init()

        self.screen = pygame.display.set_mode(
            (WIDTH, HEIGHT)
        )

        pygame.display.set_caption(
            WINDOW_TITLE
        )

        self.font = pygame.font.SysFont(
            "Arial",
            36,
        )

    def draw(self, game) -> None:
        """Draw the current game."""

        self._draw_board(game.board)

        self._draw_status(game)

        pygame.display.flip()

    def _draw_board(self, board: Board) -> None:

        self.screen.fill(BLACK)

        for row in range(ROWS):
            for col in range(COLS):

                x = col * SQUARE_SIZE
                y = (row + 1) * SQUARE_SIZE

                pygame.draw.rect(
                    self.screen,
                    BLUE,
                    (
                        x,
                        y,
                        SQUARE_SIZE,
                        SQUARE_SIZE,
                    ),
                )

                piece = board[row][col]

                colour = BLACK

                if piece == PLAYER_ONE:
                    colour = RED

                elif piece == PLAYER_TWO:
                    colour = YELLOW

                pygame.draw.circle(
                    self.screen,
                    colour,
                    (
                        x + SQUARE_SIZE // 2,
                        y + SQUARE_SIZE // 2,
                    ),
                    SQUARE_SIZE // 2 - 8,
                )

    def _draw_status(self, game) -> None:
        """Draw the text at the top."""

        pygame.draw.rect(
            self.screen,
            BLACK,
            (
                0,
                0,
                WIDTH,
                SQUARE_SIZE,
            ),
        )

        if game.game_over:

            if game.winner == PLAYER_ONE:
                text = f"{game.player_one.name} Wins!"

            elif game.winner == PLAYER_TWO:
                text = f"{game.player_two.name} Wins!"

            else:
                text = "Draw!"

        else:

            text = f"{game.current_agent.name}'s Turn"

        label = self.font.render(
            text,
            True,
            WHITE,
        )

        self.screen.blit(
            label,
            (20, 25),
        )

    def handle_events(self) -> bool:
        """Handle Pygame window events."""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return False

        return True

    def close(self) -> None:
        """Close Pygame."""

        pygame.quit()
```

---

# Task 9 – Updating `run.py`

Now we need to connect the graphical interface to the game engine.

At this point in the project, your own `StudentAgent` does **not** exist yet.

Instead, we'll use the provided `RandomAgent` for both players.

This allows us to test the complete game engine and renderer before building our own AI.

---

## TODO

Import:

- Pygame.
- `RandomAgent`.
- `Game`.
- `Renderer`.
- `FPS`.

---

## Solution

```python
import pygame

from agents.random_agent import RandomAgent

from connect4.constants import FPS
from connect4.game import Game
from connect4.renderer import Renderer
```

---

# Task 10 – Create the Game Loop

A graphical game repeatedly performs the same basic sequence:

```text
Handle Events
      ↓
Play Turn
      ↓
Draw Game
      ↓
Repeat
```

This is called the **game loop**.

---

## TODO

Create a `main()` function that:

1. Creates two `RandomAgent` objects.
2. Creates a `Game`.
3. Creates a `Renderer`.
4. Creates a Pygame clock.
5. Runs the game loop.
6. Closes Pygame when finished.

Try implementing it yourself first.

---

## Solution

```python
def main() -> None:

    player_one = RandomAgent()
    player_two = RandomAgent()

    game = Game(
        player_one=player_one,
        player_two=player_two,
    )

    renderer = Renderer()

    clock = pygame.time.Clock()

    running = True

    while running:

        running = renderer.handle_events()

        if not game.game_over:
            game.play_turn()

        renderer.draw(game)

        clock.tick(FPS)

    renderer.close()


if __name__ == "__main__":
    main()
```

---

# Complete `run.py`

Your final `run.py` should look like this:

```python
"""
run.py

Entry point for the Connect 4 AI framework.
"""

from __future__ import annotations

import pygame

from agents.random_agent import RandomAgent

from connect4.constants import FPS
from connect4.game import Game
from connect4.renderer import Renderer


def main() -> None:

    player_one = RandomAgent()
    player_two = RandomAgent()

    game = Game(
        player_one=player_one,
        player_two=player_two,
    )

    renderer = Renderer()

    clock = pygame.time.Clock()

    running = True

    while running:

        running = renderer.handle_events()

        if not game.game_over:
            game.play_turn()

        renderer.draw(game)

        clock.tick(FPS)

    renderer.close()


if __name__ == "__main__":
    main()
```

---

# Why Use a Clock?

Without a clock, the program could run through the game loop as quickly as your computer allows.

The game might finish almost instantly.

The line:

```python
clock.tick(FPS)
```

limits the game loop to the frame rate specified in `constants.py`.

This gives you control over how quickly the game progresses.

---

# Testing the Game

Run:

```bash
python run.py
```

You should now see a Pygame window containing:

- A Connect 4 board.
- Player pieces.
- A status message.
- The game progressing one move at a time.

Both players are currently using the provided `RandomAgent`.

You can close the window normally using the window's close button.

---

# What Happens Every Frame?

Your program now follows this process:

```text
┌──────────────────────┐
│ Check Window Events  │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│     Play a Turn      │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│    Draw the Game     │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│    Wait for Frame    │
└──────────┬───────────┘
           │
           └──────────────→ Repeat
```

This loop continues until:

- The game finishes.
- Or the player closes the window.

---

# Important Design Principle

Notice something about the code we've built.

The `Game` class doesn't know anything about Pygame.

It doesn't:

```python
pygame.draw.circle(...)
```

It doesn't create windows.

It doesn't handle graphical events.

The Renderer handles those responsibilities.

This separation means we could replace the graphical interface later without rewriting the game rules.

For example:

```text
Game
 │
 ├── Pygame Renderer
 │
 ├── Terminal Renderer
 │
 └── Other Interface
```

while keeping the same game engine.

---

# Important Project Structure

At the end of Week 4, your project should look like:

```text
starter_code/
├── agents/
│   ├── __init__.py
│   └── random_agent.py
│
├── connect4/
│   ├── __init__.py
│   ├── constants.py
│   ├── board.py
│   ├── rules.py
│   ├── state.py
│   ├── match_result.py
│   ├── game.py
│   └── renderer.py
│
├── requirements.txt
└── run.py
```

You should **not** create `StudentAgent` yet.

That will be introduced in Week 5.

---

# Knowledge Check

Before moving on, make sure you can answer:

1. What is Pygame responsible for?
2. What is the Renderer responsible for?
3. Why shouldn't the Game class contain rendering code?
4. What does `pygame.display.flip()` do?
5. What is a game loop?
6. Why do we use `clock.tick(FPS)`?
7. Why is separating rendering from game logic useful?
8. Why are we using `RandomAgent` for both players this week?
9. Why don't we create `StudentAgent` until Week 5?

---

# Optional Challenges

## Challenge 1 — Change the Speed

Try changing the `FPS` value in `constants.py`.

How does this affect the game?

---

## Challenge 2 — Change the Window

Experiment with:

```python
SQUARE_SIZE
```

in `constants.py`.

What happens when you increase or decrease it?

---

## Challenge 3 — Change the Appearance

Try changing the colours in `constants.py`.

For example, experiment with different RGB values.

Be careful not to change the meaning of the player constants.

---

# Week 4 Summary

Congratulations! 🎉

You've now transformed your Connect 4 engine into a graphical game.

This week you created:

- `renderer.py`

You also updated:

- `run.py`

You learned:

- How to create a Pygame window.
- How to draw rectangles and circles.
- How to display text.
- How to handle window events.
- How a game loop works.
- How to control game speed.
- Why rendering should be separated from game logic.

Your project can now display an entire Connect 4 game on screen.

---

# Looking Ahead

So far, the game has been controlled by the provided `RandomAgent`.

Next week, you'll build something much more important:

**your own AI agent.**

You'll learn:

- What an AI agent is.
- How an AI receives a game state.
- How an AI chooses a legal move.
- How to create your `StudentAgent`.
- How to begin improving your AI's strategy.

For the first time, you'll be responsible for deciding **how your AI plays the game**.

There will be no required AI algorithm or single "correct" strategy. Your goal will be to experiment, make decisions, and improve your own agent.

See you in **Week 5!** 🚀
