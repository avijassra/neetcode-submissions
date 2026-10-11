class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        R, C = len(board), len(board[0])
        visited = set()
        
        def dfs(r, c):
            visited.add((r,c))
            for nr, nc in [(r, c+1),(r+1, c),(r, c-1), (r-1, c)]:
                if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited and board[nr][nc] == 'O':
                    dfs(nr,nc)

        for r in range(R):
            if board[r][0] == 'O': dfs(r, 0)
            if board[r][C-1] == 'O': dfs(r, C-1)

        for c in range(C):
            if board[0][c] == 'O': dfs(0, c)
            if board[R-1][c] == 'O': dfs(R-1, c)

        for r in range(R):
            for c in range(C):
                # print(f'r: {r} | c: {c} | cell: {board[r][c]}')
                if board[r][c] == 'O' and (r,c) not in visited:
                    board[r][c] = 'X'
