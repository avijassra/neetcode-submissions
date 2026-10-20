class Solution:
    def canJump(self, nums: List[int]) -> bool:
        visited = {}

        def dfs(ind):
            if ind == (len(nums) - 1):
                return True

            if ind >= len(nums):
                return False
            

            for i in range(nums[ind], 0, -1):
                if (ind+i) in visited:
                    return visited[ind+i]
                else:
                    res = dfs(ind+i)
                    if res:
                        visited[ind+i] = res
                        return True

            visited[ind] = False
            return False

        return dfs(0)
        