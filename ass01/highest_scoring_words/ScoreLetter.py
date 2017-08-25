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



# Test Codes
if __name__ == "__main__":
    for letter in "abcdefghijklmnopqrstuvwxyz":
        print(ScoreLetter(letter))