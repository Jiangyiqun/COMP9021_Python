# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and finds out, for given step_number >= 1
# and step_size >= 2, the number of stairs of step_number many steps,
# with all steps of size step_size.
#
# A stair of 1 step of size 2 is of the form
# 1 1
#   1 1
#
# A stair of 2 steps of size 2 is of the form
# 1 1
#   1 1
#     1 1
#
# A stair of 1 step of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#
# A stair of 2 steps of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#         1
#         1 1 1
#
# The output lists the number of stairs from smallest step sizes to largest step sizes,
# and for a given step size, from stairs with the smallest number of steps to stairs
# with the largest number of stairs.
#
# Written by Jack (z5129432) and Eric Martin for COMP9021


from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))
############ Jack's Code Start ############
def stairs_in_grid():
    for step_size in range(2, int((dim + 1) / 2) + 1):   # the range of step_size
        # print('step_size = ', step_size)
        for i0 in range(0, int(dim - (step_size * 2) + 2)):  # starting point of exploring aera, i indicates row, j indicates column in grid[i][j]
            for j0 in range(0, int(dim - (step_size * 2) + 2)):  
                # print('i0, j0 ', (i0, j0))
                # the main part of checking, from a particular starting point of a step_size
                i = i0
                j = j0
                nb_of_steps = 0
                checked_start_point = []
                print()
                print('for step size = ', step_size)
                print('my startint point is i, j =', (i0, j0))
                for i in range (i, i + step_size):         # checking the first row of stairs 
                    if grid[i][j] == 0:
                        break                               
                else:                                       # if passing the first row test
                    while (i <= dim - step_size and j <= dim - step_size):                               # if i, j still in the range
                        print('begin to check rows and colums, from point')
                        print('i, j =', (i, j))
                        for j in range (j + 1, j + step_size):         # check the rows
                            print('checking the row')
                            print('i, j =', (i, j))
                            if grid[i][j] == 0:
                                break
                            else:                                      # if passing the row check
                                for i in range(i + 1, i + step_size):  # check the column
                                    print('checking the colum')
                                    print('i, j =', (i, j))
                                    if grid[i][j] == 0:
                                        break
                                else:                                  # if passing the row check and the column check                              
                                    nb_of_steps += 1 
                print('for step size = ', step_size)
                print('nb_of_step = ', nb_of_steps)
    # stairs = {step_size: (nb_of_steps, nb_of_stairs)}
    stairs = {2: [(1, 2), (2, 2)], 3: [(2, 4)]}
    return(stairs)



 
############ Jack's Code End ############
dim = 7
grid = [[3, 3, 0, 2, 3, 3, 2], [3, 2, 1, 1, 2, 1, 0], [2, 1, 2, 0, 0, 2, 3],
        [0, 2, 3, 2, 1, 3, 3], [2, 0, 0, 0, 3, 0, 3], 
        [2, 1, 2, 0, 1, 1, 1], [1, 3, 0, 0, 2, 3, 0]]
# print('Here is the grid that has been generated:')
# display_grid()

stairs = stairs_in_grid()
# for step_size in sorted(stairs):
#     print(f'\nFor steps of size {step_size}, we have:')
#     for nb_of_steps, nb_of_stairs in stairs[step_size]:
#         stair_or_stairs = 'stair' if nb_of_stairs == 1 else 'stairs'
#         step_or_steps = 'step' if nb_of_steps == 1 else 'steps'
#         print(f'     {nb_of_stairs} {stair_or_stairs} with {nb_of_steps} {step_or_steps}')