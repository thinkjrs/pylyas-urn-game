"""config.py

This file contains game configuration functionality.
"""
from enum import Enum


class GameConfig:
    """A class to store game configuration parameters."""

    def __init__(
        self,
        initial_red: int,
        initial_blue: int,
        first_draw: str,
        num_steps: int,
    ):
        self.initial_red = initial_red
        self.initial_blue = initial_blue
        self.first_draw = first_draw
        self.num_steps = num_steps


class BallColor(str, Enum):
    red = "red"
    blue = "blue"
