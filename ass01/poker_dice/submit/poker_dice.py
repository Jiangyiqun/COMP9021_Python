""" poker_dice
This code is written for COMP9021 Assignment 1 Question 4
    Author: Jack Jiang (z5129432)
    Version: v01
    Date: 26/08/2017
"""
from random import randint
from random import seed


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
    print('Five of a kind : {0:.2%}'.format(hand_possibility['Five of a kind']/times))
    print('Four of a kind : {0:.2%}'.format(hand_possibility['Four of a kind']/times))
    print('Full house     : {0:.2%}'.format(hand_possibility['Full house']/times))
    print('Straight       : {0:.2%}'.format(hand_possibility['Straight']/times))
    print('Three of a kind: {0:.2%}'.format(hand_possibility['Three of a kind']/times))
    print('Two pair       : {0:.2%}'.format(hand_possibility['Two pair']/times))
    print('One pair       : {0:.2%}'.format(hand_possibility['One pair']/times))
    # print('Bust            : {0:.2%}'.format(hand_possibility['Bust']/times))
    return


def roll_dice(kept_dice=[]):
    """ function
Use to generate randonly roll, presented by digits.
    Arguements: a list of kept_dice, such as [1, 2]
                default argument if []
    Returns: a list of ordered roll, such as [1, 2, 3, 4, 5].
    Dependency: random.randint
    """
    roll = [randint(0, 5) for _ in range(5 - len(kept_dice))]
    roll.extend(kept_dice)
    roll.sort()
    return roll


def print_roll(roll):
    """ print_roll
    Arguements: a list of roll, such as [1, 2, 3, 4, 5]
    Returns: print roll, such as "The roll is: Ace Queen Jack Jack 10"
    """
    poker_roll_book = {
        0: 'Ace',
        1: 'King',
        2: 'Queen',
        3: 'Jack',
        4: '10',
        5: '9'
        }
    poker_roll = ' '.join(poker_roll_book[key] for key in roll)
    print(f'The roll is: {poker_roll}')
    return


def hand_rank(roll):
    """ hand_rank
    Arguements: a list of roll, such as [1, 2, 3, 4, 5]
    Returns: a string, such as 'Straight'
    """
    number_of_a_kind = [roll.count(_) for _ in range(6)]
    number_of_a_kind.sort()
    if number_of_a_kind == [0, 0, 0, 0, 0, 5]:
        roll_hand = 'Five of a kind'
    elif number_of_a_kind == [0, 0, 0, 0, 1, 4]:
        roll_hand = 'Four of a kind'
    elif number_of_a_kind == [0, 0, 0, 0, 2, 3]:
        roll_hand = 'Full house'
    elif number_of_a_kind == [0, 0, 0, 1, 1, 3]:
        roll_hand = 'Three of a kind'
    elif number_of_a_kind == [0, 0, 0, 1, 2, 2]:
        roll_hand = 'Two pair'
    elif number_of_a_kind == [0, 0, 1, 1, 1, 2]:
        roll_hand = 'One pair'
    elif number_of_a_kind == [0, 1, 1, 1, 1, 1]:
        if (roll == [0, 2, 3, 4, 5] or
            roll == [0, 1, 3, 4, 5] or
            roll == [0, 1, 2, 4, 5] or
            roll == [0, 1, 2, 3, 5]):
            # According to https://en.wikipedia.org/wiki/Poker_dice,
            # there are only four possible Bust hands
            roll_hand = 'Bust'
        else:
            roll_hand = 'Straight'
    return roll_hand


def roll_input(roll, rounds):
    """ roll_input
    Arguements: a list of roll, such as [1, 2, 3, 4, 5]
                integer round, only allowed 'second' or 'third'
    Returns: a list of kept_dice, such as [1, 2]. if nothing left, return []
    """
    poker_roll_book = {
        'Ace': 0,
        'King': 1,
        'Queen': 2,
        'Jack': 3,
        '10': 4,
        '9': 5
        }
    kept_roll = roll
    is_all = False
    while True:
        try:
            user_input = input(f'Which dice do you want to keep for the {rounds} roll? ')
            user_input = user_input.split()
            # Check if user input is 'all' or 'All'
            if user_input == ['all'] or user_input == ['All']:
                is_all = True
                raise ValueError
            # Check user input is valid, namely they are pokers.
            for string in user_input:
                if string not in poker_roll_book:
                    raise ValueError
            # Convert input string to a list of integer
            kept_roll = [poker_roll_book[key] for key in user_input]
            kept_roll.sort()
            # Check if user input is equivalent to 'all' or 'All'
            if kept_roll == roll:
                is_all = True
                raise ValueError
            # Check if user input is a sublist of roll
            if not is_sublist(kept_roll, roll):
                raise ValueError
            break
        except ValueError:
            if is_all:
                kept_roll = roll
                print('Ok, done.')
                break
            else:
                print('That is not possible, try again!')
                # and then loop to input again
    return kept_roll


def is_sublist(sublist, motlist):
    """ print_roll
    Arguements: two list, sublist and motlist, such as [1, 2, 3, 4, 5]
    Returns: return true is sublist is the sublist(or the same list) of motlist
             return False if not
    """
    sublist_copy = sublist[:]
    motlist_copy = motlist[:]
    for element in sublist_copy:
        if element in motlist_copy:
            motlist_copy.remove(element)
        else:
            return False
    return True


# Test Codes
if __name__ == "__main__":
    seed(0)
    while True:
        print("\n Let's Start a New Game!")
        play()
