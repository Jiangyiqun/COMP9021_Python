import sys

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



# Test Codes
if __name__ == "__main__":
    print(UserInput())