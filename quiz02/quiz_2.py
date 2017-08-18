# Written by *** and Eric Martin for COMP9021


'''
Generates a list L of random nonnegative integers, the largest possible value
and the length of L being input by the user, and generates:
- a list "fractions" of strings of the form 'a/b' such that:
    . a <= b;
    . a*n and b*n both occur in L for some n
    . a/b is in reduced form
  enumerated from smallest fraction to largest fraction
  (0 and 1 are exceptions, being represented as such rather than as 0/1 and 1/1);
- if "fractions" contains then 1/2, then the fact that 1/2 belongs to "fractions";
- otherwise, the member "closest_1" of "fractions" that is closest to 1/2,
  if that member is unique;
- otherwise, the two members "closest_1" and "closest_2" of "fractions" that are closest to 1/2,
  in their natural order.
'''


import sys
from random import seed, randint
from math import gcd


# try:
#     arg_for_seed, length, max_value = input('Enter three nonnegative integers: ').split()
# except ValueError:
#     print('Incorrect input, giving up.')
#     sys.exit()
# try:
#     arg_for_seed, length, max_value = int(arg_for_seed), int(length), int(max_value)
#     if arg_for_seed < 0 or length < 0 or max_value < 0:
#         raise ValueError
# except ValueError:
#     print('Incorrect input, giving up.')
#     sys.exit()
#
# seed(arg_for_seed)
# L = [randint(0, max_value) for _ in range(length)]
# if not any(e for e in L):
#     print('\nI failed to generate one strictly positive number, giving up.')
#     sys.exit()
# print('\nThe generated list is:')
# print('  ', L)

fractions = []
spot_on, closest_1, closest_2 = [None] * 3

# this function can return two elements (float, string)
# string is a fraction of numerator/denominator
# float is the value of the fraction
# if numerator is 0, return '0'
def fran(numerator, denominator):
    if numerator * denominator == 0:
        return '0'
    else:
        divisor = gcd(int(numerator), int(denominator))
        numerator = int(numerator) / divisor
        denominator = int(denominator) / divisor
        return str(int(numerator)) + '/' + str(int(denominator))


# Jack's code begins
L = [8, 0, 4, 4,  27, 25]
print('L = ', L)

# L1 is sorted L without duplicated elements, and without 0
L1 = list(set(L))   # sort and remove duplicated elements
if 0 in L1:         # mark is there is 0 in L
    zero = True
else:
    zero = False
L1.remove(0)        # remove 0 from L1
print('zero = ', zero)
print('L1 = ', L1)

# L2 is a tuple [(float, str), (float, str),(float, str) ...]
# string is a fraction
# float is the value of the fraction
# L2 is sorted by float
L2 = []
for i in range(len(L1)):
    for j in range(i + 1,len(L1)):
        L2.append((L1[i] / L1[j], fran(L1[i], L1[j])))
L2.sort()   # sort by the first element
print('L2 = ', L2)

# generate fractions[]
if zero:                  # add 0 if needed
    fractions.append('0')
for e in L2:              # add other fractions
    fractions.append(e[1])
fractions.append('1')    # add 1

# L3 is sorted by abs(L2 - 0.5)
# search for 1/2 and generate closet_1 and closet_2
L3 = sorted(L2, key = lambda e:abs(e[0] - 0.5)) # L3 is sorted by abs(L2 - 0.5)
L3_float,L3_fran = zip(*L3)

print('L3 = ', L3)
print('L3_float = ', L3_float)
print('L3_fran = ', L3_fran)

if L3_float[0] == 0.5:
    spot_on = True
else:
    closest_1 = L3_fran[0]
    if L3_float[0] != L3_float[1]:
        closest_2 = L3_fran[1]

# Jack's code ends

print('\nThe fractions no greater than 1 that can be built from L, from smallest to largest, are:')
print('  ', '  '.join(e for e in fractions))
if spot_on:
    print('One of these fractions is 1/2')
elif closest_2 is None:
    print('The fraction closest to 1/2 is', closest_1)
else:
    print(closest_1, 'and', closest_2, 'are both closest to 1/2')
