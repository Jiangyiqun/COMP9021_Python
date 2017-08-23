# test codes
# initialize die[]
# top front right bottom back left
#  0    1     2     3     4   5
die = [3, 2, 1, 4, 5, 6]
cell = 2

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

# test code:
move_right()
move_forewards()
move_left()
move_left()
move_backwards()

# user interface: output part
print(f'On Cell {cell}, {die[0]} is at the top, {die[1]} at the front, and {die[2]} on the right')