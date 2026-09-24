class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLongestSubStr = 0
        start_ind, curr_ind = 0, 0
        char_ind = {}

        while curr_ind < len(s):
            if s[curr_ind] in char_ind and char_ind[s[curr_ind]] >= start_ind:
                start_ind = char_ind[s[curr_ind]] + 1
                char_ind[s[curr_ind]] = curr_ind
            else:
                char_ind[s[curr_ind]] = curr_ind
                maxLongestSubStr = max(maxLongestSubStr, curr_ind - start_ind + 1)

            curr_ind += 1


        return maxLongestSubStr
        
        