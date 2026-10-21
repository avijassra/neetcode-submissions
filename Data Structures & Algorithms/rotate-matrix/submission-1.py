class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        dup = [row[:] for row in matrix]

        for r in range(n):
            for c in range(n):
                matrix[c][n-1-r] = dup[r][c]