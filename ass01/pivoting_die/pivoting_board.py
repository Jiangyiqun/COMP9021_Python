# function: board
# input: cell
# output: board = {'R': number of moving right,'F':number of moving forewards,
#                    'L':number of moving left,'B':number of moving backwards}
# description:
# cell  R   F   L   B
#   1
#   2   1
#   3       1
#   4           1
#   5           2
#   6               1
#   7               2
#   8   2
#   9   3
#   10  4
#   11      2
#   12      3
#   13      4
#   14          3   
#   15          4
#   16          5
#   17          6
#   18              3
#   19              4
#   20              5
#   21              6
#   22  5
#   23  6
#   24  7
#   25  8
#   26  9
#   27      5
#   28      6
#   29      7
#   30      8
#   31      9
#   32          7
def board(cell):
    board = {'R':0,'F':0,'L':0,'B':0}   # initialize board with 0 numbers
    step = 1                            # initialize moving step in one direction
    while(cell > 1):
        for _ in range(0, step):            # moving right for "step" steps
            board['R'] += 1
            cell -= 1                       # cell is using as a counter
            if cell <= 1:
                return(board)
        for _ in range(0, step):            # moving forewards for "step" steps
            board['F'] += 1
            cell -= 1                       # cell is using as a counter
            if cell <= 1:
                return(board)
        step += 1                           # increase step by 1
        for _ in range(0, step):            # moving left for "step" steps
            board['L'] += 1
            cell -= 1                       # cell is using as a counter
            if cell <= 1:
                return(board)
        for _ in range(0, step):            # moving backwards for "step" steps
            board['B'] += 1
            cell -= 1                       # cell is using as a counter
            if cell <= 1:
                return(board)
        step += 1                           # increase step by 1
    return(board)

# test codes
print(board(6))