# Author:   Jack (z5129432) for COMP9021 Assignment 1
# Date:     23/08/2017
# Description:

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

# function: interface_output
# input: steps
# output: print
def interface_output(steps):
    if steps == 0 or steps == 1:
        unit = 'step'
    else:
        unit = 'steps'
    print(f'{steps} {unit} is needed to reach the final configuration.')
    return

# funtion: count_steps
# dependency: check_steps()
# input: state_1, state_2
# output: steps
# description: use check_steps() to calculate steps from state_1 to state_2
def count_steps(state_1, state_2):
    steps = int(0)
    if state_1 == state_2:
        return(steps)
    while True:
        steps += 1
        if check_steps(state_1, state_2, steps):
            return(steps)

# funtion: check_steps
# version: 1.0
# dependency: transformation()
# input: state_1, state_2, steps
# output: Boolean
# description: use whether use steps can transform state_1 to state_2
# 1  E   S   R
# 2  EE  ES  ER  SE  SS  SR  RE  RS  RR
# 3  EEE EES EER ESE ESS ESR SER ERS ERR SEE SES SER SSE SSS SSR SRE SRS SRR REE RES RER RSE RSS RSR RRE RRS RRR
#   example:
#   for RRE the 24 value
#   24 // (3 ** 2)  = 2, so type = 2
#   24 % (3 ** 2)   = 6 // (3 ** 1)= 2, so type = 2
#   6 % 3 = 0 // (3 ** 0) = 0, so type = 0  
def check_steps(state_1, state_2, steps):
    for sequency_of_methods in range(0, 3 ** steps): # sequency_of_methods start from 0
        # initialize variable which will be used in next loop
        state_1_copy = state_1[:]
        remainder = sequency_of_methods
        # calculate methods(sequency_of_methods)
        for i in range(1, steps + 1):           # i in the indicator of steps of one methods, start from 1
            type = remainder // (3 ** (steps - i))
            state_1_copy = transformation(state_1_copy, type)
            remainder = remainder % (3 ** (steps- i))
        if state_1_copy == state_2:
            return True        
    return False

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

# initialization
current_state = [1, 2, 3, 4, 5, 6, 7, 8]
final_configuration = interface_input() # final_configuration
steps = count_steps(current_state, final_configuration)
interface_output(steps)