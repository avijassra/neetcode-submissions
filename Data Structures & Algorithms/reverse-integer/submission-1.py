class Solution:
    def reverse(self, x: int) -> int:
        res, isNeg, limit = 0, x < 0, 2**31

        if isNeg: x = -1*x

        while x > 0:
            x, r = divmod(x, 10)
            res = res*10 + r

        if isNeg: res *= -1

        if -1*limit <= res <= limit-1: 
            return res
        else:
            return 0