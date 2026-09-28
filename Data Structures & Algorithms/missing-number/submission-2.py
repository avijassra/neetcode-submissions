class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        tXor = 0

        for n in nums: tXor ^= n
        for n in range(len(nums) + 1): tXor ^= n

        return tXor