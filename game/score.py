#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from player import Player


class Score:
    """Score class."""

    _score = 0

    def __init__(self, player: Player):
        """ ..."""
        self._score = player.get_score()

    def keep_score(self, player_score):
        """..."""
        self._score = player_score

    def compare_score(self, player: Player):
        """..."""
        if(self._score > player.get_score()):
            print(player.get_name() + ' scored higher')
        else:
            print(player.get_name() + ' scored lower')

    def show_score(self):
        """..."""
        return self._score
