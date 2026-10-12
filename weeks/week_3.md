# Week 3: Building the Game Engine

Last week, you built the Connect 4 board and learned how the game is represented in code.

This week, we'll turn that board into a fully functioning game.

By the end of this week, your project will be capable of managing turns, detecting wins and draws, and keeping track of an entire Connect 4 match.

Although there still won't be any graphics, you'll have completed the core game engine that every AI agent will use.

---

# Learning Objectives

By the end of this week, you should be able to:

- Explain the purpose of a game engine.
- Detect wins and draws.
- Manage player turns.
- Understand immutable game states.
- Understand why different classes have different responsibilities.
- Build a complete game loop.

---

# What You'll Build

This week you'll create:

```text
connect4/
├── rules.py
├── state.py
├── match_result.py
└── game.py
```

These files work together to control an entire game of Connect 4.

---

# What Is a Game Engine?

Last week, we created the **Board** class.

The Board knows where every piece is located.

However, it doesn't know:

- Whose turn it is.
- Whether someone has won.
- Whether the game has ended.
- Which player should move next.

Those responsibilities belong to the **Game Engine**.

Rather than placing all of our code inside one giant file, we'll split each responsibility into its own class.

This makes the project much easier to understand, test, and maintain.

---

# Task 1 – Creating the Rules Class

Create a new file:

```text
connect4/rules.py
```

The Rules class is responsible for checking whether a player has won or whether the game has ended in a draw.

Notice that the Board class **doesn't** perform these checks.

Each class has a single responsibility.

---

## TODO

Before looking at the solution, try creating the beginning of the `Rules` class yourself.

Hints:

- The class doesn't need a constructor.
- Every method should be a static method.
- Start by creating a method named `check_win()`.

---

## Solution

```python
"""
rules.py

Contains all game rule logic.

Responsibilities
----------------
- Win detection
- Draw detection
- Terminal-state detection

The Rules class never modifies the board.
"""

from __future__ import annotations

from .board import Board
from .constants import (
    ROWS,
    COLS,
    CONNECT,
    PLAYER_ONE,
    PLAYER_TWO,
)


class Rules:

    @staticmethod
    def check_win(
        board: Board,
        player: int,
    ) -> bool:
        ...
```

---

## How Can Someone Win?

Before writing any more code, think about the game itself.

**Question:**

How many different ways can a player connect four pieces?

Take a minute to think before continuing.

<details>
<summary>Answer</summary>

There are four possible directions:

- Horizontal
- Vertical
- Positive diagonal
- Negative diagonal

</details>

---

## TODO

Can you complete the `check_win()` method?

Hint:

It should simply call four helper methods.

---

## Solution

```python
@staticmethod
def check_win(
    board: Board,
    player: int,
) -> bool:

    return (
        Rules._horizontal(board, player)
        or Rules._vertical(board, player)
        or Rules._positive_diagonal(board, player)
        or Rules._negative_diagonal(board, player)
    )
```

---

## TODO

Every Connect 4 game can also end in a draw.

Create:

```python
check_draw(board)
```

Hint:

Think back to the `valid_moves()` function you created last week.

If there are no valid moves left, the board is full.

---

## Solution

```python
@staticmethod
def check_draw(board: Board) -> bool:
    """Return True if the board is full."""

    return len(board.valid_moves()) == 0
```

---

## TODO

Instead of checking for wins and draws separately every time, let's create one helper function.

Create a method called:

```python
is_terminal(board)
```

Hint:

A game is terminal if:

- Player One has won.
- Player Two has won.
- The game is a draw.

---

## Solution

```python
@staticmethod
def is_terminal(board: Board) -> bool:
    """
    Return True if the game has reached
    a terminal state.
    """

    return (
        Rules.check_win(board, PLAYER_ONE)
        or Rules.check_win(board, PLAYER_TWO)
        or Rules.check_draw(board)
    )
```

---

# Horizontal Win Detection

Checking every possible winning direction uses the same general idea:

1. Visit every possible starting position.
2. Look ahead four spaces.
3. Check whether all four belong to the same player.

Let's start with horizontal wins.

---

## TODO

Try writing the `_horizontal()` helper method.

Hints:

- Loop through every row.
- Don't start too close to the right edge.
- Compare four neighbouring cells.

Don't worry if you get stuck.

---

## Solution

```python
@staticmethod
def _horizontal(
    board: Board,
    player: int,
) -> bool:

    for row in range(ROWS):
        for col in range(COLS - CONNECT + 1):

            if all(
                board[row][col + offset] == player
                for offset in range(CONNECT)
            ):
                return True

    return False
```

