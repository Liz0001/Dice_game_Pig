#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Let's play a game called "PIG".

+-----------------------------------------------------------+
|  There are 2 players: You and the opponent.               |
|                                                           |
|  Players take turns to roll a dice as many times as       |
|  they wish, adding all roll results to a running total,   |
|  but if the player rolls a 1 the gained score for the     |
|  turn will be lost.                                       |
|                                                           |
|  Who gets to 100 points first wins the game.              |
+-----------------------------------------------------------+
"""

import shell


def main():
    """Execute the main program."""
    print(__doc__)
    shell.Shell().cmdloop()


if __name__ == "__main__":
    main()
