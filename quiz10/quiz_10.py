# Randomly generates N distinct integers with N provided by the user,
# inserts all these elements into a priority queue, and outputs a list
# L consisting of all those N integers, determined in such a way that:
# - inserting the members of L from those of smallest index of those of
#   largest index results in the same priority queue;
# - L is preferred in the sense that the last element inserted is as large as
#   possible, and then the penultimate element inserted is as large as possible, etc.
#
#   [27, 12, 24]
#   [12, 24, 27]
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, sample

from priority_queue_adt import *

# Possibly define some functions
def delete_node(n):
    # find the index corresponse to number n
    for i in range(1, pq._length + 1):
        if pq._data[i] == n:
            break
    pq._data[i], pq._data[pq._length] = pq._data[pq._length], pq._data[i]
    pq._length -= 1
    # When the priority queue is one quarter full, we reduce its size to make it half full,
    # provided that it would not reduce its capacity to less than the minimum required.
    if pq.min_capacity // 2 <= pq._length <= len(pq._data) // 4:
        pq._resize(len(pq._data) // 2)
    pq._bubble_down(i)
    return n


def preferred_sequence():
    preferred_sequence = []
    while len(pq):
        check_list = sorted(pq._data[1 : len(pq) + 1], reverse=True)
        # check from the largest number
        for n in check_list:
            copy_data = pq._data[:]
            delete_node(n)
            pq.insert(n)
            # if the tree keeps the same after delete and insert a particular number n
            # then prepend this number on preferred_sequence, and then delete n from pq
            if pq._data[1 : len(pq) + 1] == copy_data[1 : len(pq) + 1]:
                preferred_sequence.insert(0, n)
                delete_node(n)
                break
            # if the number is not suitable for preferred_sequence, restore pq and examine next number
            else:
                pq._data = copy_data[:]
    return preferred_sequence
    # Replace pass above with your code (altogether, aim for around 24 lines of code)


try:
    for_seed, length = [int(x) for x in input('Enter 2 nonnegative integers, the second one '
                                                                             'no greater than 100: '
                                             ).split()
                       ]
    if for_seed < 0 or length > 100:
        raise ValueError
except ValueError:
    print('Incorrect input (not all integers), giving up.')
    sys.exit()
seed(for_seed)
L = sample(list(range(length * 10)), length)
# print('L = ', L)
pq = PriorityQueue()
for e in L:
    pq.insert(e)
print('The heap that has been generated is: ')
print(pq._data[ : len(pq) + 1])
print('The preferred ordering of data to generate this heap by successsive insertion is:')
print(preferred_sequence())
