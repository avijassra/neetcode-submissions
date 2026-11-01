from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C, mins, q, freshFruits = len(grid), len(grid[0]), 0, deque([]), 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1: freshFruits += 1
                if grid[r][c] == 2: q.append((r, c))

        while q:
            if freshFruits == 0: break
            
            for _ in range(len(q)):
                cr, cc = q.popleft()

                for nr, nc in [(cr+1, cc), (cr, cc-1), (cr-1, cc), (cr, cc+1)]:
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
                        freshFruits -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))

            mins += 1

        return mins if freshFruits == 0 else -1
