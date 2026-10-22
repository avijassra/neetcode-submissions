class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            for i in range(left, right):            # top row →
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):            # right column ↓
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom): # single row/col left
                break

            for i in range(right - 1, left - 1, -1):  # bottom row ←
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):  # left column ↑
                res.append(matrix[i][left])
            left += 1

        return res