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


# Test Codes
if __name__ == "__main__":
    roll = [1, 2, 3, 4, 5]
    print_roll(roll)
