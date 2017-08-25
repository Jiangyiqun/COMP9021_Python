from itertools import permutations
from time import time
from GenerateDict import GenerateDict

# Function: CombineLetters
# Dependency: itertools.permutations
# Input: a list such as ['a', 'b', 'c']
# Output: a set such as {'ab', 'bac', 'b', 'c', 'acb', 'ca', 'bc', 'cb', 'cba', 'ba', 'bca', 'ac', 'cab', 'abc', 'a'}
# Description:
def CombineLetters(letters, word_dictionary):
    letters_combination =  set()
    for word_length in range (1, len(letters) + 1):         # generate different word length
        letters_combination |= set(''.join(e) for e in permutations(letters, word_length)) &  word_dictionary  # union all permutation()
    return(letters_combination)



# Test Codes
if __name__ == "__main__":
    Letters =  ['e', 'a', 'e', 'o', 'r', 't', 's', 'm', 'n', 'z']
    # Letters = ['a', 'b', 'c']
    word_dictionary = GenerateDict("wordsEn.txt")
    before_time = time()
    CombineLetters(Letters, word_dictionary)
    print(time()- before_time)
    print('down')