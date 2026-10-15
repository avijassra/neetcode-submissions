class Solution:
    def numDecodings(self, s: str) -> int:
        lenS = len(s)

        if lenS == 0 or s[0] == '0':
            return 0

        dp = [0] * (lenS + 1)

        dp[0] = 1
        dp[1] = 1

        for i in range(2, lenS+1):
            oneDigit = int(s[i-1])
            twoDigit = int(s[i-2:i])

            if oneDigit >= 1:
                dp[i] += dp[i-1]
            if 10 <= twoDigit <= 26:
                dp[i] += dp[i-2]

        return dp[lenS]

             