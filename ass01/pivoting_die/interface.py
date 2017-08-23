# Author: Jack (z5129432) for COMP9021 Assignment 1
# Date:   23/08/2017
# Description:
''' 
'''
import sys

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

# calculate times/dirction of moving on the board
#board = board(cell)
board = {'R':3,'F':0,'L':0,'B':0}

# simulate moving die
for _ in range(0, board['R']) :
   move_right()
for _ in range(0, board['F']) :
   move_forewards()
for _ in range(0, board['L']) :
   move_left()
for _ in range(0, board['R']) :
   move_backwards()

# user interface: output part
print(f'On Cell {cell}, {die[0]} is at the top, {die[1]} at the front, and {die[2]} on the right')