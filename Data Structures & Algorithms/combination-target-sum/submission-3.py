class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def backtracking(idx, comb, total):
            if total == 0:
                res.append(comb)
                return

            if total < 0:
                return

            for i in range(idx, len(nums)):
                backtracking(i, comb + [nums[i]], total-nums[i])

        
        backtracking(0, [], target)
        return res

