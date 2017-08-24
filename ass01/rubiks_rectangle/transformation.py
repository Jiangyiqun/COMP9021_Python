# function: transformation
# input: current_state[], type
#              0 for row Exchange
#              1 for right circular Shift
#              2 for middle clockwise rotation
# output: current_state[]
# description:
# this funtion will manipulate current_state
# initial state 1   2   3   4   5   6   7   8
# E             8   7   6   5   4   3   2   1
# S             4   1   2   3   6   7   8   5
# R             1   7   2   4   5   3   6   8
def transformation(current_state, type):
    current_state_copy = current_state[:]
    if type == 0:         # row Exchange
        current_state[0] = current_state_copy[7]
        current_state[1] = current_state_copy[6]
        current_state[2] = current_state_copy[5]
        current_state[3] = current_state_copy[4]
        current_state[4] = current_state_copy[3]
        current_state[5] = current_state_copy[2]
        current_state[6] = current_state_copy[1]
        current_state[7] = current_state_copy[0]
    if type == 1:         # right circular Shift
        current_state[0] = current_state_copy[3]
        current_state[1] = current_state_copy[0]
        current_state[2] = current_state_copy[1]
        current_state[3] = current_state_copy[2]
        current_state[4] = current_state_copy[5]
        current_state[5] = current_state_copy[6]
        current_state[6] = current_state_copy[7]
        current_state[7] = current_state_copy[4]
    if type == 2:         # middle clockwise rotation
        current_state[0] = current_state_copy[0]
        current_state[1] = current_state_copy[6]
        current_state[2] = current_state_copy[1]
        current_state[3] = current_state_copy[3]
        current_state[4] = current_state_copy[4]
        current_state[5] = current_state_copy[2]
        current_state[6] = current_state_copy[5]
        current_state[7] = current_state_copy[7]
    return(current_state)


# test code
if __name__ == "__main__":
    current_state = [1, 2, 3, 4, 5, 6, 7, 8]
    print(current_state)
    current_state = transformation(current_state, 1)
    print(current_state)