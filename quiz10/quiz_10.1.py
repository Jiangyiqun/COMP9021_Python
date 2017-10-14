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
from itertools import permutations

# Possibly define some functions
    
def preferred_sequence():
    all_possible_sequences = []
    for t in permutations(L):
        all_possible_sequences.append(t)
    all_possible_sequences.sort()


    for preferred_sequence in all_possible_sequences:
        pq_generated_by_preferred_sequence = PriorityQueue()
        for e in preferred_sequence:
            pq_generated_by_preferred_sequence.insert(e)
        if pq_generated_by_preferred_sequence._data == pq._data:
            return list(preferred_sequence)
    
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

