#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Pig Dice Game Unittesting."""

import unittest
from game import dicehand


class TestDicehandClass(unittest.TestCase):
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = dicehand.DiceHand()
        exp = dicehand.DiceHand
        self.assertIsInstance(res, exp)

        self.assertEqual(res.difficulty, "easy")
        self.assertEqual(res.check_turn, 9999999)

    def test_set_difficulty(self):
        res = dicehand.DiceHand()
        res.set_difficulty("hard")
        self.assertEqual(res.difficulty, "hard")
        self.assertEqual(res.check_turn, 2)
        res.set_difficulty("easy")
        self.assertEqual(res.difficulty, "easy")
        self.assertEqual(res.check_turn, 9999999)

    def test_keep_rolling(self):
        res = dicehand.DiceHand()
        res.cheat_number = 2
        self.assertEqual(res.keep_rolling(True), 2)
        res.cheat_number = 0
        self.assertGreaterEqual(res.keep_rolling(True), 1)
        self.assertLessEqual(res.keep_rolling(True), 6)
        self.assertEqual(res.keep_rolling(False), None)
        self.assertEqual(res.dice.roll_count, 0)
        self.assertEqual(res.dice.turn, 0)

    def test_check_hand(self):
        res = dicehand.DiceHand()

        self.assertGreater(res.check_turn, 0)
        res.check_turn = 2
        result = res.check_hand(True)
        self.assertEqual(res.check_turn, 1)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 6)
        res.check_turn = 0
        self.assertRaises(Exception, lambda: res.check_hand(True))


if __name__ == "__main__":
    unittest.main()
