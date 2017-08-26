from random import seed
from hand_rank import hand_rank
from roll_dice import roll_dice


def simulate(times):
    """ simulate
Simulate the possibility of the various hands.
    Arguements: integer (times of simulation)
    Returns: print something like that (We ignore the possibility of Bust):
        Five of a kind : 0.08%
        Four of a kind : 1.99%
        Full house : 3.93%
        Straight : 3.33%
        Three of a kind: 14.88%
        Two pair : 23.02%
        One pair : 46.58%
    """
    hand_rank_book = [
        'Five of a kind',
        'Four of a kind',
        'Full house',
        'Straight',
        'Three of a kind',
        'Two pair',
        'One pair',
        'Bust'
        ]
    hand_possibility = {}
    for key in hand_rank_book:
        hand_possibility[key] = 0
    for _ in range(times):
        hand_possibility[hand_rank(roll_dice())] += 1    # count times of a hand
    print('Five of a kind  : {0:.2%}'.format(hand_possibility['Five of a kind']/times))
    print('Four of a kind  : {0:.2%}'.format(hand_possibility['Four of a kind']/times))
    print('Full house      : {0:.2%}'.format(hand_possibility['Full house']/times))
    print('Straight        : {0:.2%}'.format(hand_possibility['Straight']/times))
    print('Three of a kind : {0:.2%}'.format(hand_possibility['Three of a kind']/times))
    print('Two pair        : {0:.2%}'.format(hand_possibility['Two pair']/times))
    print('One pair        : {0:.2%}'.format(hand_possibility['One pair']/times))
    # print('Bust            : {0:.2%}'.format(hand_possibility['Bust']/times))
    return


# Test Codes
if __name__ == "__main__":
    seed(0)
    # simulate(10)
    # simulate(100)
    # simulate(1000)
    # simulate(10000)
    simulate(100000)
