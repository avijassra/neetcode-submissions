class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        cubes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == '.':
                    continue
                
                cube_ind = (((r // 3) * 3) + (c // 3))
                if val in rows[r] or val in cols[c] or val in cubes[cube_ind]:
                    return False
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    cubes[cube_ind].add(val)
                
        return True