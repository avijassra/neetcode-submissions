class Solution:
    def rob(self, nums: List[int]) -> int:
        def robPrice(houses: List[int]) -> int:
            rob1, rob2 = 0, 0

            for h in houses:
                temp = max(h+rob1, rob2)
                rob1, rob2 = rob2, temp
        
            return rob2

        return max(nums[0], robPrice(nums[1:]), robPrice(nums[:-1]))