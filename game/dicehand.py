from dice import Dice
import random


class DiceHand:
    
    cheat_number = 0

    def __init__(self) -> None:
        self.dice = Dice()
        self.difficulty = "easy"
        self.check_turn = 9999999
    
    def set_difficulty(self, difficulty: str):
        self.difficulty = difficulty
        if 'easy' in difficulty:
            self.check_turn = 9999999
        else:
            self.check_turn = 2

    def keep_rolling(self, input: bool):
        """ Confirm from the player if he wants to roll. """
        if self.cheat_number > 0:
            self.temp = self.cheat_number
            self.cheat_number = 0
            return self.temp
        elif input:
            return self.dice.roll()
        else:
            self.dice.roll_count = 0
            self.dice.turn = 0
        return None

    def check_hand(self, cheat: bool):
        """Cheat or not."""
        if self.cheat_number == 0:
            self.cheat_number = self.keep_rolling(True)
        return self.cheat_number
