# Week 2: Building the Connect 4 Board

Last week, you prepared your development environment and set up your project.

This week, we'll begin building the foundation of Connect 4 itself.

Before we can create an AI, we first need to create a game for the AI to play.

We'll start by representing the Connect 4 board in Python and creating the `Board` class that will manage it.

By the end of this week, you'll have built the core board representation that every part of the project, including the AI, will eventually use.


---

# Learning Objectives

By the end of this week, you should be able to:

- Explain how Connect 4 is represented in code.
- Understand the purpose of the `Board` class.
- Use constants to improve code readability.
- Store a Connect 4 board using a two-dimensional list.
- Validate legal moves.
- Drop pieces into the board.
- Create independent copies of the board.
- Print the board for debugging.

---

# What You'll Build

By the end of this week, you'll have created:

```text
connect4/
├── __init__.py
├── constants.py
└── board.py
```

These files form the foundation of the rest of the project.

The `Board` class will eventually be used by:

- The game engine.
- The rules system.
- The renderer.
- Your AI agent.

---

# Before We Start

Imagine you're building a chess AI.

Would you start by programming the AI?

Probably not.

First, you'd need a chess board.

Then you'd need the rules.

Then you'd need a way to move pieces.

Only after those foundations exist can an AI begin making decisions.

The same idea applies here.

Before we build our AI, we need to build the game it will play.

---

# How Computers Represent Connect 4

Humans might see a board like this:

```text
🔴 🟡 🔴 ⚪ ⚪ ⚪ ⚪
🟡 🔴 🟡 ⚪ ⚪ ⚪ ⚪
```

A computer doesn't need coloured pieces to represent the game.

Instead, we'll use numbers:

```text
0 = Empty

1 = Player One

2 = Player Two
```

For example:

```text
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 1 0 0 0 0
2 1 2 1 2 0 0
```

This allows Python to store and manipulate the board easily.

---

# Two-Dimensional Lists

A Connect 4 board contains rows and columns.

In Python, we can represent this using a **two-dimensional list**.

For example:

```python
board = [
    [0, 0, 0],
    [1, 0, 2],
    [2, 1, 1]
]
```

You can access a specific position using:

```python
board[row][column]
```

For example:

```python
board[1][2]
```

returns:

```text
2
```

because it refers to the second row and third column.

Our Connect 4 board will contain:

- 6 rows
- 7 columns

---

# Task 1 — Create `constants.py`

Create a new file:

```text
connect4/constants.py
```

Throughout the project, we'll use several values repeatedly.

Instead of writing numbers such as `6`, `7`, or `1` throughout our code, we'll define them once as named constants.

This makes the code easier to understand and easier to maintain.

---

## TODO

Create constants for:

### Board configuration

- Number of rows.
- Number of columns.
- Number of pieces needed to connect.

### Players

- Empty space.
- Player One.
- Player Two.

### Display

We'll also define some values that will be needed when we add graphics later.

Try creating these constants yourself before viewing the solution.

---

## Solution

```python
"""
constants.py

Project-wide constants used throughout the Connect 4 project.
"""

# ==========================================================
# Board Configuration
# ==========================================================

ROWS = 6
COLS = 7
CONNECT = 4

# ==========================================================
# Players
# ==========================================================

EMPTY = 0
PLAYER_ONE = 1
PLAYER_TWO = 2

# ==========================================================
# Display
# ==========================================================

SQUARE_SIZE = 100

WIDTH = COLS * SQUARE_SIZE
HEIGHT = (ROWS + 1) * SQUARE_SIZE

FPS = 1

WINDOW_TITLE = "Connect 4 AI"

# ==========================================================
# Colours (RGB)
# ==========================================================

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

BLUE = (0, 102, 204)

RED = (220, 20, 60)
YELLOW = (255, 215, 0)
```

---

# Why Do We Use Constants?

Consider this:

```python
if player == 1:
```

What does `1` mean?

It could be Player One.

It could be something completely different.

Now compare it with:

```python
if player == PLAYER_ONE:
```

The second version is much easier to understand.

