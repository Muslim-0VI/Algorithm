def num_islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visit = set()
    islands = 0

    def dfs(r, c):
        if (r < 0 or c < 0 or 
            r >= rows or c >= cols or 
            grid[r][c] == "0" or 
            (r, c) in visit):
            return
        
        visit.add((r, c))
        
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visit:
                dfs(r, c)
                islands += 1

    return islands

if __name__ == "__main__":
    grid_map = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    
    print("Number of islands found:", num_islands(grid_map))