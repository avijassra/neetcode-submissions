class Solution:
    def countSubstrings(self, s: str) -> int:
        lenS = len(s)
        count = lenS

        def isPalindrom(l, r):
            nonlocal count
            
            while l >= 0 and r < lenS:
                if s[l] != s[r]:
                    break

                count += 1
                l, r = l-1, r+1

        for i in range(1, lenS):
            isPalindrom(i-1, i)
            isPalindrom(i-1, i+1)
            
        return count