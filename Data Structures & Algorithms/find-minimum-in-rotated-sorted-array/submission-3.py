class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while nums[0] > nums[len(nums)-1]:
            nums.insert(0, nums.pop())

        return nums[0]