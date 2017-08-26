from random import seed
from roll_dice import roll_dice
from print_roll import print_roll
from hand_rank import hand_rank
from additional_roll import additional_roll

def  play():
    """ paly
Start to play poker_dice
    Arguements: None
    Returns:
    """
    roll = roll_dice()
    print_roll(roll)
    print(f'It is a {hand_rank(roll)}')
    additional_roll(roll)
    return


# Test Codes
if __name__ == "__main__":
    seed(0)
    play()
