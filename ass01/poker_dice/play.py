from random import seed
from roll_dice import roll_dice
from print_roll import print_roll
from hand_rank import hand_rank
from roll_input import roll_input

def  play():
    """ paly
Start to play poker_dice
    Arguements: None
    Returns:
    """
    kept_roll = []
    # First roll
    roll = roll_dice()
    print_roll(roll)
    print(f'It is a {hand_rank(roll)}')
    # Secend roll
    kept_roll = roll_input(roll, 'second')
    if kept_roll != roll:
        roll = roll_dice(kept_roll)
        print_roll(roll)
        print(f'It is a {hand_rank(roll)}')
        # Thrid roll
        kept_roll = roll_input(roll, 'third')
        if kept_roll != roll:
            roll = roll_dice(kept_roll)
            print_roll(roll)
            print(f'It is a {hand_rank(roll)}')
    return


# Test Codes
if __name__ == "__main__":
    seed(0)
    while True:
        print('New trun')
        play()