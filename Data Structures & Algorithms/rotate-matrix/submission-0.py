import copy

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        dup = copy.deepcopy(matrix)

        for r in range(n):
            for c in range(n):
                matrix[c][n-1-r] = dup[r][c]