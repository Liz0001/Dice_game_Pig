import random
from dice import Dice

"""
    Creating the intellegence for the computer as to
    how it would be playing and making decisions.
"""



class Intelligence:
    """
        Printing out the turn for the bot.
    """
    die = ("\t+---+\n"
           "\t| {} |\n"
           "\t+---+")

    def __init__(self) -> None:
        """
            Initializing the variables. It would not be returning anything
            hence the return type is specified as none.
        """
        self.computer_name = "Bot"
        self.CURRENT_SCORE_HOLD = 20
        self.sum_scores = 0
        self.dice = Dice()

    def get_number_of_turns(self) -> int:
        """
            Randomly generating a number which would
            signify the times the computer would roll.
        """
        return random.randint(1, 6)

    def roll_dice_bot(self):
        """Rolling the dice."""
        return self.dice.roll()

    def hold(self) -> bool:
        """
            The computer will hold when the randomly generated number
            of turns are complete. The running score will be added to the
            final score.if the turn comes as 1, the turn is over and the
            running score will go to zero.
        """
        counter = 0
        turns = self.get_number_of_turns()
        running_score = 0
        while(counter <= turns):
            result = self.roll_dice_bot()
            print(self.die.format(result))
            if result == 1:
                running_score = 0
                break
            else:
                running_score += result
            counter += 1
        self.sum_scores += running_score
