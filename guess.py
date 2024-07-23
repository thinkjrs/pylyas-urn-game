"""guess.py

This module contains the PlayerGuess class and any other functionality needed for managing the actual guess the player makes.
"""


class PlayerGuess:
    """A class to store what the player guessed and evaluate it once the actual number is known."""

    def __init__(self, guess: int):
        self.guess = guess
        self.actual: None | int = None
        self.distance: None | int = None

    def evaluate(self, actual: int):
        self.actual = actual
        self.distance = abs(self.guess - self.actual)
