"""play.py
# Polya's Urn Game.

To play the game run the `play.py` script and follow the prompts.

```sh
$ python play.py
```

You can see documentation for the CLI using `python play.py --help`.
"""

from run import app
from output import print_welcome_message

if __name__ == "__main__":
    print_welcome_message()
    app()
