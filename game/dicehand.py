#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Let's play a game of 'Pig'."""
from dice import Dice
import random


class DiceHand:
    """Dicehand class."""

    cheat_number = 0

    def __init__(self) -> None:
        """Initiatiate the dicehand."""
        self.dice = Dice()
        self.difficulty = "easy"
        self.check_turn = 9999999

    def set_difficulty(self, difficulty: str):
        """Set the difficulty of the game.

        On easy the player can have many cheats in his turn.
        In difficult the player is only allowed to cheat twice.
        """
        self.difficulty = difficulty
        if 'easy' in difficulty:
            self.check_turn = 9999999
        else:
            self.check_turn = 2

    def keep_rolling(self, input: bool):
        """Confirm from the player if he wants to roll."""
        if self.cheat_number > 0:
            self.temp = self.cheat_number
            self.cheat_number = 0
            return self.temp
        elif input:
            return self.dice.roll()
        else:
            self.dice.roll_count = 0
            self.dice.turn = 0
        return None

    def check_hand(self, cheat: bool):
        """Cheat or not."""
        if cheat:
            if self.check_turn > 0:
                self.check_turn -= 1
                self.cheat_number = self.keep_rolling(True)
                return self.cheat_number
            else:
                raise Exception("Cheat not available for this turn")
        else:
            return None
