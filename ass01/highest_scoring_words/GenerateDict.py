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



# Test Codes
if __name__ == "__main__":
    print(GenerateDict("wordsEn.txt"))