---

# Vertical Win Detection

A vertical win looks like:

```text
🔴
🔴
🔴
🔴
```

This time, the row changes while the column stays the same.

---

## TODO

Try implementing:

```python
_vertical(board, player)
```

Hints:

- Loop through every column.
- Don't start too close to the bottom.
- Increase the row for each position you check.

---

## Solution

```python
@staticmethod
def _vertical(
    board: Board,
    player: int,
) -> bool:

    for row in range(ROWS - CONNECT + 1):
        for col in range(COLS):

            if all(
                board[row + offset][col] == player
                for offset in range(CONNECT)
            ):
                return True

    return False
```

---

# Positive Diagonal Win Detection

A diagonal win can move:

- Up and to the right.

For example:

```text
      🔴
    🔴
  🔴
🔴
```

Because of how our board is indexed, the row decreases while the column increases.

---

## TODO

Create:

```python
_positive_diagonal(board, player)
```

Hints:

- The starting row must leave enough space above it.
- The starting column must leave enough space to the right.
- Move one row upward and one column right for each position.

Try it yourself first.

---

## Solution

```python
@staticmethod
def _positive_diagonal(
    board: Board,
    player: int,
) -> bool:

    for row in range(CONNECT - 1, ROWS):
        for col in range(COLS - CONNECT + 1):

            if all(
                board[row - offset][col + offset] == player
                for offset in range(CONNECT)
            ):
                return True

    return False
```

---

# Negative Diagonal Win Detection

The other diagonal direction moves:

- Down and to the right.

For example:

```text
🔴
  🔴
    🔴
      🔴
```

Here, both the row and column increase.

---

## TODO

Create:

```python
_negative_diagonal(board, player)
```

Hints:

- Loop through possible starting positions.
- Increase both row and column.
- Check four consecutive positions.

Try it yourself first.

---

## Solution

```python
@staticmethod
def _negative_diagonal(
    board: Board,
    player: int,
) -> bool:

    for row in range(ROWS - CONNECT + 1):
        for col in range(COLS - CONNECT + 1):

            if all(
                board[row + offset][col + offset] == player
                for offset in range(CONNECT)
            ):
                return True

    return False
```

---

# Complete `rules.py`

If you got stuck, compare your implementation with the complete file below.

```python
"""
rules.py

Contains all game rule logic.

Responsibilities
----------------
- Win detection
- Draw detection
- Terminal-state detection

The Rules class never modifies the board.
"""

from __future__ import annotations

from .board import Board
from .constants import (
    ROWS,
    COLS,
    CONNECT,
    PLAYER_ONE,
    PLAYER_TWO,
)


class Rules:

    @staticmethod
    def is_terminal(board: Board) -> bool:
        return (
            Rules.check_win(board, PLAYER_ONE)
            or Rules.check_win(board, PLAYER_TWO)
            or Rules.check_draw(board)
        )

    @staticmethod
    def check_draw(board: Board) -> bool:
        return len(board.valid_moves()) == 0

    @staticmethod
    def check_win(board: Board, player: int) -> bool:
        return (
            Rules._horizontal(board, player)
            or Rules._vertical(board, player)
            or Rules._positive_diagonal(board, player)
            or Rules._negative_diagonal(board, player)
        )

    @staticmethod
    def _horizontal(board: Board, player: int) -> bool:
        for row in range(ROWS):
            for col in range(COLS - CONNECT + 1):
                if all(
                    board[row][col + offset] == player
                    for offset in range(CONNECT)
                ):
                    return True
        return False

    @staticmethod
    def _vertical(board: Board, player: int) -> bool:
        for row in range(ROWS - CONNECT + 1):
            for col in range(COLS):
                if all(
                    board[row + offset][col] == player
                    for offset in range(CONNECT)
                ):
                    return True
        return False

    @staticmethod
    def _positive_diagonal(board: Board, player: int) -> bool:
        for row in range(CONNECT - 1, ROWS):
            for col in range(COLS - CONNECT + 1):
                if all(
                    board[row - offset][col + offset] == player
                    for offset in range(CONNECT)
                ):
                    return True
        return False

    @staticmethod
    def _negative_diagonal(board: Board, player: int) -> bool:
        for row in range(ROWS - CONNECT + 1):
            for col in range(COLS - CONNECT + 1):
                if all(
                    board[row + offset][col + offset] == player
                    for offset in range(CONNECT)
                ):
                    return True
        return False
```

---

# Testing the Rules

Before continuing, test that your rules work correctly.

Create a simple board:

