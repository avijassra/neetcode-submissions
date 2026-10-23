class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = set()
        col = set()
        cube = set()

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue

                rowKey = f'{r}_{board[r][c]}'
                colKey = f'{c}_{board[r][c]}'
                cubeKey = f'{r//3}_{c//3}_{board[r][c]}'
                
                if rowKey in row:
                    return False
                if colKey in col:
                    return False
                if cubeKey in cube:
                    return False

                row.add(rowKey)
                col.add(colKey)
                cube.add(cubeKey)
        
        return True