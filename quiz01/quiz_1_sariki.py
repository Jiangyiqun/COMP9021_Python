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

# MmmmmmM
M.append(L[length // 2])
for i in range(length // 2):
    M.append(L[i])
    M.append(L[-i - 1])
if length % 2 == 0:
	del M[-1]

# NnnnnnN
N2 = [] #an empty set, used to mark used N
index_L = 0 #index of L, indicate which L[index_L] should be append into N
index_N = 0 #index of N, indicate which N[index_N] should be the new index_L

while (len(N) < len(L)):
    if (index_L not in N2):   #index is not used
        N2.append(index_L)    #mark index to be used
        N.append(L[index_L])  #add L[index] to N
        index_L = N[index_N]  #generate new index_L
        index_N += 1        #generate new index_N
    else:                   #index is used
        index_L = 0         #index is used, begin at the least
        while (index_L in N2):   #this loop can find the least L which is not used
          index_L += 1
        # if(index>=L[index]):
        #         index = L[index]
                
        #         while True:
        #             index += 1
        #             if ('L' + str(index) not in N2):
        #                 N2.add('L' + str(index))
        #                 N.append(L[index])
        #                 break
        #             else:
        #                 while True:
        
# if ('L' + str(index) not in N2):                        
#     N2.add('L' + str(index))
#     N.append(L[index])
    
    #break
	
 
print('\nHere is M:')
print('  ', M)
print('\nHere is N:')
print('  ', N)
print('\nHere is L again:')
print('  ', L)