Constants also make future changes easier.

For example, if we wanted to experiment with a larger board, we could change:

```python
ROWS = 8
```

instead of searching through the entire project for every occurrence of `6`.

---

# Task 2 — Understanding the Board Class

Create a new file:

```text
connect4/board.py
```

The `Board` class is responsible for storing the current state of the game.

It has one main responsibility:

> **Store and manage the board.**

The Board class should be able to:

- Create an empty board.
- Reset the board.
- Check whether a move is legal.
- Find all legal moves.
- Drop a piece into a column.
- Create an independent copy of the board.
- Display the board for debugging.

Notice what the Board class **doesn't** do.

It doesn't:

- Decide whose turn it is.
- Detect wins.
- Detect draws.
- Ask an AI for a move.
- Draw graphics.
- Control the game loop.

Keeping each class focused on one responsibility makes the project easier to understand and maintain.

---

# Task 3 — Creating the `Board` Class

Before looking at the solution, think about what the constructor needs to do.

A new `Board` should start completely empty.

---

## TODO

Create:

```python
class Board:
```

Then create an `__init__()` method that creates an empty board.

Try it yourself first.

---

## Solution

```python
from .constants import ROWS, COLS, EMPTY


class Board:

    def __init__(self):
        self.reset()
```

We'll build the `reset()` method next.

---

# Task 4 — Creating `reset()`

A board should be able to return to its starting state.

---

## TODO

Create a method called:

```python
reset()
```

It should create a two-dimensional list containing:

```text
ROWS × COLS
```

empty positions.

Hint:

You can use a list comprehension.

Try it yourself before viewing the solution.

---

## Solution

```python
def reset(self):
    """Reset the board to an empty state."""

    self.grid = [
        [EMPTY for _ in range(COLS)]
        for _ in range(ROWS)
    ]
```

After calling:

```python
board = Board()
```

the board will contain:

```text
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

---

# Task 5 — Checking Legal Moves

Not every column can accept a piece.

For example:

- Column `-1` doesn't exist.
- Column `7` doesn't exist.
- A completely full column cannot accept another piece.

We need a method that checks whether a move is legal.

---

## TODO

Create:

```python
is_valid_move(column)
```

The method should return:

```text
True
```

if the move is legal, and:

```text
False
```

otherwise.

Think about what conditions would make a column invalid.

---

## Solution

```python
def is_valid_move(self, column):
    """
    Return True if a move can be played
    in the given column.
    """

    if column < 0 or column >= COLS:
        return False

    return self.grid[0][column] == EMPTY
```

---

# Why Check the Top Row?

Connect 4 pieces fall downward.

If the top position of a column is already occupied, there is no space left anywhere in that column.

Therefore:

```python
self.grid[0][column]
```

is enough to determine whether the column is full.

---

# Task 6 — Finding All Legal Moves

Checking one column at a time is useful, but our game and AI will often need to know **all** available moves.

---

## TODO

Create:

```python
valid_moves()
```

It should return a list containing every legal column.

For example:

```text
[0, 1, 2, 3, 5]
```

means columns `0`, `1`, `2`, `3`, and `5` are available.

Try implementing this yourself.

---

## Solution

```python
def valid_moves(self):
    """Return every legal column."""

    return [
        column
        for column in range(COLS)
        if self.is_valid_move(column)
    ]
```

---

# Task 7 — Dropping a Piece

Now we need to simulate how a real Connect 4 piece behaves.

If a player chooses a column, their piece falls to the lowest available position.

---

## TODO

Create:

```python
drop_piece(column, player)
```

The method should:

1. Check whether the move is legal.
2. Start at the bottom row.
3. Search upward.
4. Find the first empty position.
5. Place the player's piece there.
6. Return `True` if successful.

If the move is invalid, return `False`.

Try implementing it yourself before viewing the solution.

---

## Solution

```python
def drop_piece(self, column, player):
    """
    Drop a piece into the specified column.

    Returns True if successful.
    Returns False if the move is invalid.
    """

    if not self.is_valid_move(column):
        return False

    for row in range(ROWS - 1, -1, -1):

        if self.grid[row][column] == EMPTY:

            self.grid[row][column] = player
            return True

    return False
