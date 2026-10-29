class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])

        def bfs(r, c, i):
            if i >= len(word):
                return True

            if 0 <= r < R and 0 <= c < C and board[r][c] == word[i]:
                board[r][c] = '#'
                for nr, nc in [(r, c-1), (r-1, c), (r, c+1), (r+1, c)]:
                    if bfs(nr, nc, i+1):
                        return True

                board[r][c] = word[i]
            
            return False

        return any(bfs(r, c, 0) for r in range(R) for c in range(C))