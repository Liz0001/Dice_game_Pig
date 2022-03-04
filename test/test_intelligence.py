#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Pig Dice Game Unittesting."""

import unittest
from game import intelligence
import random 


class TestIntelligenceClass(unittest.TestCase):
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = intelligence.Intelligence()
        exp = intelligence.Intelligence
        self.assertIsInstance(res, exp)
        self.assertEqual(res.CURRENT_SCORE_HOLD, 20)
        self.assertNotEqual(res.CURRENT_SCORE_HOLD, 30)
    
    def test_get_numer_off_turns(self):
        """ Testing the number of turns."""
        intell = intelligence.Intelligence()
        random.seed(42) # when randomly generating but the pattern would be the same. Can be any integer value
        self.assertEqual(random.randint(1, 10), 2)
        self.assertEqual(random.randint(1, 10), 1)# written twice to ensure that the result is same
        self.assertEqual(random.randint(1, 10), 5)
        self.assertEqual(random.randint(1, 10), 4)
        self.assertNotEqual(random.randint(1, 10), 2)
        

    def test_when_to_hold(self):
        """ Testing that the turn would be up if the score is 20 or more"""
        intell = intelligence.Intelligence()
        self.assertEqual(intell.when_to_hold(25), False)
        self.assertEqual(intell.when_to_hold(20), False)
        self.assertEqual(intell.when_to_hold(19), True)
        self.assertNotEqual(intell.when_to_hold(36), True)
        self.assertNotEqual(intell.when_to_hold(20), True)
        self.assertNotEqual(intell.when_to_hold(18), False)




if __name__ == "__main__":
    unittest.main()
