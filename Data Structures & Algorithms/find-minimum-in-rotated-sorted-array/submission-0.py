class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] < nums[r]:
                r -= 1
            else:
                l += 1

        return nums[l] if nums[l] < nums[r] else nums[r]