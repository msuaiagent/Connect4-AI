"""
run.py

Entry point for the Connect 4 AI framework.
"""

from __future__ import annotations

import pygame

from agents.student_agent import StudentAgent
from agents.random_agent import RandomAgent

from connect4.game import Game
from connect4.renderer import Renderer
from connect4.constants import FPS


def main() -> None:

    player_one = RandomAgent()
    player_two = StudentAgent()

    game = Game(
        player_one=player_one,
        player_two=player_two,
    )

    renderer = Renderer()

    clock = pygame.time.Clock()

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        if not game.game_over:
            game.play_turn()

        renderer.draw(game)

        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
