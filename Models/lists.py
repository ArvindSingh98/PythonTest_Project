def find_paths(grid, start, destination):
    def dfs(x, y, path):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == -1:
            return
        if grid[x][y] == destination:
            paths.append(path + [(x, y)])
            return
        temp = grid[x][y]
        grid[x][y] = -1  # Mark as visited
        dfs(x + 1, y, path + [(x, y)])
        dfs(x - 1, y, path + [(x, y)])
        dfs(x, y + 1, path + [(x, y)])
        dfs(x, y - 1, path + [(x, y)])
        grid[x][y] = temp  # Unmark

    paths = []
    dfs(start[0], start[1], [])
    return paths

# Example usage:
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

paths = find_paths(grid, (0, 0), 2)
print(paths)