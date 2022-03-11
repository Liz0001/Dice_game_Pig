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

    die = "\t+---+\n" "\t| {} |\n" "\t+---+"

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.game = game.Game()
        self.turn = 0

    def do_start(self, _):
        """Start a new game."""
        msg = "\nHere we go, let's start rolling." "\nA new game has started!"
        print(msg.format(self.game.start()))

    def do_rules(self, _):
        """Rules of the game."""
        print(self.rules)

    def do_roll(self, _):
        """Roll the dice."""
        print("You have rolled..")
        a_roll = self.game.roll_dice()
        print(self.die.format(a_roll))
        turn_continue = self.game.add_running_score(a_roll)
        if not turn_continue:
            print(
                f"Your turn is over.  {self.game.intelli.computer_name}"
                + " will be playing now"
            )
            self.game.intelli.hold()

    def do_hold(self, _):
        """Hold the roll results, add to total score."""
        print("Saving score, opponents turn.")
        self.game.hold_score()

        if self.game.who_is_the_winner():
            print("\n***************************")
            print("WE HAVE A   W I N N E R !!!")
            print("Current score, Game " + str(self.game.current_game_is()) + "\n")
            if self.game.get_player_score() >= 100:
                print(
                    "\t"
                    + self.game.get_name()
                    + " is the winner with score: "
                    + str(self.game.get_player_score())
                )
            else:
                print(
                    "\nBot won with score: " + str(self.game.get_intelligence_score())
                )
            print("\n\n\tCongrats!\n\n")
            self.do_start(True)

    def do_score(self, _):
        """See the score board."""
        print("Current score, Game " + str(self.game.current_game_is()) + "\n")
        print("\t" + self.game.get_name() + ": " + str(self.game.get_player_score()))
        print(
            "\t"
            + self.game.intelli.computer_name
            + ": "
            + str(self.game.get_intelligence_score())
        )

    def do_level(self, difficulty):
        """Change the difficulty of the game:'easy' and 'hard'."""
        if difficulty in ["easy", "hard"]:
            self.game.dicehand.set_difficulty(difficulty)
            print(f"Difficulty set to {difficulty}")
        else:
            print("Invalid difficulty. Only 'easy' and 'hard' allowed")

    def do_name(self, new_name):
        """Player can change their name here. name [new name]."""
        if new_name:
            self.game.change_the_name(new_name)
            print("Your new name: ", self.game.get_name())
        else:
            print("Hi " + self.game.get_name())
        self.prompt = f"\n({self.game.get_name()}) "

    def do_cheat(self, _):
        """Have a sneak peek at the next roll."""
        try:
            print("Cheater... the next roll is...")
            print(self.die.format(self.game.cheat()))
        except Exception:
            print("Cheats used for this turn")

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