```python
from connect4.board import Board
from connect4.constants import PLAYER_ONE
from connect4.rules import Rules

board = Board()

for column in range(4):
    board.drop_piece(column, PLAYER_ONE)

print(board)
print(Rules.check_win(board, PLAYER_ONE))
```

The final line should print:

```text
True
```

Try creating your own:

- Vertical win.
- Positive diagonal win.
- Negative diagonal win.
- Full board with no winner.

You can also test:

```python
print(Rules.check_draw(board))
```

and:

```python
print(Rules.is_terminal(board))
```

---

# Part 2 – Creating GameState

Create a new file:

```text
connect4/state.py
```

Our AI agents should never be allowed to modify the real game.

Instead, we'll give them an **immutable snapshot** of the current game state.

This snapshot is called a **GameState**.

---

## TODO

Create a frozen dataclass named `GameState`.

It should contain:

- The current board.
- The current player.
- Every valid move.

Try writing it yourself before viewing the solution.

---

## Solution

```python
"""
state.py

Contains the immutable GameState class.

GameState is the object exposed to AI agents.
"""

from dataclasses import dataclass

from .board import Board


@dataclass(frozen=True, slots=True)
class GameState:
    board: Board
    current_player: int
    valid_moves: tuple[int, ...]
```

---

# Why Is GameState Immutable?

Imagine an AI agent accidentally changed the real game board while deciding on its next move.

The game could become corrupted.

By making `GameState` immutable, the AI receives a snapshot of the current position rather than direct control over the game.

The game can also provide the AI with a **copy of the board**, allowing it to inspect the current position without modifying the real game board.

This separation becomes especially important when we begin improving the AI.

---

# Part 3 – Creating MatchResult

Create a new file:

```text
connect4/match_result.py
```

At the end of every game, we'll want to know:

- Who won?
- How many turns were played?

Rather than returning multiple values separately, we'll group them into a single object.

This makes our code cleaner and easier to work with.

---

## TODO

Create a dataclass called `MatchResult`.

It should store:

- The winner.
- The number of turns played.

Try creating it yourself before viewing the solution.

---

## Solution

```python
"""
match_result.py

Stores the result of a completed match.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class MatchResult:
    winner: int | None
    turns: int
```

---

# Part 4 – Building the Game Class

Create a new file:

```text
connect4/game.py
```

This is the heart of the project.

The `Game` class controls everything that happens during a match.

Its responsibilities include:

- Creating the board.
- Managing turns.
- Asking the current agent for a move.
- Updating the board.
- Detecting wins and draws.
- Ending the game.

Unlike the Board class, the Game class is responsible for the overall flow of the game.

---

## TODO 1 – Creating the Constructor

Create the `Game` class and write its constructor.

The constructor should:

- Create a Board.
- Store both players.
- Set Player One to move first.
- Keep track of the winner.
- Keep track of whether the game has finished.
- Count the number of turns played.

Try writing this before viewing the solution.

---

## Solution

```python
class Game:

    def __init__(
        self,
        player_one,
        player_two,
    ):

        self.board = Board()

        self.player_one = player_one
        self.player_two = player_two

        self.current_player = PLAYER_ONE

        self.turns = 0
        self.winner = None
        self.game_over = False
```

---

# Task 2 – Finding the Current Agent

Every turn, the game needs to know which agent should make the next move.

Create a property called:

```python
current_agent
```

Hint:

- If it's Player One's turn, return `player_one`.
- Otherwise, return `player_two`.

---

## Solution

```python
@property
def current_agent(self):

    if self.current_player == PLAYER_ONE:
        return self.player_one

    return self.player_two
```

Notice how using a property allows the rest of the project to simply write:

```python
game.current_agent
```

without worrying about whose turn it currently is.

---

# Task 3 – Creating the Game State

Our AI shouldn't receive the real board.

Instead, it should receive an immutable snapshot of the game.

Create a property called:

```python
state
```

This property should create a new `GameState` containing:

- A copy of the board.
- The current player.
- Every valid move.

---

## Solution

```python
@property
def state(self) -> GameState:

    board = self.board.copy()

    return GameState(
        board=board,
        current_player=self.current_player,
        valid_moves=tuple(board.valid_moves()),
    )
```

Take a moment to notice that the board is copied before being passed to the AI.

The AI can inspect the copied board without directly modifying the actual game board.

---

# Task 4 – Playing a Turn

The `play_turn()` method is responsible for one complete turn.

It needs to:

1. Check whether the game has already ended.
2. Ask the current agent for a move.
3. Place the piece.
4. Increase the turn counter.
5. Check for a win.
6. Check for a draw.
7. Switch players if the game continues.

