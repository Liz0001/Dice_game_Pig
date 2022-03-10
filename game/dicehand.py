from dice import Dice
import random


class DiceHand:

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
        """ 
            Confirm from the player if he wants to roll.
        """
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
                raise Exception("Cheat not available for this turn")
        else:
            return None
