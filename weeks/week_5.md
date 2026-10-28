# Week 5: Building Your First AI

Over the past four weeks, you've built a complete Connect 4 game.

You created the board, game engine, and graphical interface.

Although your game can already play itself, the agents making the moves have only been used for testing.

This week, that changes.

You'll create your own AI agent and connect it to the game.

Instead of simply following a fixed set of instructions, your AI will begin making its own decisions based on the current game state.

By the end of this week, your AI will be capable of playing complete games of Connect 4.

---

# Learning Objectives

By the end of this week, you should be able to:

- Explain what an AI agent is.
- Understand the purpose of an abstract base class.
- Create your own AI agent.
- Work with the `GameState` provided to an AI.
- Choose legal moves.
- Connect your AI to the game engine.
- Experiment with different ways of making decisions.
- Test your AI against another agent.

---

# What You'll Build

This week you'll create:

```text
agents/
├── base_agent.py
└── student_agent.py
```

`base_agent.py` defines the common interface that every AI must follow.

`student_agent.py` is where you'll build and improve your own AI.

By the end of this week, your AI will be making decisions inside the game.

---

# What is an AI Agent?

When people hear the term **Artificial Intelligence**, they often imagine something extremely complicated.

For this project, an AI agent is much simpler.

Every turn, the game asks one question:

> **"Which column would you like to play?"**

The AI receives information about the current game and returns a single legal move.

The game then makes that move.

This process repeats until the game ends.

A simple AI might make decisions randomly or follow a basic strategy.

A more advanced AI might analyze the board, consider possible future moves, or compare different outcomes.

For now, your goal is to build the foundation that allows your AI to make decisions.

---

# Task 1 – Creating the Base Agent

Create a new file:

```text
agents/base_agent.py
```

Every AI in our project should have the same basic structure.

Rather than letting every AI use different method names, we'll define a common interface.

This interface is called `BaseAgent`.

Every AI we build will inherit from this class.

---

## TODO

Before looking at the solution, think about what every AI should provide.

Hints:

- Every AI should have a name.
- Every AI should be able to choose a move.
- The move should be chosen using a `GameState`.

Try to identify the two things the Game class needs from every AI.

---

## Solution

Copy the following code into `base_agent.py`.

```python
"""
base_agent.py

Defines the abstract interface for all Connect 4 agents.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from connect4.state import GameState


class BaseAgent(ABC):
    """Abstract base class for all Connect 4 agents."""

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Human-readable name of the agent.
        """
        ...

    @abstractmethod
    def choose_move(self, state: GameState) -> int:
        """
        Decide which column to play.

        Parameters
        ----------
        state : GameState
            Immutable snapshot of the current game.

        Returns
        -------
        int
            Column index (0–6).
        """
        ...
```

---

# Why Use a Base Class?

Imagine you had ten different AI agents.

If each one used different method names, the `Game` class wouldn't know how to communicate with them.

Instead, every AI follows the same interface:

- It has a name.
- It implements `choose_move()`.

This means the `Game` class can work with **any** AI without needing to know how it was implemented.

For example, the game doesn't need to know whether an AI:

- chooses randomly,
- follows a simple strategy,
- evaluates the board,
- or uses a more advanced algorithm.

The game only needs to know that it can call:

```python
agent.choose_move(state)
```

This separation between the **game engine** and the **AI's decision-making** is an important part of the project architecture.

---

# Task 2 – Understanding GameState

Before creating your AI, take a look at:

```text
connect4/state.py
```

Your AI does not directly control the `Board`.

Instead, the game gives the AI a `GameState`.

The state contains information such as:

- The current board.
- Whose turn it is.
- Which columns are currently legal.

For example:

```python
state.board
state.current_player
state.valid_moves
```

The AI can use this information to decide what move to make.

---

## Why Give the AI a GameState?

The AI needs information about the game before it can make a decision.

For example, it needs to know:

> "Which columns can I legally play?"

That's why `GameState` contains:

```python
valid_moves
```

It also needs to know what the board currently looks like:

```python
board
```

And it needs to know which player is making the move:

```python
current_player
```

The AI uses this information to make its decision.

---

# Task 3 – Creating Your First AI

Create a new file:

```text
agents/student_agent.py
```

This is your AI.

Throughout the rest of the project, this is the AI you'll continue improving.

---

## TODO

Your AI doesn't need to be intelligent yet.

For now, simply make sure it always returns a legal move.

Hints:

- Look at `state.valid_moves`.
- The game expects a column number.
- Return one of the available moves.

Try implementing it yourself before viewing the solution.

---

## Solution

Copy the following code into `student_agent.py`.

```python
"""
student_agent.py

Students will implement their AI in this file.
"""

from __future__ import annotations

from .base_agent import BaseAgent

from connect4.state import GameState


class StudentAgent(BaseAgent):
    """Student-created Connect 4 AI."""

    @property
    def name(self) -> str:
        return "Student AI"

    def choose_move(self, state: GameState) -> int:
        """
        Choose a legal move.

        For now, select the first available move.
        """

        return state.valid_moves[0]
```

