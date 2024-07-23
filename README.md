# pylyas-urn-game

A Python text-based game to celebrate Polya's Urn.

## Playing the game

To play the game run the `play.py` script located in the `src` directory and follow the prompts.

```sh
$ python src/play.py
```

### Gameplay

```bash

❯ python src/play.py
👋 Welcome to the Polya's Urn Game. Guess the number of balls that will be in the urn
at the end. The lowest score wins!

The starting number of red balls: 10
The starting number of blue balls: 10
The number of trials to run: 100
The color to draw first [BallColor.red]: red
Enter the number of red balls in the urn at the end: 65
 Polya's Urn Trials
┏━━━━━━━━┳━━━━━━━━━┓
┃ 69 Red ┃ 51 Blue ┃
┡━━━━━━━━╇━━━━━━━━━┩
│   █    │         │
│   █    │         │
│   █    │    █    │
│   █    │    █    │
│   █    │    █    │
│   █    │    █    │
│   █    │    █    │
│   █    │    █    │
└────────┴─────────┘
Your score: 4
You guessed: 65 red balls.
```

### Docs

You can see documentation for the CLI using `python src/play.py --help`.

```bash
 Usage: play.py [OPTIONS] [INITIAL_RED] [INITIAL_BLUE] [NUMBER_OF_TRIALS]
                [FIRST_DRAW_CHOICE]:[red|blue] [USER_GUESS]

╭─ Arguments ───────────────────────────────────────────────────────────────────────╮
│   initial_red            [INITIAL_RED]               The number of red balls with │
│                                                      which to start.              │
│                                                      [default: None]              │
│   initial_blue           [INITIAL_BLUE]              The number of blue balls     │
│                                                      with which to start.         │
│                                                      [default: None]              │
│   number_of_trials       [NUMBER_OF_TRIALS]          The number of trials to      │
│                                                      simulate.                    │
│                                                      [default: None]              │
│   first_draw_choice      [FIRST_DRAW_CHOICE]:[red|b  The color of ball to draw    │
│                          lue]                        first; 🔴 or 🔵.             │
│                                                      [default: None]              │
│   user_guess             [USER_GUESS]                Your guess for the final     │
│                                                      number of balls you chose to │
│                                                      draw first after the final   │
│                                                      simulation.                  │
│                                                      [default: None]              │
╰───────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ─────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                       │
╰───────────────────────────────────────────────────────────────────────────────────╯
```

## Contributions

This is just a basic toy example. Feel free to submit a PR or issue!
