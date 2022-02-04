grid = [[0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
        [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]]


def exploreIsland(grid, r, c, visited):
    rowInbound = 0 <= r < len(grid)
    colInbound = 0 <= c < len(grid[0])

    if not rowInbound or not colInbound:
        return False

    if grid[r][c] == 1:
        return True

    position = str(r) + "," + str(c)
    if position in visited:
        return False
    visited.add(position)
    a = exploreIsland(grid, r - 1, c, visited)
    b = exploreIsland(grid, r + 1, c, visited)
    c = exploreIsland(grid, r, c - 1, visited)
    d = exploreIsland(grid, r, c + 1, visited)

    return a and b and c and d


visited = set()
count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 0:
            if exploreIsland(grid, i, j, visited):
                count += 1
print(count)
