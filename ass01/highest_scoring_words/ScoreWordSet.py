from collections import defaultdict

from ScoreWord import ScoreWord

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



# Test Codes
if __name__ == "__main__":
    word_set = set()
    # word_set = set({'eau', 'iou', 'a', 'oui', 'ie', 'ai'})
    print(ScoreWordSet(word_set))