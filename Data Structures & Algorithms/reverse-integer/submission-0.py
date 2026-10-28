class Solution:
    def reverse(self, x: int) -> int:
        res, isNeg = [], x < 0

        if isNeg: x = -1*x

        while x > 0:
            x, r = divmod(x, 10)
            res.append(r)

        lenX, output, limit = len(res), 0, 2**31

        for n in res:
            output = output*10 + n

        if isNeg: output *= -1

        if -1*limit <= output <= limit-1: 
            return output
        else:
            return 0