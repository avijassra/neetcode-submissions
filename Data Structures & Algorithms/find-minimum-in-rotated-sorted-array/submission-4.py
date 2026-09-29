class Solution:
    def findMin(self, nums: List[int]) -> int:
        nLen = len(nums)
        m = (nLen - 1) // 2

        if nLen == 1:
            return nums[0]

        if nLen == 2:
            return min(nums[0], nums[1])

        if nums[0] < nums[m] < nums[nLen-1]:
            return nums[0]

        if nums[m] < nums[0]:
            return self.findMin(nums[:m+1])
        else:
            return self.findMin(nums[m:])