```

---

# Why Search From the Bottom?

Connect 4 pieces fall downward.

Therefore, when a piece is placed in a column, we need to find the lowest empty position.

This loop:

```python
for row in range(ROWS - 1, -1, -1):
```

starts at the bottom row and moves upward.

This matches the behaviour of the real game.

---

# Task 8 — Creating a Board Copy

This is one of the most important methods we'll build this week.

Later in the project, your AI will need to experiment with possible moves.

For example, it might want to ask:

> "What would happen if I played in column 3?"

We don't want the AI to experiment on the real game board.

Instead, it can create a copy, test its idea on the copy, and leave the real board unchanged.

---

## TODO

Create:

```python
copy()
```

The method should return a completely independent copy of the current board.

Try implementing it yourself.

Hint:

You will need Python's `deepcopy()` function.

---

## Solution

First import:

```python
from copy import deepcopy
```

Then create:

```python
def copy(self):
    """Return a deep copy of the board."""

    new_board = Board()
    new_board.grid = deepcopy(self.grid)

    return new_board
```

---

# Why Do We Need `deepcopy()`?

Consider this:

```python
new_board.grid = self.grid
```

Both boards would now refer to the same list.

Changing one board could therefore change the other.

That's not what we want.

Instead:

```python
deepcopy(self.grid)
```

creates a completely independent copy.

This allows an AI to safely experiment with possible moves.

---

# Task 9 — Printing the Board

Being able to inspect the board is extremely useful while debugging.

---

## TODO

Add a method that allows:

```python
print(board)
```

to display the board contents.

Hint:

Python uses a special method called:

```python
__str__()
```

Try creating it yourself.

---

## Solution

```python
def __str__(self):
    """Return a printable version of the board."""

    return "\n".join(
        " ".join(str(cell) for cell in row)
        for row in self.grid
    )
```

---

# Task 10 — Accessing Board Positions

Throughout the project, we'll frequently want to access a board position like:

```python
board[row][column]
```

Our board currently stores the actual data in:

```python
board.grid
```

We can make `board[row][column]` work directly by implementing `__getitem__()`.

---

## TODO

Create:

```python
__getitem__(row)
```

It should return the requested row from the board.

---

## Solution

```python
def __getitem__(self, row):
    """Allow board[row][column] syntax."""

    return self.grid[row]
```

Now both of these refer to the same position:

```python
board.grid[2][3]
```

and:

```python
board[2][3]
```

The second form will make the rest of our project cleaner.

---

# Complete `board.py`

You've now built every part of the `Board` class.

If you got stuck along the way, compare your file with the complete version below.

```python
"""
board.py

Contains the Board class.

Responsibilities
----------------
- Store the board state
- Validate moves
- Drop pieces
- Reset the board
- Create board copies

The Board class intentionally contains NO game logic such as
win detection or draw detection. Those responsibilities belong
to Rules.
"""

from __future__ import annotations

from copy import deepcopy

from .constants import ROWS, COLS, EMPTY


class Board:
    """Represents a Connect 4 board."""

    def __init__(self) -> None:
        self.reset()

    @property
    def rows(self) -> int:
        return ROWS

    @property
    def cols(self) -> int:
        return COLS

    def reset(self) -> None:
        """Clear the board."""

        self.grid = [
            [EMPTY for _ in range(COLS)]
            for _ in range(ROWS)
        ]

    def copy(self) -> "Board":
        """Return a deep copy of the board."""

        new_board = Board()
        new_board.grid = deepcopy(self.grid)
        return new_board

    def is_valid_move(self, column: int) -> bool:
        """Return True if a piece can be dropped into the column."""

        if not 0 <= column < COLS:
            return False

        return self.grid[0][column] == EMPTY

    def valid_moves(self) -> list[int]:
        """Return all legal moves."""

        return [
            column
            for column in range(COLS)
            if self.is_valid_move(column)
        ]

    def drop_piece(
        self,
        column: int,
        player: int,
    ) -> bool:
        """
        Drop a piece into the specified column.

        Returns
        -------
        bool
            True if successful.
            False if the move is invalid.
        """

        if not self.is_valid_move(column):
            return False

        for row in range(ROWS - 1, -1, -1):

            if self.grid[row][column] == EMPTY:

                self.grid[row][column] = player
                return True

        return False

    def __getitem__(self, row: int):
        """Allow board[row][column] syntax."""

        return self.grid[row]

    def __str__(self) -> str:

        return "\n".join(
            " ".join(str(cell) for cell in row)
            for row in self.grid
        )
