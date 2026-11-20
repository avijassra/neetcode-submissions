from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        arr = [(n, c) for n, c in count.items()]
        arr.sort(key=lambda x: x[1], reverse=True)

        res = [n for n, _ in arr[:k]]

        return res