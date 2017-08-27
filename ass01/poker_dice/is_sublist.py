def is_sublist(sublist, motlist):
    """ print_roll
    Arguements: two list, sublist and motlist, such as [1, 2, 3, 4, 5]
    Returns: return true is sublist is the sublist(or the same list) of motlist
             return False if not
    """
    sublist_copy = sublist[:]
    motlist_copy = motlist[:]
    for e in sublist_copy:
        if e in motlist_copy:
            motlist_copy.remove(e)
        else:
            return False
    return True


# Test Codes
if __name__ == "__main__":
    sublist = [1, 2, 4, 5]
    print(sublist)
    motlist = [1, 2, 3, 5]
    print(motlist)
    print(is_sublist(sublist, motlist))
    print(sublist)
    print(motlist)