```

---

# Testing Your Board

Before moving on, let's make sure everything works.

Create a temporary Python file or use the VS Code Python terminal.

Run:

```python
from connect4.board import Board
from connect4.constants import PLAYER_ONE, PLAYER_TWO

board = Board()

print(board)
```

You should see:

```text
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```

---

# Test Dropping Pieces

Now try:

```python
board.drop_piece(3, PLAYER_ONE)
board.drop_piece(3, PLAYER_TWO)

print(board)
```

You should see the two pieces stacked in column `3`.

The second piece should appear directly above the first because Connect 4 pieces fall downward.

---

# Test Legal Moves

Run:

```python
print(board.valid_moves())
```

You should see a list of available columns.

Now fill a column completely:

```python
for _ in range(6):
    board.drop_piece(0, PLAYER_ONE)
```

Then:

```python
print(board.is_valid_move(0))
```

should return:

```text
False
```

because column `0` is now full.

---

# Test Board Copies

Let's make sure our copies are independent.

Run:

```python
original = Board()

original.drop_piece(3, PLAYER_ONE)

copy = original.copy()

copy.drop_piece(3, PLAYER_TWO)

print("Original:")
print(original)

print()

print("Copy:")
print(copy)
```

The two boards should be different.

The original board should contain only Player One's piece.

The copied board should contain both pieces.

This confirms that the boards are independent.

---

# Checkpoint

Before moving on, make sure you can answer the following questions:

- Why do we use constants instead of writing numbers directly?
- How is the Connect 4 board stored in memory?
- What does `valid_moves()` return?
- Why does `drop_piece()` search from the bottom upwards?
- Why is `copy()` important for AI?
- What is the responsibility of the `Board` class?

If you can answer these questions and your tests work correctly, you've completed the main objectives of Week 2.

---

# Optional Challenges

## Challenge 1 — Change the Board Size

Change:

```python
ROWS = 6
```

to:

```python
ROWS = 8
```

What happens?

Can you explain why?

Try changing `COLS` as well.

---

## Challenge 2 — Fill a Column

Write a short loop that fills one column completely.

Then check:

```python
board.is_valid_move(column)
```

What does it return?

---

## Challenge 3 — Experiment With Copies

Create a board, make a copy, and make several different moves on each board.

Can you verify that changing one board never changes the other?

---

# Week 2 Summary

Congratulations! 🎉

This week you've built the foundation of the entire project.

You created:

- `constants.py`
- `board.py`

You learned:

- How Connect 4 is represented in code.
- Why constants improve readability.
- How a two-dimensional list represents the board.
- How the `Board` class stores game state.
- How legal moves are validated.
- How pieces fall into a column.
- How to create independent board copies.
- How to inspect the board while debugging.

Although we haven't built the game engine or AI yet, you've completed one of the most important foundations of the project.

Every component we build from this point forward will rely on the `Board` class.

---

# Looking Ahead

Next week, we'll turn the board into a functioning Connect 4 game engine.

You'll build:

```text
connect4/
├── rules.py
├── state.py
├── match_result.py
└── game.py
```

You'll learn how to:

- Detect wins.
- Detect draws.
- Manage player turns.
- Track the current game state.
- Create a complete game loop.
- Separate different responsibilities into different classes.

By the end of Week 3, your project will be able to manage an entire Connect 4 game from beginning to end.

See you in **Week 3!** 🚀
