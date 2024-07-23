import pytest
from run import (
    run_game,
)
from config import GameConfig

config = GameConfig(10, 10, "red", 10)


def test_run_game():
    game, player_guess = run_game(config, 10)
    assert game.urn["red"] > 1, "Initial values not set correctly."
    assert game.urn["blue"] > 1, "Initial values not set correctly."
    assert player_guess.guess == 10, "Player guess not set correctly."
    assert player_guess.actual is not None, "player_guess.actual was None."


if __name__ == "__main__":
    pytest.main()
