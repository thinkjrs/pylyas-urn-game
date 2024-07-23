"""state.py 

This module contains the GameState class
"""


class GameState:
    """A class to store the game state."""

    def __init__(self, initial_red: int, initial_blue: int):
        self.urn = {"red": initial_red, "blue": initial_blue}
        self.draw_history = []

    def draw_ball(self, color: str):
        self.urn[color] += 1
        self.draw_history.append(color)
