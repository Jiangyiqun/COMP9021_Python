from collections import defaultdict
from search_nearby import search_nearby


def get_paths(grid, max_length):
    """ get_paths
Calculate the number of paths of input grids. 
Its output is a dictionary paths, such as:
{0: No. of Paths, 1: No. of Paths, 2: No. of Paths ...}
    """
    paths = defaultdict()
    for key in range(1, max_length + 1):
        paths[key] = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                paths[1] += 1
                patchs = search_nearby(i, j, grid, paths, 1)
    return paths


if __name__ == "__main__":
    max_length = 4
    grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 3, 0, 2, 4, 3, 3, 2, 0], 
    [0, 3, 2, 4, 1, 4, 1, 2, 1, 0],
    [0, 0, 4, 2, 4, 4, 1, 2, 0, 0],
    [0, 0, 2, 3, 4, 0, 2, 3, 2, 0],
    [0, 4, 1, 4, 3, 3, 4, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    print(get_paths(grid, max_length))  # paths = {4:2, 3:5, 2:1}

