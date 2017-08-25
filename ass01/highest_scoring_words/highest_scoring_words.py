# Author:   Jack (z5129432) for COMP9021 Assignment 1
# Date:     25/08/2017
# Description: Qustion 3
from itertools import permutations
from collections import defaultdict
import sys

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

# Function: FindHighestScoreWords
# Dependency: ScoreWord
# Input:  an unsorted dictionary contains words, such as {8: [['oui'], ['iou']], 2: [['a'], ['ie']], 7: [['eau']], 3: [['ai']]}
# Output: search in the input set. return an integer (highest score), such as 8
#         followed by a list (highest score words) orderd alphabetaly, such as [['iou'], ['oui']]
# Description:
def FindHighestScoreWords(scored_word_set):
    if len(scored_word_set) != 0:
        highest_score = sorted(scored_word_set.keys())[len(scored_word_set) - 1]
        highest_score_words = sorted(scored_word_set[highest_score])
    else:
        highest_score = 0
        highest_score_words = []
    return highest_score, highest_score_words

# Function: GenerateDict.py
# Dependency: 
# Input: a string such as "wordsEn.txt"
# Output: a set of the words in the dictionary such as {'backup', 'way', 'rink'}
# Description:
def GenerateDict(file_name):
    word_dictionary = set()
    with open("wordsEn.txt") as book:
        for line in book:
            word_dictionary.add(line.strip())
    return(word_dictionary)

# Function: ScoreLetter
# Dependency: 
# Input: a letter 'i'
# Output: an integer(score of letter)
# Description:
def ScoreLetter(letter):
    magic_book = {
                  'a': 2, 'b': 5, 'c': 4, 'd': 4, 'e': 1, 'f': 6, \
                  'g': 5, 'h': 5, 'i': 1, 'j': 7, 'k': 6, 'l': 3, \
                  'm': 5, 'n': 2, 'o': 3, 'p': 5, 'q': 7, 'r': 2, \
                  's': 1, 't': 2, 'u': 4, 'v': 6, 'w': 6, 'x': 7, \
                  'y': 5, 'z': 7
                  }
    return(magic_book[letter])

# Function: ScoreWord
# Dependency: ScoreLetter
# Input: a string 'iou'
# Output: an integer (score) such as 8 for 'iou'
# Description:
def ScoreWord(word):
    score = int(0)
    for letter in word:
        score += ScoreLetter(letter)
    return(score)

# Function: ScoreWordSet
# Dependency: ScoreWord, collections.defaultdict
# Input: a set contains words, such as {'eau', 'iou', 'a', 'oui', 'ie', 'ai'}
# Output: an unsorted dictionary contains words, such as {8: [['oui'], ['iou']], 2: [['a'], ['ie']], 7: [['eau']], 3: [['ai']]}
# Description:
def ScoreWordSet(word_set):
    scored_word_set = defaultdict(list)
    word_set = list(word_set)
    for word in word_set:
        scored_word_set[ScoreWord(word)].append([word])
    return(scored_word_set)

# Function: UserInput   Version: 01
# Dependency: sys.exit
# Input: 3 ~ 10 lowercase letters from user
# Output: a list ['a', 'e', 'i', 'o', 'u']
# Description:
def UserInput():
    converted_letters = []
    try:
        input_letters = input('Enter between 3 and 10 lowercase letters: ').replace(" ", "")
        if len(input_letters) < 3 or len(input_letters) > 10:
            raise ValueError
        for e in input_letters:
            if e.islower():
                converted_letters.append(e)                
            else:
                raise ValueError
    except ValueError:
        print('Incorrect input, giving up...')
        sys.exit()
    return(converted_letters)

# Function: UserOutput   Version: 01
# Dependency: sys.exit
# Input: an integer (highest score), such as 8
#        followed by a list (highest score words) orderd alphabetaly, such as [['iou'], ['oui']]
# Output: print
# Description:
def UserOutput(highest_score, highest_score_words):
    if len(highest_score_words) == 0:
        print('No word is built from some of those letters.')
    elif len(highest_score_words) == 1:
        print(f'The highest score is {highest_score}.')
        print(f'The highest scoring word is {highest_score_words[0][0]}')
    else:
        print(f'The highest score is {highest_score}.')
        print('The highest scoring words are, in alphabetical order:')
        for the_words in highest_score_words:
            print(f'    {the_words[0]}')
    return

##### main function
debug_mode = 0          # toggle debug_mode, print output of every functions
input_letters = UserInput()
if debug_mode == 1:
    print('input_letters =', input_letters)

word_dictionary = GenerateDict("wordsEn.txt")
if debug_mode == 3:
    print('word_dictionary =', word_dictionary)

letters_combination = CombineLetters(input_letters, word_dictionary)
if debug_mode == 2:
    print('letters_combination =', letters_combination)

scored_word_set = ScoreWordSet(letters_combination)
if debug_mode == 5:
    print('scored_word_set =', scored_word_set)

highest_score, highest_score_words = FindHighestScoreWords(scored_word_set)
if debug_mode == 6:
    print('scored_word_set =', scored_word_set)
    print(highest_score)
    print(highest_score_words)

UserOutput(highest_score, highest_score_words)