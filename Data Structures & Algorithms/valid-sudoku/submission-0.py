class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        memo = set()

        def memoCheck(key: str):
            nonlocal memo

            if key in memo:
                return False
            else:
                memo.add(key)
                return True

        for r, rs in enumerate(board):
            for c, cs in enumerate(rs):
                
                if cs != '.' and (not memoCheck(f'row_{r}_{cs}') or not memoCheck(f'col_{c}_{cs}') or not memoCheck(f'cube_{r // 3}_{c // 3}_{cs}')):
                    return False

        return True