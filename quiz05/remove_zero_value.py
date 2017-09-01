def remove_zero_value(dict_with_zero_value):
    """remove_zero_value
Remove keys from dictionary which value is zero in order to fit output format.
    """
    dict_without_zero_value = dict(dict_with_zero_value)
    for key in dict_with_zero_value:
        if dict_without_zero_value[key] == 0:
            del dict_without_zero_value[key]
    return dict_without_zero_value


if __name__ == "__main__":
    dict_with_zero_value = {1: 0, 2: 1, 3: 5, 4: 2}
    print(remove_zero_value(dict_with_zero_value))
