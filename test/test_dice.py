#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Pig Dice Game Unittesting."""

import unittest
from game import dice


class TestDiceClass(unittest.TestCase):
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = dice.Dice()
        exp = dice.Dice

        self.assertIsInstance(res, exp)
        self.assertEqual(res.roll_count, 0)
        self.assertEqual(res.turn, 0)

    def test_roll(self):
        res = dice.Dice()

        self.assertGreaterEqual(res.roll(), 1)
        self.assertEqual(res.roll_count, 1)
        self.assertLessEqual(res.roll(), 6)
        self.assertEqual(res.roll_count, 2)

    # def test_str(self):
    #     res = dice.Dice()
    #     roll = res.roll()
    #     expected = f"You have rolled {roll}.\n Your roll count is 1."
    #     self.assertEqual(str(res), expected)
    #     roll1 = res.roll()
    #     expected1 = f"You have rolled {roll1}.\n Your roll count is 2."
    #     self.assertEqual(str(res), expected1)


if __name__ == "__main__":
    unittest.main()
