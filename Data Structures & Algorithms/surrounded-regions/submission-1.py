class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        R, C = len(board), len(board[0])
        
        def dfs(r, c):
            board[r][c] = 'T'
            for nr, nc in [(r, c+1),(r+1, c),(r, c-1), (r-1, c)]:
                if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == 'O':
                    dfs(nr,nc)

        for r in range(R):
            if board[r][0] == 'O': dfs(r, 0)
            if board[r][C-1] == 'O': dfs(r, C-1)

        for c in range(C):
            if board[0][c] == 'O': dfs(0, c)
            if board[R-1][c] == 'O': dfs(R-1, c)

        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
