import pytest
from unittest.mock import patch
from output import (
    print_welcome_message,
    get_ball_color,
    print_results,
    make_chart,
)
from config import GameConfig
from guess import PlayerGuess


def test_print_welcome_message(capsys):
    print_welcome_message()
    captured = capsys.readouterr()
    assert "👋 Welcome to the Polya's Urn Game" in captured.out
    assert "The lowest score wins!" in captured.out


def test_get_ball_color():
    result = get_ball_color("red")
    assert result == "[red]red balls[/red]"
    result = get_ball_color("blue")
    assert result == "[blue]blue balls[/blue]"


def test_print_results(capsys):
    config = GameConfig(
        initial_red=10, initial_blue=10, first_draw="red", num_steps=10
    )
    guess = PlayerGuess(guess=10)
    print_results(config, guess)
    captured = capsys.readouterr()
    assert "Your score: " in captured.out
    assert "You guessed: 10" in captured.out


def test_make_chart(capsys):
    with patch("output.console.print") as mock_print:
        make_chart(5, 3, "Test Title")
        mock_print.assert_called_once()
        args, _ = mock_print.call_args
        table = args[0]
        assert "5 Red" in table.columns[0].header
        assert "3 Blue" in table.columns[1].header
        assert table.title == "Test Title"


if __name__ == "__main__":
    pytest.main()
