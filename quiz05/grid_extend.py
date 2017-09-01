def grid_extend(grid):
    """grid_extend
Extend grid with 0 value surrounded by origin data.
    """
    grid_ext = grid[:]
    if grid_ext:                               # if it is not empty
        for i in range(len(grid_ext)):         # extend two columns with zero
            grid_ext[i] = [0] + grid_ext[i] + [0]
        empty_line = [[0 for _ in range(len(grid_ext[0]))]] # extend two rows with zero
        grid_ext = empty_line + grid_ext + empty_line
    return grid_ext




if __name__ == "__main__":
    grid = [
        [3, 3, 0, 2, 4, 3, 3, 2],
        [3, 2, 4, 1, 4, 1, 2, 1],
        [0, 4, 2, 4, 4, 1, 2, 0],
        [0, 2, 3, 4, 0, 2, 3, 2],
        [4, 1, 4, 3, 3, 4, 2, 0]
        ]
    print(grid_extend(grid))
