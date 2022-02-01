grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]


def exploreLand(grid, r, c, visited):
    rowInbounds = 0 <= r < len(grid)
    colInbounds = 0 <= c < len(grid[0])

    if not rowInbounds or not colInbounds:
        return False

    if grid[r][c] == "W":
        return False

    position = str(r) + "," + str(c)
    if position in visited:
        return False
    visited.add(position)

    exploreLand(grid, r - 1, c, visited)  # move up
    exploreLand(grid, r + 1, c, visited)  # move down
    exploreLand(grid, r, c - 1, visited)  # move left
    exploreLand(grid, r, c + 1, visited)  # move right

    return True


visited = set()
count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        # print(exploreLand(grid, i, j, visited))
        if exploreLand(grid, i, j, visited):
            count += 1
print(count)
