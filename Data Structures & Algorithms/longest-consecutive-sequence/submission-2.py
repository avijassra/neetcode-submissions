class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        len_n = len(nums)

        if len_n == 0:
            return 0
        
        nums.sort()
        counter = 1
        res = 0

        for i in range(1, len_n):
            if nums[i] == nums[i-1] + 1:
                counter += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                res = max(res, counter)
                counter = 1

        return max(res, counter)