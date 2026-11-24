from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        max_area_island = 0

        def dfs(r, c):
            nonlocal max_area_island

            curr_area_island = 0
            q = deque([(r, c)])
            grid[r][c] = -1

            while q:
                for _ in range(len(q)):
                    (dr, dc) = q.popleft()
                    curr_area_island += 1

                    for nr, nc in [(dr, dc-1), (dr-1, dc), (dr, dc+1), (dr+1, dc)]:
                        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
                            grid[nr][nc] = -1
                            q.append((nr, nc))

            max_area_island = max(max_area_island, curr_area_island)

        for row in range(R):
            for col in range(C):
                if grid[row][col] == 1:
                    dfs(row, col)

        return max_area_island