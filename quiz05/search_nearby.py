from collections import defaultdict


def search_nearby(i, j, grid, paths, n):
    """search_nearby
    Returns:
    A dictionary which format is like:
    {0: No. of Paths, 1: No. of Paths, 2: No. of Paths ...}
    Description:
    This is a recursive function.
    It starts from a coordinate (i, j) which value is n.
    Search for n+1 in the nearst 4 coordinate.
    """
    n_can_be_extended = False
    if grid[i][j - 1] == n + 1:
        paths[n + 1] += 1
        n_can_be_extended = True
        paths = search_nearby(i, j - 1, grid, paths, n + 1)
    if grid[i][j + 1] == n + 1:
        paths[n + 1] += 1
        n_can_be_extended = True
        paths = search_nearby(i, j + 1, grid, paths, n + 1)
    if grid[i - 1][j] == n + 1:
        paths[n + 1] += 1
        n_can_be_extended = True
        paths = search_nearby(i - 1, j, grid, paths, n + 1)
    if grid[i + 1][j] == n + 1:
        paths[n + 1] += 1
        n_can_be_extended = True
        paths = search_nearby(i + 1, j, grid, paths, n + 1)
    if n_can_be_extended:
        paths[n] -= 1
    return paths


if __name__ == "__main__":
    i, j, max_length = 2, 8, 4
    paths = defaultdict()
    paths = {1: 1, 2: 0, 3: 0, 4: 0}
    # print(paths)
    grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 3, 0, 2, 4, 3, 3, 2, 0],
    [0, 3, 2, 4, 1, 4, 1, 2, 1, 0],
    [0, 0, 4, 2, 4, 4, 1, 2, 0, 0],
    [0, 0, 2, 3, 4, 0, 2, 3, 2, 0],
    [0, 4, 1, 4, 3, 3, 4, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    search_nearby(i, j, grid, paths, 1)
    print(paths)
