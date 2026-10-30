class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C, count = len(grid), len(grid[0]), 0

        def dfs(r, c):
            if 0 <= r < R and 0 <= c < C:
                if grid[r][c] == '1':
                    grid[r][c] = '#'
                    for nr, nc in [(r, c+1), (r+1, c), (r, c-1), (r-1, c)]:
                        dfs(nr, nc)

        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    dfs(r, c)
                    count += 1

        return count