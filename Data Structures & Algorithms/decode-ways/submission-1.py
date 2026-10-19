class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or len(s) == 0 or s[0] == '0': return 0

        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            oneNumCode = int(s[i-1])
            twoNumCode = int(s[i-2:i])

            if 0 < oneNumCode < 10:
                dp[i] += dp[i-1]
            if 10 <= twoNumCode <= 26:
                dp[i] += dp[i-2]

        return dp[n]