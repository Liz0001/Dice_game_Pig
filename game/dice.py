#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Let's play a game of 'Pig'."""
import random


class Dice:
    """Dice."""

    def __init__(self) -> None:
        """Initialize the values."""
        self.roll_count = 0
        self.turn = 0

    def roll(self) -> int:
        """Generate a value randomly. Increase a roll count."""
        self.turn = random.randint(1, 6)
        self.roll_count += 1
        return self.turn

    def __str__(self) -> str:
        """Print out the score and the roll count."""
        return f"You have rolled {self.turn}.\n Your roll count is {self.roll_count}."
