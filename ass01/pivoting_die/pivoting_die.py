# Author: Jack (z5129432) for COMP9021 Assignment 1
# Date:   23/08/2017
# Description:
''' 
'''
import sys

# function: move
# input: null
# output: die[] after moved
def move_right():
    die_copy = die[:]
    die[3] = die_copy[2] # right become bottom
    die[2] = die_copy[0] # top become right
    die[0] = die_copy[5] # left become top
    die[5] = die_copy[3] # bottom become left
    return
def move_left():
    die_copy = die[:]
    die[0] = die_copy[2] # right become top
    die[5] = die_copy[0] # top become left
    die[3] = die_copy[5] # left become bottom
    die[2] = die_copy[3] # bottom become right
    return
def move_forewards():
    die_copy = die[:]
    die[1] = die_copy[0] # top become front
    die[3] = die_copy[1] # front become bottom
    die[4] = die_copy[3] # bottom become back
    die[0] = die_copy[4] # back become top
    return
def move_backwards():
    die_copy = die[:]
    die[4] = die_copy[0] # top become back
    die[0] = die_copy[1] # front become top
    die[1] = die_copy[3] # bottom become front
    die[3] = die_copy[4] # back become bottom
    return


# user interface: input part
while True:
    try:
        cell = int(input('Enter the desired goal cell number: '))
        if cell <= 0:
            raise ValueError
        break
    except ValueError:
        print('Incorrect value, try again')

# initialize die[]
# top front right bottom back left
#  0    1     2     3     4   5
die = [3, 2, 1, 4, 5, 6]
# initialize moving step in one direction
step = 1    
# initialize counter     
i = cell                       

# simulate moving die
# function: move
# input: null
# output: die[] after moved
while(i > 1):
    for _ in range(0, step):            # moving right for "step" steps
        move_right()
        i -= 1                      
        if i <= 1:
            break
    if i <= 1:
            break
    for _ in range(0, step):            # moving forewards for "step" steps
        move_forewards()
        i -= 1                      
        if i <= 1:
            break
    if i <= 1:
            break
    step += 1                           # increase step by 1
    for _ in range(0, step):            # moving left for "step" steps
        move_left()
        i -= 1                      
        if i <= 1:
            break
    if i <= 1:
            break
    for _ in range(0, step):            # moving backwards for "step" steps
        move_backwards()
        i -= 1                      
        if i <= 1:
            break
    step += 1                           # increase step by 1

# user interface: output part
print(f'On cell {cell}, {die[0]} is at the top, {die[1]} at the front, and {die[2]} on the right.')