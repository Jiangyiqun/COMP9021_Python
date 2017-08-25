from itertools import permutations
from time import time

# Function: CombineLetters
# Dependency: itertools.permutations
# Input: a list such as ['a', 'b', 'c']
# Output: a set such as {'ab', 'bac', 'b', 'c', 'acb', 'ca', 'bc', 'cb', 'cba', 'ba', 'bca', 'ac', 'cab', 'abc', 'a'}
# Description:
def CombineLetters(letters):
    letters_combination = set()
    for word_length in range (1, len(letters) + 1):         # generate different word length
        letters_combination |= set(''.join(e) for e in permutations(letters, word_length))  # union all permutation()
    return(letters_combination)



# Test Codes
if __name__ == "__main__":
    Letters =  ['e', 'a', 'e', 'o', 'r', 't', 's', 'm', 'n', 'z']
    # Letters = ['a', 'b', 'c']
    before_time = time()
    CombineLetters(Letters)
    print(time()- before_time)
    print('down')