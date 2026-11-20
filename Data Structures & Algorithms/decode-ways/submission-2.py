class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == '0': return 0

        res = [0] * (n+1)
        res[0] = res[1] = 1

        for i in range(2, n+1):
            one_digit = int(s[i-1])
            two_digit = int(s[i-2:i])

            if 0 < one_digit < 10:
                res[i] += res[i-1]
            if 10 <= two_digit <= 26:
                res[i] += res[i-2]

        return res[n]