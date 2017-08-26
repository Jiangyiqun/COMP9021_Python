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


# Test Codes
if __name__ == "__main__":
    roll = [1, 1, 1, 1, 1]
    print(hand_rank(roll))
    roll = [1, 1, 1, 1, 2]
    print(hand_rank(roll))
    roll = [1, 1, 1, 3, 3]
    print(hand_rank(roll))
    roll = [1, 1, 1, 2, 3]
    print(hand_rank(roll))
    roll = [1, 1, 2, 2, 3]
    print(hand_rank(roll))
    roll = [0, 2, 3, 4, 5]
    print(hand_rank(roll))
    roll = [1, 2, 3, 4, 5]
    print(hand_rank(roll))
