class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        r, c = 0, 0

        while r < R:
            if matrix[r][C-1] == target:
                return True
            elif matrix[r][C-1] > target:
                break
            
            r += 1

        if r == R: return False

        lt, rt = 0, C - 1

        while lt < rt:
            m = lt + (rt-lt) // 2
            
            if matrix[r][m] == target:
                return True
            
            if matrix[r][m] < target:
                lt = m + 1
            else:
                rt = m - 1

        
        return True if matrix[r][lt] == target else False