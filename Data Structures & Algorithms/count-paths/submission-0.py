class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        opt_count = 0

        def gen_path(i, j):
            nonlocal opt_count

            if i == m-1 and j == n-1:
                opt_count += 1

            if i < m-1:
                gen_path(i+1, j)

            if j < n-1:
                gen_path(i, j+1)

        gen_path(0,0)

        return opt_count