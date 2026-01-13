import random
class die:
    """
    Docstring for die
    """
    def __init__(self, sides=6):
        """
        Docstring for __init__
        
        :param self: Description
        :param sides: Description
        """
        self.sides = sides

    def roll_die(self):
        """
        Docstring for roll_die
        
        :param self: Description
        """
        return random.randint(1, self.sides)
sides = [6, 10, 20]
for side in sides:
    my_die = die(side)
    print(f"rolling a {side}-sided die 10 times:")
    for roll in range(10):
        print(my_die.roll_die())
    print("\n")
