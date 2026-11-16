class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(idx, subset, total):
            if total == 0:
                res.append(subset.copy())
                return

            if idx >= len(candidates): return

            if candidates[idx] <= total:
                subset.append(candidates[idx])
                dfs(idx + 1, subset, total - candidates[idx])

                subset.pop()
                while idx+1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                    idx += 1
                dfs(idx + 1, subset, total)

        dfs(0, [], target)
        return res