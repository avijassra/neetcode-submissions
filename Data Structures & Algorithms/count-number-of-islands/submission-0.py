class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        count = 0
        def isIsland(r, c, update):
            nonlocal count
            if not (0 <= r < R and 0 <= c < C and grid[r][c] == '1'):
                return
            
            grid[r][c] = '#'
            [isIsland(r+dr, c+cr, False) for dr, cr in [(-1,0), (0, 1), (1, 0), (0, -1)]]

            if update:
                count += 1

        [isIsland(r, c, True) for r in range(R) for c in range(C)]
        return count