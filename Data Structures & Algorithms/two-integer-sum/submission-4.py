class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums_ind = [[nums[i], i] for i in range(len(nums))]
        # nums_ind.sort(key=lambda x: x[0])

        # l, r = 0, len(nums_ind) - 1

        # while l < r:
        #     total = nums_ind[l][0] + nums_ind[r][0]

        #     if total > target:
        #         r -= 1
        #     elif total < target:
        #         l += 1
        #     else:
        #         return sorted([nums_ind[l][1], nums_ind[r][1]])

        # return []
        seen = {}
        
        for i, num in enumerate(nums):
            diff = target - num

            if diff in seen:
                return [seen[diff], i]

            seen[num] = i

        return []