from ScoreWordSet import ScoreWordSet

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


# Test Codes
if __name__ == "__main__":
    # scored_word_set = {}
    scored_word_set = {8: [['oui'], ['iou']], 2: [['a'], ['ie']], 7: [['eau']], 3: [['ai']]}
    highest_score, highest_score_words = FindHighestScoreWords(scored_word_set)
    print(highest_score)
    print(highest_score_words)