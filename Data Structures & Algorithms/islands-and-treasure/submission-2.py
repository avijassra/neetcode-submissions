from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        R, C = len(grid), len(grid[0])
        q = deque([])

        q = deque((r, c) for r in range(R) for c in range(C) if grid[r][c] == 0)

        while q:
            cr, cc = q.popleft()

            for nr, nc in [(cr-1, cc), (cr, cc+1), (cr+1, cc), (cr, cc-1)]:
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == INF:
                    grid[nr][nc] = 1 + grid[cr][cc]
                    q.append((nr,nc))