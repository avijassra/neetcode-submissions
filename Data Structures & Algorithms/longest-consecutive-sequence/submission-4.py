class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxCounter = 0

        for n in numSet:
            if n-1 in numSet:
                continue

            counter = 0
            t = n
            while t in numSet:
                counter += 1
                t += 1

            maxCounter = max(maxCounter, counter)

        return maxCounter