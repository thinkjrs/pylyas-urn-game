"""output.py 

This file contains functionality that print game items to the console.
"""

from rich.table import Table, Column
from rich import print
from rich.console import Console
from config import GameConfig
from guess import PlayerGuess


console = Console()


def print_welcome_message():
    print(
        "👋 Welcome to the [cornflower_blue]Polya's Urn Game[/cornflower_blue]. Guess the number of balls that will be in the urn at the end. The lowest score wins!"
    )
    print()


def get_ball_color(color: str) -> str:
    return f"[{color}]{color} balls[/{color}]"


def print_results(config: GameConfig, guess: PlayerGuess):
    ball_color = get_ball_color(config.first_draw)
    print(f"Your score: {guess.distance}")
    print(f"You guessed: {guess.guess} {ball_color}.")


def make_chart(num_red, num_blue, title):
    max_height = 8
    # Calculate the scaling factor to fit the bars within the max_height
    total = num_red + num_blue
    red_height = int((num_red / total) * max_height * 2)
    blue_height = int((num_blue / total) * max_height * 2)

    # Ensure at least one unit is shown for non-zero values
    red_height = max(red_height, 1) if num_red > 0 else 0
    blue_height = max(blue_height, 1) if num_blue > 0 else 0

    # Create the table
    table = Table(
        Column(f"{num_red} Red", justify="center"),
        Column(f"{num_blue} Blue", justify="center"),
        title=title,
    )
    # Create the bar chart using Panels
    for i in range(max_height, 0, -1):
        red_bar = "█" if i <= red_height else " "
        blue_bar = "█" if i <= blue_height else " "
        table.add_row(
            f"[red]{red_bar}[/red]",
            f"[blue]{blue_bar}[/blue]",
        )

    # Render the table
    console.print(table)
