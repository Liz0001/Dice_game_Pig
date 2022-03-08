
import random


class Dice:
    
    def __init__(self) -> None:
        """ Initializing the values """
        self.roll_count = 0
        self.turn = 0
        
    def roll(self) -> int:
        """ Generating a value randomly. Increasing a roll count """
        
        self.turn = random.randint(1,6)
        self.roll_count += 1
        return self.turn
        
    def __str__(self) -> str:
        """ Priniting out the score and the roll count"""
        return f"You have rolled {self.turn}.\n Your roll count is {self.roll_count}." 


