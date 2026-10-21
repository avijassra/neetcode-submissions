class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = currSum = nums[0]

        for n in nums[1:]:
            currSum += n
            currSum = max(currSum, n)
            maxSum = max(maxSum, currSum)

        return maxSum