---

## TODO

Try implementing `play_turn()` yourself.

Think carefully about the order of the operations.

In particular, the game should check whether the current player won **before** switching to the other player.

---

## Solution

```python
def play_turn(self) -> bool:

    if self.game_over:
        return False

    move = self.current_agent.choose_move(self.state)

    if not self.board.drop_piece(
        move,
        self.current_player,
    ):
        raise ValueError(
            f"{self.current_agent.name} returned "
            f"an invalid move ({move})."
        )

    self.turns += 1

    if Rules.check_win(
        self.board,
        self.current_player,
    ):
        self.winner = self.current_player
        self.game_over = True
        return False

    if Rules.check_draw(self.board):
        self.winner = None
        self.game_over = True
        return False

    self._switch_player()

    return True
```

The `True` or `False` return value tells the program whether the game should continue.

---

# Task 5 – Resetting the Game

It can be useful to restart a game without creating a new `Game` object.

---

## TODO

Create:

```python
reset()
```

It should:

- Reset the board.
- Set the current player back to Player One.
- Reset the turn counter.
- Clear the winner.
- Mark the game as active.

---

## Solution

```python
def reset(self) -> None:

    self.board.reset()

    self.current_player = PLAYER_ONE
    self.turns = 0
    self.winner = None
    self.game_over = False
```

---

# Task 6 – Switching Players

If the game isn't over, the other player needs to move.

---

## TODO

Create:

```python
_switch_player()
```

If the current player is Player One, switch to Player Two.

Otherwise, switch back to Player One.

---

## Solution

```python
def _switch_player(self) -> None:

    if self.current_player == PLAYER_ONE:
        self.current_player = PLAYER_TWO
    else:
        self.current_player = PLAYER_ONE
```

---

# Task 7 – Getting the Match Result

We created `MatchResult` earlier so that the outcome of a completed game can be represented by a single object.

Create:

```python
result()
```

The method should:

- Make sure the game has finished.
- Return a `MatchResult`.
- Include the winner.
- Include the number of turns played.

---

## Solution

```python
def result(self) -> MatchResult:

    if not self.game_over:
        raise RuntimeError("Game is not finished.")

    return MatchResult(
        winner=self.winner,
        turns=self.turns,
    )
```

---

# Complete `game.py`

If you got stuck, compare your implementation with the complete file below.

```python
"""
game.py

Main game engine for Connect 4.

Responsibilities
----------------
- Manage player turns
- Ask agents for moves
- Update the board
- Detect wins and draws
- Track game state

This class contains NO rendering logic and NO AI logic.
"""

from __future__ import annotations

from typing import Any

from .board import Board
from .constants import PLAYER_ONE, PLAYER_TWO
from .match_result import MatchResult
from .rules import Rules
from .state import GameState


class Game:
    """Controls a single game of Connect 4."""

    def __init__(
        self,
        player_one: Any,
        player_two: Any,
    ) -> None:

        self.board = Board()

        self.player_one = player_one
        self.player_two = player_two

        self.current_player = PLAYER_ONE

        self.turns = 0
        self.winner: int | None = None
        self.game_over = False

    @property
    def current_agent(self) -> Any:
        """Return the agent whose turn it is."""

        if self.current_player == PLAYER_ONE:
            return self.player_one

        return self.player_two

    @property
    def state(self) -> GameState:
        """Return an immutable snapshot of the current game."""

        board = self.board.copy()

        return GameState(
            board=board,
            current_player=self.current_player,
            valid_moves=tuple(board.valid_moves()),
        )

    def play_turn(self) -> bool:
        """
        Play exactly one turn.

        Returns
        -------
        bool
            True if the game should continue.
            False if the game has ended.
        """

        if self.game_over:
            return False

        move = self.current_agent.choose_move(self.state)

        if not self.board.drop_piece(
            move,
            self.current_player,
        ):
            raise ValueError(
                f"{self.current_agent.name} returned "
                f"an invalid move ({move})."
            )

        self.turns += 1

        if Rules.check_win(
            self.board,
            self.current_player,
        ):
            self.winner = self.current_player
            self.game_over = True
            return False

        if Rules.check_draw(self.board):
            self.winner = None
            self.game_over = True
            return False

        self._switch_player()

        return True

    def reset(self) -> None:
        """Reset the game."""

        self.board.reset()

        self.current_player = PLAYER_ONE
        self.turns = 0
        self.winner = None
        self.game_over = False

    def result(self) -> MatchResult:
        """
        Return the result of a completed game.

        Raises
        ------
        RuntimeError
            If the game has not finished.
        """

        if not self.game_over:
            raise RuntimeError("Game is not finished.")

        return MatchResult(
            winner=self.winner,
            turns=self.turns,
        )

    def _switch_player(self) -> None:
        """Switch to the other player."""

        if self.current_player == PLAYER_ONE:
            self.current_player = PLAYER_TWO
        else:
            self.current_player = PLAYER_ONE
```

