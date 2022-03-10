from dice import Dice
import random


class DiceHand:

    def __init__(self, difficulty: bool) -> None:
        self.dice = Dice()
        if difficulty:
            self.check_turn = 99999999
        else:
            self.check_turn = 2

    def keep_rolling(self, input: bool):
        """ Confirm the player if he wants to roll. """
        if input:
            return self.dice.roll()
        else:
            self.dice.roll_count = 0
            self.dice.turn = 0
        return None

    def check_hand(self, cheat: bool):
        if cheat:
            if self.check_turn > 0:
                self.check_turn -= 1
                return random.randint(1, 6)
            else:
                raise Exception("Cheat available for this turn")
        else:
            return None
