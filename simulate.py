"""simulate.py 

This module contains a function to simulate the number of balls in the urn.
"""

import random
from state import GameState


def simulate_draw(game_state: GameState, steps: int):
    """A function to simulate the number of balls in the urn."""
    for _ in range(steps):
        total_balls = sum(game_state.urn.values())
        draw_prob = random.random()
        red_prob = game_state.urn["red"] / total_balls
        if draw_prob < red_prob:
            game_state.draw_ball("red")
            continue
        game_state.draw_ball("blue")
