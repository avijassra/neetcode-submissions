class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sInd, maxLen, seen = 0, 0, {}

        for i, c in enumerate(s):
            if c not in seen or seen[c] < sInd:
                seen[c] = i
                maxLen = max(maxLen, i-sInd+1)
            else:
                sInd = seen[c] + 1
                seen[c] = i

        return maxLen