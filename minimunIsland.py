grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]

visited = set()


def exploreIsland(grid, r, c, visited):
    rowInbound = 0 <= r < len(grid)
    colInbound = 0 <= c < len(grid[0])

    if not rowInbound or not colInbound:
        return 0
    if grid[r][c] == 'W':
        return 0

    position = str(r) + "," + str(c)
    if position in visited:
        return 0
    visited.add(position)

    size = 1
    size += exploreIsland(grid, r - 1, c, visited)
    size += exploreIsland(grid, r + 1, c, visited)
    size += exploreIsland(grid, r, c - 1, visited)
    size += exploreIsland(grid, r, c + 1, visited)
    return size


wehave = float('inf')
for i in range(len(grid)):
    for j in range(len(grid[0])):
        size = exploreIsland(grid, i, j, visited)
        if 0 < size < wehave:
            wehave = size

print(wehave)
