class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        remove, (ps, pe) = 0, intervals[0]

        for s,e in intervals[1:]:
            if pe > s:
                remove += 1
            else:
                ps, pe = s, e

        return remove
