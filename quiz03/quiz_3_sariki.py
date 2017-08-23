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
# Written by *** and Eric Martin for COMP9021


from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))

def stairs_in_grid():
    # Replace return {} above with your code
    
#here it starts
    from random import seed,randint
def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))
seed(0)
grid = [[randint(0, 3) for _ in range(9)] for _ in range(9)]
print('Here is the grid that has been generated:')
display_grid()

step_1=0

for j in range(len(grid)):
    for i in range(len(grid)):
        if grid[j][i] !=0:
            try:
                if grid[j][i+1] != 0:
                    if grid[j+1][i+1] !=0:
                        if grid[j+1][i+2] not in [0,-1]:
                            grid[j+1][i+2] = -1
                            step_1 += 1
                            print(j,i)
            except IndexError:
                pass
        else:
            continue
print(step_1)
# here it ends

# Possibly define other functions

try:
    arg_for_seed, density, dim = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density, dim = int(arg_for_seed), int(density), int(dim)
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
# A dictionary whose keys are step sizes, and whose values are pairs of the form
# (number_of_steps, number_of_stairs_with_that_number_of_steps_of_that_step_size),
# ordered from smallest to largest number_of_steps.
stairs = stairs_in_grid()
for step_size in sorted(stairs):
    print(f'\nFor steps of size {step_size}, we have:')
    for nb_of_steps, nb_of_stairs in stairs[step_size]:
        stair_or_stairs = 'stair' if nb_of_stairs == 1 else 'stairs'
        step_or_steps = 'step' if nb_of_steps == 1 else 'steps'
        print(f'     {nb_of_stairs} {stair_or_stairs} with {nb_of_steps} {step_or_steps}')
