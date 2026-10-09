class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C = len(grid), len(grid[0])
        inf_num = 2**31 - 1
        q = deque((r, c) for r in range(R) for c in range(C) if grid[r][c] == 0)

        while q:
            nr, nc = q.popleft()
            
            for dr, dc in [(nr-1,nc),(nr,nc+1),(nr+1,nc),(nr,nc-1)]:
                if 0 <= dr < R and 0 <= dc < C and grid[dr][dc] == inf_num:
                    grid[dr][dc] = grid[nr][nc] + 1
                    q.append((dr,dc))