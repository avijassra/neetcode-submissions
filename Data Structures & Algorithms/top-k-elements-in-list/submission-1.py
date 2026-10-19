from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = defaultdict(int)

        for n in nums:
            numsDict[n] += 1

        descNumsDict = sorted(numsDict, key=numsDict.get, reverse=True)

        return descNumsDict[:k]
