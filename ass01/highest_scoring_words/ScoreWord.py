from ScoreLetter import ScoreLetter

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



# Test Codes
if __name__ == "__main__":
    print(ScoreWord(''))