class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        p, a = set(), set()

        def dfs(r, c, visited):
            if (r, c) not in visited:
                visited.add((r,c))

                for nr, nc in [(r, c-1), (r-1, c), (r, c+1), (r+1, c)]:
                    if 0 <= nr < R and 0 <= nc < C and heights[r][c] <= heights[nr][nc]:
                        dfs(nr, nc, visited)


        for r in range(R):
            dfs(r, 0, p)
            dfs(r, C-1, a)

        for c in range(C):
            dfs(0, c, p)
            dfs(R-1, c, a)

        return list(a & p)