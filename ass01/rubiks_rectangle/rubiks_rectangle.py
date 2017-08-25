# Author:   Jack (z5129432) for COMP9021 Assignment 1
# Date:     23/08/2017
# Description:

import sys

# funtion: calculate_next_step
# version: v01
# dependency: transformation()
# input: this_step[]
# output: next_step[]
# description: just add new elements to next_step[], I mean this_step is included into next_step
def calculate_next_step(this_step):
    this_step = list(this_step)
    next_step = set()
    for i in range(len(this_step)):         # find every elements this_step[i]
        for type in range(3):               # apply 3 transformations on each elements
            next_step.add(transformation(this_step[i], type))  
    return(next_step)

# funtion: count_steps
# dependency: check_steps()
# input: state_1, state_2
# output: steps
# description: use check_steps() to calculate steps from state_1 to state_2
def count_steps(state_1, state_2):
    steps = int(0)
    if state_1 == state_2:
        return(steps)

    this_step = [state_1]
    while True:
        steps += 1
        this_step = calculate_next_step(this_step)
        for e in this_step:
            if state_2 == e:
                return(steps)

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
    return(tuple(final_configuration))

# function: interface_output
# input: steps
# output: print
def interface_output(steps):
    if steps == 0 or steps == 1:
        unit = 'step is'
    else:
        unit = 'steps are'
    print(f'{steps} {unit} needed to reach the final configuration.')
    return

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

# initialization
current_state = (1, 2, 3, 4, 5, 6, 7, 8)
final_configuration = interface_input()
steps = count_steps(current_state, final_configuration)
interface_output(steps)