class Solution:
    def countSubstrings(self, s: str) -> int:
        found = len(s)

        def expand(l, r):
            nonlocal found

            while l >= 0 and r < len(s) and s[l] == s[r]:
                found += 1
                l -= 1
                r += 1    

        for i in range(len(s)):
            # odd count palindrome
            expand(i-1, i+1)
            # even count palindrome
            expand(i, i+1)

        return found