import random

""" Creating the intellegence for the computer a s to how it would be playing and making decisions """


class Intelligence:
    """Opponent."""

    def __init__(self) -> None:
        """
            Initializing the variables. It would not be returning anything
            hence the return type is specified as none
        """
        random.seed(42)
        self.CURRENT_SCORE_HOLD = 20
        self.sum_scores = 0

    def get_number_of_turns(self) -> int:
        """
            Randomly generating a number which would
            signify the times the computer would roll
        """
        return random.randint(1, 10)

    """  """
    def when_to_hold(self, current_dice_value: int) -> bool:
        self.sum_scores += current_dice_value
        if self.sum_scores >= self.CURRENT_SCORE_HOLD:
            return False
        return True