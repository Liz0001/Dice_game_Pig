#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Let's play a game of 'Pig'."""
import random
from dice import Dice


class Intelligence:
    """
    Creating the intelligence for the computer as to
    how it would be playing and making decisions.
    Print out the turn for the bot.
    """

    die = "\t+---+\n" "\t| {} |\n" "\t+---+"

    def __init__(self) -> None:
        """Initialise the variables.

        It would not be returning anything
        hence the return type is specified as none.
        """
        # random.seed(42)
        self.computer_name = "Bot"
        self.sum_scores = 0
        self.dice = Dice()

    def get_number_of_turns(self) -> int:
        """Randomly generating a number
        which would signify the times the computer would
        roll.
        """
        return random.randint(2, 8)

    def roll_dice_bot(self):
        """Roll the dice."""
        return self.dice.roll()

    def hold(self, turns=None, result=None, running_score=0) -> bool:
        """Hold turn.

        The computer will hold when the randomly generated number
        of turns are complete. The running score will be added to the
        final score.if the turn comes as 1, the turn is over and the
        running score will go to zero.
        """
        counter = 0
        if not turns:
            turns = self.get_number_of_turns()
        running_score = 0
        temp = 0
        while counter < turns:
            if not result or result == temp:
                result = self.roll_dice_bot()
            print(self.die.format(result))
            if result == 1:
                running_score = 0
                break
            else:
                running_score += result
            temp = result
            counter += 1
        self.sum_scores += running_score
