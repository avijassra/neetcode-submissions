class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)

        for n in nums:
            res[n] += 1

        return sorted(res, key=lambda k: res[k], reverse=True)[:k]