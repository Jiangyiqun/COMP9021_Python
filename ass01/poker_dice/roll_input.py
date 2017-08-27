from is_sublist import is_sublist


def roll_input(roll, round):
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
            user_input = input(f'Which dice do you want to keep for the {round} roll? ')
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


# Test Codes
if __name__ == "__main__":
    roll = [5, 5, 5, 5, 5]
    print(roll_input(roll, 'second'))
