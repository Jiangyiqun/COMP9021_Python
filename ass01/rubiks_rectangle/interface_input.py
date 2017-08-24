import sys

# funtion: interface_input
# dependency: sys
# input: user input
# output: final_configuration[]
def interface_input():
    try:
        user_input = input('Input final configuration: ')
        user_input = user_input.replace(" ", "")     # remove space
        if len(user_input) != 8:                             # check the length of input is equal to 8
            raise ValueError  
        final_configuration = []                                                           
        for i in range(8):                               
            if int(list(user_input)[i]) in range(1, 9):      # check if they are all digits and between 0 and 8
                final_configuration.append(int(list(user_input)[i]))
            else:
                raise ValueError
        if len(set(final_configuration)) < 8:                   # check if there are duplicate value
            raise ValueError
    except ValueError:
        print('Incorrect configuration, giving up...')
        sys.exit()
    return(final_configuration)


# test code
if __name__ == "__main__":
    final_configuration = interface_input()
    print(final_configuration)