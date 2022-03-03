#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Using the cmd module to create a shell for the main program.

You can read about the cmd module in the docs:
    cmd — support for line-oriented command interpreters
    https://docs.python.org/3/library/cmd.html
"""

import cmd
import game


class Shell(cmd.Cmd):
    """Shell class with command actions to play a dice game."""

    intro = "Welcome to the game. Type 'help' to list commands."
    prompt = "\n(Pig) "
    rules = """
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

    die = ("\t+---+\n"
           "\t| {} |\n"
           "\t+---+")

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.game = game.Game()

    def do_start(self, _):
        """Start a new game."""
        msg = (
            "Here we go, let\'s start rolling."
        )
        self.game.start()
        print(msg.format(self.game.start()))

    def do_rules(self, _):
        """Rules of the game."""
        print(self.rules)

    def do_roll(self, _):
        """Roll the dice."""
        print("You have rolled..")
        print(self.die.format(self.game.roll_dice()))

    def do_hold(self, _):
        """Hold the roll results, add to total score."""
        pass

    def do_score(self, _):
        """See the score bord."""
        pass

    def do_level(self, _):
        """Change the difficulty of the game."""
        pass

    def do_history(self, _):
        """See the game history."""
        pass

    def do_name(self, _):
        """Player can change their name here."""
        pass

    def do_cheat(self, _):
        """Have a sneak peek at the next roll."""
        print("Cheater... the next roll is...")
        print(self.die.format(self.game.cheat()))

    # End of the game functionality: exit, quit, q, and EOF
    def do_exit(self, _):
        # pylint: disable=no-self-use
        """Leave the game."""
        print("Bye bye")
        return True

    def do_quit(self, arg):
        """Leave the game."""
        return self.do_exit(arg)

    def do_q(self, arg):
        """Leave the game."""
        return self.do_exit(arg)

    def do_EOF(self, arg):
        # pylint: disable=invalid-name
        """Leave the game."""
        return self.do_exit(arg)
