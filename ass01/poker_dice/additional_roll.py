from roll_dice import roll_dice
from print_roll import print_roll
from roll_input import roll_input

def additional_roll(roll):
    """ additional_roll
Start additional rolls, there will be none to twice.
    Arguements: a list of roll, such as [1, 2, 3, 4, 5]
    Returns: print additonal rolls if possible
    """
    # now is the secend roll
    kept_roll = roll_input(roll, 2)    
    if kept_roll:   # if kept_roll is not []
        roll = roll_dice(kept_roll)
        print_roll(roll)
        # now is the third roll
        kept_roll = roll_input(roll, 3)
        if kept_roll:   # if kept_roll is not []
            roll = roll_dice(kept_roll)
            print_roll(roll)
    return


# Test Codes
if __name__ == "__main__":
    roll = [1, 2, 3, 4, 5]
    additional_roll(roll)

