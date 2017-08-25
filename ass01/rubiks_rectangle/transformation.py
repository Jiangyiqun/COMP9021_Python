# function: transformation
# version: v02
# input: before_transformation(), type
#              0 for row Exchange
#              1 for right circular Shift
#              2 for middle clockwise rotation
# output: after_transformation()
# description:
# this funtion will manipulate current_state
# initial state 1   2   3   4   5   6   7   8
# E             8   7   6   5   4   3   2   1
# S             4   1   2   3   6   7   8   5
# R             1   7   2   4   5   3   6   8

def transformation(before_transformation, type):
    before_transformation = list(before_transformation)
    after_transformation = before_transformation[:]
    if type == 0:         # row Exchange
        after_transformation[0] = before_transformation[7]
        after_transformation[1] = before_transformation[6]
        after_transformation[2] = before_transformation[5]
        after_transformation[3] = before_transformation[4]
        after_transformation[4] = before_transformation[3]
        after_transformation[5] = before_transformation[2]
        after_transformation[6] = before_transformation[1]
        after_transformation[7] = before_transformation[0]
    if type == 1:         # right circular Shift
        after_transformation[0] = before_transformation[3]
        after_transformation[1] = before_transformation[0]
        after_transformation[2] = before_transformation[1]
        after_transformation[3] = before_transformation[2]
        after_transformation[4] = before_transformation[5]
        after_transformation[5] = before_transformation[6]
        after_transformation[6] = before_transformation[7]
        after_transformation[7] = before_transformation[4]
    if type == 2:         # middle clockwise rotation
        after_transformation[0] = before_transformation[0]
        after_transformation[1] = before_transformation[6]
        after_transformation[2] = before_transformation[1]
        after_transformation[3] = before_transformation[3]
        after_transformation[4] = before_transformation[4]
        after_transformation[5] = before_transformation[2]
        after_transformation[6] = before_transformation[5]
        after_transformation[7] = before_transformation[7]
    return(tuple(after_transformation))


# test code
if __name__ == "__main__":
    current_state = (1, 2, 3, 4, 5, 6, 7, 8)
    print(current_state)
    print(transformation(current_state, 0))
    print(transformation(current_state, 1))
    print(transformation(current_state, 2))