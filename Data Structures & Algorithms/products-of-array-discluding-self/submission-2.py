class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lenN = len(nums)
        res = [1] * lenN

        prod = 1
        for i in range(lenN):
            res[i] = prod
            prod *= nums[i]

        prod = 1
        for i in range(lenN-1, -1, -1):
            res[i] *= prod
            prod *= nums[i]
        
        return res