---

# Understanding the Game Loop

Every Connect 4 game follows the same cycle:

```text
Start Game
      │
      ▼
Current Player Chooses Move
      │
      ▼
Drop Piece
      │
      ▼
Win?
 ├── Yes → End Game
 └── No
      │
      ▼
Draw?
 ├── Yes → End Game
 └── No
      │
      ▼
Switch Player
      │
      ▼
Repeat
```

This sequence is known as the **game loop**.

Almost every turn-based game follows a similar pattern.

---

# Testing the Game Engine

We don't have a graphical interface yet.

That's okay.

We can still test the engine using simple Python code.

For now, create two simple test agents.

```python
class TestAgent:

    @property
    def name(self):
        return "Test Agent"

    def choose_move(self, state):
        return state.valid_moves[0]
```

Then:

```python
from connect4.game import Game

agent_one = TestAgent()
agent_two = TestAgent()

game = Game(agent_one, agent_two)

while not game.game_over:
    game.play_turn()

print("Game Over")
print("Winner:", game.winner)
print("Turns:", game.turns)
print(game.board)
```

The game should finish without crashing.

The exact result will depend on how the test agents choose their moves.

---

# Architecture Checkpoint

Your project now has a clear separation of responsibilities:

```text
Board
 │
 ├── Stores pieces
 ├── Validates moves
 └── Copies the board
       │
       ▼
Rules
 │
 ├── Detects wins
 ├── Detects draws
 └── Detects terminal states
       │
       ▼
GameState
 │
 └── Describes the current position
       │
       ▼
Game
 │
 ├── Manages turns
 ├── Requests moves
 ├── Controls the match
 └── Stores the result
```

Each class has a specific responsibility.

This separation will become very important when we add the graphical interface next week.

---

# Knowledge Check

Before moving on, make sure you can answer the following questions:

1. Why doesn't the Board class detect wins?
2. What is the purpose of the `Rules` class?
3. Why is `GameState` immutable?
4. Why does `GameState` contain `valid_moves`?
5. Why does the Game create a copy of the board for the AI?
6. What does `current_agent` do?
7. What happens after an AI chooses a move?
8. Why does the game check for a win before switching players?
9. What is the purpose of `MatchResult`?
10. What happens when `play_turn()` returns `False`?

If you can answer these questions confidently, you've understood the architecture of the game engine.

---


# Week 3 Checklist

Before moving on to Week 4, make sure you've completed:

- [ ] Created `rules.py`
- [ ] Implemented horizontal win detection
- [ ] Implemented vertical win detection
- [ ] Implemented positive diagonal win detection
- [ ] Implemented negative diagonal win detection
- [ ] Implemented draw detection
- [ ] Implemented terminal-state detection
- [ ] Tested different win patterns
- [ ] Created `state.py`
- [ ] Created the immutable `GameState`
- [ ] Created `match_result.py`
- [ ] Created `MatchResult`
- [ ] Created `game.py`
- [ ] Implemented player switching
- [ ] Implemented game turns
- [ ] Implemented game reset
- [ ] Implemented match results
- [ ] Successfully ran a complete game
- [ ] Committed and pushed your work to GitHub

---

# Week 3 Summary

Congratulations! 🎉

This week you've completed the core game engine.

You created:

- `rules.py`
- `state.py`
- `match_result.py`
- `game.py`

You also learned:

- How wins and draws are detected.
- Why software projects separate responsibilities into different classes.
- Why immutable game states are useful.
- How a game loop works.
- How an entire Connect 4 match is controlled.
- How the game communicates with AI agents.
- How completed matches can be represented with a result object.

Your project can now manage a complete game from start to finish.

---

# Looking Ahead

Next week, we'll bring everything to life.

You'll use **Pygame** to create a graphical interface that displays the board, pieces, and game state.

You'll learn how to:

- Create a game window.
- Draw the Connect 4 board.
- Draw player pieces.
- Display game information.
- Connect the renderer to your game engine.
- Build a basic graphical game loop.

By the end of Week 4, you'll be able to watch your Connect 4 game play out visually on the screen.

See you in **Week 4!** 🚀
