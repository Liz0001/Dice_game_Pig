#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Let's play a game of 'Pig'."""

import player
import intelligence
import dicehand
import score


class Game:
    """Game class is where the magic happens."""

    def __init__(self):
        """Init the object."""
        self.p = player.Player()
        # init the intelligence
        # init the dicehand (dice init in dicehand)
        # init score

    # def start(self):
    #     """(Re)Starts the game (all scores to zero)."""
    #     self.p.score = 0
    #     # intelligence score to zero also
    #     # init the score (one round history)
        

    # def cheat(self):
    #     """Get the number."""
    #     return 3

    # def change_the_name(self, arg):
    #     """Name change for the player."""

    # def roll_dice(self):
    #     """Rolling the dice."""
    #     return 6

