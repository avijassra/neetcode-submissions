class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []

        res = defaultdict(list)
        for i, s in enumerate(strs):
            sorted_s = "".join(sorted(s))
            res[sorted_s].append(s)

        return list(res.values())