#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Let's play a game of 'Pig'."""

import player
import intelligence
import dicehand
import score


class Game:
    """Game class is where the magic happens."""
    running_score = 0
    th_game = 1

    def __init__(self, cheat=0):
        """Init the objects."""
        self.player = player.Player()
        self.intelli = intelligence.Intelligence()
        self.dicehand = dicehand.DiceHand()

    def start(self):
        """(Re)Starts the game (all scores to zero)."""
        # Name of the function call
        if (self.player.get_score() > 0 or self.intelli.sum_scores > 0):
            self.player.score = 0
            self.intelli.sum_scores = 0
            self.th_game += 1
            # save the current score also

        self.running_score = 0
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

    def add_running_score(self, run_score):
        """Add to running score till player hits 1."""
        if run_score == 1:
            self.running_score = 0
            print(f"Your turn is over. {self.intelli.computer_name} will be playing now")
            self.intelli.roll_dice_bot()
        else:
            self.running_score += run_score

    def hold_score(self):
        """Add running score to total. Opponent's time"""
        self.player.add_score(self.running_score)
        self.running_score = 0
        # hand over the turn to computer

    def get_player_score(self):
        """Get the score."""
        return self.player.get_score()

    def get_intelligence_score(self):
        """Get the score."""
        return self.intelli.sum_scores

    def current_game_is(self):
        """What number is this game now?."""
        return self.th_game
