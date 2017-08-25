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



# Test Codes
if __name__ == "__main__":
    highest_score_words = [['iou'], ['oui']]
    UserOutput(8, highest_score_words)