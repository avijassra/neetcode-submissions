class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_set = set()
        for n in nums:
            if n in nums_set:
                nums_set.discard(n)
            else:
                nums_set.add(n)

        return list(nums_set)[0]