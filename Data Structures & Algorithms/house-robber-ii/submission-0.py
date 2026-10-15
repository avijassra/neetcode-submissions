class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(houses: List[int]):
            rob1, rob2 = 0, 0

            for h in houses:
                temp = max(rob1+h, rob2)
                rob1 = rob2
                rob2 = temp

            return rob2

        return max(nums[0], dp(nums[:-1]), dp(nums[1:]))
        