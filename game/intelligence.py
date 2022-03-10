import random

"""
    Creating the intellegence for the computer as to
    how it would be playing and making decisions.
    """



class Intelligence:
    """Opponent."""

    def __init__(self) -> None:
        """
            Initializing the variables. It would not be returning anything
            hence the return type is specified as none.
        """
        random.seed(42)
        self.CURRENT_SCORE_HOLD = 20
        self.sum_scores = 0

    def get_number_of_turns(self) -> int:
        """
            Randomly generating a number which would
            signify the times the computer would roll.
        """
        return random.randint(1, 10)

    def roll(self) -> int:
        """
            The computer will roll its turn.
        """
        return self.dice.roll()

    def when_to_hold(self, current_dice_value: int) -> bool:
        """
            The computer will hold when it is either out of turn
            or when it has a sum of 20 in the current turn.
            """
        self.sum_scores += current_dice_value
        if self.sum_scores >= self.CURRENT_SCORE_HOLD:
            return False
        return True
