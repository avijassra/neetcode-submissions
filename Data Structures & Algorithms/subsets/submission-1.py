class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        subset = []

        def dfs(idx):
            if idx >= len(nums): return

            subset.append(nums[idx])
            output.append(subset.copy())
            dfs(idx+1)

            subset.pop()
            dfs(idx+1)
            

        dfs(0)
        return output + [[]]