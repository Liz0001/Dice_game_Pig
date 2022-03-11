#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pig Dice Game Unittesting."""

# import logging
import unittest

from game.game import Game

# from game.player import Player
# from game.intelligence import Intelligence
# from game.game import dicehand


class TestGameClass(unittest.TestCase):
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = Game()
        exp = Game
        self.assertIsInstance(res, exp)

    def test_start(self):
        """Test if game starts, restarts."""
        a_game = Game()
        a_game.start()
        res = a_game.running_score == 0
        self.assertTrue(res)

        a_game.player.score = 10
        a_game.start()
        res = a_game.player.score == 0
        self.assertTrue(res)

    def test_cheat(self):
        """Test to get the number."""
        a_game = Game()
        a_game.cheat()
        res = a_game.cheat()
        exp = a_game.roll_dice()
        self.assertEqual(res, exp)

    def test_change_name(self):
        """Test to chanhe the name on the player."""
        a_game = Game()
        a_game.change_the_name("winner")
        res = a_game.player.get_name()
        exp = a_game.player.name
        self.assertEqual(res, exp)

    def test_get_name(self):
        """Test to get name."""
        a_game = Game()
        res = a_game.get_name()
        exp = a_game.player.name
        self.assertEqual(res, exp)

    def test_get_history(self):
        """Test if we can get history."""
        pass

    def test_add_running_score(self):
        """Running score."""
        a_game = Game()
        a_game.add_running_score(1)
        res = a_game.running_score == 0
        self.assertTrue(res)

        a_game.add_running_score(3)
        res = a_game.running_score == 3
        self.assertTrue(res)
        # logging.warning(f'\nRESULT: { res }')

    def test_hold_score(self):
        """Hold score."""
        a_game = Game()
        a_game.running_score = 10
        a_game.hold_score()
        res = a_game.player.score == 10
        self.assertTrue(res)

    def test_get_player_score(self):
        """Get the Score."""
        a_game = Game()
        res = a_game.get_player_score()
        exp = a_game.player.score
        self.assertEqual(res, exp)

    def test_get_intelligence_score(self):
        """Get score."""
        a_game = Game()
        res = a_game.get_intelligence_score() == a_game.intelli.sum_scores
        self.assertTrue(res)
        # logging.warning(f'\nRESULT: { res }')

    def test_current_game_is(self):
        """Find out what number of game is it."""
        a_game = Game()
        a_game.th_game = 3
        res = a_game.current_game_is()
        exp = a_game.th_game
        self.assertEqual(res, exp)
        # logging.warning(f'\nRESULT: { res }')

    def test_who_is_the_winner(self):
        """Check if there is a winner."""
        a_game = Game()
        a_game.who_is_the_winner()
        res = a_game.player.get_score()
        exp = False
        self.assertEqual(res, exp)

        a_game.who_is_the_winner()
        a_game.player.add_score(101)
        res = a_game.who_is_the_winner()
        self.assertTrue(res)
        # logging.warning(f'\nRESULT: { res }')


if __name__ == "__main__":
    unittest.main()