---

# Understanding Your First AI

Your AI is extremely simple right now.

When the game asks:

```python
move = agent.choose_move(state)
```

your AI looks at the legal moves and returns the first one.

For example, if:

```python
state.valid_moves
```

contains:

```text
(0, 1, 2, 3, 4, 5, 6)
```

your AI returns:

```text
0
```

If column `0` becomes unavailable, the list might look like:

```text
(1, 2, 3, 4, 5, 6)
```

and your AI will return:

```text
1
```

The strategy isn't important yet.

What's important is that you've created an AI that follows the required interface and makes legal moves.

---

# Task 4 – Connecting Your AI to the Game

Now connect your new AI to the game engine.

Open:

```text
run.py
```

Import your `StudentAgent`:

```python
from agents.student_agent import StudentAgent
```

Then create your players:

```python
player_one = RandomAgent()
player_two = StudentAgent()
```

Your `run.py` should now use the two agents in the game:

```python
game = Game(
    player_one=player_one,
    player_two=player_two,
)
```

Run the project:

```bash
python run.py
```

Your AI should now be playing complete games against the `RandomAgent`.

---

# Testing Your AI

Play several games and make sure:

- The game starts normally.
- Your AI makes a move every turn.
- Your AI never chooses a full column.
- The game correctly detects wins.
- The game correctly detects draws.
- The game eventually ends.

If you encounter an error, check that:

- `StudentAgent` inherits from `BaseAgent`.
- `choose_move()` accepts a `GameState`.
- `choose_move()` returns a value from `state.valid_moves`.
- `run.py` imports `StudentAgent` correctly.

---

# Task 5 – Start Experimenting

Your AI currently makes legal moves, but it doesn't make meaningful decisions.

Now it's time to start experimenting.

There is **no single correct strategy** you need to use.

The goal of this project is for you to develop your own approach to making decisions.

Think about questions such as:

- What information should my AI pay attention to?
- How could my AI decide which legal move is better?
- What makes one move stronger than another?
- Should the AI consider the opponent's position?
- Should it consider what might happen after a move?
- How can I test whether a change actually improves my AI?

You don't need to solve all of these questions this week.

The important thing is to start thinking about Connect 4 as a **decision-making problem**.

---

# Experimentation Challenge

Modify your `choose_move()` method so that your AI makes a decision using information from the `GameState`.

You are free to experiment.

For example, you could investigate:

- Different ways of selecting legal moves.
- How the current board affects your decision.
- How your own pieces affect your choices.
- How your opponent's pieces affect your choices.
- Whether your AI performs differently when you change its decision-making process.

**Do not worry about creating a perfect AI.**

At this stage, you're learning how to turn an idea into a program that makes decisions.

---

# Testing Different Ideas

A change to your AI doesn't automatically mean your AI became better.

You need to test it.

Try playing multiple games against the `RandomAgent`.

Record your observations.

For example:

| Version | Games Played | Wins | Losses | Draws |
|---------|--------------|------|--------|-------|
| Original | 10 | — | — | — |
| Experiment 1 | 10 | — | — | — |
| Experiment 2 | 10 | — | — | — |

The exact results will depend on your implementation.

The important part is learning to compare different versions of your AI.

---

# Knowledge Check

Before moving on, make sure you can answer the following questions.

1. What is the purpose of `BaseAgent`?
2. Why does every AI inherit from it?
3. What information does the AI receive?
4. What does `state.valid_moves` contain?
5. What must `choose_move()` return?
6. Why does the game give the AI a `GameState` instead of the entire game?
7. Why is testing important when improving an AI?

If you can answer these questions confidently, you've completed the core concepts of this week's lesson.

---

# Optional Challenge

Can you make your AI behave differently without changing the `Game` class?

Try experimenting with your `StudentAgent`.

Your goal is to make the AI's decisions more deliberate while keeping the same interface:

```python
def choose_move(self, state: GameState) -> int:
```

Remember:

**The Game controls the game.**

**Your AI controls the decisions.**

Keep that separation in mind as you experiment.

---

# Week 5 Summary

Congratulations! 🎉

This week you've built your first AI agent.

You created:

- `base_agent.py`
- `student_agent.py`

You also learned:

- What an AI agent is.
- Why common interfaces are useful.
- What an abstract base class does.
- How the game communicates with an AI.
- What information is contained in a `GameState`.
- How to choose legal moves.
- How to connect your AI to the game.
- How to test and compare different AI ideas.

Most importantly, you've moved from building the game itself to building a program that makes decisions inside the game.

Your AI is still simple, but it now has the foundation needed to become much stronger.

---

# Looking Ahead

Your AI can now make legal decisions, but there is plenty of room for improvement.

Next week, you'll focus on making your AI more intelligent.

You'll experiment with ways to:

- Recognize useful opportunities.
- Respond to the opponent.
- Evaluate possible moves.
- Compare different decisions.
- Measure whether your changes actually improve performance.

The exact approach you take is up to you.

By the end of Week 6, you'll have a much stronger version of your own Connect 4 AI.

See you in **Week 6!** 🚀
