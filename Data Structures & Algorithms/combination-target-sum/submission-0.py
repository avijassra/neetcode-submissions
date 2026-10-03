class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dp(i, candidates, total):
            if total == target:
                res.append(candidates.copy())
                return
            
            if i >= len(nums) or total > target:
                return

            candidates.append(nums[i])
            dp(i, candidates, total + nums[i])
            candidates.pop()
            dp(i+1, candidates, total)

        dp(0, [], 0)

        return res