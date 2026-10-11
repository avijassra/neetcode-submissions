class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        R, C = len(heights), len(heights[0])
        pac = set()
        atl = set()

        def dfs(r, c, visited):
            visited.add((r, c))
            for nr, nc in [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]:
                if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)

        for r in range(R):
            dfs(r, 0, pac)
            dfs(r, C - 1, atl)

        for c in range(C):
            dfs(0, c, pac)
            dfs(R - 1, c, atl)

        return [[r, c] for r, c in pac & atl]