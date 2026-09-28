class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numSet = set(nums)
        i = 0

        while i < len(nums):
            if i in numSet:
                i += 1
            else:
                return i

        return i