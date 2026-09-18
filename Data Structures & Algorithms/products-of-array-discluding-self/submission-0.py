import copy

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        prod = 1
        zero_ind = None
        for i, n in enumerate(nums):
            if n == 0:
                if zero_ind is not None:
                    return res
                else:
                    zero_ind = i
            else:
                prod = (prod * nums[i])
            

        for i in range(len(nums)):
            if zero_ind is not None:
                if zero_ind != i:
                    res[i] = 0
                else:
                    res[i] = prod
            else:
                res[i] = prod // nums[i]


        return res