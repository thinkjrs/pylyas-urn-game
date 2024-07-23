"""run.py 

This module contains the main functions that run the game.
"""
from state import GameState
from config import GameConfig, BallColor
from simulate import simulate_draw
from guess import PlayerGuess
import typer
from typing import Optional
from typing_extensions import Annotated
from output import print_results, make_chart
from input import parse_inputs


def run_game(config, guess_value):
    # Initialize game state
    game_state = GameState(config.initial_red, config.initial_blue)

    # First draw
    game_state.draw_ball(config.first_draw)

    # Simulate remaining steps
    simulate_draw(game_state, config.num_steps - 1)

    # Player's guess
    player_guess = PlayerGuess(guess_value)

    # Evaluate the guess
    player_guess.evaluate(
        game_state.urn[config.first_draw]
    )  # or 'blue' depending on what the player guessed

    # Return results
    return game_state, player_guess


def main(
    initial_red: Annotated[
        Optional[int],
        typer.Argument(
            help="The number of red balls with which to start.",
        ),
    ] = None,
    initial_blue: Annotated[
        Optional[int],
        typer.Argument(help="The number of blue balls with which to start."),
    ] = None,
    number_of_trials: Annotated[
        Optional[int],
        typer.Argument(help="The number of trials to simulate."),
    ] = None,
    first_draw_choice: Annotated[
        Optional[BallColor],
        typer.Argument(help="The color of ball to draw first; 🔴 or 🔵."),
    ] = None,
    user_guess: Annotated[
        Optional[int],
        typer.Argument(
            help="Your guess for the final number of balls you chose to draw first after the final simulation.",
        ),
    ] = None,
):
    (
        initial_red,
        initial_blue,
        number_of_trials,
        first_draw_choice,
        user_guess,
    ) = parse_inputs(
        initial_red,
        initial_blue,
        number_of_trials,
        first_draw_choice,
        user_guess,
    )
    # setup config
    config = GameConfig(
        initial_red, initial_blue, first_draw_choice.value, number_of_trials
    )

    # run the simulation
    state, guess = run_game(config, user_guess)

    # report the results
    make_chart(
        state.urn[BallColor.red],
        state.urn[BallColor.blue],
        "Polya's Urn Trials",
    )
    print_results(config, guess)
