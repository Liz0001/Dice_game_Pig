# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-

# """Pig Dice Game Unittesting."""

# import unittest
# from game import score
# from game import player


# class TestScoreClass(unittest.TestCase):
#     """Test the class."""

#     def test_init_default_object(self) -> None:
#         res = score
#         exp = score()
#         self.assertIsInstance(res, exp)

#     def test_keep_score(self):
#         """Test to get name of the player."""  
#         s = score
#         s.keep_score(player.Player(), 2)
#         res = s.games
#         exp = [player.Player(), 2]
#         self.assertEqual(res, exp)

#     def test_compare_score(self):
#         """Test to get the score of the player."""
#         p1 = player.Player()
#         p1.change_name("P1")
#         p2 = player.Player()
#         p2.change_name("P2")

#         s = score
#         score.keep_score(p1, 3)
#         score.keep_score(p2, 4)
#         res = s.compare_score(0, 1)
#         exp = "P2"
#         self.assertEqual(res, exp)

#     def test_show_score(self):
#         """Testing if we are able to get name and score."""
#         p = player.Player()
#         s = score
#         res = s.show_score(0)
#         exp = 3
#         self.assertEqual(res, exp)

# if __name__ == "__main__":
#     unittest.main()
