#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Pig Dice Game Unittesting."""

import unittest
from game import intelligence


class TestIntelligenceClass(unittest.TestCase):
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = intelligence.Intelligence()
        exp = intelligence.Intelligence

        self.assertIsInstance(res, exp)
        self.assertEqual(res.computer_name, "Bot")
        self.assertEqual(res.sum_scores, 0)

    def test_get_number_of_turns(self):

       intell = intelligence.Intelligence()
       self.assertGreaterEqual(intell.get_number_of_turns(), 2)
       self.assertLessEqual(intell.get_number_of_turns(), 8)

    def test_roll_dice_bot(self):

        """ Testing the number of turns."""
        intell = intelligence.Intelligence()

        self.assertGreaterEqual(intell.roll_dice_bot(), 1)
        self.assertLessEqual(intell.roll_dice_bot(), 6)

    def test_when_to_hold(self):
        """ Testing that the turn would be up if the score is 20 or more"""
        intell = intelligence.Intelligence()
        intell.hold(turns=2, result=1, running_score=0)
        self.assertEqual(intell.sum_scores, 0)
        intell.hold(turns=2, result=2, running_score=0)
        self.assertEqual(intell.sum_scores, 4)


if __name__ == "__main__":
    unittest.main()
