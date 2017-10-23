def input_players():
    """ input_players
input a list of valid players
    Arguements: None
    Returns: a list of all_players
    """
    while True:
        try:
            all_players = input('请输入玩家姓名，以空格键区分: ').split()
            if not all_players:
                print('你至少需要一位玩家!')
                raise ValueError
            if len(all_players) != len(set(all_players)):
                print('玩家姓名不能重复!')
                raise ValueError
            break
        except ValueError:
            print('请重新输入...')
    return all_players


# Test Codes
if __name__ == "__main__":
    print(input_players())

