class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0

        maxProd, currMax, currMin = nums[0], nums[0], nums[0]

        for n in nums[1:]:
            if n < 0:
                currMax, currMin = currMin, currMax

            currMax = max(n, currMax * n)
            currMin = min(n, currMin * n)

            maxProd = max(maxProd, currMax)

        return maxProd