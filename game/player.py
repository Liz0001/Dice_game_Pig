#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Let's create our player."""


class Player:
    """All about the Player."""

    def __init__(self):
        """Player initiated with default name value."""
        self.name = "Player"
        self.score = 99

    def change_name(self, new_name):
        """Player can change their name."""
        self.name = new_name

    def add_score(self, player_score):
        """Add the score to the player."""
        self.score += player_score

    def get_name(self):
        """Name of the player."""
        return self.name

    def get_score(self):
        """Score of the player."""
        return self.score

    def get_player_data(self):
        """Returns player name and current score."""
        return "{}: {} points".format(self.name, self.score)
