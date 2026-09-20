class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums_set = set(nums)

        print(nums_set)

        max_len, counter = 1, 1
        
        for num in nums_set:
            if num-1 not in nums_set:
                counter = 1
                while num+counter in nums_set:
                    counter += 1
                max_len = max(max_len, counter)

        return max(max_len, counter)