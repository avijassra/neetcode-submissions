from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C, edges = len(board), len(board[0]), set()

        q = deque([])

        for r in range(R):
            if board[r][0] == 'O': q.append((r,0))
            if board[r][C-1] == 'O': q.append((r,C-1))

        for c in range(C):
            if board[0][c] == 'O': q.append((0, c))
            if board[R-1][c] == 'O': q.append((R-1,c))

        while q:
            cr, cc = q.popleft()
            edges.add((cr,cc))

            for nr, nc in [(cr-1,cc), (cr,cc-1), (cr+1,cc), (cr,cc+1)]:
                if 0 <= nr < R and 0 <= nc < C and (nr,nc) not in edges and board[nr][nc] == 'O':
                    q.append((nr,nc))

        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O' and (r, c) not in edges:
                    board[r][c] = 'X'

