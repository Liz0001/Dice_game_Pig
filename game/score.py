#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from player import Player


class Score:
    """Score class."""

    games = []
    game_number = 0;

    def keep_score(self, player: Player, score):
        """..."""
        self.games[self.game_number] = [player, score]
        self.game_number = self.game_number + 1

    def compare_score(self, game1, game2):
        """..."""
        score1 = self.games[game1][1]
        score2 = self.games[game2][1]
        if(score2 > score1):
            return(self.games[game2][0].get_name())
        else:
            return(self.games[game1][0].get_name())


    def show_score(self, game):
        """..."""
        return self.games[game][1]
