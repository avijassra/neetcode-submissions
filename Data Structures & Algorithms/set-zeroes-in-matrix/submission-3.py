class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = set()
        col = set()

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    row.add(r)
                    col.add(c)

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if r in row or c in col:
                    matrix[r][c] = 0
