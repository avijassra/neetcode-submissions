class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        islands = 0

        def isIsland(r, c):
            if 0 <= r < R and 0 <= c < C:
                if grid[r][c] == '1':
                    grid[r][c] = '#'

                    for dr, dc in [(r, c+1), (r+1, c), (r, c-1), (r-1, c)]:
                        isIsland(dr, dc)

        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    isIsland(r, c)
                    islands += 1

        return islands
        