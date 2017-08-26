from random import randint
from random import seed

def roll_dice(kept_dice=[]):
    """ function
Use to generate randonly roll, presented by digits.
    Arguements: a list of kept_dice, such as [1, 2]
                default argument if []
    Returns: a list of ordered roll, such as [1, 2, 3, 4, 5].
    Dependency: random.randint
    """
    roll = [randint(0, 5) for _ in range(5 - len(kept_dice))]
    roll.sort()
    return roll


# Test Codes
if __name__ == "__main__":
    kept_dice = [1, 2]
    seed()
    print(roll_dice())
