class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxTotal = currTotal = nums[0]
        
        for n in nums[1:]:
            if currTotal + n < n:
                currTotal = n
            else:
                currTotal += n

            maxTotal = max(maxTotal, currTotal)

        return maxTotal