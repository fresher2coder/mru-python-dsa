class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            # Boundary check and stop recursion if it's water or visited
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            grid[r][c] = "0"  # Mark as visited
            # Explore all 4 directions
            dfs(r+1, c)  # Down
            dfs(r-1, c)  # Up
            dfs(r, c+1)  # Right
            dfs(r, c-1)  # Left

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":  # Start DFS for new island
                    count += 1
                    dfs(r, c)

        return count