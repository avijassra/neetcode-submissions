class Solution:
    def longestPalindrome(self, s: str) -> str:
        lenS, max_pal_len, start, end = len(s), 1, 0, 0

        def chkPalindrome(sInd, eInd):
            nonlocal max_pal_len, start, end

            while sInd >= 0 and eInd < lenS and s[sInd] == s[eInd]:
                if max_pal_len < eInd - sInd + 1:
                    max_pal_len = eInd - sInd + 1
                    start, end = sInd, eInd
                
                sInd -= 1
                eInd += 1

        for ind in range(lenS):
            # old palindrome
            chkPalindrome(ind - 1, ind + 1)
            # even palindrom
            chkPalindrome(ind, ind + 1)
            
        return s[start:end+1]