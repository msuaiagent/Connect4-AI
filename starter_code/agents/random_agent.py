"""
random_agent.py

Simple benchmark AI.
"""

from __future__ import annotations

import random

from .base_agent import BaseAgent

from connect4.state import GameState


class RandomAgent(BaseAgent):
    """Random-move benchmark agent."""

    @property
    def name(self) -> str:
        return "Random AI"

    def choose_move(self, state: GameState) -> int:
        """Return a random legal move."""

        return random.choice(state.valid_moves)
