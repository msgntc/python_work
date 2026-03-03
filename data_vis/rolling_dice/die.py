from random import randint

class Die:
    """a class for repersenting a single die"""

    def __init__(self, num_sides=6):
        """assume a six_sidded die"""
        self.num_sides = num_sides

    def roll(self):
        """return a random value between 1 and number of sides"""
        return randint(1, self.num_sides)