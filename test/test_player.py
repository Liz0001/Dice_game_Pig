#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pig Dice Game Unittesting."""

# import logging
import unittest
from game import player


class TestPlayerClass(unittest.TestCase):
    """Test the class."""

    def test_init_default_object(self) -> None:
        """
        Instantiate an object and check its properties.

        Check if the object has default name and value.
        """
        # Testing if the object is instance of player class
        res = player.Player()
        exp = player.Player
        self.assertIsInstance(res, exp)

        # Testing if the object has default name
        p = player.Player()
        res = p.name
        self.assertEqual(res, "Player")
        self.assertNotEqual(res, "Player1")

        # Testing if the player dafault score is 0
        res = p.score
        self.assertEqual(res, 0)
        self.assertNotEqual(res, 1)

    def test_change_name(self):
        """Testing if we can change the name."""
        p = player.Player()
        p.change_name("Winner")
        res = p.name

        self.assertEqual(res, "Winner")
        self.assertNotEqual(res, "Player")
        self.assertNotEqual(res, "Name")

    def test_add_score(self):
        """Test to see if we can add a score."""
        p = player.Player()
        p2 = player.Player()
        p3 = player.Player()

        # (Default) 0 + 5 = 5
        p.add_score(5)
        res = p.score
        self.assertEqual(res, 5)

        # 5 + 15 = 20... totalling
        p.add_score(15)
        res = p.score
        self.assertEqual(res, 20)

        p2.add_score(5)
        res = p2.score
        self.assertNotEqual(res, 15)

        p3.add_score(5)
        res = p3.score
        self.assertNotEqual(res, -5)

    def test_get_name(self):
        """Test to get name of the player."""
        p = player.Player()
        res = p.get_name()
        exp = p.name
        self.assertEqual(res, exp)

    def test_get_score(self):
        """Test to get the score of the player."""
        p = player.Player()
        res = p.get_score()
        exp = p.score
        self.assertEqual(res, exp)

    def test_get_player_data(self):
        """Testing if we are able to get name and score."""
        p = player.Player()
        res = p.get_player_data()
        exp = "{}: {} points".format(p.name, p.score)
        self.assertEqual(res, exp)

        # logging.warning(f'\nRESULT: { res }')


if __name__ == "__main__":
    unittest.main()
