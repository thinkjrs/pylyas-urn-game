import pytest
from input import parse_inputs
from config import BallColor


def test_parse_inputs_all_provided():
    initial_red = 5
    initial_blue = 3
    number_of_trials = 10
    first_draw_choice = BallColor.red
    user_guess = 7

    result = parse_inputs(
        initial_red,
        initial_blue,
        number_of_trials,
        first_draw_choice,
        user_guess,
    )
    assert result == (
        initial_red,
        initial_blue,
        number_of_trials,
        first_draw_choice,
        user_guess,
    )


def test_parse_inputs_missing_initial_red(monkeypatch):
    monkeypatch.setattr("input.IntPrompt.ask", lambda *args, **kwargs: 5)
    result = parse_inputs(None, 3, 10, BallColor.red, 7)
    assert result == (5, 3, 10, BallColor.red, 7)


def test_parse_inputs_missing_initial_blue(monkeypatch):
    monkeypatch.setattr("input.IntPrompt.ask", lambda *args, **kwargs: 3)
    result = parse_inputs(5, None, 10, BallColor.red, 7)
    assert result == (5, 3, 10, BallColor.red, 7)


def test_parse_inputs_missing_number_of_trials(monkeypatch):
    monkeypatch.setattr("input.IntPrompt.ask", lambda *args, **kwargs: 10)
    result = parse_inputs(5, 3, None, BallColor.red, 7)
    assert result == (5, 3, 10, BallColor.red, 7)


def test_parse_inputs_missing_first_draw_choice(monkeypatch):
    monkeypatch.setattr(
        "input.click.prompt", lambda *args, **kwargs: BallColor.red
    )
    result = parse_inputs(5, 3, 10, None, 7)
    assert result == (5, 3, 10, BallColor.red, 7)


def test_parse_inputs_missing_user_guess(monkeypatch):
    monkeypatch.setattr("input.IntPrompt.ask", lambda *args, **kwargs: 7)
    result = parse_inputs(5, 3, 10, BallColor.red, None)
    assert result == (5, 3, 10, BallColor.red, 7)


def test_parse_inputs_missing_multiple_values(monkeypatch):
    inputs = iter([5, 3, 10, 7])
    monkeypatch.setattr(
        "input.IntPrompt.ask", lambda *args, **kwargs: next(inputs)
    )
    monkeypatch.setattr(
        "input.click.prompt", lambda *args, **kwargs: BallColor.red
    )
    result = parse_inputs(None, None, None, None, None)
    assert result == (5, 3, 10, BallColor.red, 7)


# def test_parse_inputs_raises_value_error(monkeypatch):
#    inputs = iter([5, 3, 10, 7])
#
#    with pytest.raises(
#        ValueError, match="You did not set all values. Try again."
#    ):
#        monkeypatch.setattr(
#            "input.click.prompt", lambda *args, **kwargs: BallColor.red
#        )
#
#        parse_inputs(None, None, None, None, None)


if __name__ == "__main__":
    pytest.main()
