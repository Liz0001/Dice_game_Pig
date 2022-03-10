#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Let's play a game of 'Pig'."""

import player
import intelligence
import dicehand
import score


class Game:
    """Game class is where the magic happens."""

    def __init__(self, cheat=0):
        """Init the objects."""
        self.player = player.Player()
        self.intelli = intelligence.Intelligence()
        self.dicehand = dicehand.DiceHand(cheat)

    def start(self):
        """(Re)Starts the game (all scores to zero)."""
        # Name of the function call
        if ((self.player.get_score() and self.intelli.get_score()) != 0):
            self.player.score = 0
            self.intelli.score = 0
            # save the current score also

        # self.score = score.score()

    def cheat(self):
        """Get the number."""
        return self.dicehand.check_hand(True)

    def change_the_name(self, arg):
        """Name change for the player."""
        self.player.change_name(arg)

    def get_name(self):
        """Get the players name."""
        return self.player.get_name()

    def roll_dice(self):
        """Rolling the dice."""
        return self.dicehand.keep_rolling(True)

    def get_history(self):
        """Show players history."""
        pass




    def get_player_score(self):
        """Get the score."""
        return 8
    
    def get_intelligence_score(self):
        """Get the score."""
        return 7