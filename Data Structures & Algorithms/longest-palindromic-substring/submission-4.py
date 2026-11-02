class Solution:
    def longestPalindrome(self, s: str) -> str:
        lenS = len(s)
        if lenS == 1: return s

        maxLen, maxInd = 1, [0,1]

        def isPalindrom(l, r):
            nonlocal maxLen, maxInd
            
            while l >= 0 and r < lenS:
                if s[l] != s[r]:
                    break

                if r-l+1 > maxLen:
                    maxLen = r-l+1
                    maxInd = [l, r+1]

                l, r = l-1, r+1

        for i in range(1, lenS):
            isPalindrom(i-1, i)
            isPalindrom(i-1, i+1)
            
        return s[maxInd[0]:maxInd[1]]