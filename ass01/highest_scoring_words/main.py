# Author:   Jack (z5129432) for COMP9021 Assignment 1
# Date:     25/08/2017
# Description: Qustion 3

from UserInput import UserInput
from UserOutput import UserOutput
from CombineLetters import CombineLetters
from GenerateDict import GenerateDict
from ScoreWordSet import ScoreWordSet
from FindHighestScoreWords import FindHighestScoreWords


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