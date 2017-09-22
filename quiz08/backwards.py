from stack_adt import *


def backwards(grid, target, path, current_sum):
    '''
    North(-1, 0) --> East(0, 1) --> South(1, 0) --> West(0, -1)
    '''
    change_direction = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}
    # initialize direction
    present_x, present_y = path.pop()
    current_sum -= grid[present_x][present_y]
    try:
        previous_x, previous_y = path.peek()
        direction_x, direction_y = present_x -  previous_x, present_y - previous_y
    except EmptyStackError:
        return False, current_sum
    direction_x, direction_y = change_direction[direction_x, direction_y]
    # try other directions and check its validaty
    # if direction is North, then return, because north has been used at the first time
    while (direction_x, direction_y) != (-1, 0):
        next_x, next_y = previous_x + direction_x, previous_y + direction_y
        if next_x >= 10 or next_x <0 \
                or next_y >= 10 or next_y <0 \
                or (next_x, next_y) in path._data:  # if next point is out of board or has used before
            direction_x, direction_y = change_direction[direction_x, direction_y]
        elif current_sum + grid[next_x][next_y] > target:                   # if next point causes sum out of target
            direction_x, direction_y = change_direction[direction_x, direction_y]
        else:
            current_sum += grid[next_x][next_y]
            path.push((next_x, next_y))
            return False, current_sum
    return True, current_sum

if __name__ == "__main__":
    grid = [[6, 6, 0, 4, 8, 7, 6, 4, 7, 5],\
            [9, 3, 8, 2, 4, 2, 1, 9, 4, 8],\
            [9, 2, 4, 1, 1, 5, 7, 8, 1, 5],\
            [6, 5, 9, 3, 8, 7, 7, 8, 4, 0],\
            [8, 0, 1, 6, 0, 9, 7, 5, 3, 5],\
            [1, 3, 9, 3, 3, 2, 8, 7, 1, 1],\
            [5, 8, 7, 1, 4, 8, 4, 1, 8, 5],\
            [8, 3, 9, 8, 9, 4, 7, 1, 9, 6],\
            [5, 9, 3, 4, 2, 3, 2, 0, 9, 4],\
            [7, 1, 1, 2, 2, 0, 1, 8, 6, 8]]
    target = 20
    path = Stack()
    path.push((3, 3))
    path.push((2, 3))
    path.push((1, 3))
    path.push((0, 3))
    path.push((0, 4))
    current_sum = 18
    (return_x, return_y) = backwards(grid, target, path, current_sum)
    print((return_x, return_y))
    print(path.peek())