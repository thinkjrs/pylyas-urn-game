"""input.py 

This module contains functions for parsing command-line arguments and reporting erros to the player.
"""
import click
from rich.prompt import IntPrompt
from config import BallColor


def parse_inputs(
    initial_red: None | int,
    initial_blue: None | int,
    number_of_trials: None | int,
    first_draw_choice: BallColor | None,
    user_guess: int | None,
):
    if not initial_red:
        initial_red = IntPrompt.ask(
            "The starting number of [red]red balls[/red]",
        )
    if not initial_blue:
        initial_blue = IntPrompt.ask(
            "The starting number of [blue]blue balls[/blue]",
        )
    if not number_of_trials:
        number_of_trials = IntPrompt.ask("The number of trials to run")
    if not first_draw_choice:
        first_draw_choice = click.prompt(
            "The color to draw first", type=BallColor, default=BallColor.red
        )
    if (
        not initial_red
        or not initial_blue
        or not number_of_trials
        or not first_draw_choice
    ):
        raise ValueError("You did not set all values. Try again.")

    if not user_guess:
        # prompt user for a guess
        user_guess = IntPrompt.ask(
            f"Enter the number of [{first_draw_choice.value}]{first_draw_choice.value} balls[/{first_draw_choice.value}] in the urn at the end",
        )
    return (
        initial_red,
        initial_blue,
        number_of_trials,
        first_draw_choice,
        user_guess,
    )
