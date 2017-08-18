# Written by *** and Eric Martin for COMP9021


'''
Generates a list L of random nonnegative integers smaller than the length of L,
whose value is input by the user, and outputs two lists:
- a list M consisting of L's middle element, followed by L's first element,
  followed by L's last element, followed by L's second element, followed by
  L's penultimate element...;

- a list N consisting of L[0], possibly followed by L[L[0]], possibly followed by
  L[L[L[0]]]..., for as long as L[L[0]], L[L[L[0]]]... are unused, and then,
  for the least i such that L[i] is unused, followed by L[i], possibly followed by
  L[L[i]], possibly followed by L[L[L[i]]]..., for as long as L[L[i]], L[L[L[i]]]...
  are unused, and then, for the least j such that L[j] is unused, followed by L[j],
  possibly followed by L[L[j]], possibly followed by L[L[L[j]]]..., for as long as
  L[L[j]], L[L[L[j]]]... are unused... until all members of L have been used up.
'''


import sys
from random import seed, randrange


try:
    arg_for_seed, length = input('Enter two nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length = int(arg_for_seed), int(length)
    if arg_for_seed < 0 or length < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randrange(length) for _ in range(length)]
print('\nThe generated list L is:')
print('  ', L)
M = []
N = []

# Start: Written by Jack

# Test code:
# L = []
# length = len(L)
# print('L = ', L)
# print('length = ', length)

# Calculate M[]
if length > 0:
  M = [0] * length
  M[0] = L[int(length / 2)] # initialize the first two values in M[i]
  if length > 1:
    M[1] = L[int(0)]
    for i in range(2, length):  # calculate the other values in M[i]
        if i % 2 == 0:
            M[int(i)] = L[int(length) - (int(i) // 2)]
        else:
            M[int(i)] = L[int(i) // 2]

# Calculate N[]
if length > 0:
  N = [0] * length
  Mark_L = [True] + [False] * (length -1)   #mark the used bit in L[j]
  N[0] = L[0] # initialize the first value in N[i]
  for i in range(1, length): 
    j = N[int(i - 1)]   # N[i] = L[j], calculate j
    if Mark_L[j]:  #if L[j] is already used, find the lest j which is not used
        for j in range(length):
            if not Mark_L[j]:
                break
    N[i] = L[j]  # calculate the other values in N[i]
    Mark_L[j] = True

# End: Written by Jack

print('\nHere is M:')
print('  ', M)
print('\nHere is N:')
print('  ', N)
print('\nHere is L again:')
print('  ', L)
