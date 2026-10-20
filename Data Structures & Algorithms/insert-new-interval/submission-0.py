class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i, n = 0, len(intervals)
        start, end = newInterval

        # Phase 1: intervals ending before newInterval starts
        while i < n and intervals[i][1] < start:
            res.append(intervals[i])
            i += 1

        # Phase 2: merge all overlapping intervals
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        res.append([start, end])

        # Phase 3: everything after
        res.extend(intervals[i:])
        return res